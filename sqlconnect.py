import pyodbc
import datetime
import pandas
def Sqlfetch(qrytext,qryparm):
    '''
    查询lims服务器上的检验中数据
    '''
    SQL_query = qrytext
    SQL_parm = qryparm
    server = '172.30.11.26'  
    database = 'CYLIMS_Exam'  
    username = 'gkapi'  
    password = 'Cwmda@2023'  
    driver= '{SQL Server}'  # 根据实际情况修改  
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'  
    conn = pyodbc.connect(connection_string)  
    cursor = conn.cursor()  
    cursor.execute(SQL_query,SQL_parm)
    qrydata= cursor.fetchall()
    return qrydata
   