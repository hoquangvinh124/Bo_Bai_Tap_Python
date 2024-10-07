from FtoC import Ui_MainWindow

from PyQt6 import QtGui

class FtoCext(Ui_MainWindow):
    def __init__(self):
         pass

    def setupUi(self, MainWindow):
         super().setupUi(MainWindow)
         self.MainWindow=MainWindow
         self.pushButtonConvert.clicked.connect(self.TinhC)
         font = QtGui.QFont()
         font.setPointSize(13)
         self.labelShowC.setFont(font)


    def TinhC(self):
     try:
        Fahrenheit=float(self.fahrenheitFLineEdit.text())
        Celsius = (Fahrenheit - 32) / 1.8
        Celsius=round(Celsius,2)
        self.labelShowC.setText(str(Celsius))
     except ValueError:
        self.labelShowC.setText(str('Giá trị không hợp lệ!'))


    def show(self):
        self.MainWindow.show()

