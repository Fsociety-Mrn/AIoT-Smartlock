import sys,background


from PyQt5.QtWidgets import QApplication
from pages.Main_Menu import MainWindow

# from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    # Create a new QApplication object
    app = QApplication(sys.argv)
 
    New_menu = MainWindow()
    New_menu.show()

    sys.exit(app.exec_()) 