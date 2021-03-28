from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
     QLineEdit, QGridLayout)

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300,200)
        self.move(300,300)
        self.setWindowTitle('RowSpan dan ColmSpan')

        self.label1 = QLabel('Nama')
        self.lineEdit1 = QLineEdit()

        self.label2 = QLabel('No. Telelpon')
        self.lineEdit2 = QLineEdit()

        self.button = QPushButton('Ok')

        layout = QGridLayout()
        layout.addWidget(self.label1,0,0)
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)

        layout.addWidget(self.button,2,0,1,2)

        self.setLayout(layout)

