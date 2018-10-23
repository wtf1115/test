from selenium.webdriver.common.by import By
from base.basepage import BasePage



class Managecentrepage(BasePage):
#论坛元素
    luntan=(By.CSS_SELECTOR,"#header_forum")
#创建新版块元素
    new_plate=(By.CSS_SELECTOR,".lastboard .addtr")
#新版块名称输入元素
    new_plate_input=(By.CSS_SELECTOR,"#cpform table tbody:nth-child(3) tr:nth-child(1) td:nth-child(3) div  input")
#新版块提交元素
    new_plate_submit=(By.ID,"submit_editsubmit")
#退出元素
    back_submit=(By.CSS_SELECTOR,"#frametable .mainhd #frameuinfo p:nth-child(1) a")