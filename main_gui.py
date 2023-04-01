
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from tab3 import *
from tab2 import *
from tab1 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1180, 700))


    # -------------------------------------------------------------- custom code section_______________________________
    # idea is:  create and add the tab as a simple widget, then create the tab ui and set the tab ui parent to the tab

        self.tab1 = QWidget()
        self.ui1 = Ui_Tab1()
        self.ui1.setupUi(self.tab1)
        self.tabWidget.addTab(self.tab1, 'Tab1')
        self.tab1.setStyleSheet(u"color: rgb(40, 34, 57);\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0.058, x2:0.521, y2:0.248, stop:0.0227273 rgba(156, 158, 179, 255), stop:0.545455 rgba(184, 198, 208, 255));\n"
"font: 700 14pt \"Segoe Print\";")


        self.tab2 = QWidget()
        self.ui2 = Ui_Tab2()
        self.ui2.setupUi(self.tab2)
        self.tabWidget.addTab(self.tab2, 'Tab2')


        self.tab3 = QWidget()
        self.ui3 = Ui_Tab3()
        self.ui3.setupUi(self.tab3)
        self.tabWidget.addTab(self.tab3,'Tab3')

    #_____________________________________________________________ end of section to add tabs__________________________

        icon = QIcon()
        icon.addFile(u"usmc.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

       # self.tabWidget.


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Cypher Demo")


      #  self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))




