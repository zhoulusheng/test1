import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QHBoxLayout, QWidget, QPushButton

class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None): #初始化
        super(FirstMainWindow, self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('第一个主窗口')
        #设置窗口尺寸
        self.resize(300,400)

        # 添加按钮
        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onclick_button)
        # 创建布局：把按钮放到布局上
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        #将水平布局放到窗口上
        mainframe = QWidget()
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe) # 充满屏幕



        #获取状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
    # 添加按钮单击事件的方法
    def onclick_button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()



    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        new_left = (screen.width()-size.width())/2
        new_top = (screen.height()-size.height())/2

        self.move(new_left,new_top)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())