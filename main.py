from PyQt5.QtWidgets import QWidget,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passwordWidget import passwordClass
from passlib.hash import sha256_crypt
from encryption import decrypt
import pickle 

class GUI(QWidget):
    def __init__(self,password):
        super(GUI,self).__init__()
        self.password = password
        self.setWindowTitle("Encrypted Notebook")
        self.resulation = pickle.load(open("resulationInfo.pkl","rb"))
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
        with open("encrypted.txt","r") as file:
            data = file.read()
            decrypted = decrypt(self.password,data)

            decrypted = decrypted.decode("utf-8")

        self.editor.setPlainText(decrypted)

    def saveFunction(self):
        text = self.editor.toPlainText()
        self.passwordPop = passwordClass(text)
        self.passwordPop.show()
        self.close()

	