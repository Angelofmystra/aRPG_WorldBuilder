#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QToolTip
from PyQt4.QtGui import QFont

# My current intention is to have each window as a separate class.
class Menu(QtGui.QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('World Builder')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg")))
        btn_create_world = QtGui.QPushButton('Create World', self)
        btn_load_world = QtGui.QPushButton('Load World', self)
        btn_create_world.setToolTip('This creates a new world for aRPG MUD.')
        btn_load_world.setToolTip('This loads an existing world for aRPG MUD.')
        btn_create_world.resize(btn_create_world.sizeHint())
        btn_load_world.resize(btn_load_world.sizeHint())
        btn_create_world.move(50, 50)
        btn_load_world.move(50, 100)


        self.setPalette(palette)

        self.show()
    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():

    app = QtGui.QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
