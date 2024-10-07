from PyQt6.QtWidgets import QApplication, QMainWindow

from FtoCext import FtoCext

app=QApplication([])
myWindow=FtoCext()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()