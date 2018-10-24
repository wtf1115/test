from base.basepage import BasePage
from pageobject.Defaultplatepage import Secondpage


class Helpsecondpage(BasePage):
#点击nihao文章方法
    def click_eaasy1(self):
        self.click(*Secondpage.essay_title1)

#点击发表帖子
    def click_vote(self):
        self.click(*Secondpage.fatie_button)
#鼠标移动到发帖按钮上

#点击发起投票按钮

#点击比比看谁傻文章方法
    def click_eaasy2(self):
        self.click(*Secondpage.essay_title2)
#发帖输入标题方法
    def fatie_input_title(self,content):
        self.sendkeys(content,*Secondpage.fatie_title)
#发帖输入内容方法
    def fatie_input_content(self,content):
        self.sendkeys(content, *Secondpage.fatie_content)
#提交发帖按钮方法
    def fatie_click(self):
        self.click(*Secondpage.fatie_submit)

#点击退出方法
    def quit_click(self):
        self.click(*Secondpage.quit_button)