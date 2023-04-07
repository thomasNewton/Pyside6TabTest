# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a_serv1NfmkOd.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(420, 420)
        self.setWindowTitle('Websocket Server')
        self.start_button = QPushButton('Start Server')
        self.stop_button = QPushButton("Stop Server")
        self.send_button = QPushButton("Send Message")
        self.gla =  QGridLayout()
        self.gla.addWidget(self.start_button)
        self.gla.addWidget(self.stop_button)
        self.gla.addWidget(self.send_button)
        self.centralWidget =QWidget()
        self.centralWidget.setLayout(self.gla)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app =QApplication()
    window = Ui_MainWindow()
    window.show()
    app.exec()