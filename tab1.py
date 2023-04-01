

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from cyphers import *

class Ui_Tab1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1180, 660)
        font = QFont()
        font.setFamily(u"Segoe UI Emoji")
        Form.setFont(font)
        Form.setWindowTitle(u"tab1")
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.058, x2:0.521, y2:0.248, stop:0.0227273 rgba(156, 158, 179, 255), stop:0.545455 rgba(184, 198, 208, 255));")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 1160, 660))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setText(u"The Ceaser Cypher:  ")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.textEdit_2, 5, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(150, 146, 177);")

        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.textEdit, 2, 0, 2, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(150, 146, 177);")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)

        self.textEdit_3 = QTextEdit(self.widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
#__________________________________________add action listeners
        self.pushButton.clicked.connect(self.encode)
        self.pushButton_2.clicked.connect(self.unencode)
        self.gridLayout.addWidget(self.textEdit_3, 7, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter Original Text", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"The Cypher-Text", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Unencoded Text", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Unencode", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Encode", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Enter Key:", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"13", None))
        pass
    # retranslateUi

    def encode(self):
        if self.textEdit.toPlainText() == "":
            self.textEdit.setText("The text field was empty, so we will add a sample string to test out.\n"
            " ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890")
        else:
            self.textEdit_2.setText(caeser(self.textEdit.toPlainText(),self.lineEdit.text()))

    def unencode(self):
        self.textEdit_3.setText(caeser(self.textEdit_2.toPlainText(), 26-int(self.lineEdit.text())))