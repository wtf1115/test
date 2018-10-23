from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Secondpage(BasePage):
    #已经发表的nihao 文章元素
    essay_title1=(By.CSS_SELECTOR,"#normalthread_1 tr th a.s.xst")

    #已经发表的比比看谁傻文章元素
    essay_title2=(By.CSS_SELECTOR,"#normalthread_8 tr th a.s.xst")
    #发帖按钮元素
    fatie_button=(By.CSS_SELECTOR,"#nv_forum .wp .boardnav .mn #pgt #newspecial")

    #发起投票元素
    toupiao_button=(By.CSS_SELECTOR,"#nv_forum .wp #newspecial_menu .poll a")

    #发帖输入标题元素
    fatie_title=(By.CSS_SELECTOR,"#subject")
    #发帖输入内容元素
    fatie_content=(By.CSS_SELECTOR,"#fastpostmessage")
    #发帖提交按钮
    fatie_submit=(By.CSS_SELECTOR,"#fastpostsubmit")
    #退出元素
    quit_button=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(17)")