from PyQt6.QtWidgets import QApplication, QMainWindow

from CalenderEX import CalenderEX

app=QApplication([])
qMainWindow=QMainWindow()
myWindow=CalenderEX()
myWindow.setupUi(qMainWindow)
qMainWindow.show()
app.exec()