from PyQt5.QtWidgets import QWidget,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passwordWidget import passwordClass
from passlib.hash import sha256_crypt
from encryption import decrypt
import pickle 
from functions import LoadText,loadSystemInfo

class GUI(QWidget):
    def __init__(self,tag,password):
        super(GUI,self).__init__()
        self.password = password
        self.tag = tag

        self.setWindowTitle("Encrypted Notebook")
        
        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        
        self.setGeometry(self.resulation[0]//2-510,self.resulation[1]//2-250,1020,500)

        self.initUI()

    def initUI(self):
        self.verticalLayout = QVBoxLayout()
        self.bottomHorizontal = QHBoxLayout()
        self.editor = QPlainTextEdit()
        self.saveButton = QPushButton("Save")
        self.bottomHorizontal.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.editor)
        self.verticalLayout.addLayout(self.bottomHorizontal)
        self.saveButton.clicked.connect(self.saveFunction)
        self.load()
        self.setLayout(self.verticalLayout)

    def load(self):
        decrypted = LoadText(self.tag,self.password)
        

        self.editor.setPlainText(decrypted)


    def saveFunction(self):
        text = self.editor.toPlainText()
        self.passwordPop = passwordClass(self.tag,text)
        self.passwordPop.show()
        self.close()

	