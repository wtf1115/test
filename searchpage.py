from selenium.webdriver.common.by import By
from base.basepage import BasePage


class searchpage(BasePage):
#点击某一篇搜索文章的元素
    essay=(By.CSS_SELECTOR,"#nv_search #ct .tl .xs3 a")