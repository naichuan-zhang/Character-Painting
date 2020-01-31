# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 600))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_conversion = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_conversion.setGeometry(QtCore.QRect(550, 420, 101, 101))
        self.pushButton_conversion.setStyleSheet("background-image:url(:/png/img/conversion.png);")
        self.pushButton_conversion.setText("")
        self.pushButton_conversion.setObjectName("pushButton_conversion")

        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(550, 160, 101, 31))
        self.pushButton_input.setStyleSheet("background-image:url(:/png/img/import.png);")
        self.pushButton_input.setText("")
        self.pushButton_input.setObjectName("pushButton_input")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(550, 220, 101, 94))
        self.textEdit.setStyleSheet("color:rgb(255,0,0);")
        self.textEdit.setObjectName("textEdit")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 350, 101, 31))
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")

        self.input_img = QtWidgets.QLabel(self.centralwidget)
        self.input_img.setGeometry(QtCore.QRect(28, 85, 500, 500))
        self.input_img.setText("")
        self.input_img.setScaledContents(True)
        self.input_img.setObjectName("input_img")

        self.export_img = QtWidgets.QLabel(self.centralwidget)
        self.export_img.setGeometry(QtCore.QRect(674, 85, 500, 500))
        self.export_img.setText("")
        self.export_img.setScaledContents(True)
        self.export_img.setAlignment(QtCore.Qt.AlignCenter)
        self.export_img.setObjectName("export_img")

        self.loading = QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(550, 250, 100, 100))
        self.loading.setText("")
        self.loading.setObjectName("loading")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入字符"))
        self.comboBox.setItemText(0, _translate("MainWindow", "清晰"))
        self.comboBox.setItemText(1, _translate("MainWindow", "一般"))
        self.comboBox.setItemText(2, _translate("MainWindow", "字符"))


import img_qc_rc
