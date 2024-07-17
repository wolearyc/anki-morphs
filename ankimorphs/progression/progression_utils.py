from __future__ import annotations

import copy
import csv
from pathlib import Path

from .. import ankimorphs_config
from .. import ankimorphs_globals as am_globals
from ..ankimorphs_db import AnkiMorphsDB
from ..morpheme import MorphOccurrence
from .progression_output_dialog import OutputOptions
from ..recalc.morph_priority_utils import _get_morph_priority

class Bins:
    """Stores bins for morph priority."""
    def __init__(
        self, min_priority: int, max_priority: int, bin_size: int, 
        is_cumulative: bool
    ) -> None:

        self.min_priority = min_priority
        self.max_priority = max_priority
        self.bin_size = bin_size
        self.is_cumulative = is_cumulative

        # Placeholder
        if min_priority >= max_priority: 
                raise InvalidBinIndexException((min_priority,max_priority))

        self.indexes = []
        min_index = min_priority
        while min_index+bin_size-1 < max_priority:
            if is_cumulative:
                self.indexes.append((min_priority,min_index+bin_size-1))
            else:
                self.indexes.append((min_index,min_index+bin_size-1))
            
            min_index += bin_size

        if is_cumulative:
            self.indexes.append((min_priority,max_priority))
        else:
            self.indexes.append((min_index,max_priority))

        

class ProgressReport:

    def __init__(
        self, min_priority: int, max_priority: int
    ) -> None:
        
        if min_priority < 1 or max_priority < min_priority:
            raise InvalidBinIndexException()
        
        self.min_priority = min_priority
        self.max_priority = max_priority

        # Ideally, these would be sets of Morphemes. However, I haven't
        # yet figured out if these objects are easily accessible. 
        self.unique_known: set[str] = set()
        self.unique_learning: set[str] = set()
        self.unique_unknowns: set[str] = set()
        self.unique_missing: set[str] = set()

    def get_total_known(self) -> int:
        return len(self.unique_known)
    
    def get_total_learning(self) -> int:
        return len(self.unique_learning)
    
    def get_total_unknowns(self) -> int:
        return len(self.unique_unknowns)

    def get_total_missing(self) -> int:
        return len(self.unique_missing)
    
    def get_total_morphs(self) -> int:
        return self.get_total_known() + self.get_total_learning() + \
               self.get_total_unknowns() + self.get_total_missing()


def _update_progress_report(
    progress_report: ProgressReport,
    morph: str,
    morph_status: str
) -> None:

    if morph_status == "known":
        progress_report.unique_known.add(morph)
    elif morph_status == "learning":
        progress_report.unique_learning.add(morph)
    elif morph_status == "unknown":
        progress_report.unique_unknowns.add(morph)
    elif morph_status == "missing":
        progress_report.unique_missing.add(morph)
    else:
        raise  

def get_progress_reports(
        am_db: AnkiMorphsDB, bins: Bins, 
        morph_priorities: dict[(str,str),int], only_lemma_priorities: bool
) -> list[ProgressReport]:
    
    reports = []

    # This could be cleaner - it would be good to reimplemnt these db methods
    morph_learning_statuses: dict[str,str]
    if only_lemma_priorities:
        morph_learning_statuses = am_db.get_morph_lemmas_learning_statuses()
    else:
        morph_learning_statuses = am_db.get_morph_inflections_learning_statuses()

    for min_priority, max_priority in bins.indexes:
        
        report = ProgressReport(min_priority,max_priority)
        morph_priorities_subset = _get_morph_priorities_subset(morph_priorities, 
            min_priority, max_priority)
        for morph in morph_priorities_subset:
            learning_status_key = morph[0] + morph[1]
            if only_lemma_priorities:
                learning_status_key = morph[0] # expect morph=(lemma,lemma)

            morph_status = 'missing'
            if learning_status_key in morph_learning_statuses: # if the morph is in the database
                morph_status = morph_learning_statuses[learning_status_key]
            _update_progress_report(report, morph, morph_status)
        
        reports.append(report)

    return reports


def _get_morph_priorities_subset(
        morph_priorities: dict[(str,str),int], min_priority: int, max_priority: int
) -> dict[str,int]:
    def is_in_range(item):
        _, priority = item
        return priority >= min_priority and priority <= max_priority

    return dict(filter(is_in_range, morph_priorities.items()))

def get_priority_ordered_morph_statuses(
        am_db: AnkiMorphsDB, bins: Bins, 
        morph_priorities: dict[(str,str),int], only_lemma_priorities: bool
) -> list[(int,str,str,str)]:
    
    # (lemma, inflection, and status) in increasing priority order
    morph_statuses: list[(int,str,str,str)] = []

    morph_priorities = _get_morph_priorities_subset(morph_priorities, 
        bins.min_priority, bins.max_priority)

    sorted_morph_priorities = dict(
        sorted(
            morph_priorities.items(),
            key=lambda item: item[1],
        )
    )

    morph_learning_statuses: dict[str,str]
    if only_lemma_priorities:
        morph_learning_statuses = am_db.get_morph_lemmas_learning_statuses()
    else:
        morph_learning_statuses = am_db.get_morph_inflections_learning_statuses()

    for morph in sorted_morph_priorities:
        priority = sorted_morph_priorities[morph]
        learning_status_key = morph[0] + morph[1]
        if only_lemma_priorities:
            learning_status_key = morph[0] # expect morph=(lemma,lemma)
        
        morph_status = 'missing'
        if learning_status_key in morph_learning_statuses: # if the morph is in the database
            morph_status = morph_learning_statuses[learning_status_key]

        if only_lemma_priorities:
            morph_statuses.append((priority,morph[0], '-', morph_status))
        else:
            morph_statuses.append((priority,morph[0],morph[1],morph_status))

    return morph_statuses









