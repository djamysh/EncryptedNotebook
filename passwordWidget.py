from PyQt5.QtWidgets import QWidget,QLineEdit,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passlib.hash import sha256_crypt
from encryption import encrypt
import pickle 

from functions import HandleFile,encrypting,loadSystemInfo
from specialWidgets import HoverEchoLineEdit,HoverButton

class passwordClass(QWidget):
    def __init__(self,tag,data):
        super(passwordClass,self).__init__()
        self.data = data
        self.tag = tag
        
        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        self.setStyleSheet("background-color : #352925;")
        self.setWindowTitle("Encrypted Notebook")
        self.setGeometry(self.resulation[0]//2-250,self.resulation[1]//2-75,500,150)
        self.initUI()

    def initUI(self):
        self.vertical = QVBoxLayout()
        self.horizontalLay = QHBoxLayout()

        self.labelPassword = QLabel("Password : ")
        self.labelPassword.setStyleSheet("border-left:5px solid #36454f;background-color : #6E6E70;font-size : 16px;font-family : 'NewRocker';padding : 3px;font-weight:bold;border-top-right-radius:10px;color:#141e22;")
        self.labelPassword.setFixedHeight(50)
        self.labelPassword.setFixedWidth(100)



        self.passwordLE = HoverEchoLineEdit()
        self.passwordLE.setStyleSheet("border-radius:4px;background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,stop: 0 #352925, stop: 1 #292535);font-size:16px;font-family:Arsenal;color:#667169;padding:3px;")        

        self.passwordLE.setFixedHeight(50)
        self.passwordLE.setFixedWidth(250)
        

        self.button = HoverButton("OK","border-radius:3px;background-color:#a2b2b8;color:#0d1416;font-size:16px;font-family:'NewRocker';font-weight:750;","border-radius:3px;background-color:#0d1416;color:#a2b2b8;font-size:16px;font-family:'NewRocker';font-weight:750;")
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(120)

        self.button.setStyleSheet("border-radius:3px;background-color:#0d1416;color:#a2b2b8;font-size:16px;font-family:'NewRocker';font-weight:750;")


        self.button.clicked.connect(self.savePassword)

        self.horizontalLay.addWidget(self.labelPassword)
        self.horizontalLay.addWidget(self.passwordLE)
        self.horizontalLay.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.vertical.addLayout(self.horizontalLay)
        self.vertical.addWidget(self.button,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.vertical.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)

        self.setLayout(self.vertical)

    def savePassword(self):
        self.password = self.passwordLE.text()
        self.password = self.password
        self.data = self.data
        HandleFile(self.tag,self.data,self.password,dataType = "string")

        self.close()