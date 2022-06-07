import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget,QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __int__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('XXX')
        self.resize(980, 450)
        #窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

         #创建布局
        layout = QVBoxLayout()
        #1.创建顶部的菜单布局
        header_layout = QHBoxLayout()
        #1.1创建按钮，加入headre_layout
        btn_start = QPushButton('开始')
        header_layout.addWidget(self.btn_star)
        mainframe = QWidget()
        mainframe.setLayout(header_layout)
        self.setCentralWidget(mainframe)

        #2.创建上面的菜单布局
        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)

        #3.创建中间的菜单布局
        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)

        #4.创建底部的菜单布局
        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())