import json

from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow

class MainWindowEX(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.getInformation)
    def getInformation(self):
        fullName=self.lineEditFullName.text()
        email=self.lineEditEmail.text()
        gender="Woman"
        if not self.radWoman.isChecked():
            gender=self.radMan.text()
        address=self.lineEditAddress.text()
        degree="Bachelor"
        if self.radMaster.isChecked():
            degree=self.radMaster.text()
        elif self.radDoctoral.isChecked():
            degree=self.radDoctoral.text()
        information={"FullName":fullName,
                     "Email":email,
                     "Gender":gender,
                     "Address":address,
                     "Degree":degree
                     }
        self.msgBox=QMessageBox()
        self.msgBox.setWindowTitle("Information")
        self.msgBox.setText(json.dumps(information, ensure_ascii=False))
        self.msgBox.show()
    def show(self):
        self.MainWindow.show()