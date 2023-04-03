# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab2doVuuG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from cyphers import rkc, rkc_reverse



class Ui_Tab2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1180, 660)
        Form.setBaseSize(QSize(1180, 660))
        Form.setWindowTitle(u"Tab 2")

        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.0113636, x2:1, y2:1, stop:0 rgba(238, 231, 219, 255), stop:0.949153 rgba(219, 216, 255, 255));")
        self.widget = QWidget(Form)
        self.key = []
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 90, 651, 561))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 2, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.plainTextEdit_2 = QPlainTextEdit(self.widget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.verticalLayout.addWidget(self.plainTextEdit_2)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.plainTextEdit_3 = QPlainTextEdit(self.widget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.verticalLayout.addWidget(self.plainTextEdit_3)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 30, 651, 50))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 2)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(710, 30, 381, 221))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.textBrowser = QTextBrowser(self.widget2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.retranslateUi(Form)
        self.lineEdit.textChanged.connect(self.key_changed)


        pixmap = QPixmap("gd1.png")
        background_label = QLabel(Form)
        background_label.setPixmap(pixmap)
        background_label.setGeometry(700, 260, 200, 400)
        QMetaObject.connectSlotsByName(Form)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(940, 280, 150, 150))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(940, 480, 150, 150))
        self.pushButton.setText("Encode")
        self.pushButton_2.setText("UnEncode")
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.068, y1:0.063, x2:1, y2:1, stop:0 rgba(230, 196, 223, 255), stop:1 rgba(209, 221, 134, 255));")
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.068, y1:0.063, x2:1, y2:1, stop:0 rgba(230, 196, 223, 255), stop:1 rgba(209, 221, 134, 255));")
        self.pushButton.clicked.connect(self.encode)
        self.pushButton_2.clicked.connect(self.unencode)









    def key_changed(self):
        txt =self.lineEdit.text()
        display =''
        self.key.clear()
        for x in txt:
            if x.isalpha():
                x=x.upper()
                self.key.append(ord(x)-65)
                display += f"{str(ord(x)-65)},"

        self.lineEdit_2.setText(display)



    def encode(self):
        if self.lineEdit.text() == '':
            self.lineEdit.setText("Swordfish, Its always Swordfish. Do you use your dogs name?")
        if self.plainTextEdit.toPlainText() == "":
            self.plainTextEdit.setPlainText("No Sample Text in the text field, so we put some in.  Notice that only letters\n"
    "will be encoded in this algorithem.  You can still read punctuation and numbers and spaces:!@#$%^ and 123456\n"
            "will be the same BUT THE WAY THIS IS WRITTEN, CAPITILIZATION WILL BE PRESERVED!!!!!\n"
            " We are doing the mapping twice, Once for the CapitoL Letters, and Again For The Lowercase, can you improve?\n"
            "  ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrtsuvwxyz 1234567890")

        self.plainTextEdit_2.setPlainText(rkc(self.plainTextEdit.toPlainText(),self.key))



    def unencode(self):

        self.plainTextEdit_3.setPlainText(rkc_reverse(self.plainTextEdit_2.toPlainText(),self.key))





    def retranslateUi(self, Form):
        self.label_4.setText(QCoreApplication.translate("Form", u"Enter Text", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Crypto Text", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Unencoded Text", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter the key string:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"The shift key", None))
        self.label.setText(QCoreApplication.translate("Form", u"The Running Key Cypher", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In this cypher we make the key more complex.  We will use an array of transform values, and change the value for each character.  If the string is longer than the key we will loop back around and start from the begginning. To get the key array, we will use the the letters in a key string.  If our key string is ABD we would use the shift keys 0,1,3 repeatedly on the string.  </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We will use the ord() value of the l"
                        "etters in the key string to get the key values. To avoid to much complexity, we will use only letters for our shift keys, A and a have the same value, no shift 0, and Z z will represent a shift of 25. Spaces and other symbols will be ignored for the shift key.</p></body></html>", None))
        pass
    # retranslateUi

