import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QFileDialog

import call

class log_window(call.Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(log_window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.display_page1)
        self.pushButton_2.clicked.connect(self.display_page2)
        self.pushButton_3.clicked.connect(self.display_page3)



    def display_page1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_page3(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        #未main_window类和login_window类创建对象
        main_window = log_window()
        main_window.show()
        sys.exit(app.exec_())



