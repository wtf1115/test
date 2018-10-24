from selenium.webdriver.common.keys import Keys
import time
import unittest
from pageobject.homepage import Homepage
from helppage.Help_homepage import Helphomepage
from helppage.Help_defaltpage import Helpsecondpage
from helppage.Help_articlepage import Helpthirdpage
from helppage.Help_managepage import Helpmanagepage
from helppage.Help_managecentrepage import Helpmanagecentrepage
from tesecase.test_base import test_basecase

class luntan_1(test_basecase):
    def test_luntan1(self):#test开头的方法是测试方法 基类可以识别
        home_page=Helphomepage(self.driver)
        home_page.open_url("http://127.0.0.1/upload/forum.php")
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)  # 激活当前窗口
        home_page.luntanlogin("admin","admin")
        print(self.driver.title)
        time.sleep(5)
        home_page.click_manage()
        # home_page.click_mrbk()
        # time.sleep(5)
        # secondpage=Helpsecondpage(self.driver)
        # secondpage.click_eaasy2()
        # thirdpage=Helpthirdpage(self.driver)
        # thirdpage.delete_essay()

        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        manageloginpage=Helpmanagepage(self.driver)
        time.sleep(3)
        manageloginpage.manage_login("admin")

        managecentrepage=Helpmanagecentrepage(self.driver)

        managecentrepage.click_luntan()
        self.driver.switch_to.frame("main")
        managecentrepage.build_plate("新版块3")
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)

        home_page.click_xbk()
        secondpage = Helpsecondpage(self.driver)
        secondpage.fatie_input_title("pop")
        secondpage.fatie_input_content("lploolpl")
        secondpage.fatie_click()





if __name__=="__main__":
    unittest.main()
