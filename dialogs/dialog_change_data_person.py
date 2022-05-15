from PyQt5.QtWidgets import QDialog, \
                            QPushButton, \
                            QLineEdit, \
                            QLabel



class ChangeCustomDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Change data of custom")
        #// Run fucntions
        self._create_widgets()
    
    
    def _create_widgets(self):
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
        
        #// Moving LineEdits
        self.line_edit_surname.move(10, 40)
        self.line_edit_name.move(100, 80)
        self.line_edit_second_name.move(100, 120)
        self.line_edit_phone_number.move(100, 160)

        #// Create PushButtons
        self.push_button_okey = QPushButton("Продолжить", self)
        self.push_button_cancel = QPushButton("Отменить", self)

        #// Moving PushButtons
        self.push_button_cancel.move(60, 200)
        self.push_button_okey.move(160, 200)

        

