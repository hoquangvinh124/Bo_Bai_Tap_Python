# Form implementation generated from reading ui file 'D:\LearnQHBoxLayout\MainWindowFirstDegreeEquation.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 309)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(12, 10, 561, 240))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEditCoefficientA = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditCoefficientA.setObjectName("lineEditCoefficientA")
        self.horizontalLayout_5.addWidget(self.lineEditCoefficientA)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEditCoefficientB = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditCoefficientB.setObjectName("lineEditCoefficientB")
        self.horizontalLayout_6.addWidget(self.lineEditCoefficientB)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEditsolution = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEditsolution.setObjectName("lineEditsolution")
        self.horizontalLayout_7.addWidget(self.lineEditsolution)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonSolution = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonSolution.setObjectName("pushButtonSolution")
        self.horizontalLayout_2.addWidget(self.pushButtonSolution)
        self.pushButtonClear = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout_2.addWidget(self.pushButtonExit)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 26))
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
        self.label.setText(_translate("MainWindow", "First Degree Equation "))
        self.label_2.setText(_translate("MainWindow", "He so a:"))
        self.label_3.setText(_translate("MainWindow", "He so b:"))
        self.label_4.setText(_translate("MainWindow", "Nghiem:"))
        self.pushButtonSolution.setText(_translate("MainWindow", "Solution"))
        self.pushButtonClear.setText(_translate("MainWindow", "Clear"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
