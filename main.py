from PyQt5.QtWidgets import QWidget,QPlainTextEdit,QHBoxLayout,QVBoxLayout,QApplication,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt,QTimer
from passwordWidget import passwordClass
from passlib.hash import sha256_crypt
from encryption import decrypt

class GUI(QWidget):
    def __init__(self,password):
        super(GUI,self).__init__()
        self.password = password
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

	