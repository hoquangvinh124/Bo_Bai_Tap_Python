# Form implementation generated from reading ui file 'D:\BaiTap127\FtoC.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 320)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fahrenheitFLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.fahrenheitFLineEdit.setGeometry(QtCore.QRect(200, 110, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fahrenheitFLineEdit.setFont(font)
        self.fahrenheitFLineEdit.setObjectName("fahrenheitFLineEdit")
        self.fahrenheitFLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fahrenheitFLabel.setGeometry(QtCore.QRect(50, 110, 134, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fahrenheitFLabel.setFont(font)
        self.fahrenheitFLabel.setObjectName("fahrenheitFLabel")
        self.labelC = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelC.setGeometry(QtCore.QRect(80, 150, 101, 51))
        self.labelC.setObjectName("labelC")
        self.labelShowC = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelShowC.setGeometry(QtCore.QRect(200, 160, 231, 31))
        self.labelShowC.setObjectName("labelShowC")
        self.pushButtonConvert = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonConvert.setGeometry(QtCore.QRect(70, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonConvert.setFont(font)
        self.pushButtonConvert.setObjectName("pushButtonConvert")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(290, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonClose.setFont(font)
        self.pushButtonClose.setObjectName("pushButtonClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonClose.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hồ Quang Vinh - F to C"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Chuyển đổi nhiệt độ</span></p></body></html>"))
        self.fahrenheitFLabel.setText(_translate("MainWindow", "Fahrenheit (F):"))
        self.labelC.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Celsius (C):</span></p></body></html>"))
        self.labelShowC.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButtonConvert.setText(_translate("MainWindow", "Convert"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))
