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
        self.setStyleSheet("background-color : #352925;")
        self.option = option
        self.setWindowTitle("Password")
        self.setGeometry(self.resulation[0]//2-250,self.resulation[1]//2-75,500,150)
        self.initUI()
    
    def initUI(self):
        self.setMouseTracking(True)


        self.verticalLay = QVBoxLayout()

        self.GridLayout = QGridLayout()

        self.labelTag = QLabel("Tag : ")
        self.labelTag.setStyleSheet("border-left:5px solid #36454f;background-color : #6E6E70;font-size : 16px;font-family : 'NewRocker';padding : 3px;font-weight:bold;border-top-right-radius:10px;color:#141e22;")
        self.labelTag.setAlignment(Qt.AlignVCenter|Qt.AlignRight)
        self.tagLE = HoverEchoLineEdit()
        self.tagLE.setStyleSheet("border-radius:4px;background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,stop: 0 #352925, stop: 1 #253529);font-size:16px;font-family:Arsenal;color:#696671;padding:3px;")
        self.tagLE.setFixedHeight(50)
        self.tagLE.setFixedWidth(250)

        self.labelPassword = QLabel("Password : ")
        self.labelPassword.setStyleSheet("border-left:5px solid #36454f;background-color : #6E6E70;font-size : 16px;font-family : 'NewRocker';padding : 3px;font-weight:bold;border-top-right-radius:10px;color:#141e22;")

        self.passwordLE = HoverEchoLineEdit()
        self.passwordLE.setStyleSheet("border-radius:4px;background-color: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,stop: 0 #352925, stop: 1 #292535);font-size:16px;font-family:Arsenal;color:#667169;padding:3px;")
        
        self.passwordLE.setFixedHeight(50)
        self.passwordLE.setFixedWidth(250)
        

        self.button = HoverButton("OK")
        self.button.setFixedHeight(40)
        self.button.setFixedWidth(120)

        self.button.setStyleSheet("border-radius:3px;background-color:#0d1416;color:#a2b2b8;font-size:16px;font-family:'NewRocker';font-weight:750;")

        self.button.clicked.connect(self.Progress)

        self.GridLayout.addWidget(self.labelTag,0,0,alignment = Qt.AlignVCenter|Qt.AlignRight)
        self.GridLayout.addWidget(self.tagLE,0,1,alignment = Qt.AlignVCenter| Qt.AlignHCenter)

        self.GridLayout.addWidget(self.labelPassword,1,0,alignment = Qt.AlignVCenter|Qt.AlignRight)
        self.GridLayout.addWidget(self.passwordLE,1,1,alignment = Qt.AlignVCenter| Qt.AlignHCenter)

        self.GridLayout.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.verticalLay.addLayout(self.GridLayout)
        self.verticalLay.addWidget(self.button,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.verticalLay.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
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

class HoverEchoLineEdit(QLineEdit):
    def __init__(self,parent = None):
        super(HoverEchoLineEdit,self).__init__(parent)

    def enterEvent(self,event):
        self.setEchoMode(False)

    def leaveEvent(self,event):
        self.setEchoMode(QLineEdit.Password)

class HoverButton(QPushButton):

    def __init__(self,text, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setText(text)

    def enterEvent(self,event):
        self.setStyleSheet("border-radius:3px;background-color:#a2b2b8;color:#0d1416;font-size:16px;font-family:'NewRocker';font-weight:750;")

    def leaveEvent(self,event):
        self.setStyleSheet("border-radius:3px;background-color:#0d1416;color:#a2b2b8;font-size:16px;font-family:'NewRocker';font-weight:750;")

