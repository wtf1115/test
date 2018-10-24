from base.basepage import BasePage
from pageobject.articlepage import Thirdpage


class Helpthirdpage(BasePage):
#删除文章方法
    def delete_essay(self):
        self.click(*Thirdpage.delete_subject)
        self.click(*Thirdpage.delete_sure)


#回复评论
    def reply(self,content):
        self.sendkeys(content,*Thirdpage.reply_content)
        self.click(*Thirdpage.reply_button)
#文章验证方法
    def comparison(self):
        content1=self.print1(*Thirdpage.essay_content)
        str(content1)
        print(type(content1))
        content="lllo"
        if content1 not in content:
            print("文章验证失败")
        else:
            print("文章验证成功")

#点击退出方法
    def quit_click(self):
        self.click(*Thirdpage.quit_button)