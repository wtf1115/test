from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os.path
from framework.logger import Logger

logger=Logger(logger="BasePage").getlog()

class BasePage(object):


    def __init__(self,driver):

        self.driver=driver

    def back(self):

        self.driver.back()

    def close(self):
        self.driver.close()

    def move_click(self,*loc,):

        elem=self.find_element(*loc)
        elem1=self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(elem).click(elem1).perform()
            logger.info("The element  was moved and clicked." )
        except Exception as e:
            logger.error("Faild to move and click the element ")

    def change_window(self):
        self.driver.switch_to.window(self.driver.current_window_handle)

    def change_window1(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def change_window2(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def change_window3(self):
        self.driver.switch_to.window(self.driver.window_handles[2])


    def forward(self):

        self.driver.forward()

    def frame(self,loc):
        self.driver.switch_to.frame(loc)

    def open_url(self,url):

        self.driver.get(url)

    def quit_browser(self):

        self.driver.quit()

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素%s",*loc)

        except:
            logger.error("%s 页面中未能找到%s元素"%(self, loc))

    # 保存图片
    def get_windows_img(self):

        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info()
        except Exception as e:
            self.get_windows_img()
            logger.error()

    # 输入
    def sendkeys(self, text,*loc):
        elem = self.find_element(*loc)
        elem.clear()
        try:
            elem.send_keys(text)
        except Exception as e:
            self.get_windows_img()

    # 清除文本框
    def clear(self,*loc):
        elem = self.find_element(*loc)
        try:
            elem.clear()
        except Exception as e:
            self.get_windows_img()

    # 点击元素
    def click(self,*loc):
        elem = self.find_element(*loc)
        try:
            elem.click()
            logger.info("The element  %s was clicked." % elem.text )
        except Exception as e:
            logger.error("Faild to click the element %s" % elem.text )

    def print1(self,*loc):
        elem = self.find_element(*loc)
        print(elem.text)
        try:
            logger.info("The element %s was print." % elem.text)
        except Exception as e:
            logger.error("Failed to print the element with %s"  % elem.text)


