from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Votedetailpage(BasePage):
    #投票元素
    vote_button=(By.CSS_SELECTOR,"#nv_forum #wp #ct #editorbox  ul li:nth-child(2) a")
