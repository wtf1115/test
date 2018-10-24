from selenium.webdriver.common.keys import Keys
import time
import unittest
from pageobject.homepage import Homepage
from helppage.Help_homepage import Helphomepage
from helppage.Help_defaltpage import Helpsecondpage
from helppage.Help_articlepage import Helpthirdpage
from tesecase.test_base import test_basecase

class luntan_1(test_basecase):
    def test_luntan1(self):#test开头的方法是测试方法 基类可以识别
        home_page=Helphomepage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")
        time.sleep(2)
        home_page.luntanlogin("admin","admin")
        print(self.driver.title)
        time.sleep(5)
        home_page.click_mrbk()
        secondpage=Helpsecondpage(self.driver)
        secondpage.fatie_input_title("lpp")
        secondpage.fatie_input_content("lllo")
        secondpage.fatie_click()
        thirdpage=Helpthirdpage(self.driver)
        thirdpage.reply("olo")

if __name__=="__main__":
    unittest.main()
