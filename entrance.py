from PyQt5.QtWidgets import QWidget,QLineEdit,QVBoxLayout,QApplication,QPushButton,QLabel
from passlib.hash import sha256_crypt
from main import GUI
import pickle 
from functions import checkData,loadSystemInfo,HandleFile


class passwordEnter(QWidget):
    def __init__(self,option = 1,pathForNewOne = None):# option : 1-> open a loaded file , 2-> new file , 3-> load new file
        super(passwordEnter,self).__init__() 
        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        self.pathForNewOne = pathForNewOne# If it is no 'none', obviously option is 3 . 

        self.option = option
        self.setWindowTitle("Password")
        self.setGeometry(self.resulation[0]//2-200,self.resulation[1]//2-200,350,50)
        self.initUI()
    
    def initUI(self):
        self.verticalLay = QVBoxLayout()
        self.tagLE = QLineEdit()
        self.passwordLE = QLineEdit()
        #self.passwordLE.setEchoMode(True)

        self.button = QPushButton("OK")

        self.button.clicked.connect(self.Progress)
        self.verticalLay.addWidget(self.tagLE)
        self.verticalLay.addWidget(self.passwordLE)
        self.verticalLay.addWidget(self.button)
        self.setLayout(self.verticalLay)

    def Progress(self):
        enteredTag = self.tagLE.text()
        enteredPassword = self.passwordLE.text()

        if self.option == 1:
            if checkData(enteredTag,enteredPassword):
                self.gui = GUI(enteredTag,enteredPassword)
                self.gui.show()
                self.close()

            else:
                pop = QLabel("Something wrong !")
                pop.show()

        elif self.option == 2:
            HandleFile(enteredTag,"",enteredPassword,dataType="path",createNew=True)
            self.gui = GUI(enteredTag,enteredPassword)
            self.gui.show()
            self.close()

        elif self.option == 3:
            HandleFile(enteredTag,self.pathForNewOne,enteredPassword,dataType="path")
            self.gui = GUI(enteredTag,enteredPassword)
            self.gui.show()
            self.close()
                        
        else:
            pass