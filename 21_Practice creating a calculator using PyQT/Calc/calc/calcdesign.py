# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 766)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 39, 751, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.pushButton_n7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n7.setGeometry(QtCore.QRect(20, 190, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n7.setFont(font)
        self.pushButton_n7.setObjectName("pushButton_n7")
        self.pushButton_n8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n8.setGeometry(QtCore.QRect(180, 190, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n8.setFont(font)
        self.pushButton_n8.setObjectName("pushButton_n8")
        self.pushButton_n9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n9.setGeometry(QtCore.QRect(330, 190, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n9.setFont(font)
        self.pushButton_n9.setObjectName("pushButton_n9")
        self.pushButton_n4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n4.setGeometry(QtCore.QRect(20, 330, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n4.setFont(font)
        self.pushButton_n4.setObjectName("pushButton_n4")
        self.pushButton_n5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n5.setGeometry(QtCore.QRect(180, 330, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n5.setFont(font)
        self.pushButton_n5.setObjectName("pushButton_n5")
        self.pushButton_n6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n6.setGeometry(QtCore.QRect(330, 330, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n6.setFont(font)
        self.pushButton_n6.setObjectName("pushButton_n6")
        self.pushButton_n1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n1.setGeometry(QtCore.QRect(20, 460, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n1.setFont(font)
        self.pushButton_n1.setObjectName("pushButton_n1")
        self.pushButton_n2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n2.setGeometry(QtCore.QRect(180, 460, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n2.setFont(font)
        self.pushButton_n2.setObjectName("pushButton_n2")
        self.pushButton_n3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n3.setGeometry(QtCore.QRect(330, 460, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n3.setFont(font)
        self.pushButton_n3.setObjectName("pushButton_n3")
        self.pushButton_n0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_n0.setGeometry(QtCore.QRect(20, 590, 120, 110))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_n0.setFont(font)
        self.pushButton_n0.setObjectName("pushButton_n0")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(510, 190, 103, 251))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(512, 465, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(330, 590, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setObjectName("pushButton_dot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_n7.setText(_translate("MainWindow", "7"))
        self.pushButton_n8.setText(_translate("MainWindow", "8"))
        self.pushButton_n9.setText(_translate("MainWindow", "9"))
        self.pushButton_n4.setText(_translate("MainWindow", "4"))
        self.pushButton_n5.setText(_translate("MainWindow", "5"))
        self.pushButton_n6.setText(_translate("MainWindow", "6"))
        self.pushButton_n1.setText(_translate("MainWindow", "1"))
        self.pushButton_n2.setText(_translate("MainWindow", "2"))
        self.pushButton_n3.setText(_translate("MainWindow", "3"))
        self.pushButton_n0.setText(_translate("MainWindow", "0"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_dot.setText(_translate("MainWindow", "."))