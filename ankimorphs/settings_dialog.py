from functools import partial
from typing import Optional

from anki.models import FieldDict
from aqt import mw
from aqt.qt import QCheckBox, QComboBox, QDialog, QMessageBox, QTableWidgetItem
from aqt.utils import tooltip

from ankimorphs.config import (
    get_all_default_configs,
    get_config,
    get_default_config,
    update_configs,
)
from ankimorphs.morphemizer import get_all_morphemizers
from ankimorphs.ui.settings_dialog_ui import Ui_SettingsDialog


def get_cbox_index(items, filter_field) -> Optional[int]:
    for index, field in enumerate(items):
        if field == filter_field:
            return index
    return None


def get_model_cbox_index(items, filter_field) -> Optional[int]:
    for index, model in enumerate(items):
        if model.name == filter_field:
            return index
    return None


class PreferencesDialog(QDialog):
    """
    The UI comes from ankimorphs/ui/settings_dialog.ui which is used in Qt Designer,
    which is then converted to ankimorphs/ui/settings_dialog_ui.py,
    which is then imported here.

    Here we make the final adjustments that can't be made (or are hard to make) in
    the Qt Designer, like setting up tables and widget-connections.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mw = parent
        self.models = None
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.config_filters = get_config("filters")
        self.setup_note_filters_table(self.config_filters)
        self.setup_extra_fields_table(self.config_filters)
        self.populate_tags_tab()
        self.populate_parse_tab()
        self.populate_skip_tab()
        self.populate_shortcuts_tab()
        self.populate_recalc_tab()
        self.setup_buttons()
        self.ui.tabWidget.currentChanged.connect(self.tab_change)
        self.ui.ankimorphs_version_label.setText(
            f"AnkiMorphs version: {mw.ANKIMORPHS_VERSION}"
        )

    def setup_note_filters_table(self, config_filters):
        self.ui.note_filters_table.setColumnWidth(0, 150)
        self.ui.note_filters_table.setColumnWidth(3, 150)
        self.ui.note_filters_table.setRowCount(len(config_filters))
        self.ui.note_filters_table.setAlternatingRowColors(True)
        self.models = mw.col.models.all_names_and_ids()

        for row, am_filter in enumerate(config_filters):
            self.set_note_filters_table_row(row, am_filter)

    def set_note_filters_table_row(self, row, config_filter):
        self.ui.note_filters_table.setRowHeight(row, 35)

        note_type_cbox = QComboBox(self.ui.note_filters_table)
        note_type_cbox.addItems([model.name for model in self.models])
        note_type_name_index = get_model_cbox_index(
            self.models, config_filter["note_type"]
        )
        if note_type_name_index is not None:
            note_type_cbox.setCurrentIndex(note_type_name_index)

        current_model_id = self.models[note_type_cbox.currentIndex()].id
        note_type = mw.col.models.get(current_model_id)

        fields: dict[str, tuple[int, FieldDict]] = mw.col.models.field_map(note_type)
        field_cbox = QComboBox(self.ui.note_filters_table)
        field_cbox.addItems(fields)
        field_cbox_index = get_cbox_index(fields, config_filter["field"])
        if field_cbox_index is not None:
            field_cbox.setCurrentIndex(field_cbox_index)

        # Fields are dependent on note-type
        note_type_cbox.currentIndexChanged.connect(
            partial(self.update_fields_cbox, field_cbox, note_type_cbox)
        )

        morphemizer_cbox = QComboBox(self.ui.note_filters_table)
        morphemizers = get_all_morphemizers()
        morphemizers = [mizer.get_description() for mizer in morphemizers]
        morphemizer_cbox.addItems(morphemizers)
        morphemizer_cbox_index = get_cbox_index(
            morphemizers, config_filter["morphemizer"]
        )
        if morphemizer_cbox_index is not None:
            morphemizer_cbox.setCurrentIndex(morphemizer_cbox_index)

        read_checkbox = QCheckBox()
        read_checkbox.setChecked(config_filter["read"])
        read_checkbox.setStyleSheet("margin-left:auto; margin-right:auto;")

        modify_checkbox = QCheckBox()
        modify_checkbox.setChecked(config_filter["modify"])
        modify_checkbox.setStyleSheet("margin-left:auto; margin-right:auto;")

        tags = ", ".join(config_filter["tags"])

        self.ui.note_filters_table.setCellWidget(row, 0, note_type_cbox)
        self.ui.note_filters_table.setItem(row, 1, QTableWidgetItem(tags))
        self.ui.note_filters_table.setCellWidget(row, 2, field_cbox)
        self.ui.note_filters_table.setCellWidget(row, 3, morphemizer_cbox)
        self.ui.note_filters_table.setCellWidget(row, 4, read_checkbox)
        self.ui.note_filters_table.setCellWidget(row, 5, modify_checkbox)

    def setup_extra_fields_table(self, config_filters):
        self.ui.extra_fields_table.setColumnWidth(0, 150)
        self.ui.extra_fields_table.setColumnWidth(1, 120)
        self.ui.extra_fields_table.setColumnWidth(2, 120)
        self.ui.extra_fields_table.setAlternatingRowColors(True)

        note_filters_table_rows = self.ui.note_filters_table.rowCount()

        self.ui.extra_fields_table.setRowCount(note_filters_table_rows)

        for row in range(note_filters_table_rows):
            self.set_extra_fields_table_row(row, config_filters)

    def set_extra_fields_table_row(self, row, config_filters):
        self.ui.extra_fields_table.setRowHeight(row, 35)

        note_type_widget = self.ui.note_filters_table.cellWidget(row, 0)
        note_type_text = note_type_widget.itemText(note_type_widget.currentIndex())
        current_model_id = self.models[note_type_widget.currentIndex()].id
        note_type = mw.col.models.get(current_model_id)

        fields: dict[str, tuple[int, FieldDict]] = mw.col.models.field_map(note_type)

        matching_filter = None
        for config_filter in config_filters:
            if note_type_text == config_filter["note_type"]:
                matching_filter = config_filter
                break

        focus_morph_cbox = QComboBox(self.ui.extra_fields_table)
        focus_morph_cbox.addItems(["(none)"])
        focus_morph_cbox.addItems(fields)

        if matching_filter is not None:
            focus_morph_cbox_index = get_cbox_index(
                fields, matching_filter["focus_morph"]
            )
            if focus_morph_cbox_index is not None:
                focus_morph_cbox_index += 1  # to offset the added (none) item
                focus_morph_cbox.setCurrentIndex(focus_morph_cbox_index)

        highlighted_cbox = QComboBox(self.ui.extra_fields_table)
        highlighted_cbox.addItems(["(none)"])
        highlighted_cbox.addItems(fields)

        if matching_filter is not None:
            highlighted_cbox_cbox_index = get_cbox_index(
                fields, matching_filter["highlighted"]
            )
            if highlighted_cbox_cbox_index is not None:
                highlighted_cbox_cbox_index += 1  # to offset the added (none) item
                highlighted_cbox.setCurrentIndex(highlighted_cbox_cbox_index)

        difficulty_cbox = QComboBox(self.ui.extra_fields_table)
        difficulty_cbox.addItems(["(none)"])
        difficulty_cbox.addItems(fields)

        if matching_filter is not None:
            difficulty_cbox_cbox_index = get_cbox_index(
                fields, matching_filter["difficulty"]
            )
            if difficulty_cbox_cbox_index is not None:
                difficulty_cbox_cbox_index += 1  # to offset the added (none) item
                difficulty_cbox.setCurrentIndex(difficulty_cbox_cbox_index)

        self.ui.extra_fields_table.setItem(row, 0, QTableWidgetItem(note_type_text))
        self.ui.extra_fields_table.setCellWidget(row, 1, focus_morph_cbox)
        self.ui.extra_fields_table.setCellWidget(row, 2, highlighted_cbox)
        self.ui.extra_fields_table.setCellWidget(row, 3, difficulty_cbox)

    def populate_tags_tab(self):
        self.ui.ripe_tag_input.setText(get_config("tag_ripe"))
        self.ui.budding_tag_input.setText(get_config("tag_budding"))
        self.ui.stale_tag_input.setText(get_config("tag_stale"))

    def restore_tags_defaults(self, skip_confirmation=False):
        if not skip_confirmation:
            title = "Confirmation"
            text = "Are you sure you want to restore default tags settings?"
            confirmed = self.warning_dialog(title, text)

            if not confirmed:
                return None

        self.ui.ripe_tag_input.setText(get_default_config("tag_ripe"))
        self.ui.budding_tag_input.setText(get_default_config("tag_budding"))
        self.ui.stale_tag_input.setText(get_default_config("tag_stale"))

    def populate_parse_tab(self):
        self.ui.parse_ignore_bracket_contents_input.setChecked(
            get_config("parse_ignore_bracket_contents")
        )
        self.ui.parse_ignore_round_bracket_contents_input.setChecked(
            get_config("parse_ignore_round_bracket_contents")
        )
        self.ui.parse_ignore_slim_round_bracket_contents_input.setChecked(
            get_config("parse_ignore_slim_round_bracket_contents")
        )
        self.ui.parse_ignore_proper_nouns_input.setChecked(
            get_config("parse_ignore_proper_nouns")
        )
        self.ui.parse_ignore_suspended_cards_content_input.setChecked(
            get_config("parse_ignore_suspended_cards_content")
        )

    def populate_shortcuts_tab(self):
        self.ui.shortcut_browse_same_ripe_input.setText(
            get_config("shortcut_browse_same_unknown_ripe")
        )
        self.ui.shortcut_browse_same_ripe_budding_input.setText(
            get_config("shortcut_browse_same_unknown_ripe_budding")
        )
        self.ui.shortcut_known_and_skip_input.setText(
            get_config("shortcut_set_known_and_skip")
        )
        self.ui.shortcut_learn_now_input.setText(get_config("shortcut_learn_now"))
        self.ui.shortcut_view_morphs_input.setText(
            get_config("shortcut_view_morphemes")
        )

    def restore_parse_defaults(self, skip_confirmation=False):
        if not skip_confirmation:
            title = "Confirmation"
            text = "Are you sure you want to restore default parse settings?"
            confirmed = self.warning_dialog(title, text)

            if not confirmed:
                return None

        self.ui.parse_ignore_bracket_contents_input.setChecked(
            get_default_config("parse_ignore_bracket_contents")
        )
        self.ui.parse_ignore_round_bracket_contents_input.setChecked(
            get_default_config("parse_ignore_round_bracket_contents")
        )
        self.ui.parse_ignore_slim_round_bracket_contents_input.setChecked(
            get_default_config("parse_ignore_slim_round_bracket_contents")
        )
        self.ui.parse_ignore_proper_nouns_input.setChecked(
            get_default_config("parse_ignore_proper_nouns")
        )
        self.ui.parse_ignore_suspended_cards_content_input.setChecked(
            get_default_config("parse_ignore_suspended_cards_content")
        )

    def restore_shortcuts_defaults(self, skip_confirmation=False):
        if not skip_confirmation:
            title = "Confirmation"
            text = "Are you sure you want to restore default shortcuts settings?"
            confirmed = self.warning_dialog(title, text)

            if not confirmed:
                return None

        self.ui.shortcut_browse_same_ripe_input.setText(
            get_default_config("shortcut_browse_same_unknown_ripe")
        )
        self.ui.shortcut_browse_same_ripe_budding_input.setText(
            get_default_config("shortcut_browse_same_unknown_ripe_budding")
        )
        self.ui.shortcut_known_and_skip_input.setText(
            get_default_config("shortcut_set_known_and_skip")
        )
        self.ui.shortcut_learn_now_input.setText(
            get_default_config("shortcut_learn_now")
        )
        self.ui.shortcut_view_morphs_input.setText(
            get_default_config("shortcut_view_morphemes")
        )

    def populate_recalc_tab(self):
        self.ui.preferred_sentence_length_input.setValue(
            get_config("recalc_preferred_sentence_length")
        )
        self.ui.recalc_unknown_morphs_count_input.setValue(
            get_config("recalc_unknown_morphs_count")
        )
        self.ui.recalc_before_sync_input.setChecked(get_config("recalc_before_sync"))
        self.ui.recalc_prioritize_collection_input.setChecked(
            get_config("recalc_prioritize_collection")
        )
        self.ui.recalc_prioritize_textfile_input.setChecked(
            get_config("recalc_prioritize_textfile")
        )

    def restore_recalc_defaults(self, skip_confirmation=False):
        if not skip_confirmation:
            title = "Confirmation"
            text = "Are you sure you want to restore default recalc settings?"
            confirmed = self.warning_dialog(title, text)

            if not confirmed:
                return None

        self.ui.preferred_sentence_length_input.setValue(
            get_default_config("recalc_preferred_sentence_length")
        )
        self.ui.recalc_unknown_morphs_count_input.setValue(
            get_default_config("recalc_unknown_morphs_count")
        )
        self.ui.recalc_before_sync_input.setChecked(
            get_default_config("recalc_before_sync")
        )
        self.ui.recalc_prioritize_collection_input.setChecked(
            get_default_config("recalc_prioritize_collection")
        )
        self.ui.recalc_prioritize_textfile_input.setChecked(
            get_default_config("recalc_prioritize_textfile")
        )

    def populate_skip_tab(self):
        self.ui.skip_stale_cards_input.setChecked(get_config("skip_stale_cards"))
        self.ui.skip_unknown_morph_seen_today_cards_input.setChecked(
            get_config("skip_unknown_morph_seen_today_cards")
        )
        self.ui.skip_show_num_of_skipped_cards_input.setChecked(
            get_config("skip_show_num_of_skipped_cards")
        )

    def restore_skip_defaults(self, skip_confirmation=False):
        if not skip_confirmation:
            title = "Confirmation"
            text = "Are you sure you want to restore default skip settings?"
            confirmed = self.warning_dialog(title, text)

            if not confirmed:
                return None

        self.ui.skip_stale_cards_input.setChecked(
            get_default_config("skip_stale_cards")
        )
        self.ui.skip_unknown_morph_seen_today_cards_input.setChecked(
            get_default_config("skip_unknown_morph_seen_today_cards")
        )
        self.ui.skip_show_num_of_skipped_cards_input.setChecked(
            get_default_config("skip_show_num_of_skipped_cards")
        )

    def restore_all_defaults(self):
        title = "Confirmation"
        text = "Are you sure you want to restore <b>all</b> default settings?"
        confirmed = self.warning_dialog(title, text)

        if confirmed:
            default_configs = get_all_default_configs()
            default_filters = default_configs["filters"]
            self.setup_note_filters_table(default_filters)
            self.setup_extra_fields_table(default_filters)
            self.restore_tags_defaults(skip_confirmation=True)
            self.restore_parse_defaults(skip_confirmation=True)
            self.restore_skip_defaults(skip_confirmation=True)
            self.restore_recalc_defaults(skip_confirmation=True)
            self.restore_shortcuts_defaults(skip_confirmation=True)

    def setup_buttons(self):
        self.ui.save_button.clicked.connect(self.save_to_config)
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.add_new_row_button.clicked.connect(self.add_new_row)
        self.ui.delete_row_button.clicked.connect(self.delete_row)
        self.ui.restore_tags_defaults_button.clicked.connect(self.restore_tags_defaults)
        self.ui.restore_recalc_defaults_button.clicked.connect(
            self.restore_recalc_defaults
        )
        self.ui.restore_shortcut_defaults_button.clicked.connect(
            self.restore_shortcuts_defaults
        )
        self.ui.restore_parse_defaults_button.clicked.connect(
            self.restore_parse_defaults
        )
        self.ui.restore_skip_defaults_button.clicked.connect(self.restore_skip_defaults)
        self.ui.restore_all_defaults_button.clicked.connect(self.restore_all_defaults)

    def delete_row(self):
        selected_row = self.ui.note_filters_table.currentRow()
        self.ui.note_filters_table.removeRow(selected_row)

    def add_new_row(self):
        self.ui.note_filters_table.setRowCount(
            self.ui.note_filters_table.rowCount() + 1
        )
        config_filter = get_default_config("filters")[0]
        row = self.ui.note_filters_table.rowCount() - 1
        self.set_note_filters_table_row(row, config_filter)

    def save_to_config(self):
        new_config = {
            "tag_ripe": self.ui.ripe_tag_input.text(),
            "tag_budding": self.ui.budding_tag_input.text(),
            "tag_stale": self.ui.stale_tag_input.text(),
            "shortcut_browse_same_unknown_ripe": self.ui.shortcut_browse_same_ripe_input.text(),
            "shortcut_browse_same_unknown_ripe_budding": self.ui.shortcut_browse_same_ripe_budding_input.text(),
            "shortcut_set_known_and_skip": self.ui.shortcut_known_and_skip_input.text(),
            "shortcut_learn_now": self.ui.shortcut_learn_now_input.text(),
            "shortcut_view_morphemes": self.ui.shortcut_view_morphs_input.text(),
            "recalc_preferred_sentence_length": self.ui.preferred_sentence_length_input.value(),
            "recalc_unknown_morphs_count": self.ui.recalc_unknown_morphs_count_input.value(),
            "recalc_before_sync": self.ui.recalc_before_sync_input.isChecked(),
            "recalc_prioritize_collection": self.ui.recalc_prioritize_collection_input.isChecked(),
            "recalc_prioritize_textfile": self.ui.recalc_prioritize_textfile_input.isChecked(),
            "parse_ignore_bracket_contents": self.ui.parse_ignore_bracket_contents_input.isChecked(),
            "parse_ignore_round_bracket_contents": self.ui.parse_ignore_round_bracket_contents_input.isChecked(),
            "parse_ignore_slim_round_bracket_contents": self.ui.parse_ignore_slim_round_bracket_contents_input.isChecked(),
            "parse_ignore_proper_nouns": self.ui.parse_ignore_proper_nouns_input.isChecked(),
            "parse_ignore_suspended_cards_content": self.ui.parse_ignore_suspended_cards_content_input.isChecked(),
            "skip_stale_cards": self.ui.skip_stale_cards_input.isChecked(),
            "skip_unknown_morph_seen_today_cards": self.ui.skip_unknown_morph_seen_today_cards_input.isChecked(),
            "skip_show_num_of_skipped_cards": self.ui.skip_show_num_of_skipped_cards_input.isChecked(),
        }

        filters = []
        rows = self.ui.note_filters_table.rowCount()
        for row in range(rows):
            note_type_widget = self.ui.note_filters_table.cellWidget(row, 0)
            field_widget = self.ui.note_filters_table.cellWidget(row, 2)
            morphemizer_widget = self.ui.note_filters_table.cellWidget(row, 3)

            focus_morph_widget = self.ui.extra_fields_table.cellWidget(row, 1)
            highlighted_widget = self.ui.extra_fields_table.cellWidget(row, 2)
            difficulty_widget = self.ui.extra_fields_table.cellWidget(row, 3)

            _filter = {
                "note_type": note_type_widget.itemText(note_type_widget.currentIndex()),
                "note_type_id": self.models[note_type_widget.currentIndex()].id,
                "tags": [self.ui.note_filters_table.item(row, 1).text()],
                "field": field_widget.itemText(field_widget.currentIndex()),
                "morphemizer": morphemizer_widget.itemText(
                    morphemizer_widget.currentIndex()
                ),
                "read": self.ui.note_filters_table.cellWidget(row, 4).isChecked(),
                "modify": self.ui.note_filters_table.cellWidget(row, 5).isChecked(),
                "focus_morph": focus_morph_widget.itemText(
                    focus_morph_widget.currentIndex()
                ),
                "highlighted": highlighted_widget.itemText(
                    highlighted_widget.currentIndex()
                ),
                "difficulty": difficulty_widget.itemText(
                    difficulty_widget.currentIndex()
                ),
            }
            filters.append(_filter)
        new_config["filters"] = filters
        update_configs(new_config)
        self.config_filters = get_config("filters")
        tooltip("Please recalc to avoid unexpected behaviour", parent=mw)

    def update_fields_cbox(self, field_cbox, note_type_cbox):
        current_model_id = self.models[note_type_cbox.currentIndex()].id
        note_type = mw.col.models.get(current_model_id)
        fields: dict[str, tuple[int, FieldDict]] = mw.col.models.field_map(note_type)
        field_cbox.clear()
        field_cbox.addItems(fields)

    def tab_change(self, tab_index):
        """
        The extra fields settings are dependent on the note filters, so
        everytime the extra fields tab is opened we just re-populate it
        in case the note filters have changed.
        """
        if tab_index == 1:
            self.setup_extra_fields_table(self.config_filters)

    def warning_dialog(self, title, text) -> bool:
        warning_box = QMessageBox(self)
        warning_box.setWindowTitle(title)
        warning_box.setIcon(QMessageBox.Icon.Warning)
        warning_box.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        warning_box.setText(text)
        answer = warning_box.exec()
        if answer == QMessageBox.StandardButton.Yes:
            tooltip("Remember to save!", parent=mw)
            return True
        return False


def main():
    mw.ankimorphs_preferences_dialog = PreferencesDialog(mw)
    mw.ankimorphs_preferences_dialog.exec()