from pageobject.homepage import Homepage
from helppage.Help_homepage import Helphomepage
from helppage.Help_defaltpage import Helpsecondpage
from helppage.Help_articlepage import Helpthirdpage
from helppage.Help_managepage import Helpmanagepage
from helppage.Help_managecentrepage import Helpmanagecentrepage
from helppage.Help_searchpage import Helpsearchpage
from helppage.Help_detailvotepage import Helpdetailpage
from tesecase.test_base import test_basecase
from helppage.Help_votepage import Helpvotepage
from helppage.Help_votepartpage import Helpvotepage1
import time
import unittest

class luntan1(test_basecase):
    def test_luntan4(self):
        home_page = Helphomepage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)
        home_page.luntanlogin("admin", "admin")
        time.sleep(2)
        home_page.click_mrbk()
        time.sleep(2)
        second_page = Helpsecondpage(self.driver)
        time.sleep(2)
        second_page.click_vote()
        detail_vote=Helpdetailpage(self.driver)
        detail_vote.click_vote()

        vote_page=Helpvotepage(self.driver)
        vote_page.vote("比比看谁笨","崔泽明","张志强","刘彩凤")

        votepart_page=Helpvotepage1(self.driver)
        votepart_page.vote()
        time.sleep(2)
        votepart_page.print_vote()

if __name__=="__main__":
    unittest.main()