from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.changeTextpushButton.clicked.connect(self.processChangeText)
        self.fontSizepushButton.clicked.connect(self.processChangeFontSize)
        self.alignLeftpushButton.clicked.connect(self.processAlignLeft)
        self.alignCenterpushButton.clicked.connect(self.processAlignCenter)
        self.alignRightpushButton.clicked.connect(self.processAlignRight)
        self.ShowPNGpushButton.clicked.connect(self.processChangePNG)
        self.showGIFpushButton.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.Titlelabel.setText("https://www.facebook.com/profile.php?id=61550589671046")
    def processChangeFontSize(self):
        font=self.Titlelabel.font()
        font.setPointSize(20)
        font.setItalic(True)
        font.setBold(True)
        font.setFamily("cambria")
        self.Titlelabel.setFont(font)
    def processAlignLeft(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.Titlelabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        pixmap=QPixmap("images/WIN_20231206_15_26_07_Pro.jpg")
        self.imageLabel.setPixmap(pixmap)
    def processChangeGIF(self):
        movie=QMovie("images/omen-valorant.gif")
        self.imageLabel.setMovie(movie)
        movie.start()