#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPixmap

# My current intention is to have each window as a separate class.
class Menu(QtGui.QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('World Builder')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg")))

        self.setPalette(palette)

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
