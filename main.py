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
        self.setStyleSheet("background-color:  #061e18;")
        
        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        
        self.setGeometry(self.resulation[0]//2-510,self.resulation[1]//2-280,1020,560)
        self.initUI()

    def initUI(self):
        self.verticalLayout = QVBoxLayout()
        self.tagLabel = QLabel(self.tag)
        self.tagLabel.setStyleSheet("font-family:'NewRocker';font-size : 32px;background-color : #061e18;color : #bab5ae;border-radius:1px;margin : 10px;padding:5px;")
        self.tagLabel.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.bottomHorizontal = QHBoxLayout()
        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("font-family:'Special Elite';font-size:15px;background-color :#8ab1a7;border-radius:3px;padding : 15px;color:#020a08;")
        self.editor.setFixedHeight(450)
        self.editor.setFixedWidth(960)

        self.saveButton = HoverButton("Save")
        self.saveButton.setStyleSheet("background-color: #bab5ae;font-family:'NewRocker';font-size:16px;font-weight:bold;color:#4E4343;width:160px;height:30px;border-radius:3px;")



        self.verticalLayout.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.bottomHorizontal.setAlignment(Qt.AlignVCenter| Qt.AlignHCenter)
        self.bottomHorizontal.addWidget(self.saveButton,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.tagLabel)
        self.verticalLayout.addWidget(self.editor,alignment = Qt.AlignVCenter| Qt.AlignHCenter)
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

    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.showNormal()

        elif event.key() == Qt.Key_F11:
            self.showFullScreen()

        elif (event.modifiers() & Qt.ControlModifier):
            if event.key() == Qt.Key_S: #Control Save
                self.saveFunction()

class HoverButton(QPushButton):

    def __init__(self,text, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setText(text)

    def enterEvent(self,event):
        self.setStyleSheet("background-color: #c7c3be;font-family:'NewRocker';font-size:16px;font-weight:bold;color:#4E4343;width:160px;height:30px;border-radius:3px;")

    def leaveEvent(self,event):
        self.setStyleSheet("background-color: #bab5ae;font-family:'NewRocker';font-size:16px;font-weight:bold;color:#4E4343;width:160px;height:30px;border-radius:3px;")


