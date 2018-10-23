from selenium.webdriver.common.by import By
from base.basepage import BasePage


class Homepage(BasePage):
#登录元素
    login_name_input=(By.CSS_SELECTOR,"#ls_username")
    login_pwd_input=(By.CSS_SELECTOR,"#ls_password")
    login_submit=(By.CSS_SELECTOR,".widthauto #nv_forum #hd .wp #lsform div  div  table tbody tr:nth-child(2) td.fastlg_l button")
#默认板块元素
    fatie_mrbk=(By.CSS_SELECTOR,"#nv_forum .wp #ct .mn #category_1  table  tbody tr:nth-child(1) td:nth-child(2)  h2  a")
#新板块元素
    xbk=(By.CSS_SELECTOR,".wp #category_1 table tbody tr:nth-child(3) td:nth-child(2) h2 a")
#管理中心元素
    glzx_button=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(16)")

#搜索元素
    search_input=(By.CSS_SELECTOR,"#scbar_form .scbar_txt_td #scbar_txt")
#搜索按钮
    search_button=(By.CSS_SELECTOR,"#scbar_form .scbar_btn_td #scbar_btn")
#退出元素
    quit_input=(By.CSS_SELECTOR,"#um > p:nth-child(2) > a:nth-child(17)")






