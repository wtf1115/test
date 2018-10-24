from base.basepage import BasePage
from pageobject.Managecentrepage import Managecentrepage


class Helpmanagecentrepage(BasePage):
#点击进入论坛方法
    def click_luntan(self):

        self.click(*Managecentrepage.luntan)
#进入iframe框架
    def frame(self):
        self.frame("main")
#创建新版块方法
    def build_plate(self,content):

        self.click(*Managecentrepage.new_plate)
        self.clear(*Managecentrepage.new_plate_input)
        self.sendkeys(content,*Managecentrepage.new_plate_input)
        self.click(*Managecentrepage.new_plate_submit)

#退出方法
    def  back(self):
        self.click(*Managecentrepage.back_submit)