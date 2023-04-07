import asyncio
from PySide6 import QtCore, QtWidgets, QtNetwork, QtWebSockets


class WebSocketClient(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the GUI
        self.setWindowTitle('WebSocket Client')
        self.setMinimumSize(640, 480)

        # Create the message input field and send button
        self.message_input = QtWidgets.QLineEdit()
        self.send_button = QtWidgets.QPushButton('Send')
        self.send_button.clicked.connect(self.on_send_clicked)
        input_layout = QtWidgets.QHBoxLayout()
        input_layout.addWidget(self.message_input)
        input_layout.addWidget(self.send_button)

        # Create the message area
        self.message_area = QtWidgets.QTextEdit()
        self.message_area.setReadOnly(True)

        # Add the widgets to the main window
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addWidget(self.message_area)
        self.setLayout(layout)

        # Set up the network connection
        self.socket = QtWebSockets.QWebSocket()
        self.socket.connected.connect(self.on_connected)
        self.socket.disconnected.connect(self.on_disconnected)
        self.socket.textMessageReceived.connect(self.on_message_received)

    def on_connected(self):
        self.log_message('Connected to server')

    def on_disconnected(self):
        self.log_message('Disconnected from server')

    def on_message_received(self, message):
        self.log_message('Server response: {}'.format(message))

    def on_send_clicked(self):
        message = self.message_input.text()
        self.socket.sendTextMessage(message)
        self.log_message('Sent message: {}'.format(message))

    def log_message(self, message):
        self.message_area.append(message)

    def start(self):
        self.socket.open(QtCore.QUrl('ws://localhost:8888'))

    def stop(self):
        self.socket.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    client = WebSocketClient()
    client.show()
    client.start()
    app.exec_()
