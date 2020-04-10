from PyQt5.QtWidgets import QWidget,QLineEdit,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passlib.hash import sha256_crypt
from encryption import encrypt

class passwordClass(QWidget):
    def __init__(self,data):
        super(passwordClass,self).__init__()
        self.data = data
        self.initUI()
    def initUI(self):
        self.horizontalLay = QHBoxLayout()
        self.passwordLE = QLineEdit()
        #self.passwordLE.setEchoMode(True)

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.savePassword)
        self.horizontalLay.addWidget(self.passwordLE)
        self.horizontalLay.addWidget(self.button)
        self.setLayout(self.horizontalLay)

    def savePassword(self):
        self.password = self.passwordLE.text()
        self.hashed = sha256_crypt.hash(self.password)
        with open("hashed.txt","w") as file:
            file.write(self.hashed)

        self.password = self.password.encode("utf-8")
        self.data = self.data.encode("utf-8")
        encrypted = encrypt(self.password,self.data)
        with open("encrypted.txt","w") as file:
            file.write(encrypted)

        self.message = QLabel("Congrulations!")
        self.message.show()
        self.close()