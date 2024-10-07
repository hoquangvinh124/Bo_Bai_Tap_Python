from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox
from TienDien import Ui_MainWindow

class TienDienExt(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonSHBT.clicked.connect(self.SHBT)
        self.pushButtonKD.clicked.connect(self.KinhDoanh)
        self.pushButtonSX.clicked.connect(self.SanXuat)
        self.pushButtonT.clicked.connect(self.CuaSoThoat)
        self.pushButtonHD.clicked.connect(self.CuaSoThongBao)
        font = QtGui.QFont("Roboto", 13)
        font.setBold(True)
        self.label_7.setFont(font)

    def SHBT(self):
        pay = 0
        try:
            A = float(self.lineEditCSC.text())
            B = float(self.lineEditCSM.text())
            C = float(self.lineEditSHBT.text())
            if A > B or A < 0 or B < 0 or C <= 0:
                pass
            else:
                used = B - A
                self.lineEditKWH.setText(str(used))
                if B - A <= 50 * C:
                    pay = (B - A) * 1484
                elif B - A <= 100 * C:
                    pay = (50 * C * 1484) + ((B - A) - 50 * C) * 1533
                elif B - A <= 200 * C:
                    pay = (50 * C * 1484) + (50 * C * 1533) + ((B - A) - 100 * C) * 1786
                elif B - A <= 300 * C:
                    pay = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + ((B - A) - 200 * C) * 2242
                elif B - A <= 400 * C:
                    pay = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + (100 * C * 2242) + ((B - A) - 300 * C) * 2503
                else:
                    pay = (50 * C * 1484) + (50 * C * 1533) + (100 * C * 1786) + (100 * C * 2242) + (100 * C * 2503) + (
                                (B - A) - 400 * C) * 2587

            self.label_7.setStyleSheet("color: rgb(230, 126, 34);")
            self.label_7.setText(f'{pay:,.0f} VNĐ')
        except ValueError:
            pass

    def KinhDoanh(self):
        try:
            A = float(self.lineEditCSC.text())
            B = float(self.lineEditCSM.text())
            if A > B or A < 0 or B < 0:
                pass
            else:
                used = B - A
                self.lineEditKWH.setText(str(used))
                pay = (B - A) * 2320
                self.label_7.setStyleSheet("color: rgb(0, 170, 255);")
                self.label_7.setText(f'{pay:,.0f} VNĐ')
        except ValueError:
            pass

    def SanXuat(self):
        try:
            A = float(self.lineEditCSC.text())
            B = float(self.lineEditCSM.text())
            if A > B or A < 0 or B < 0:
                pass
            else:
                used = B - A
                self.lineEditKWH.setText(str(used))
                pay = (B-A)*1518
                self.label_7.setStyleSheet("color: rgb(0, 128, 0);")
                self.label_7.setText(f'{pay:,.0f} VNĐ')
        except ValueError:
            pass

    def CuaSoThoat(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận")
        dlg.setText("Bạn chắc chắn muốn thoát chứ?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()
        button = QMessageBox.StandardButton(button)
        if button == QMessageBox.StandardButton.Yes:
            self.MainWindow.close()
        else:
            pass

    def CuaSoThongBao(self):
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Thông báo")
        dlg.setText("Đây là phần mềm tính tiền điện\n"
                    "Kỹ sư thiết kế: Hồ Quang Vinh")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.setIcon(QMessageBox.Icon.Information)
        button = dlg.exec()


    def show(self):
        self.MainWindow.show()


