from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QWidget
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QEvent
from  Ui_mainWindow import Ui_Form
import sqlconnect
import sys,os
import pandas as pd
import datetime

file_path_txt = ""
class CallMain(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.pushSourceFile =self.findChild(QtWidgets.QPushButton,'pushSourceFile')
        self.textResult = self.findChild(QtWidgets.QTextBrowser,'textResult')
        self.pushViewData = self.findChild(QtWidgets.QPushButton,'pushViewData')
        self.pushDataDump = self.findChild(QtWidgets.QPushButton,'pushDataDump')
        self.pushSampleInfo =self.findChild(QtWidgets.QPushButton,'pushSampleInfo')
        self.tvSampleInfo = self.findChild(QtWidgets.QTableView,'tvSampleInfo')
        self.groupBoxSample=self.findChild(QtWidgets.QGroupBox,'groupBoxSample')
        self.groupBoxResult=self.findChild(QtWidgets.QGroupBox,'groupBoxResult')
        self.groupSourceFile=self.findChild(QtWidgets.QGroupBox,'groupSourceFile')
        self.horizontalLayout=self.findChild(QtWidgets.QHBoxLayout,'horizontalLayout')
        self.horizontalLayoutWidget=self.findChild(QtWidgets.QWidget,'horizontalLayoutWidget')
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
        self.tvSampleInfo.setColumnWidth(1,60)
        self.tvSampleInfo.setColumnWidth(2,80)
        self.tvSampleInfo.setColumnWidth(3,160)
        self.tvSampleInfo.setColumnWidth(4,50)
        self.tvSampleInfo.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def initUI(self):
        self.show()


    def Chg_sample(self,file_txt,dump=0):
        filename = file_txt
        file_out = os.path.splitext(filename)[0] + "_out" + os.path.splitext(filename)[1]
        try:
            df = pd.read_csv(filename, encoding="gbk", names=["SampleNo", "Name", "Val", "Sr"])
        except UnicodeDecodeError:
            df_result='文件格式不正确！'
            return df_result
        
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
        searchdate = datetime.date.today() - datetime.timedelta(days=30)
        SQL_parm=(str(searchdate),)
        SQL_query = "SELECT d.SampleNoAuto,d.BarcodeSub,f.PatientName, d.LabGroupCode,d.TestDate, d.SampleNo,d.SampleState,d.ApplyItemCodes,d.ApplyItemNames \
            FROM Exam_Sample as d INNER JOIN Exam_SamePatient as f on d.Barcode = f.Barcode WHERE d.SampleState=400 AND d.LabGroupCode = 'GK011'"
        SQLdata=sqlconnect.Sqlfetch(SQL_query)
        table_head=['SampleNoAuto','BarcodeSub','PatientName','LabGroupCode','TestDate','SampleNo','SampleState','ApplyItemCodes','ApplyItemNames']
        result = [dict(zip(table_head, row)) for row in SQLdata]  
        if len(result):
            pddata =pd.DataFrame(result)
            pddata=pddata.set_index('SampleNoAuto')
            if isinstance(pddata,str):
                return
        else:
            message=QtWidgets.QMessageBox()
            message.warning(self,"警告","当前没有过敏原待检测数据")
            return
        col = 0
        for val in pddata.index:
            try:
                data=pddata.loc[val]
                #print(f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}')
                row =[data[0],data[1],data[3].strftime('%Y-%m-%d'),data[7]]
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

    #重写changEvent,判断窗体变化，如最大化调整控件大小
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                max_width = self.frameGeometry().width()
                max_height = self.frameGeometry().height()
                # 调整标签的大小以适应窗口的最大尺寸
                new_width = int(max_width * 0.62)  # 标签宽度为窗口宽度的一半
                new_height = int(max_height * 0.64)  # 标签高度为窗口高度的五分之一
                self.groupBoxSample.setGeometry(QtCore.QRect(0, 0, int(max_width*0.63), int(max_height*0.64)))
                self.tvSampleInfo.setGeometry(QtCore.QRect(int(max_width*0.01), int(max_height*0.03), new_width-20, new_height-20))
                self.groupBoxResult.setGeometry(QtCore.QRect(int(max_width*0.64), 0, int(max_width*0.35), int(max_height*0.64)))
                self.textResult.setGeometry(QtCore.QRect(10, 20, int(max_width*0.33), int(max_height*0.58)))
                self.groupSourceFile.setGeometry(QtCore.QRect(20, int(max_height * 0.66), 721, 59))
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(int(max_width*0.22), int(max_height*0.86), int(max_width*0.47), 51))
                self.tvSampleInfo.setColumnWidth(0,160)
                self.tvSampleInfo.setColumnWidth(1,96)
                self.tvSampleInfo.setColumnWidth(2,128)
                self.tvSampleInfo.setColumnWidth(3,256)
                self.tvSampleInfo.setColumnWidth(4,80)
            else:
                self.groupBoxSample.setGeometry(QtCore.QRect(0, 0, 541, 291))
                self.tvSampleInfo.setGeometry(QtCore.QRect(10, 20, 521, 261))
                self.groupBoxResult.setGeometry(QtCore.QRect(550, 0, 301, 291))
                self.textResult.setGeometry(QtCore.QRect(10, 20, 281, 261))
                self.groupSourceFile.setGeometry(QtCore.QRect(20, 300, 721, 59))
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 370, 401, 51))
                self.tvSampleInfo.setColumnWidth(0,100)
                self.tvSampleInfo.setColumnWidth(1,60)
                self.tvSampleInfo.setColumnWidth(2,80)
                self.tvSampleInfo.setColumnWidth(3,160)
                self.tvSampleInfo.setColumnWidth(4,50)
        super(CallMain, self).changeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main=CallMain()
    main.show()
    sys.exit(app.exec_())



