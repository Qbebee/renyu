import sys
import os
from PyQt5 import QtWidgets, QtCore


#if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
    #widget = QtWidgets.QWidget()
    #widget.resize(800, 600)
    #widget.setWindowTitle("Hello, PyQt5")
    #widget.show()

import sys   
from PyQt5.QtWidgets import QApplication, QWidget, QStackedLayout, QVBoxLayout, QPushButton


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QStackedLayout()
        self.layout.addWidget(QPushButton("Button1"))
        self.layout.addWidget(QPushButton("Button2"))
        self.layout.addWidget(QPushButton("Button3"))
        self.layout.addWidget(QPushButton("Button4"))

        self.setLayout(self.layout)
        self.setWindowTitle("Stack Layout")
        # 设置栈顶显示第2个组件
        #self.layout.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())

#-----------------------------------
#©著作权归作者所有：来自51CTO博客作者天山老妖S的原创作品，请联系作者获取转载授权，否则将追究法律责任
#PyQt5快速入门（五）PyQt5布局管理
#https://blog.51cto.com/u_9291927/2423303

#-----------------------------------
#©著作权归作者所有：来自51CTO博客作者天山老妖S的原创作品，请联系作者获取转载授权，否则将追究法律责任
#PyQt5快速入门（一）PyQt5简介
#https://blog.51cto.com/u_9291927/2422184
