import sys

#// PyQt
from PyQt5.QtWidgets import QApplication

#// Custom
from logic import MainWindow


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
