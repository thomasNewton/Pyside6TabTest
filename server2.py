import sys

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'server2kCcHXn.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QCoreApplication, QUrl
from PySide6.QtWebSockets import QWebSocketServer, QWebSocket
from PySide6.QtNetwork import QHostAddress




# Create a subclass of QWebSocket to handle incoming connections
class MyWebSocket(QWebSocket):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textMessageReceived.connect(self.processTextMessage)

    def processTextMessage(self, message):
        print("the server got a message  process text message triggered")
        # Handle incoming text message
        pass
        # Add your message handling logic here

# Create a subclass of QWebSocketServer to handle WebSocket server operations
class MyServer(QWebSocketServer):
    def __init__(self, port, parent=None):
        super().__init__("MyWebSocketServer", QWebSocketServer.NonSecureMode, parent)
        self.listen(QHostAddress.LocalHost, 5555)
        self.newConnection.connect(self.onNewConnection)

    def onNewConnection(self):
        # Handle new WebSocket connection
        print("from server On New Conneciton.... client sent message?")
        pass
        # Add your connection handling logic here








class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(367, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 341, 501))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.textBrowser = QTextBrowser(self.splitter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.splitter.addWidget(self.textBrowser)
        self.textBrowser_2 = QTextBrowser(self.splitter)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.splitter.addWidget(self.textBrowser_2)

        self.gridLayout_2.addWidget(self.splitter, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 367, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.start_server)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"5555", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  Server ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"url", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"message", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"hellow client", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"send", None))
    # retranslateUi

    def start_server(self):
        print("in start server")
        self.server =MyServer(5555)
        if self.server.isListening():
            print("WebSocket server is listening on port {}".format(self.server.serverPort()))
        else:
            print("Failed to start WebSocket server!")
            pass












if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
