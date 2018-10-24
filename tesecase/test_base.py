from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from framework.browser_engine import BrowserEngin
import unittest
import time
class test_basecase(unittest.TestCase):

    def setUp(self):  # 前提准备工作  ./当前目录  ../根目录（上一级目录）
        browser = BrowserEngin()
        self.driver = browser.open_browser()


def tearDown(self):#测试结束后的销毁工作
        time.sleep(3)
        self.driver.quit()