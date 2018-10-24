from base.basepage import BasePage
from selenium.webdriver.common.keys import Keys
from pageobject.homepage import Homepage


class Helphomepage(BasePage):
#登录方法
    def luntanlogin(self, content1, content2):
        self.sendkeys(content1,*Homepage.login_name_input)
        self.sendkeys(content2,*Homepage.login_pwd_input)
        self.click(*Homepage.login_submit)
#点击默认板块方法
    def click_mrbk(self):
        self.click(*Homepage.fatie_mrbk)
#点击新版块方法
    def click_xbk(self):
        self.click(*Homepage.xbk)
#点击管理中心方法
    def click_manage(self):
        self.click(*Homepage.glzx_button)
#搜索内容方法
    def search(self,content):
        self.sendkeys(content,*Homepage.search_input)
        self.click(*Homepage.search_button)
#点击退出方法
    def quit_click(self):
        self.click(*Homepage.quit_input)