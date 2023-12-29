from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from  Ui_mainWindow import Ui_Form
import sqlconnect
import sys,os
import pandas as pd

file_path_txt = ""
class CallMain(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.pushSourceFile =self.findChild(QtWidgets.QPushButton,'pushSourceFile')
        self.textResult = self.findChild(QtWidgets.QTextBrowser,'textResult')
        self.pushViewData = self.findChild(QtWidgets.QPushButton,'pushViewData')
        self.pushDataDump = self.findChild(QtWidgets.QPushButton,'pushDataDump')
        self.pushSampleInfo =self.findChild(QtWidgets.QPushButton,'pushSampleInfo')
        self.tvSampleInfo = self.findChild(QtWidgets.QTableView,'tvSampleInfo')
        #self.show()
        self.pushSourceFile.clicked.connect(self.SelectFileTXT)
        self.pushViewData.clicked.connect(self.ViewData)
        self.pushDataDump.clicked.connect(self.DumpData)
        self.pushSampleInfo.clicked.connect(self.GetSampleInfo)
        self.viewmodel = QStandardItemModel()
        sql_head = ['条码','姓名','检测时间','申请项目','上机号']
        self.viewmodel.setHorizontalHeaderLabels(sql_head)
        self.tvSampleInfo.setModel(self.viewmodel)
        self.tvSampleInfo.setColumnWidth(0,100)
        self.tvSampleInfo.setColumnWidth(1,50)
        self.tvSampleInfo.setColumnWidth(2,80)
        self.tvSampleInfo.setColumnWidth(3,90)
        self.tvSampleInfo.setColumnWidth(4,50)
        self.tvSampleInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def Chg_sample(self,file_txt,dump=0):
        filename = file_txt
        file_out = os.path.splitext(filename)[0] + "_out" + os.path.splitext(filename)[1]
        df = pd.read_csv(filename, encoding="gbk", names=["SampleNo", "Name", "Val", "Sr"])
        for val in range(self.viewmodel.rowCount()):
            barcodedata = self.viewmodel.item(val,0)
            machinedata = self.viewmodel.item(val,4)
            try:
                barcode = barcodedata.data(QtCore.Qt.DisplayRole)
                machineno = machinedata.data(QtCore.Qt.DisplayRole)
                if isinstance(machineno,str):
                    df["SampleNo"].replace(int(machineno), barcode, inplace=True)
            except AttributeError:
                pass
        if dump == 1:
            try:
                df.to_csv(file_out, index=False, header=False,encoding="utf-8-sig")
                df_result= file_out +'文件生成！'
            except PermissionError:
                df_result='导出文件被占用,请先关闭该文件!'
            except Exception as e:
                df_result='出现错误！错误信息：' + e
            return df_result
        elif dump == 0:
            return df

    def GetSampleInfo(self):
        SQLdata=sqlconnect.Sqlfetch()
        if isinstance(SQLdata,str):
            return
        col = 0
        for val in SQLdata.index:
            try:
                data=SQLdata.loc[val]
                #print(data)
                row =[val,data[0],data[2].strftime('%Y-%m-%d'),data[6]]
                for j in range(4):
                    item= QStandardItem(str(row[j]))
                    self.viewmodel.setItem(col,j,item)
                col = col+1
            except KeyError:
                pass

    def SelectFileTXT(self):
        global file_path_txt
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("TEXT Files (*.txt)")
        dialog.show()
        if dialog.exec_() == QFileDialog.Accepted:
            selectTXTFiles = dialog.selectedFiles()
            file_path_txt=selectTXTFiles[0]
        if file_path_txt:   
            self.textSourceFile.setText(file_path_txt)
            return file_path_txt
        return None
    
    def ViewData(self):
        intFile = len(file_path_txt)
        if  intFile > 0 :
            result = self.Chg_sample(file_path_txt)
            result_str = result.to_string()
            self.textResult.clear()
            self.textResult.append(result_str)
            self.textResult.show()

    def DumpData(self):
        intFile = len(file_path_txt)
        result_msg = QtWidgets.QMessageBox()
        if  intFile > 0 :
            result = self.Chg_sample(file_path_txt, 1)
            result_msg.information(None,'信息',result)
        else:
            result_msg.information(None,'错误',"未选择文件！")
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main=CallMain()
    main.show()
    sys.exit(app.exec_())



