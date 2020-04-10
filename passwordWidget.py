from PyQt5.QtWidgets import QWidget,QLineEdit,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passlib.hash import sha256_crypt
from encryption import encrypt
import pickle 

class passwordClass(QWidget):
    def __init__(self,data):
        super(passwordClass,self).__init__()
        self.data = data
        self.resulation = pickle.load(open("resulationInfo.pkl","rb"))
        self.setGeometry(self.resulation[0]//2-200,self.resulation[1]//2-200,350,50)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("New Password")
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

        self.message = QLabel("Your Text File Successfully Encrypted !")
        self.message.setStyleSheet("margin:10px;padding:10ğx;background-color:grey;color:white;")
        self.message.setWindowTitle("Message!")
        self.message.setGeometry(self.resulation[0]//2-125,self.resulation[1]//2-25,250,50)
        self.message.show()
        self.close()