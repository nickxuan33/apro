# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\workspace\python\my_tools\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 70, 371, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 164, 72, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.domain_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.domain_lineEdit.setGeometry(QtCore.QRect(180, 160, 331, 31))
        self.domain_lineEdit.setObjectName("domain_lineEdit")
        self.go_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.go_pushButton.setGeometry(QtCore.QRect(520, 160, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.go_pushButton.setFont(font)
        self.go_pushButton.setObjectName("go_pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 490, 511, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.show_label = QtWidgets.QLabel(self.centralwidget)
        self.show_label.setGeometry(QtCore.QRect(120, 210, 561, 16))
        self.show_label.setText("")
        self.show_label.setObjectName("show_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 270, 511, 151))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "nick發外鏈"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ff0000;\">nick發外鏈</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">要發什麼呢～</span></p></body></html>"))
        self.domain_lineEdit.setText(_translate("MainWindow", "www.ibet1668m.com"))
        self.go_pushButton.setText(_translate("MainWindow", "Go"))