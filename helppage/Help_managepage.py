from base.basepage import BasePage
from pageobject.Managementloginpage import Fourthdpage


class Helpmanagepage(BasePage):
#管理中心登录方法
    def manage_login(self,content):
        print("hhhhhhhhahah颈康胶囊  借记卡")
        self.sendkeys(content, *Fourthdpage.manage_login)
        self.click(*Fourthdpage.manage_submit)
