from sys import exit

#// PyQt
from PyQt5.QtWidgets import QMainWindow, \
                            QMenu, \
                            QMenuBar, \
                            QAction, QTableWidget




class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("lab work 9")
        self.setFixedSize(800, 600)

        #// Run functions
        self._create_actions()
        self._create_widgets()
        self._connect_actions() 
        self._create_table()


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


    def _create_table(self):
        """
        Create table in main window.
        Add database's information into this table
        """
        self.main_table = QTableWidget(self)
        self.main_table.setMinimumSize(550, 400)
        self.main_table.move(110, 100)
        self.main_table.setRowCount(1)
        self.main_table.setColumnCount(4)

        self.main_table.setHorizontalHeaderLabels(["Фамилия", "Имя",
                                                   "Отчество", "Телефон"])
        
