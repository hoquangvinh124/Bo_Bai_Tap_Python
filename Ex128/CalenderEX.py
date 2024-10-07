from PyQt6 import QtGui
from Calender import Ui_MainWindow


class CalenderEX(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.doilich)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelly.setFont(font)

    def doilich(self):
        try:
            can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
            chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
            year = int(self.lineEdit.text())
            if year<0:
                self.labelly.setText('')
            else:
                can = can_list[year % 10]
                chi = chi_list[year % 12]
                self.labelly.setText(f"{can} {chi}")
        except ValueError:
            pass
                              
    def show(self):
        self.MainWindow.show()