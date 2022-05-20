import sys
import call3
from PyQt5.QtWidgets import QApplication , QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = QMainWindow()
    ui = call3.Ui_Form()
    ui.setupUi(mywindow)
    mywindow.show()
    sys.exit(app.exec_())

