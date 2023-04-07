import sys
from PySide6 import QtWidgets, QtWebSockets, QtNetwork,QtCore
from PySide6.QtGui import QIntValidator
class Server(QtWebSockets.QWebSocketServer):
    def __init__(self, parent=None):
        super(Server, self).__init__('MyServer', QtWebSockets.QWebSocketServer.NonSecureMode, parent)
        self.clients = []

    def incomingConnection(self, socketDescriptor):
        print("in coming detected")
        client = self.nextPendingConnection()
        client.textMessageReceived.connect(self.handleMessage)
        client.disconnected.connect(self.handleDisconnect)
        self.clients.append(client)

    def handleMessage(self, message):
        for client in self.clients:
            client.sendTextMessage(message)

    def handleDisconnect(self):
        client = self.sender()
        self.clients.remove(client)
        client.deleteLater()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PySide6 WebSockets Server')
        self.startButton = QtWidgets.QPushButton('Start', self)
        self.startButton.clicked.connect(self.startServer)
        self.stopButton = QtWidgets.QPushButton('Stop', self)
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stopServer)
        self.sendButton = QtWidgets.QPushButton('Send', self)
        self.sendButton.setEnabled(False)
        self.sendButton.clicked.connect(self.sendMessage)
        self.portLineEdit = QtWidgets.QLineEdit('8080', self)
        self.portLineEdit.setPlaceholderText('Enter port number...')
        self.portLineEdit.setValidator(QIntValidator(0, 65535, self))
        self.messageLineEdit = QtWidgets.QLineEdit(self)
        self.messageLineEdit.setPlaceholderText('Enter message...')
        self.messageLineEdit.setEnabled(False)
        self.messageEdit = QtWidgets.QPlainTextEdit(self)
        self.messageEdit.setReadOnly(True)
        self.messageEdit.setPlaceholderText('Received messages will be displayed here...')
        self.notificationEdit = QtWidgets.QPlainTextEdit(self)
        self.notificationEdit.setReadOnly(True)
        self.notificationEdit.setMaximumHeight(50)
        self.notificationEdit.setPlaceholderText('Server started/stopped messages will be displayed here...')
        layout = QtWidgets.QVBoxLayout()
        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.startButton)
        buttonLayout.addWidget(self.stopButton)
        buttonLayout.addWidget(self.sendButton)
        layout.addWidget(self.portLineEdit)
        layout.addWidget(self.messageLineEdit)
        layout.addLayout(buttonLayout)
        layout.addWidget(self.messageEdit)
        layout.addWidget(self.notificationEdit)
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.server = None

    def startServer(self):
        #port = int(self.portLineEdit.text())
        port = 5555
        self.server = Server(self)
        if self.server.listen(QtNetwork.QHostAddress.LocalHost, port):
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)
            self.sendButton.setEnabled(True)
            self.portLineEdit.setEnabled(False)
            self.messageLineEdit.setEnabled(True)
            self.notificationEdit.setPlainText(f'Server started on port {port}')
        else:
            QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to start server on port {port}')

    def stopServer(self):
        self.server.close()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.sendButton.setEnabled(False)
        self.portLineEdit.setEnabled(True)
        self.messageLineEdit.setEnabled(False)
        self.notificationEdit.setPlainText('Server stopped')

    def sendMessage(self):
        message = self.messageLineEdit.text()
        if message:
            for client in self.server.clients:
                client.sendTextMessage(message)
            self.messageLineEdit.clear()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
