from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                             QPushButton, QListWidget)

from EntryForm import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(450, 350)
        self.move(300,200)
        self.setWindowTitle('Phonebook Manager')

        self.addButton = QPushButton('Tambah')
        self.editButton =QPushButton('Ubah')
        self.deleteButton = QPushButton('Hapus')
        self.clearButton = QPushButton('Kosongkan')
        self.exitButton = QPushButton('Keluar')

        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addWidget(self.clearButton)
        hbox.addWidget(self.exitButton)

        self.contacList = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.contacList)
        layout.addLayout(hbox)

        self.setLayout(layout)

        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.clearButton.clicked.connect(self.contacList.clear)
        self.exitButton.clicked.connect(self.close)

    def addButtonClick(self):
        self.entryForm = EntryForm()

        if self.entryForm.exec_() == QDialog.Accepted:
            self.contacList.addItem(
                self.entryForm.nameLineEdit.text()+' - '+
                self.entryForm.phoneLineEdit.text())



    def editButtonClick(self):
        if self.contacList.currentRow() < 0: return
        self.entryForm = EntryForm()
        s = str(self.contacList.currentItem().text())
        idx = s.index('-')
        self.entryForm.nameLineEdit.setText(s[:(idx-1)])
        self.entryForm.phoneLineEdit.setText(s[(idx+2):])

        if self.entryForm.exec_() == QDialog.Accepted:
            self.contacList.currentItem().setText(
            self.entryForm.nameLineEdit.text()+'-'+
            self.entryForm.phoneLineEdit.text())


    def deleteButtonClick(self):
        row = self.contacList.currentRow()
        if row >= 0:
            self.contacList.takeItem(row)

