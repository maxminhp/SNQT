# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\projectcode\client\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 768)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 891, 711))
        self.tableView.setObjectName("tableView")
        self.pushSQLdata = QtWidgets.QPushButton(self.centralwidget)
        self.pushSQLdata.setGeometry(QtCore.QRect(920, 160, 101, 23))
        self.pushSQLdata.setObjectName("pushSQLdata")
        self.pushQMdata = QtWidgets.QPushButton(self.centralwidget)
        self.pushQMdata.setGeometry(QtCore.QRect(920, 200, 101, 23))
        self.pushQMdata.setObjectName("pushQMdata")
        self.pushQuit = QtWidgets.QPushButton(self.centralwidget)
        self.pushQuit.setGeometry(QtCore.QRect(920, 250, 101, 23))
        self.pushQuit.setObjectName("pushQuit")
        self.grpBoxStartDate = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxStartDate.setGeometry(QtCore.QRect(910, 10, 131, 51))
        self.grpBoxStartDate.setObjectName("grpBoxStartDate")
        self.dateStartDate = QtWidgets.QDateEdit(self.grpBoxStartDate)
        self.dateStartDate.setGeometry(QtCore.QRect(10, 20, 110, 22))
        self.dateStartDate.setObjectName("dateStartDate")
        self.grpBoxEndDate = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxEndDate.setGeometry(QtCore.QRect(910, 70, 131, 51))
        self.grpBoxEndDate.setObjectName("grpBoxEndDate")
        self.dateEndDate = QtWidgets.QDateEdit(self.grpBoxEndDate)
        self.dateEndDate.setGeometry(QtCore.QRect(10, 20, 110, 22))
        self.dateEndDate.setObjectName("dateEndDate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "千麦报告单状态"))
        self.pushSQLdata.setText(_translate("MainWindow", "LIS数据"))
        self.pushQMdata.setText(_translate("MainWindow", "千麦数据"))
        self.pushQuit.setText(_translate("MainWindow", "退出"))
        self.grpBoxStartDate.setTitle(_translate("MainWindow", "开始日期"))
        self.grpBoxEndDate.setTitle(_translate("MainWindow", "结束日期"))
