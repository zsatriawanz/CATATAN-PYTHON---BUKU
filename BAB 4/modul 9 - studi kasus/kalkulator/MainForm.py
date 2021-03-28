from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit ,
                             QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(250, 250)
        self.move(300,300)
        self.setWindowTitle('Kalkulator')

        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignRight)
        self.lineEdit.setFont(QFont('SansSerif',14))
        self.lineEdit.setDisabled(True)

        self._7button = QPushButton('7')
        self._8button = QPushButton('8')
        self._9button = QPushButton('9')
        self.divbutton = QPushButton('/')
        self.clearbutton = QPushButton('clr')
        self._4button = QPushButton('4')
        self._5button = QPushButton('5')
        self._6button = QPushButton('6')
        self.mulbutton = QPushButton('x')
        self._1button = QPushButton('1')
        self._2button = QPushButton('2')
        self._3button = QPushButton('3')
        self.minusbutton = QPushButton('-')
        self._0button = QPushButton('0')
        self.dotbutton = QPushButton('.')
        self.percenbutton = QPushButton('%')
        self.plusbutton = QPushButton('+')
        self.calculateButton = QPushButton('=')

        layout = QGridLayout()
        layout.addWidget(self.lineEdit,0,0,1,4)
        layout.addWidget(self._7button,1,0)
        layout.addWidget(self._8button,1,1)
        layout.addWidget(self._9button,1,2)
        layout.addWidget(self.clearbutton,1,3)
        layout.addWidget(self._4button,2,0)
        layout.addWidget(self._5button,2,1)
        layout.addWidget(self._6button,2,2)
        layout.addWidget(self.mulbutton,2,3)
        layout.addWidget(self._1button,3,0)
        layout.addWidget(self._2button,3,1)
        layout.addWidget(self._3button,3,2)
        layout.addWidget(self.divbutton,3,3)
        layout.addWidget(self._0button,4,0)
        layout.addWidget(self.dotbutton,4,1)
        layout.addWidget(self.minusbutton,4,2)
        layout.addWidget(self.plusbutton,4,3)
        layout.addWidget(self.percenbutton,5,0)
        layout.addWidget(self.calculateButton,5,1,1,3)

        self.setLayout(layout)

        self._0button.clicked.connect(lambda: self.writeDigit(0))
        self._1button.clicked.connect(lambda: self.writeDigit(1))
        self._2button.clicked.connect(lambda: self.writeDigit(2))
        self._3button.clicked.connect(lambda: self.writeDigit(3))
        self._4button.clicked.connect(lambda: self.writeDigit(4))
        self._5button.clicked.connect(lambda: self.writeDigit(5))
        self._6button.clicked.connect(lambda: self.writeDigit(6))
        self._7button.clicked.connect(lambda: self.writeDigit(7))
        self._8button.clicked.connect(lambda: self.writeDigit(8))
        self._9button.clicked.connect(lambda: self.writeDigit(9))
        self.mulbutton.clicked.connect(lambda: self.writeOperator('*'))
        self.divbutton.clicked.connect(lambda: self.writeOperator('/'))
        self.plusbutton.clicked.connect(lambda: self.writeOperator('+'))
        self.minusbutton.clicked.connect(lambda: self.writeOperator('-'))
        self.dotbutton.clicked.connect(self.writePoint)
        self.clearbutton.clicked.connect(self.lineEdit.clear)
        self.calculateButton.clicked.connect(self.calculateButtonClick)
        self.percenbutton.clicked.connect(self.percenbuttonClick)

    def writeDigit(self, digit):
        if digit in range(0,10):
            self.lineEdit.setText(
                self.lineEdit.text()+str(digit))

    def writeOperator(self, operator):
        if len(self.lineEdit.text()) == 0 : return
        if operator in ['*','/','+','-']:
            if self.lineEdit.text()[-1] in ['*','/','+','-']:
                self.lineEdit.setText(
                    self.lineEdit.text()[:-1] + operator)
            else:
                self.lineEdit.setText(
                    self.lineEdit.text() + operator)

    def writePoint(self):
        if len(self.lineEdit.text()) == 0 or \
        self.lineEdit.text()[-1] in ['*','/','+','-']:
            return
        self.lineEdit.setText(
            self.lineEdit.text() + '.')

    def calculateButtonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0 : return
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')


    def percenbuttonClick(self):
        expression = self.lineEdit.text()
        if len(expression) == 0 :return
        try:
            result = eval(expression) / 100
            self.lineEdit.setText(str(result))
        except:
            self.lineEdit.setText('ERROR')
