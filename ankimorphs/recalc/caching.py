from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

from aqt import mw

from .. import ankimorphs_globals as am_globals
from .. import progress_utils
from ..ankimorphs_config import AnkiMorphsConfig, AnkiMorphsConfigFilter
from ..ankimorphs_db import AnkiMorphsDB
from ..exceptions import CancelledOperationException, KnownMorphsFileMalformedException
from ..morphemizers import morphemizer as morphemizer_module
from ..morphemizers import spacy_wrapper
from ..morphemizers.morphemizer import SpacyMorphemizer
from ..text_preprocessing import (
    get_processed_expression,
    get_processed_morphemizer_morphs,
    get_processed_spacy_morphs,
)
from . import anki_data_utils
from .anki_data_utils import AnkiCardData


def cache_anki_data(  # pylint:disable=too-many-locals, too-many-branches, too-many-statements
    am_config: AnkiMorphsConfig,
    read_enabled_config_filters: list[AnkiMorphsConfigFilter],
) -> None:
    # Extracting morphs from cards is expensive, so caching them yields a significant
    # performance gain.
    #
    # Note: this function is a monstrosity, but at some point it's better to have
    # most of the logic in the same function in a way that gives a better overview
    # of all the things that are happening. Refactoring this into even smaller pieces
    # will in effect lead to spaghetti code.

    assert mw is not None

    # Rebuilding the entire ankimorphs db every time is faster and much simpler than
    # updating it since we can bulk queries to the anki db.
    am_db = AnkiMorphsDB()
    am_db.drop_all_tables()
    am_db.create_all_tables()

    # These lists contain data that will be inserted into ankimorphs.db
    card_table_data: list[dict[str, Any]] = []
    morph_table_data: list[dict[str, Any]] = []
    card_morph_map_table_data: list[dict[str, Any]] = []

    # We only want to cache the morphs on the note-filters that have 'read' enabled
    for config_filter in read_enabled_config_filters:

        cards_data_dict: dict[int, AnkiCardData] = (
            anki_data_utils.create_card_data_dict(
                am_config,
                config_filter,
            )
        )
        card_amount = len(cards_data_dict)

        # Batching the text makes spacy much faster, so we flatten the data into the all_text list.
        # To get back to the card_id for every entry in the all_text list, we create a separate list with the keys.
        # These two lists have to be synchronized, i.e., the indexes align, that way they can be used for lookup later.
        all_text: list[str] = []
        all_keys: list[int] = []

        for key, _card_data in cards_data_dict.items():
            # Some spaCy models label all capitalized words as proper nouns,
            # which is pretty bad. To prevent this, we lower case everything.
            # This in turn makes some models not label proper nouns correctly,
            # but this is preferable because we also have the 'Mark as Name'
            # feature that can be used in that case.
            expression = get_processed_expression(
                am_config, _card_data.expression.lower()
            )
            all_text.append(expression)
            all_keys.append(key)

        nlp = None  # spacy.Language
        morphemizer = morphemizer_module.get_morphemizer_by_description(
            config_filter.morphemizer_description
        )
        assert morphemizer is not None

        if isinstance(morphemizer, SpacyMorphemizer):
            spacy_model = config_filter.morphemizer_description.removeprefix("spaCy: ")
            nlp = spacy_wrapper.get_nlp(spacy_model)

        # Since function overloading isn't a thing in python, we use
        # this ugly branching with near identical code. An alternative
        # approach of using variable number of arguments (*args) would
        # require an extra function call, so this is faster.
        #
        # We don't want to store duplicate morphs because it can lead
        # to the same morph being counted twice, which is bad for the
        # scoring algorithm. We therefore convert the lists of morphs
        # we receive from the morphemizers into sets.
        if nlp is not None:
            for index, doc in enumerate(nlp.pipe(all_text)):
                progress_utils.background_update_progress_potentially_cancel(
                    label=f"Extracting morphs from<br>{config_filter.note_type} cards<br>card: {index} of {card_amount}",
                    counter=index,
                    max_value=card_amount,
                )
                morphs = set(get_processed_spacy_morphs(am_config, doc))
                key = all_keys[index]
                cards_data_dict[key].morphs = morphs
        else:
            for index, _expression in enumerate(all_text):
                progress_utils.background_update_progress_potentially_cancel(
                    label=f"Extracting morphs from<br>{config_filter.note_type} cards<br>card: {index} of {card_amount}",
                    counter=index,
                    max_value=card_amount,
                )
                morphs = set(
                    get_processed_morphemizer_morphs(
                        morphemizer, _expression, am_config
                    )
                )
                key = all_keys[index]
                cards_data_dict[key].morphs = morphs

        for counter, card_id in enumerate(cards_data_dict):
            progress_utils.background_update_progress_potentially_cancel(
                label=f"Caching {config_filter.note_type} cards<br>card: {counter} of {card_amount}",
                counter=counter,
                max_value=card_amount,
            )
            card_data: AnkiCardData = cards_data_dict[card_id]

            if card_data.automatically_known_tag or card_data.manually_known_tag:
                highest_interval = am_config.interval_for_known_morphs
            elif card_data.type == 1:  # 1: learning
                # cards in the 'learning' state have an interval of zero, but we don't
                # want to treat them as 'unknown', so we change the value manually.
                highest_interval = 1
            else:
                highest_interval = card_data.interval

            card_table_data.append(
                {
                    "card_id": card_id,
                    "note_id": card_data.note_id,
                    "note_type_id": card_data.note_type_id,
                    "card_type": card_data.type,
                    "fields": card_data.fields,
                    "tags": card_data.tags,
                }
            )

            if card_data.morphs is None:
                continue

            for morph in card_data.morphs:
                morph_table_data.append(
                    {
                        "lemma": morph.lemma,
                        "inflection": morph.inflection,
                        "highest_lemma_learning_interval": None,
                        "highest_inflection_learning_interval": highest_interval,
                    }
                )
                card_morph_map_table_data.append(
                    {
                        "card_id": card_id,
                        "morph_lemma": morph.lemma,
                        "morph_inflection": morph.inflection,
                    }
                )

    if am_config.read_known_morphs_folder is True:
        progress_utils.background_update_progress(label="Importing known morphs")
        morph_table_data += _get_morphs_from_files(am_config)

    progress_utils.background_update_progress(label="Updating learning intervals")
    _update_learning_intervals(am_config, morph_table_data)

    progress_utils.background_update_progress(label="Saving to ankimorphs.db")
    am_db.insert_many_into_morph_table(morph_table_data)
    am_db.insert_many_into_card_table(card_table_data)
    am_db.insert_many_into_card_morph_map_table(card_morph_map_table_data)
    # am_db.print_table("Morphs")
    am_db.con.close()


def _get_morphs_from_files(am_config: AnkiMorphsConfig) -> list[dict[str, Any]]:
    assert mw is not None

    morphs_from_files: list[dict[str, Any]] = []
    known_morphs_dir_path: Path = Path(
        mw.pm.profileFolder(), am_globals.KNOWN_MORPHS_DIR_NAME
    )

    print(f"known_morphs_dir_path: {known_morphs_dir_path}")

    input_files: list[Path] = []

    for path in known_morphs_dir_path.rglob("*.csv"):
        input_files.append(path)

    print(f"input_files: {input_files}")
    print(f"input_files len: {len(input_files)}")

    for input_file in input_files:
        if mw.progress.want_cancel():  # user clicked 'x'
            raise CancelledOperationException

        progress_utils.background_update_progress(
            label=f"Importing known morphs from file:<br>{input_file.relative_to(known_morphs_dir_path)}",
        )

        # todo: add comment about supporting backwards compatibility

        print(f"input_file: {input_file}")

        with open(input_file, encoding="utf-8") as csvfile:
            morph_reader = csv.reader(csvfile, delimiter=",")
            headers: list[str] | None = next(morph_reader, None)

            if headers is None:
                raise KnownMorphsFileMalformedException(input_file)

            headers_lower = [header.lower() for header in headers]
            # print(f"headers_lower_case: {headers_lower}")
            # print(f"am_globals.LEMMA_HEADER.lower(): {am_globals.LEMMA_HEADER.lower()}")

            if am_globals.LEMMA_HEADER.lower() not in headers_lower:
                raise KnownMorphsFileMalformedException(input_file)

            lemma_column: int = headers_lower.index(am_globals.LEMMA_HEADER.lower())
            inflection_column: int = -1

            try:
                inflection_column = headers_lower.index(
                    am_globals.INFLECTION_HEADER.lower()
                )
            except ValueError:
                print("ValueError!")

            if inflection_column == -1:
                morphs_from_files += _get_morphs_from_minimum_format(
                    am_config, morph_reader, lemma_column
                )
            else:
                morphs_from_files += _get_morphs_from_full_format(
                    am_config, morph_reader, lemma_column, inflection_column
                )

    return morphs_from_files


def _get_morphs_from_minimum_format(
    am_config: AnkiMorphsConfig, morph_reader: Any, lemma_column: int
) -> list[dict[str, Any]]:
    morphs_from_files: list[dict[str, Any]] = []

    print("_get_morphs_from_minimum_format")
    for row in morph_reader:
        print(f"row: {row}")
        lemma: str = row[lemma_column]
        print(f"lemma: {lemma}")
        morphs_from_files.append(
            {
                "lemma": lemma,
                "inflection": lemma,
                "highest_lemma_learning_interval": am_config.interval_for_known_morphs,
                "highest_inflection_learning_interval": am_config.interval_for_known_morphs,
            }
        )
    return morphs_from_files


def _get_morphs_from_full_format(
    am_config: AnkiMorphsConfig,
    morph_reader: Any,
    lemma_column: int,
    inflection_column: int,
) -> list[dict[str, Any]]:
    morphs_from_files: list[dict[str, Any]] = []

    print("_get_morphs_from_full_format")

    for row in morph_reader:
        print(f"row: {row}")
        lemma: str = row[lemma_column]
        inflection: str = row[inflection_column]
        print(f"lemma: {lemma}, inflection: {inflection}")
        morphs_from_files.append(
            {
                "lemma": lemma,
                "inflection": inflection,
                "highest_lemma_learning_interval": am_config.interval_for_known_morphs,
                "highest_inflection_learning_interval": am_config.interval_for_known_morphs,
            }
        )
    return morphs_from_files


def _update_learning_intervals(
    am_config: AnkiMorphsConfig, morph_table_data: list[dict[str, Any]]
) -> None:
    learning_intervals_of_lemmas: dict[str, int] = _get_learning_intervals_of_lemmas(
        morph_table_data
    )

    if am_config.evaluate_morph_lemma:
        # update both the lemma and inflection intervals
        for morph_data_dict in morph_table_data:
            lemma = morph_data_dict["lemma"]
            morph_data_dict["highest_lemma_learning_interval"] = (
                learning_intervals_of_lemmas[lemma]
            )
            morph_data_dict["highest_inflection_learning_interval"] = (
                learning_intervals_of_lemmas[lemma]
            )
    else:
        # only update lemma intervals
        for morph_data_dict in morph_table_data:
            lemma = morph_data_dict["lemma"]
            morph_data_dict["highest_lemma_learning_interval"] = (
                learning_intervals_of_lemmas[lemma]
            )


def _get_learning_intervals_of_lemmas(
    morph_table_data: list[dict[str, Any]]
) -> dict[str, int]:
    learning_intervals_of_lemmas: dict[str, int] = {}

    for morph_data_dict in morph_table_data:
        lemma = morph_data_dict["lemma"]
        inflection_interval = morph_data_dict["highest_inflection_learning_interval"]

        if lemma in learning_intervals_of_lemmas:
            if inflection_interval > learning_intervals_of_lemmas[lemma]:
                learning_intervals_of_lemmas[lemma] = inflection_interval
        else:
            learning_intervals_of_lemmas[lemma] = inflection_interval

    return learning_intervals_of_lemmas
