import json
from sys import exit
from os import stat

#// PyQt
from PyQt5.QtWidgets import QMainWindow, \
                            QMenu, \
                            QMenuBar, \
                            QAction, QMessageBox, QTableWidget, \
                            QTableWidgetItem
#// Custom
from dialogs.dialog_add_data_person import AddCustomDialog
from dialogs.dialog_change_data_person import ChangeCustomData




class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("lab work 9")
        self.setFixedSize(800, 600)

        #// Values
        self.table_row_count = 0

        #// Run functions
        self._create_actions()
        self._create_widgets()
        self._connect_actions() 
        self._create_table()
        self.update_table()



    def _create_widgets(self) -> None:
        """Create widgets in QMainWindow."""
        self.menu_bar = QMenuBar(self)

        self.menu_operation = QMenu("Операции")
        self.menu_operation.addAction(self.add_data_person)
        self.menu_operation.addAction(self.change_data_person)
        self.menu_operation.addAction(self.clear_data_person)

        self.menu_exit = QMenu("Выход")
        self.menu_exit.addAction(self.exit_app)

        self.menu_bar.addMenu(self.menu_operation)
        self.menu_bar.addMenu(self.menu_exit)

        self.setMenuBar(self.menu_bar)


    def _create_actions(self) -> None:
        """Create actions to menu."""
        self.add_data_person = QAction("Добавить клиента", self)
        self.change_data_person = QAction("Изменить данные", self)
        self.clear_data_person = QAction("Удалить клиента", self)

        self.exit_app = QAction("Закрыть приложение", self)
        

    def _connect_actions(self):
        """Connect actions to menubar."""
        self.exit_app.triggered.connect(lambda: exit())
        self.add_data_person.triggered.connect(self._run_table_add_custom)
        self.change_data_person.triggered.connect(self._run_table_change_custom)
        self.clear_data_person.triggered.connect(self._delete_custom)


    def _run_table_add_custom(self):
        """Add table of class AddCustomDialog"""
        self.dialog_window_add = AddCustomDialog()
        self.dialog_window_add.show()
        self.dialog_window_add.push_button_okey.clicked.connect(self.update_table)


    def _run_table_change_custom(self):
        """Add table of class ChangeCustomDialog"""
        if stat("database.json").st_size > 2:
            current_row = self.main_table.currentRow()
            self.dialog_window_change = ChangeCustomData(
                    self.main_table.item(current_row, 0).text(),
                    self.main_table.item(current_row, 1).text(),
                    self.main_table.item(current_row, 2).text(),
                    self.main_table.item(current_row, 3).text(),
                    )
            self.dialog_window_change.show()
            self.dialog_window_change.push_button_okey.clicked.connect(self.update_table)
        else:
            QMessageBox.information(self, "Ошибка", "Ваш файл пустой, " \
                    "поэтому изменять его нельзя!")


    def _delete_custom(self):
        if stat("database.json").st_size > 2:
            current_row = self.main_table.currentRow()
            self._write_data_in_database(current_row)
        elif stat("database.json").st_size == 0:
            QMessageBox.information(self, "Ошибка", "Ваш файл пустой, " \
                    "поэтому изменять его нельзя!")
        elif stat("database.json").st_size == 2:
            self.update_table()
        self.update_table()
        


    def _write_data_in_database(self, current_row):
        """Write dict with data of custom in JSON file."""

        with open("database.json", "r", encoding="utf-8") as json_file_read:
            if stat("database.json").st_size != 0:
                file_data = json.load(json_file_read)

                for key, data in list(file_data.items()):
                    if data[0] == self.main_table.item(current_row, 0).text() and \
                       data[1] == self.main_table.item(current_row, 1).text():
                       #data[2] == self.main_table.item(current_row, 2).text() and \
                       #data[2] == self.main_table.item(current_row, 3).text():
                           del file_data[key]

                with open("database.json", "w", encoding="utf-8") as json_file_append:
                    json_file_append.write(json.dumps(file_data,\
                            indent=4, ensure_ascii=False))


    def _create_table(self):
        """
        Create table in main window.
        Add database's information into this table
        """
        self.main_table = QTableWidget(self)
        self.main_table.setMinimumSize(550, 400)
        self.main_table.move(110, 100)
        # self.main_table.setRowCount(1)
        self.main_table.setColumnCount(4)

        self.main_table.setHorizontalHeaderLabels(["Фамилия", "Имя",
                                                   "Отчество", "Телефон"])


    def update_table(self):
        """Update main table after add/change/delete custom."""
        if stat("database.json").st_size > 2:
            with open("database.json", "r", encoding="utf-8") as file:
                json_data = json.load(file)
                row = 0
                for data in json_data.values():
                    self.main_table.setColumnCount(4)
                    self.main_table.setRowCount(row + 1)

                    self.main_table.setItem(row, 0, QTableWidgetItem(data[0]))
                    self.main_table.setItem(row, 1, QTableWidgetItem(data[1]))
                    self.main_table.setItem(row, 2, QTableWidgetItem(data[2]))
                    self.main_table.setItem(row, 3, QTableWidgetItem(data[3]))
                    row += 1  
        elif stat("database.json").st_size == 2:
            self.main_table.clear()

