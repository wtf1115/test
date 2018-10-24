from base.basepage import BasePage
from pageobject.Votepage import Votepage


class Helpvotepage(BasePage):
#写发起投票文章方法
    def vote(self,content1,content2,content3,content4,):
        self.sendkeys(content1,*Votepage.vote_title)
        self.sendkeys(content2, *Votepage.vote_part1)
        self.sendkeys(content3, *Votepage.vote_part2)
        self.sendkeys(content4, *Votepage.vote_part3)
        self.click(*Votepage.vote_button)