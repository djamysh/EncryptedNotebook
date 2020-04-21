from PyQt5.QtWidgets import QWidget,QLineEdit,QVBoxLayout,QApplication,QPushButton,QLabel,QRadioButton,QHBoxLayout,QGridLayout
from PyQt5.QtCore import QTimer,Qt
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
        self.setGeometry(self.resulation[0]//2-250,self.resulation[1]//2-75,500,150)
        self.initUI()
    
    def initUI(self):
        self.verticalLay = QVBoxLayout()

        self.GridLayout = QGridLayout()

        self.labelTag = QLabel("Tag : ")

        self.tagLE = QLineEdit()
        self.tagLE.setFixedWidth(250)


        self.readableTag = QRadioButton()


        self.labelPassword = QLabel("Password : ")

        self.passwordLE = QLineEdit()
        self.passwordLE.setFixedWidth(250)
        
        self.readablePassword = QRadioButton()

        self.button = QPushButton("OK")

        self.timer = QTimer() #For password
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)

        self.button.clicked.connect(self.Progress)

        self.GridLayout.addWidget(self.labelTag,0,0,alignment = Qt.AlignVCenter|Qt.AlignRight)
        self.GridLayout.addWidget(self.tagLE,0,1,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.GridLayout.addWidget(self.readableTag,0,2,alignment = Qt.AlignVCenter|Qt.AlignLeft)

        self.GridLayout.addWidget(self.labelPassword,1,0,alignment = Qt.AlignVCenter|Qt.AlignRight)
        self.GridLayout.addWidget(self.passwordLE,1,1,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.GridLayout.addWidget(self.readablePassword,1,2,alignment = Qt.AlignVCenter|Qt.AlignLeft)

        self.GridLayout.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.verticalLay.addLayout(self.GridLayout)
        self.verticalLay.addWidget(self.button,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.verticalLay.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.setLayout(self.verticalLay)

    def _update(self):
        if self.readablePassword.isChecked():
            self.passwordLE.setEchoMode(False)
        else:
            self.passwordLE.setEchoMode(QLineEdit.Password)

        if self.readableTag.isChecked():
            self.tagLE.setEchoMode(False)
        else:
            self.tagLE.setEchoMode(QLineEdit.Password)


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
