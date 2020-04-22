from PyQt5.QtWidgets import QWidget,QLineEdit,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passlib.hash import sha256_crypt
from encryption import encrypt
import pickle 

from functions import HandleFile,encrypting,loadSystemInfo


class passwordClass(QWidget):
    def __init__(self,tag,data):
        super(passwordClass,self).__init__()
        self.data = data
        self.tag = tag
        
        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        
        self.setGeometry(self.resulation[0]//2-250,self.resulation[1]//2-75,500,150)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("{}".format(self.tag))
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
        self.password = self.password
        self.data = self.data
        HandleFile(self.tag,self.data,self.password,dataType = "string")

        
        self.message = QLabel("Your Text File Successfully Encrypted !")
        self.message.setStyleSheet("margin:10px;padding:10px;background-color:grey;color:white;")
        self.message.setWindowTitle("Message!")
        self.message.setGeometry(self.resulation[0]//2-125,self.resulation[1]//2-25,250,50)
        self.message.show()
        self.close()