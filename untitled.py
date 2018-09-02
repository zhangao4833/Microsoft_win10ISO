# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import win32clipboard as w
import win32con
from PyQt5.QtGui import QIcon, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 禁止拉伸窗口大小
        MainWindow.resize(553, 499)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 390, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 90, 531, 23))
        self.progressBar.setAccessibleName("")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 150, 531, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 210, 531, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(198, 93, 181, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 30, 331, 31))
        self.label_2.setStyleSheet("font: 16pt \"幼圆\";\n""")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(85, 55, 370, 38))
        self.label_9.setStyleSheet("font: 10pt \"幼圆\";\n""")
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(215, 154, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(213, 213, 141, 16))
        self.label_4.setObjectName("label_4")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(10, 270, 531, 23))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(201, 273, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 460, 231, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(391, 459, 141, 20))
        self.label_7.setStyleSheet("font: 75 11pt \"Lao UI\";")
        self.label_7.setObjectName("label_7")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(10, 330, 531, 23))
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(227, 332, 311, 20))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 357, 201, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "微软官网Windows10ISO文件爬取器---作者：www.imzhangao.com"))
        self.setWindowIcon(QIcon('lib/favicon.ico'))
        self.pushButton.setText(_translate("MainWindow", "开始获取"))
        self.label.setText(_translate("MainWindow", "爬取微软官方链接中..."))
        self.label_2.setText(_translate("MainWindow", "微软官网Windows10ISO文件爬取器"))
        self.label_9.setText(_translate("MainWindow", "（该软件请搭配最新的Chrome浏览器使用，否则会闪退！）"))
        self.label_3.setText(_translate("MainWindow", "获取现有版本中..."))
        self.label_4.setText(_translate("MainWindow", "获取现有语言中..."))
        self.label_5.setText(_translate("MainWindow", "获取所有位数的系统..."))
        self.label_6.setText(_translate("MainWindow", "作者提醒:该软件BUG尚多，请勿瞎几把操作"))
        self.label_7.setText(_translate("MainWindow", "www.imzhangao.com"))
        self.label_8.setText(_translate("MainWindow", "开始下载中..."))
        self.pushButton_2.setText(_translate("MainWindow", "下载器下载太慢?点此复制下载链接"))
