# Form implementation generated from reading ui file 'D:\LearnCheckBox\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 407)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 491, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 460, 52))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 61, 31))
        self.label_2.setObjectName("label_2")
        self.lineEditFullName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditFullName.setGeometry(QtCore.QRect(110, 120, 371, 22))
        self.lineEditFullName.setObjectName("lineEditFullName")
        self.lineEditEmail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(110, 150, 371, 22))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 22))
        self.label_3.setObjectName("label_3")
        self.chkMachineLearning = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkMachineLearning.setGeometry(QtCore.QRect(180, 220, 460, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkMachineLearning.setFont(font)
        self.chkMachineLearning.setObjectName("chkMachineLearning")
        self.chkDeepLearning = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkDeepLearning.setGeometry(QtCore.QRect(180, 250, 460, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkDeepLearning.setFont(font)
        self.chkDeepLearning.setObjectName("chkDeepLearning")
        self.chkSmartContract = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkSmartContract.setGeometry(QtCore.QRect(180, 280, 460, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkSmartContract.setFont(font)
        self.chkSmartContract.setObjectName("chkSmartContract")
        self.pushButtonSubmit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(200, 320, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButtonSubmit.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/PC LENOVO/Downloads/713df0fd071543324ecb6b43477362eb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSubmit.setIcon(icon)
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#00aaff;\">Đăng ký khóa học</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffaa00;\">Lựa chọn khóa học </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Email:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Họ và tên:</span></p></body></html>"))
        self.chkMachineLearning.setText(_translate("MainWindow", "Machine Learning"))
        self.chkDeepLearning.setText(_translate("MainWindow", "Deep Learning"))
        self.chkSmartContract.setText(_translate("MainWindow", "Smart Contract"))
        self.pushButtonSubmit.setText(_translate("MainWindow", "Submit"))
