from base.basepage import BasePage
from pageobject.Votepartpage import Votepartpage


class Helpvotepage1(BasePage):
#投票方法
    def vote(self):
        self.click(*Votepartpage.vote_select)
        self.click(*Votepartpage.vote_button)
    def print_vote(self):
        self.print1(*Votepartpage.vote_titleprint)
        self.print1(*Votepartpage.vote_print)
        self.print1(*Votepartpage.vote_print_1)
        self.print1(*Votepartpage.vote_print2)
        self.print1(*Votepartpage.vote_print_2)
        self.print1(*Votepartpage.vote_print3)
        self.print1(*Votepartpage.vote_print_3)
