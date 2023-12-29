import pyodbc
import datetime
import pandas
def Sqlfetch():
    '''
    查询lims服务器上的检验中数据
    '''
    server = '172.30.11.26'  
    database = 'CYLIMS_Exam'  
    username = 'gkapi'  
    password = 'Cwmda@2023'  
    driver= '{SQL Server}'  # 根据实际情况修改  
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'  
    conn = pyodbc.connect(connection_string)  
    cursor = conn.cursor()  
    SQL_query = "SELECT d.Barcode,f.PatientName, d.LabGroupCode,d.TestDate, d.SampleNo,d.SampleState,d.ApplyItemCodes,d.ApplyItemNames \
                FROM Exam_Sample as d INNER JOIN Exam_SamePatient as f on d.Barcode = f.Barcode \
                WHERE d.SampleState=400 AND d.LabGroupCode = 'GK011' AND d.TestDate >= ? "
    searchdate = datetime.date.today() - datetime.timedelta(days=7)
    search_date=(str(searchdate),)
    table_head=['Barcode','PatientName','LabGroupCode','TestDate','SampleNo','SampleState','ApplyItemCodes','ApplyItemNames']
    cursor = conn.cursor()
    cursor.execute(SQL_query,search_date)
    result = [dict(zip(table_head, row)) for row in cursor.fetchall()]  
    if len(result):
        pd =pandas.DataFrame(result)
        pd=pd.set_index('Barcode')
        return pd
    return ''