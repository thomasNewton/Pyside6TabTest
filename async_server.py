import asyncio
import threading
import websockets
from PySide6 import QtCore, QtWidgets

class ServerThread(threading.Thread):
    def __init__(self, gui):
        super().__init__()
        self.gui = gui

    def run(self):
        asyncio.run(self.gui.start_server())

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.setWindowTitle('Websocket Server')
        self.setMinimumSize(640, 480)

        # Create the start/stop server button
        s
        self.start_button.clicked.connect(self.on_start_clicked)
        self.stop_button = QtWidgets.QPushButton('Stop Server')
        self.stop_button.clicked.connect(self.on_stop_clicked)
        self.stop_button.setEnabled(False)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)

        # Create the message area
        self.message_area = QtWidgets.QTextEdit()
        self.message_area.setReadOnly(True)

        # Add the widgets to the main window
        central_widget = QtWidgets.QWidget()
        central_layout = QtWidgets.QVBoxLayout()
        central_layout.addLayout(button_layout)
        central_layout.addWidget(self.message_area)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Set up the server thread
        self.server_thread = ServerThread(self)
        self.server_running = False

    async def handle_websocket(self, websocket, path):
        async for message in websocket:
            if message == 'a':
                response = '1'
            elif message == 'b':
                response = '2'
            elif message == 'c':
                response = '3'
            else:
                response = 'Invalid input'
            await websocket.send(response)

    async def start_server(self):
        async with websockets.serve(self.handle_websocket, 'localhost', 8888):
            self.server_running = True
            self.log_message('Server started on localhost:8888')
            while self.server_running:
                await asyncio.sleep(1)
            self.log_message('Server stopped')

    def on_start_clicked(self):
        # Start the server thread
        self.server_thread.start()

        # Update the GUI
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def on_stop_clicked(self):
        # Stop the server thread
        self.server_running = False

        # Update the GUI
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def log_message(self, message):
        self.message_area.append(message)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
