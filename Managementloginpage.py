from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Fourthdpage(BasePage):
    #管理中心登录元素
    manage_login=(By.CSS_SELECTOR,"#loginform .txt")
    #提交元素
    manage_submit=(By.CSS_SELECTOR,"#loginform .loginnofloat .btn")