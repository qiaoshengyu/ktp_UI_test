"""
====================================
Author：樵夫
Time：2020/5/31    18:15
====================================
"""
from selenium.webdriver.common.by import By


class LetterLocator:
    """私信页面元素定位"""
    #   信息输入框
    info_ele = (By.XPATH, "//textarea[@class='ps-container']")
    #   发送信息按钮
    info_btn = (By.XPATH, "//div[@class='btn-group']//a")
    #   附件选择按钮
    file_btn = (By.XPATH, "//input[@type='file']")
    #   正确信息弹框
    success_tip_ele = (By.XPATH, "id='show-tip’")
    #   错误信息弹框
    error_tip_ele = (By.XPATH, "//div[@id='error-tip']//span")
    #   聊天框自己发送的信息
    self_send_info = (By.XPATH, "//div[@class='m-message ps-container']//li[last()]//div[@class='text']")
