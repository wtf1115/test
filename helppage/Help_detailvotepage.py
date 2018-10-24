from pageobject.detailvotepage import Votedetailpage
from base.basepage import BasePage

class Helpdetailpage(BasePage):
    def click_vote(self):
        self.click(*Votedetailpage.vote_button)
