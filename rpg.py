#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QPalette
from PyQt4.QtGui import QBrush
from PyQt4.QtGui import QPixmap
from PyQt4.QtGui import QToolTip
from PyQt4.QtGui import QFont
from PyQt4.QtCore import pyqtSlot

import functools

################################################################
# I used functools.partial in order to have a self.createButton()
# which took as a parameter a function in order to facilitate
# code reuse.
################################################################




################################################################
# ============================================================ #
################################################################
        # Host Server Window #
################################################################
# ============================================================ #
################################################################


class Menu(QtGui.QWidget):

    def __init__(self):
        super(Menu, self).__init__()

        self.initUI()
        self.window2 = None

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.center()
        self.setWindowTitle('RPG')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg")))
        # Layout
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
################################################################
        # BUTTONS #
################################################################
        grid.addWidget(self.createButton(
                                        "Start Client",
                                        0,
                                        0,
                                        "Click this to look for servers",
                                        functools.partial(self.end)
                                        ))
        grid.addWidget(self.createButton(
                                        "Start Server",
                                        1,
                                        0,
                                        "Click this to host a server",
                                        functools.partial(self.start_server)
                                        ))
        grid.addWidget(self.createButton(
                                        "Update",
                                        2,
                                        0,
                                        "Click this to update the client",
                                        functools.partial(self.end)
                                        ))
        grid.addWidget(self.createButton(
                                        "Documentation",
                                        3,
                                        0,
                                        "Click this to view the help files",
                                        functools.partial(self.end)
                                        ))
        grid.addWidget(self.createButton("Quit",
                                        4,
                                        0,
                                        "Click this to close the software",
                                        functools.partial(self.end)
                                        ))
        self.setPalette(palette)

        self.show()
################################################################
        # FUNCTIONS #
################################################################

    def createButton(self, name, x, y, tooltip, func):
        btn = QtGui.QPushButton(name, self)
        btn.move(x,y)
        btn.resize(btn.sizeHint())
        btn.setToolTip(tooltip)
        btn.clicked.connect(func)
        return btn

    @pyqtSlot()
    def start_server(self):
        if self.window2 is None:
            self.window2 = HostServer()
        self.window2.show()
        self.close

    @pyqtSlot()
    def start_client(self):
        return 0

    @pyqtSlot()
    def update_client(self):
        return 0

    @pyqtSlot()
    def view_doc(self):
        return 0

    @pyqtSlot()
    def end(self):
        self.close()

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
# ============================================================ #
################################################################
        # Host Server Window #
################################################################
# ============================================================ #
################################################################


class HostServer(QtGui.QWidget):

    def __init__(self):
        super(HostServer, self).__init__()

        self.initUI()

    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        self.center()
        self.setWindowTitle('Host')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg")))
        # Layout
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
################################################################
        # BUTTONS #
################################################################
        server_name = QtGui.QLabel('Server Name')
        server_admin = QtGui.QLabel('Server Admin')
        ip_address = QtGui.QLabel('IP Address')
        port_number = QtGui.QLabel('Port Number')
        server_description = QtGui.QLabel('Server Description')

        server_nameEdit = QtGui.QLineEdit()
        server_adminEdit = QtGui.QLineEdit()
        ip_addressEdit = QtGui.QLineEdit()
        port_numberEdit = QtGui.QLineEdit()
        server_descriptionEdit = QtGui.QTextEdit()

        grid.addWidget(server_name,1,0)
        grid.addWidget(server_nameEdit,1,1)
        grid.addWidget(server_admin,2,0)
        grid.addWidget(server_adminEdit,2,1)
        grid.addWidget(ip_address,3,0)
        grid.addWidget(ip_addressEdit,3,1)
        grid.addWidget(port_number,4,0)
        grid.addWidget(port_numberEdit,4,1)
        grid.addWidget(server_description,5,0)
        grid.addWidget(server_descriptionEdit,5,1)

        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        grid.addWidget(okButton,6,0)
        grid.addWidget(cancelButton,6,1)

        self.setLayout(grid)

        self.setPalette(palette)

        self.show()
################################################################
        # FUNCTIONS #
################################################################

    def createButton(self, name, x, y, tooltip, func):
        btn = QtGui.QPushButton(name, self)
        btn.move(x,y)
        btn.resize(btn.sizeHint())
        btn.setToolTip(tooltip)
        btn.clicked.connect(func)
        return btn

    @pyqtSlot()
    def start_server(self):
        host = HostServer()

    @pyqtSlot()
    def start_client(self):
        return 0

    @pyqtSlot()
    def update_client(self):
        return 0

    @pyqtSlot()
    def view_doc(self):
        return 0

    @pyqtSlot()
    def end(self):
        self.close()

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
# ============================================================ #
################################################################
        # Main #
################################################################
# ============================================================ #
################################################################

################################################################
def main():

    app = QtGui.QApplication(sys.argv)
    window = Menu()
    window.show()
    sys.exit(app.exec_())

################################################################

if __name__ == '__main__':
    main()
