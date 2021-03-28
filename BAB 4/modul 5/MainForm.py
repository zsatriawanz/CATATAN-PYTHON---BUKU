from PyQt5.QtWidgets import QWidget, QDesktopWidget

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300,200)
        self.setCenter()
        self.setWindowTitle('Menengahkan Form')

    def setCenter(self):
        deskop = QDesktopWidget()

        screenwidth = deskop.screen().width()
        screenheight = deskop.screen().height()

        self.setGeometry((screenwidth - self.width()) // 2,
                          (screenheight - self.height()) // 2,
                          self.width(),
                          self.height())

