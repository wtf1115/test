from selenium import webdriver
import os
from framework.logger import Logger
from configparser import ConfigParser


logger = Logger(logger="BrowserEngin").getlog()
class BrowserEngin(object):

    driver_dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_full_path = driver_dir + '\\tools\chromedriver.exe'

    def open_browser(self):
# 创建一个引用对象
        config = ConfigParser()
# 获取配置文件的全路径
        config_full_path = os.path.dirname(os.path.abspath('.')) + "\\config\config.ini"
# 通过该 read(一个参数是全路径) 方法 ---> 读取到.ini配置文件的内容
        config.read(config_full_path)
        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
#得到初始化打开的URL页面
        url = config.get("testServer","URL")
        logger.info("The test server url is: %s "% url)

        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_full_path)
            logger.info("Starting Chrome browser.")
        elif browser == "FireFox":
            driver=webdriver.Firefox("...没有下载对应的驱动driver.....")
            logger.info("No Firefox driver.")
        elif browser == "IE":
            driver=webdriver.Edge("...没有 IE=Edge 驱动文件...")
            logger.info("No IE driver.")


        driver.get(url)
        logger.info("open url:%s"% url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver


    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()

