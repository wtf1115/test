from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Votepartpage(BasePage):
    #投票选项元素
    vote_select=(By.CSS_SELECTOR,"#option_3")
    #投票选项提交按钮元素
    vote_button=(By.CSS_SELECTOR,"#pollsubmit")

    #投票打印元素
    vote_print=(By.CSS_SELECTOR,"#nv_forum .wp .pcht .pvt label")
    vote_titleprint=(By.CSS_SELECTOR,"#nv_forum .wp #postlist #thread_subject")
    vote_print_1 =(By.CSS_SELECTOR,"#nv_forum .wp #poll div.pcht table tbody tr:nth-child(2) td:nth-child(2)")
    vote_print2=(By.CSS_SELECTOR,"#nv_forum .wp .pcht tr:nth-child(3) .pvt label")
    vote_print_2=(By.CSS_SELECTOR,"#nv_forum .wp #poll div.pcht table tbody tr:nth-child(4) td:nth-child(2)")
    vote_print3=(By.CSS_SELECTOR,"#nv_forum .wp .pcht tr:nth-child(5) .pvt label")
    vote_print_3=(By.CSS_SELECTOR,"#nv_forum .wp #poll div.pcht table tbody tr:nth-child(6) td:nth-child(2)")