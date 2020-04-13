from entrance import passwordEnter
from PyQt5.QtWidgets import QWidget,QLineEdit,QVBoxLayout,QApplication,QPushButton,QLabel,QFileDialog
from functions import loadSystemInfo

class optionPage(QWidget):
    def __init__(self):
        super(optionPage,self).__init__()

        self.systemInfo = loadSystemInfo()
        self.resulation = (self.systemInfo["width"],self.systemInfo["height"])
        
        self.setWindowTitle("Password")
        self.setGeometry(self.resulation[0]//2-200,self.resulation[1]//2-200,350,75)
        self.initUI()
    
    def initUI(self):
        self.verticalLay = QVBoxLayout()
        self.label = QLabel("Options")

        self.newFile = QPushButton("[*]New Empty File")
        self.newFile.clicked.connect(self.newFileFunction)

        self.loadNew = QPushButton("[*]Load A New File")
        self.loadNew.clicked.connect(self.loadNewFunction)

        self.enterNormal = QPushButton("[*]Open Loaded File")
        self.enterNormal.clicked.connect(self.enterNormalFunction)
        

        self.verticalLay.addWidget(self.label)
        self.verticalLay.addWidget(self.newFile)
        self.verticalLay.addWidget(self.loadNew)
        self.verticalLay.addWidget(self.enterNormal)
        self.setLayout(self.verticalLay)

    def enterNormalFunction(self):
    	self.pop = passwordEnter(option = 1)
    	self.pop.show()
    	self.close()

    def newFileFunction(self):
    	self.pop = passwordEnter(option = 2)
    	self.pop.show()
    	self.close()    	

    def loadNewFunction(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        path = fileName[0]# Not checked is it text or not
        self.pop = passwordEnter(option = 3,pathForNewOne = path)
        self.pop.show()
        self.close()
    	

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = optionPage()
    window.show()
    app.exec()          	