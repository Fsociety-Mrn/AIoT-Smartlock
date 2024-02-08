from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QDialogButtonBox


class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        

        grid_layout = self.layout()

        qt_msgboxex_icon_label = self.findChild(QLabel, "qt_msgboxex_icon_label")
        qt_msgboxex_icon_label.deleteLater()

        qt_msgbox_label = self.findChild(QLabel, "qt_msgbox_label")
        qt_msgbox_label.setAlignment(Qt.AlignCenter)
        qt_msgbox_label.setMinimumWidth(400)  # Set minimum width
        grid_layout.removeWidget(qt_msgbox_label)

        qt_msgbox_buttonbox = self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        grid_layout.removeWidget(qt_msgbox_buttonbox)

        grid_layout.addWidget(qt_msgbox_label, 0, 0, alignment=Qt.AlignCenter)
        grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0, alignment=Qt.AlignCenter)
        
        # Set a fixed size for the message box
        self.setFixedSize(800, 600)


def main():
    app = QApplication([])

    msg = MessageBox()

    msg.setWindowTitle("Software Update")
    msg.setText("A software update is available.Do you want to update now?")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setStyleSheet("""
                      QLabel{
                          min-width: 600px; 
                          min-height: 50px; 
                          font-size: 20px;
                        }
                                          QPushButton { 
                      width: 250px; 
                      height: 30px; 
                      font-size: 15px;
                  }
                    """)

    msg.exec_()


# if __name__ == "__main__":
#     main()
