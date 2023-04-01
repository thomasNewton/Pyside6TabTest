from main_gui import *
from PySide6.QtWidgets import *



if __name__ == '__main__':
   ui=Ui_MainWindow()
   app =QApplication()
   window=QMainWindow()
   ui.setupUi(window)
   window.show()
  # window.setWindowTitle("My Main Window")     this  overrides the simmalr line in main gui....
   app.exec()









