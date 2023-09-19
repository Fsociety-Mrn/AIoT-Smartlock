import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu Example")
        self.setGeometry(300, 300, 400, 300)

        self.settings_btn = QPushButton("Settings", self)
        self.settings_btn.setGeometry(10, 10, 80, 30)
        self.settings_btn.clicked.connect(self.showMenu)

        self.menu = QMenu(self)
        self.menu.addAction(QAction("Option 1", self))
        self.menu.addAction(QAction("Option 2", self))
        self.menu.addAction(QAction("Option 3", self))

    def showMenu(self):
        self.menu.exec_(self.settings_btn.mapToGlobal(self.settings_btn.rect().bottomLeft()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
