from PyQt5.QtWidgets import QWidget, QLabel, QPushButton

class TextForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('DemoTag Html')

        self.label = QLabel('<h1>Hallo<font color=red>PyQt5</font></h1')
        self.label.move(10,10)
        self.label.setParent(self)


        self.label1 = QLabel('''
             Text ini dibuat dengan Tag HTML. Text dapat dijadikan <b>tebal</b> dijalankan<i> miring</i>, dan <u>bergaris</u>
        ''')
        self.label1.setWordWrap(True)
        self.label1.move(10,50)
        self.label1.setParent(self)






