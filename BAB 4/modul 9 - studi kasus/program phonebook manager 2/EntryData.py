from PyQt5.QtWidgets import (QDialog, QPushButton, QLabel,
                            QGridLayout, QLineEdit)

class EntryData(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300,100)
        self.move(300,200)
        self.setWindowTitle('Entry Data')

        self.nama = QLabel('Nama : ')
        self.noHp = QLabel('No.Hp : ')

        self.isiNama = QLineEdit()
        self.isiNoHp = QLineEdit()

        self.button1 = QPushButton('Ok')
        self.button2 = QPushButton('Batal')

        grid = QGridLayout()
        grid.addWidget(self.nama,0,0)
        grid.addWidget(self.noHp,1,0)
        grid.addWidget(self.isiNama,0,1,)
        grid.addWidget(self.isiNoHp,1,1)
        grid.addWidget(self.button1,2,0)
        grid.addWidget(self.button2,2,1)

        self.setLayout(grid)

        self.button1.clicked.connect(self.accept)
        self.button2.clicked.connect(self.reject)
