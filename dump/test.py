from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *



Dialog = QDialog()
Dialog.setWindowTitle("Pin Code Dialog")
Dialog.setModal(True)  # Make the dialog modal
        
Dialog.resize(461, 307)
Dialog.setStyleSheet("background-image:url(Images/background-removebg-preview.png);\n"
        "background-color: rgb(231, 229, 213);")

username = QtWidgets.QLineEdit(Dialog)
username.setGeometry(QtCore.QRect(30, 60, 401, 51))
font = QtGui.QFont()
font.setFamily("Segoe UI")
font.setPointSize(14)
username.setFont(font)
username.setStyleSheet("background: transparents;\n"
"color: #3D989A;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #3D989A;\n"
"border-radius: 25px;")
username.setAlignment(QtCore.Qt.AlignCenter)
username.setObjectName("username")
username.setPlaceholderText("Email")
        
        # layout = QVBoxLayout(Dialog)
        # Dialog.setLayout(layout)

        # label = QLabel("Enter your pin code:", Dialog)
        # layout.addWidget(label)

        # pincode_edit = QLineEdit(Dialog)
        # layout.addWidget(pincode_edit)

        # button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Dialog)
        # button_box.accepted.connect(Dialog.accept)
        # button_box.rejected.connect(Dialog.reject)
        # layout.addWidget(button_box)
        
Dialog.exec_()