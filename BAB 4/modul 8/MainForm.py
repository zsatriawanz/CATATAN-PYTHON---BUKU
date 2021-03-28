from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300,100)
        self.move(400,200)
        self.setWindowTitle("Demo Signal & Slot")

        self.lineEdit = QLineEdit()
        self.lineEdit.setText('Demo Signal dan Slot')

        self.button1 = QPushButton('Bersihkan')
        self.button2 = QPushButton('Tutup')

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lineEdit)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.button1.clicked.connect(self.lineEdit.clear)
        self.button2.clicked.connect(self.close)