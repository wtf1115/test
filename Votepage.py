from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Votepage(BasePage):
    #投票标题元素
    vote_title=(By.CSS_SELECTOR,"#subject")
    #投票选项元素
    vote_part1=(By.CSS_SELECTOR,"#pollm_c_1  p:nth-child(1)  input")
    vote_part2=(By.CSS_SELECTOR,"#pollm_c_1  p:nth-child(2)  input")
    vote_part3=(By.CSS_SELECTOR,"#pollm_c_1  p:nth-child(3)  input")
    #投标提交按钮元素
    vote_button=(By.CSS_SELECTOR,"#postsubmit")