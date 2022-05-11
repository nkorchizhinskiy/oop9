import sys

#// PyQt
from PyQt5.QtWidgets import QMainWindow, \
                            QMenu, \
                            QMenuBar, \
                            QAction




class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Лабораторная работа 9")
        self.setFixedSize(800, 600)

        #// Run functions
        self._create_actions()
        self._create_widgets()
        self._connect_actions() 


    def _create_widgets(self) -> None:
        """Create widgets in QMainWindow."""
        self.menu_bar = QMenuBar(self)

        self.menu_operation = QMenu("Операции")
        self.menu_operation.addAction(self.add_data_person)
        self.menu_operation.addAction(self.change_data_person)
        self.menu_operation.addAction(self.clear_data_person)

        self.menu_exit = QMenu("Выход")

        self.menu_bar.addMenu(self.menu_operation)
        self.menu_bar.addMenu(self.menu_exit)

        self.setMenuBar(self.menu_bar)


    def _create_actions(self) -> None:
        """Create actions to menu."""
        self.add_data_person = QAction("Добавить клиента", self)
        self.change_data_person = QAction("Изменить данные", self)
        self.clear_data_person = QAction("Удалить клиента", self)
        

    def _connect_actions(self):
        """Connect actions to menubar."""
        pass
