from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEX import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()