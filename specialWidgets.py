from PyQt5.QtWidgets import QLineEdit,QPushButton

class HoverEchoLineEdit(QLineEdit):
    def __init__(self,parent = None):
        super(HoverEchoLineEdit,self).__init__(parent)

    def enterEvent(self,event):
        self.setEchoMode(False)

    def leaveEvent(self,event):
        self.setEchoMode(QLineEdit.Password)

class HoverButton(QPushButton):

    def __init__(self,text,stylesheet_enter,stylesheet_leave,parent=None):
        super(HoverButton, self).__init__(parent)
        self.setText(text)
        self.enterSS = stylesheet_enter
        self.leaveSS = stylesheet_leave

        self.setStyleSheet(self.enterSS)

    def enterEvent(self,event):
        self.setStyleSheet(self.enterSS)        
    def leaveEvent(self,event):
        self.setStyleSheet(self.leaveSS)
