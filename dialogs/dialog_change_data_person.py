from PyQt5.QtWidgets import QDialog, QMessageBox, \
                            QPushButton, \
                            QLineEdit, \
                            QLabel

import re
import json
from os import stat




class ChangeCustomData(QDialog):

    def __init__(self, surname: str, name: str, second_name: str, phone: str):
        super().__init__()
        self.setWindowTitle("Change custom data")

        #// Values
        self.customers = {}
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.phone = phone

        #// Run fucntions
        self._create_widgets()
        self._set_signals()
    
    
    def _create_widgets(self) -> None:
        """Create widgets in dialog window."""
        #// Create Labels
        self.label_surname = QLabel("Фамилия", self)
        self.label_name = QLabel("Имя", self)
        self.label_second_name = QLabel("Отчество", self)
        self.label_phone_number = QLabel("Телефон", self)

        #// Moving Labels
        self.label_surname.move(30, 40)
        self.label_name.move(30, 80)
        self.label_second_name.move(30, 120)
        self.label_phone_number.move(30, 160)

        #// Create LineEdits
        self.line_edit_surname = QLineEdit(self)
        self.line_edit_name = QLineEdit(self)
        self.line_edit_second_name = QLineEdit(self)
        self.line_edit_phone_number = QLineEdit(self)

        #// Set Default
        self.line_edit_surname.setText(self.surname)
        self.line_edit_name.setText(self.name)
        self.line_edit_second_name.setText(self.second_name)
        self.line_edit_phone_number.setText(self.phone)
        
        #// Moving LineEdits
        self.line_edit_surname.move(100, 40)
        self.line_edit_name.move(100, 80)
        self.line_edit_second_name.move(100, 120)
        self.line_edit_phone_number.move(100, 160)

        #// Create PushButtons
        self.push_button_okey = QPushButton("Продолжить", self)
        self.push_button_cancel = QPushButton("Отменить", self)
        self.push_button_okey.setDisabled(True)

        #// Moving PushButtons
        self.push_button_cancel.move(60, 200)
        self.push_button_okey.move(160, 200)


    def _set_signals(self) -> None:
        """Set signals to widgets."""
        #// Signals to LineEdits
        self.line_edit_surname.textEdited.connect(lambda: self._validate_values(
            self.line_edit_surname.text(), "surname"
            ))
        self.line_edit_name.textEdited.connect(lambda: self._validate_values(
            self.line_edit_name.text(), "name"
            ))
        self.line_edit_second_name.textEdited.connect(lambda: self._validate_values(
            self.line_edit_second_name.text(), "second_name"
            ))
        self.line_edit_phone_number.editingFinished.connect(lambda: self._validate_values(
            self.line_edit_phone_number.text(), "phone"
            ))
        #// Signals to button.
        self.push_button_okey.clicked.connect(self._write_data_in_database)
        self.push_button_cancel.clicked.connect(lambda: self.close())
        
    def _validate_values(self, value: str, box_id: str) -> None:
        """Validate values in textEdited boxed."""
        match box_id:
            case "surname":
                if not re.fullmatch(r"[А-я]*", value):
                    QMessageBox.information(
                            self,
                            "Предупреждение",
                            "Вам не нужно использовать цифры и другие символы, кроме букв!")
                    self._clear_cell(self.line_edit_surname)
                    self.push_button_okey.setDisabled(True)
            case "name":
                if not re.fullmatch(r"[А-я]*", value):
                    QMessageBox.information(
                            self,
                            "Предупреждение",
                            "Вам не нужно использовать цифры и другие символы, кроме букв!")
                    self._clear_cell(self.line_edit_name)
                    self.push_button_okey.setDisabled(True)
            case "second_name":
                if not re.fullmatch(r"[А-я]*", value):
                    QMessageBox.information(
                            self,
                            "Предупреждение",
                            "Вам не нужно использовать цифры и другие символы, кроме букв!")
                    self._clear_cell(self.line_edit_second_name)
                    self.push_button_okey.setDisabled(True)
            case "phone":
                if not re.fullmatch(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", value):
                    QMessageBox.information(
                            self,
                            "Предупреждение",
                            "Введите телефон в формате - +7(961)-702-55-42")
                    self._clear_cell(self.line_edit_phone_number)
                    self.push_button_okey.setDisabled(True)
        try:
            if self.line_edit_surname.text() not in ("", None) and \
               self.line_edit_name.text() not in ("", None) and \
               self.line_edit_second_name.text() not in ("", None) and \
               self.line_edit_phone_number.text() not in ("", None):
                   self.push_button_okey.setDisabled(False)
        except Exception:
            self.push_button_okey.setDisabled(True)


    def _clear_cell(self, name_of_line_edit) -> None:
        """Block signals and clear cell, when arises warning."""
        name_of_line_edit.blockSignals(True)
        name_of_line_edit.setText('')
        name_of_line_edit.blockSignals(False)
        

    def _write_data_in_database(self):
        """Write dict with data of custom in JSON file."""

        with open("database.json", "r", encoding="utf-8") as json_file_read:
            if stat("database.json").st_size > 2:
                file_data = json.load(json_file_read)

                for data in file_data.values():
                    if data[0] == self.surname and \
                       data[1] == self.name and \
                       data[2] == self.second_name and \
                       data[3] == self.phone:
                            data[0] = self.line_edit_surname.text()
                            data[1] = self.line_edit_name.text()
                            data[2] = self.line_edit_second_name.text()
                            data[3] = self.line_edit_phone_number.text()


                with open("database.json", "w", encoding="utf-8") as json_file_append:
                    json_file_append.write(json.dumps(file_data,\
                            indent=4, ensure_ascii=False))

        self.close()
