from PyQt5.QtWidgets import QWidget,QLineEdit,QHBoxLayout,QApplication,QPushButton
from passlib.hash import sha256_crypt
from main import GUI

class passwordEnter(QWidget):
    def __init__(self):
        super(passwordEnter,self).__init__()
        self.readHash()
        self.initUI()
    def initUI(self):
        self.horizontalLay = QHBoxLayout()
        self.passwordLE = QLineEdit()
        #self.passwordLE.setEchoMode(True)

        self.button = QPushButton("OK")
        self.button.clicked.connect(self.checkPassword)
        self.horizontalLay.addWidget(self.passwordLE)
        self.horizontalLay.addWidget(self.button)
        self.setLayout(self.horizontalLay)

    def checkPassword(self):
        enteredPassword = self.passwordLE.text()


        if sha256_crypt.verify(enteredPassword,self.hashed):
            enteredPassword = enteredPassword.encode("utf-8")
            self.gui = GUI(enteredPassword)
            self.gui.show()
            self.close()

        else:
            print("Wrong")

    def readHash(self):
        with open("hashed.txt","r") as file:
            self.hashed = file.read()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = passwordEnter()
    window.show()
    app.exec()      