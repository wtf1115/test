from selenium.webdriver.common.keys import Keys
import time
import unittest
from pageobject.homepage import Homepage
from helppage.Help_homepage import Helphomepage
from helppage.Help_defaltpage import Helpsecondpage
from helppage.Help_articlepage import Helpthirdpage
from helppage.Help_managepage import Helpmanagepage
from helppage.Help_managecentrepage import Helpmanagecentrepage
from helppage.Help_searchpage import Helpsearchpage
from tesecase.test_base import test_basecase

class luntan1(test_basecase):
    def test_luntan3(self):
        home_page = Helphomepage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)
        home_page.luntanlogin("admin","admin")
        time.sleep(2)
        home_page.search("lpp")
        time.sleep(3)
        search_page=Helpsearchpage(self.driver)
        self.driver.switch_to.window(self.driver.window_handles[1])
        search_page.click_search_essay()
        self.driver.close()


        article_page=Helpthirdpage(self.driver)
        self.driver.switch_to.window(self.driver.window_handles[1])
        article_page.comparison()



if __name__=="__main__":
    unittest.main()