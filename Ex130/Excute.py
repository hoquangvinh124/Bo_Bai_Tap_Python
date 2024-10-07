from PyQt6.QtWidgets import QApplication, QMainWindow

from KeToanEx import KeToanEx

app=QApplication([])
myWindow=KeToanEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()