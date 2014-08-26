#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QToolTip
from PyQt4.QtGui import QFont

################################################################
class Menu(QtGui.QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.resize(800,600)
        self.center()
        self.setWindowTitle('Character Creation')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg")))
        # Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        #
        # Strengths:
        # + Less variable handling
        # Weaknesses:
        # + Unable to assign tooltips
        # + DRY
        #
        grid.addWidget(QtGui.QPushButton("new"),0,0)
        grid.addWidget(QtGui.QPushButton("open"),0,1)
        grid.addWidget(QtGui.QPushButton("save"),0,2)
        grid.addWidget(QtGui.QPushButton("export"),0,3)
        grid.addWidget(QtGui.QPushButton("json"),0,4)
        #
        # Strengths:
        # + Less variable handling
        # Weaknesses:
        # + Unable to assign tooltips
        # + Pretty useless since you cant modify button names like this
        #
        for x in range(0,4):
            grid.addWidget(QtGui.QPushButton("btn"),1,x)
        #
        # Strengths:
        # + Less variable handling
        # Weaknesses:
        # + Unable to assign tooltips
        # + You must know the row in advance via this syntax
        #
        [grid.addWidget(QtGui.QPushButton(y),2,x) for x,y in enumerate(["A", "B", "C", "D", "E"])]

        #
        # Strengths:
        # + You get to practice your typing skills
        # + It looks like you've done alot of work due to the high lines of code
        #
        # Weakness:
        # + Continue with this approach and you will not have a concise program
        # +
        btn_create_world = QtGui.QPushButton('Create World', self)
        btn_create_world.setToolTip('This creates a new world for aRPG MUD.')
        btn_create_world.resize(btn_create_world.sizeHint())
        btn_create_world.move(50, 50)

        btn_load_world = QtGui.QPushButton('Load World', self)
        btn_load_world.setToolTip('This loads an existing world for aRPG MUD.')
        btn_load_world.resize(btn_load_world.sizeHint())
        btn_load_world.move(50, 100)

        #
        # Strengths:
        # + Less variable handling
        # + The least syntax heavy
        # Weaknesses:
        # +
        # +
        grid.addWidget(self.createButton("Swag",3,0,"Lots of swag"))
        #
        # Strengths:
        # +
        # + The least syntax heavy
        # Weaknesses:
        # + The createButton() approach does not work well with enumerate since you cant handle tooltips
        # +

        [grid.addWidget(self.createButton(y,4,x, "")) for x,y in enumerate(["Woo", "Meow", "Woof", "Jam"])]
        self.setPalette(palette)

        self.show()

    def createButton(self, name, x, y, tooltip):
        btn = QtGui.QPushButton(name, self)
        btn.move(x,y)
        btn.resize(btn.sizeHint())
        btn.setToolTip(tooltip)
        return btn

    def closeEvent(self, event):

        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def center(self):

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

################################################################
def main():

    app = QtGui.QApplication(sys.argv)
    menu = Menu()
    sys.exit(app.exec_())

################################################################

if __name__ == '__main__':
    main()
