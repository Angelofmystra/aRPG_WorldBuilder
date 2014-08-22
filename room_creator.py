#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class RoomCreator(QtGui.QWidget):

    def __init__(self):
        super(RoomCreator, self).__init__()

        self.initUI()

    def initUI(self):

        title = QtGui.QLabel('Name')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Desc')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        descriptionEdit = QtGui.QTextEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(descriptionEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Room Creator')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = RoomCreator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
