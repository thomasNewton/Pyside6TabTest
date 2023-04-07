import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QColor, QPainter, QBrush, QPen, QFont
from PySide6.QtCore import Qt, QRectF

class MatrixWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Matrix Widget')
        self.setGeometry(100, 100, 300, 300)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setGeometry(50, 50, 200, 200)
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.angle = 0

    def setAngle(self, value):
        self.angle = value
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255, 255, 255))
        painter.setBrush(brush)
        painter.drawRect(0, 0, self.width() - 1, self.height() - 1)

        painter.translate(self.width() / 2, self.height() / 2)
        painter.rotate(self.angle)

        font = QFont()
        font.setPixelSize(50)
        painter.setFont(font)

        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem(str(self.matrix[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.render(painter, QRectF(-100, -100, 200, 200), self.tableWidget.viewportRegion())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrixWidget = MatrixWidget()
    matrixWidget.show()
    sys.exit(app.exec())
