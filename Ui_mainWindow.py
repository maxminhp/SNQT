# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\projectcode\SNQT\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 453)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        Form.setFont(font)
        self.groupBoxSample = QtWidgets.QGroupBox(Form)
        self.groupBoxSample.setGeometry(QtCore.QRect(0, 0, 541, 291))
        self.groupBoxSample.setObjectName("groupBoxSample")
        self.tvSampleInfo = QtWidgets.QTableView(self.groupBoxSample)
        self.tvSampleInfo.setGeometry(QtCore.QRect(10, 20, 521, 261))
        self.tvSampleInfo.setObjectName("tvSampleInfo")
        self.groupBoxResult = QtWidgets.QGroupBox(Form)
        self.groupBoxResult.setGeometry(QtCore.QRect(550, 0, 301, 291))
        self.groupBoxResult.setObjectName("groupBoxResult")
        self.textResult = QtWidgets.QTextBrowser(self.groupBoxResult)
        self.textResult.setGeometry(QtCore.QRect(10, 20, 281, 261))
        self.textResult.setObjectName("textResult")
        self.groupSourceFile = QtWidgets.QGroupBox(Form)
        self.groupSourceFile.setGeometry(QtCore.QRect(20, 300, 721, 59))
        self.groupSourceFile.setObjectName("groupSourceFile")
        self.pushSourceFile = QtWidgets.QPushButton(self.groupSourceFile)
        self.pushSourceFile.setGeometry(QtCore.QRect(610, 20, 75, 23))
        self.pushSourceFile.setObjectName("pushSourceFile")
        self.textSourceFile = QtWidgets.QTextBrowser(self.groupSourceFile)
        self.textSourceFile.setGeometry(QtCore.QRect(10, 20, 501, 21))
        self.textSourceFile.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textSourceFile.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textSourceFile.setObjectName("textSourceFile")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 370, 401, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hLayoutPushArea = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayoutPushArea.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.hLayoutPushArea.setContentsMargins(0, 0, 0, 0)
        self.hLayoutPushArea.setSpacing(50)
        self.hLayoutPushArea.setObjectName("hLayoutPushArea")
        self.pushSampleInfo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushSampleInfo.setObjectName("pushSampleInfo")
        self.hLayoutPushArea.addWidget(self.pushSampleInfo)
        self.pushViewData = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushViewData.setObjectName("pushViewData")
        self.hLayoutPushArea.addWidget(self.pushViewData)
        self.pushDataDump = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushDataDump.setObjectName("pushDataDump")
        self.hLayoutPushArea.addWidget(self.pushDataDump)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "过敏原样本号替换小程序"))
        self.groupBoxSample.setTitle(_translate("Form", "样本信息"))
        self.groupBoxResult.setTitle(_translate("Form", "结果信息"))
        self.groupSourceFile.setTitle(_translate("Form", "源数据文件"))
        self.pushSourceFile.setText(_translate("Form", "选择文件"))
        self.pushSampleInfo.setText(_translate("Form", "获取数据"))
        self.pushViewData.setText(_translate("Form", "查看"))
        self.pushDataDump.setText(_translate("Form", "导出"))
