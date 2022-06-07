import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon #添加图标

class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None): #初始化
        super(FirstMainWindow, self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('第一个主窗口')
        #设置窗口尺寸
        self.resize(300,400)
        #获取状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('../python/111.ico'))
    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())
