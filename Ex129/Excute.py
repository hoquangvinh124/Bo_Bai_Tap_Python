from PyQt6.QtWidgets import QApplication, QMainWindow

from TienDienExt import TienDienExt

app=QApplication([])
myWindow=TienDienExt()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()