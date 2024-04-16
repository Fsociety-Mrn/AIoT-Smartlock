import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel, QDialogButtonBox,QDialog,QDesktopWidget
from PyQt5.QtGui import QPixmap

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

class Dialog(QDialog):
    def __init__(self, warning_text="", image_path="", parent=None):
        super().__init__(parent)
        
        self.setObjectName("Dialog")
        self.setWindowModality(QtCore.Qt.NonModal)
        self.resize(700, 500)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 801, 501))
        self.widget.setStyleSheet("background-color: #f5f5f5;")
        self.widget.setObjectName("widget")
        
        self.Warning = QtWidgets.QLabel(self.widget)
        self.Warning.setGeometry(QtCore.QRect(0, 0, 701, 121))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.Warning.setFont(font)
        self.Warning.setTextFormat(QtCore.Qt.MarkdownText)
        self.Warning.setAlignment(QtCore.Qt.AlignCenter)
        self.Warning.setObjectName("Warning")
        self.Warning.setText(warning_text)
        
        self.Picture = QtWidgets.QLabel(self.widget)
        self.Picture.setGeometry(QtCore.QRect(150, 110, 411, 311))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Picture.setFont(font)
        self.Picture.setText("")

        if image_path:
            self.Picture.setPixmap(QtGui.QPixmap(image_path))
            
        self.Picture.setScaledContents(True)
        self.Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.Picture.setObjectName("Picture")
        

        
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(260, 440, 191, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
        "\n"
        "border-radius: 15px;\n"
        "color: white;\n"
        "padding: 10px;")
        
        # Center the main window
        self.center()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
       
        # self.Warning.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Reminder: Before authenticating, please remove any glasses or headgear.</span></p><p align=\"center\"><span style=\" font-size:11pt;\">If you keep them on, it might be harder for us to recognize you.</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Thank you!</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "okay"))
        # Connect the clicked signal of the push button to close the dialog
        self.pushButton.clicked.connect(self.close_dialog)
        


    def center(self):
        # Get the center point of the screen
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def close_dialog(self):
        self.close()
        


            
    
# def main():
#     app = QApplication([])

#     msg = MessageBox()

#     msg.setWindowTitle("Software Update")
#     msg.setText("A software update is available.Do you want to update now?")
#     msg.setStandardButtons(QMessageBox.Ok)
#     msg.setStyleSheet("""
#                       QLabel{
#                           min-width: 600px; 
#                           min-height: 50px; 
#                           font-size: 20px;
#                         }
#                                           QPushButton { 
#                       width: 250px; 
#                       height: 30px; 
#                       font-size: 15px;
#                   }
#                     """)

#     msg.exec_()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#         # Define the warning text and image path
#     warning_text = "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Reminder: Before authenticating, please remove any glasses or headgear.</span></p><p align=\"center\"><span style=\" font-size:11pt;\">If you keep them on, it might be harder for us to recognize you.</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Thank you!</span></p></body></html>"
#     image_path = "Images/WARNING.png"
#     dialog = Dialog(warning_text, image_path)
#     dialog.exec_()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()
