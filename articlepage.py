from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Thirdpage(BasePage):
    #删除主题元素
    delete_subject=(By.CSS_SELECTOR,"#modmenu a:nth-child(1)")
    #确定删除元素
    delete_sure=(By.CSS_SELECTOR,"#modsubmit")
    #删除文章的列表
    delete_list=(By.CSS_SELECTOR,"#threadlist div.bm_c #threadlisttableid'")


    #某篇文章的内容框
    essay_content=(By.CSS_SELECTOR,"#nv_forum #wp #ct #postmessage_36")

    #内容回复元素
    reply_content=(By.CSS_SELECTOR,"#fastpostmessage")
    #确定回复按钮元素
    reply_button=(By.CSS_SELECTOR,"#fastpostsubmit")
    #退出元素
    # 退出元素
    quit_button = (By.CSS_SELECTOR, "#um > p:nth-child(2) > a:nth-child(17)")
