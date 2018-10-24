from base.basepage import BasePage
from pageobject.searchpage import searchpage


class Helpsearchpage(BasePage):
    def click_search_essay(self):
        self.click(*searchpage.essay)