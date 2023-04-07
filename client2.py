
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client2oxBOVq.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QAbstractSocket
from PySide6.QtWebSockets import QWebSocket



# Create a subclass of QWebSocket to handle WebSocket client operations
class MyClient(QWebSocket):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.connected.connect(self.onConnected)
        self.disconnected.connect(self.onDisconnected)
        self.textMessageReceived.connect(self.onTextMessageReceived)

    def connectToServer(self, url):
        # Connect to the specified WebSocket server URL
        self.open(QUrl(url))

    def onConnected(self):
        # Handle WebSocket client connection established
        print("Connected to WebSocket server")

    def onDisconnected(self, closeCode):
        # Handle WebSocket client connection closed
        print("Disconnected from WebSocket server with code: {}".format(closeCode))

    def onTextMessageReceived(self, message):
        # Handle incoming text message
        print("Received message: {}".format(message))








class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(455, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 421, 497))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 4, 2, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 2)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 4)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.splitter.addWidget(self.textBrowser)
        self.textBrowser_2 = QTextBrowser(self.splitter)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.splitter.addWidget(self.textBrowser_2)

        self.gridLayout.addWidget(self.splitter, 4, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 455, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.start_client)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"message", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5555", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"client", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"url", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Connet", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi


    def start_client(self):
        self.client =MyClient()
        self.client.connectToServer('localhost:5555')
        self.client.sendTextMessage("hi from c to s")
        print("in start client")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
