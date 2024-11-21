import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QDate
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from Ui_main import Ui_MainWindow
import sqlconnect,qmfetch
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem
import pandas

class CallMain(QMainWindow, Ui_MainWindow):
    '''
    创建窗体
    '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableView = self.findChild(QtWidgets.QTableView,'tableView')
        self.pushSQLdata =self.findChild(QtWidgets.QPushButton,'pushSQLdata')
        self.pushQMdata =self.findChild(QtWidgets.QPushButton,'pushQMdata')
        self.pushQuit =self.findChild(QtWidgets.QPushButton,'pushQuit')
        self.dateStartDate=self.findChild(QtWidgets.QDateEdit,'dateStartDate')
        self.dateEndDate=self.findChild(QtWidgets.QDateEdit,'dateEndDate')
        self.pushSQLdata.clicked.connect(self.get_SQLdata)
        self.pushQMdata.clicked.connect(self.get_QMdata)
        self.pushQuit.clicked.connect(self.push_Quit)
        #设置表格tableView的表头
        self.viewmodel = QStandardItemModel()
        sql_head = ['条码','检测时间','专业组','流水号','申请项目','千麦条码','姓名','千麦目的','样本状态','检测时间']
        self.viewmodel.setHorizontalHeaderLabels(sql_head)
        self.tableView.setModel(self.viewmodel)  # 设置模型为表格视图的数据源。  
        self.tableView.setColumnWidth(1,80)
        self.tableView.setColumnWidth(2,50)
        #设置开始日期，结束日期
        now_day =QDate.currentDate()
        self.dateEndDate.setDate(now_day)
        self.dateStartDate.setDate(now_day.addDays(-7))
    
    def get_SQLdata(self):
        '''
        获取sql server数据并更新到tableview中
        '''
        SQL_query = "SELECT LabGroupCode,TestDate,SampleNo,Barcode,SampleState,SampleTypeCode,SampleTypeName,ApplyItemCodes,ApplyItemNames,LabRemark \
                 FROM Exam_Sample WHERE SampleState=400 AND TestDate >= ? ORDER BY LabGroupCode ASC, TestDate ASC"
        starttime = self.dateStartDate.date()
        start_date = QDate.toString(starttime,'yyyy-MM-dd') #.strftime('%Y-%m-%d')
        sql_parm= (start_date,)
        SQLdata=sqlconnect.Sqlfetch(SQL_query,sql_parm)
        table_head=['LabGroupCode','TestDate','SampleNo','Barcode','SampleState','SampleTypeCode','SampleTypeName','ApplyItemCodes','ApplyItemNames']
        result = [dict(zip(table_head, row)) for row in SQLdata]  
        pd =pandas.DataFrame(result)
        pddata=pd.set_index('Barcode')
        col = 0
        for val in pddata.index:
            try:
                data = pddata.loc[val]
                if data[0] == 'GK001':
                    labgroup='PCR'
                elif data[0] == 'GK002':
                    labgroup='外送'
                elif data[0] == 'GK004':
                    labgroup='微生物'
                elif data[0] == 'GK005':
                    labgroup='生化'
                elif data[0] == 'GK006':
                    labgroup='免疫'
                elif data[0] == 'GK007':
                    labgroup='质谱'
                elif data[0] == 'GK008':
                    labgroup='流式'
                elif data[0] == 'GK009':
                    labgroup='病理'
                elif data[0] == 'GK010':
                    labgroup='NGS'
                elif data[0] == 'GK011':
                    labgroup='过敏原'
                if labgroup =='外送':
                    row=[val,data[1].strftime('%Y-%m-%d'),labgroup,data[2],data[7]]
                    for j in range(5):
                        item= QStandardItem(str(row[j]))
                        self.viewmodel.setItem(col,j,item)
                    col = col+1
            except KeyError:
                pass

    def get_QMdata(self):
        '''
        获取千麦报告单查询数据，并将获得的数据与lims数据进行匹配，有匹配项的更新数据
        '''
        #starttime= datetime.now() - timedelta(days=7)
        starttime = self.dateStartDate.date()
        start_date = QDate.toString(starttime,'yyyy-MM-dd') #.strftime('%Y-%m-%d')
        endtime = self.dateEndDate.date()
        end_date = QDate.toString(endtime,'yyyy-MM-dd')
        result_msg=QMessageBox()
        qmdata = qmfetch.Requestqm(start_date,end_date)
        if isinstance(qmdata,str):
            if qmdata == '日期格式不正确':
                result_msg.information(None,'错误','日期格式不正确')
                return
            elif qmdata == '开始日期大于结束日期':
                result_msg.information(None,'日期设置错误','开始日期大于结束日期')
                return
        for valtable in range(self.viewmodel.rowCount()):
            table_item =self.viewmodel.item(valtable,0)
            barcode =table_item.data(Qt.DisplayRole)
            try: 
                row_data =qmdata.loc[barcode]
                inst_data = [row_data[3],row_data[5],row_data[8],row_data[9],row_data[20]]
                for j in range(5):
                    ditem= QStandardItem(str(inst_data[j]))
                    self.viewmodel.setItem(valtable,j+5,ditem)
            except KeyError:
                pass

    def push_Quit(self):
        self.close()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main=CallMain()
    main.show()
    sys.exit(app.exec_())