from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QListWidget,
                            QGridLayout, QLineEdit)

from EntryData import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(450, 350)
        self.move(300,200)
        self.setWindowTitle('List PhoneBooks')

        self.button1 = QPushButton('Tambah')
        self.button2 = QPushButton('Edit')
        self.button3 =QPushButton('Hapus')
        self.button4 = QPushButton('Reset')

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        hbox.addWidget(self.button4)

        self.lineList = QListWidget()

        grid = QGridLayout()
        grid.addWidget(self.lineList,0,0,1,3)
        grid.addLayout(hbox,1,0,1,3)

        self.setLayout(grid)


        self.button1.clicked.connect(self.tambahData)
        self.button2.clicked.connect(self.edit)
        self.button3.clicked.connect(self.hapus)
        self.button4.clicked.connect(self.lineList.clear)


    def tambahData(self):
        self.entryData = EntryData()

        if self.entryData.exec_() == QDialog.Accepted:
            self.lineList.addItem(
            self.entryData.isiNama.text() + " - " +
            self.entryData.isiNoHp.text())


    def edit(self):
        if self.lineList.currentRow() < 0 : return
        self.entryData = EntryData()

        kata = str(self.lineList.currentItem().text())
        noIndex = kata.index('-')
        self.entryData.isiNama.setText(kata[:(noIndex-1)])
        self.entryData.isiNoHp.setText(kata[(noIndex+2):])

        if self.entryData.exec_() == QDialog.Accepted:
            self.lineList.currentItem().setText(
            self.entryData.isiNama.text() + " - " +
            self.entryData.isiNoHp.text())

    def hapus(self):
        row = self.lineList.currentRow()

        if row >= 0:
            self.lineList.takeItem(row)




