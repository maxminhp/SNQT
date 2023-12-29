from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
import pandas
from datetime import datetime
def Is_validDate(date_string):
    '''
    测试日期是否有效。检测传入的字符串是否可以被转换，可以返回True,否则返回False
    '''
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def Requestqm(starttime,endtime=''):  
    '''
    向千麦报告查询网站获取数据，starttime为查询的开始时间，endtime为查询的结束时间
    '''
    # 检测传入的日期格式是否正确 
    today_date = datetime.strftime(datetime.today(),'%Y-%m-%d')
    if Is_validDate(starttime):
        start_date=datetime.strptime(starttime,'%Y-%m-%d')
        if endtime:
                if Is_validDate(endtime):
                    end_date =datetime.strptime(endtime,'%Y-%m-%d')
                    if end_date < start_date:
                        return '开始日期大于结束日期'
                    elif endtime == today_date:
                        endtime=''
    else:
        return '日期格式不正确'
    #加载selenium的驱动并创建服务
    driverfile_path= r'D:\Python31\Scripts\MicrosoftWebDriver.exe'
    service = EdgeService(executable_path=driverfile_path)
    driver = webdriver.Edge(service=service) 
    wait = WebDriverWait(driver,60)
    driver.get("https://center.cmlabs.com.cn/account/login")  
    driver.implicitly_wait(60)
    driver.maximize_window() 
    # 定位输入框并输入用户名和密码  
    username_input = driver.find_element(By.ID, "UserName")  
    password_input = driver.find_element(By.ID, "Password")  
    username_input.send_keys("817343")  
    password_input.send_keys("Abc123,")  
    # 定位登录按钮并点击  
    login_button = driver.find_element(By.ID, "btnLogin")  
    login_button.click()  
    # 点击报告查询
    main_menu = driver.find_element(By.CSS_SELECTOR,".el-submenu")
    AC(driver).move_to_element(main_menu).click(main_menu).perform()
    # 点击报告查询
    reportbtn = driver.find_element(By.XPATH,"//span[contains(text(),'报告管理')]")
    reportbtn.click()
    # 修改类型为检测时间
    type_time =driver.find_element(By.XPATH,"//div[@class='el-input el-input--mini el-input--suffix']//input[@type='text' and @placeholder='']")
    driver.execute_script("arguments[0].click();",type_time)
    exam_time = driver.find_element(By.XPATH,"//SPAN[contains(text(),'检测时间')]")
    exam_time.click()
    # 传入开始日期和结束日期并查询
    if starttime:
        starttimebtn=driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='开始日期' and @class='el-input__inner']")
        starttimebtn.clear()
        starttimebtn.send_keys(starttime)
    if endtime:
        endtimebtn=driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='结束日期' and @class='el-input__inner']")
        endtimebtn.clear()
        endtimebtn.send_keys(endtime)
    querybtn = driver.find_element(By.XPATH,"//div[@id='div_dom_1']//span[contains(text(),'查询')]")
    driver.execute_script("arguments[0].click();", querybtn)
    # 开始获取表格内数据
    body_data=[]
    tablebody=wait.until(EC.visibility_of_element_located((By.XPATH,"//table[@class='vxe-table--body']")))  
    bodyrows=tablebody.find_elements(By.TAG_NAME,"tr")
    for body in bodyrows:
        body_cols= body.find_elements(By.TAG_NAME,"td")
        col_data=[]
        for col in body_cols:
            col_data.append(col.text)
        body_data.append(col_data)
    driver.close()
    head_data=['选择','采集时间','接收时间','样本条码','医院名称','姓名','性别','年龄','检验目的','样本状态','科室','病区','床号','送检医生','门诊住院号','医院条码','备注','证件号','手机号','检验者','检测日期','审核者','审核时间']
    pd=pandas.DataFrame(body_data,columns=head_data)
    pd=pd.set_index('医院条码',drop=True)
    return pd
