
from PySide6 import QtWidgets, QtWebSockets, QtNetwork,QtCore
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QUrl
import sys


class Client(QtWebSockets.QWebSocket):
    def __init__(self, parent=None):
        super(Client, self).__init__('MyClient', QtWebSockets.QWebSocketProtocol.Version13, parent)
        self.textMessageReceived.connect(self.handleMessage)

    def handleMessage(self, message):
        mainWindow.messageEdit.appendPlainText(f'Received: {message}')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide6 WebSockets Client')
        self.connectButton = QtWidgets.QPushButton('Connect', self)
        self.connectButton.clicked.connect(self.connectToServer)
        self.disconnectButton = QtWidgets.QPushButton('Disconnect', self)
        self.disconnectButton.setEnabled(False)
        self.disconnectButton.clicked.connect(self.disconnectFromServer)
        self.sendButton = QtWidgets.QPushButton('Send', self)
        self.sendButton.setEnabled(False)
        self.sendButton.clicked.connect(self.sendMessage)
        self.hostLineEdit = QtWidgets.QLineEdit('localhost', self)
        self.hostLineEdit.setPlaceholderText('Enter server host...')
        self.portLineEdit = QtWidgets.QLineEdit('8080', self)
        self.portLineEdit.setPlaceholderText('Enter server port...')
        self.portLineEdit.setValidator(QIntValidator(0, 65535, self))
        self.messageLineEdit = QtWidgets.QLineEdit(self)
        self.messageLineEdit.setPlaceholderText('Enter message...')
        self.messageLineEdit.setEnabled(False)
        self.messageEdit = QtWidgets.QPlainTextEdit(self)
        self.messageEdit.setReadOnly(True)
        self.messageEdit.setPlaceholderText('Sent and received messages will be displayed here...')
        layout = QtWidgets.QVBoxLayout()
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.connectButton)
        buttonLayout.addWidget(self.disconnectButton)
        buttonLayout.addWidget(self.sendButton)
        layout.addWidget(self.hostLineEdit)
        layout.addWidget(self.portLineEdit)
        layout.addWidget(self.messageLineEdit)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.messageEdit)
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.client = None

    def connectToServer(self):
       # host = self.hostLineEdit.text()
        #port = int(self.portLineEdit.text())
        host ="localhost"
        port = 5555
        self.client = Client(self)
        self.client.open(QUrl(f'ws://{host}:{port}'))
        self.connectButton.setEnabled(False)
        self.disconnectButton.setEnabled(True)
        self.sendButton.setEnabled(True)
        self.hostLineEdit.setEnabled(False)
        self.portLineEdit.setEnabled(False)
        self.messageLineEdit.setEnabled(True)
        self.client.sendTextMessage("sent a message")

    def disconnectFromServer(self):
        self.client.close()
        self.connectButton.setEnabled(True)
        self.disconnectButton.setEnabled(False)
        self.sendButton.setEnabled(False)
        self.hostLineEdit.setEnabled(True)
        self.portLineEdit.setEnabled(True)
        self.messageLineEdit.setEnabled(False)

    def sendMessage(self):
        message = self.messageLineEdit.text()
        if message:
            self.client.sendTextMessage(message)
            self.messageEdit.appendPlainText(f'Sent: {message}')
            self.messageLineEdit.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
