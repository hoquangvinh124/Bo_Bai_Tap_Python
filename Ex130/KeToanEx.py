from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QFont
from KeToan import Ui_MainWindow


class KeToanEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.TinhKhauHao)
        self.pushButtonxctkh.clicked.connect(self.xctkh)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        font = QFont()
        font.setBold(True)
        font.setPointSize(9)
        header_item_1 = self.tableWidget.horizontalHeaderItem(0)
        header_item_2 = self.tableWidget.horizontalHeaderItem(1)
        header_item_1.setFont(font)
        header_item_2.setFont(font)

    def TinhKhauHao(self):
            try:
                pp = float(self.gmmLineEdit.text())
                t = float(self.pvcLineEdit.text())
                ld = float(self.pldLineEdit.text())
                snsd = int(self.snsdLineEdit.text())
                if pp <= 0 or t<0 or ld<0 or snsd<=0:
                    pass
                else:
                    opofa= pp + ld + t
                    adr = opofa / snsd
                    mdr = adr/12
                    self.ngtscdLineEdit.setText(f'{opofa:,.0f}')
                    self.mtkhnLineEdit.setText(f'{adr:,.0f}')
                    self.mtkhtLineEdit.setText(f'{mdr:,.0f}')
            except ValueError:
                pass

    def xctkh(self):
        try:
            pp = float(self.gmmLineEdit.text())
            t = float(self.pvcLineEdit.text())
            ld = float(self.pldLineEdit.text())
            snsd = int(self.snsdLineEdit.text())
            if pp <= 0 or t < 0 or ld < 0 or snsd <= 0:
                pass
            else:
                opofa = pp + ld + t
                adr = opofa / snsd
                self.tableWidget.setRowCount(snsd)
                for i in range(1, snsd + 1):
                    ad = adr * i
                    fpdr = opofa - ad
                    self.tableWidget.setItem( i-1, 0, QTableWidgetItem(f"Năm {i}"))
                    self.tableWidget.setItem( i-1, 1, QTableWidgetItem(f"{fpdr:,.0f}"))
        except ValueError:
            pass

    def show(self):
        self.MainWindow.show()