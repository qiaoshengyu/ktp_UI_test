"""
====================================
Author：樵夫
Time：2020/5/31    16:51
====================================
"""
from selenium.webdriver.common.by import By


class LoginLocator:
    """登录页面元素定位"""
    #   账号输入框
    name_ele = (By.XPATH, "//input[@name='account']")
    #   密码输入框
    pwd_ele = (By.XPATH, "//input[@name='pass']")
    #   登录按钮
    login_btn = (By.XPATH, "//div[@class='padding-cont pt-login']//a[@class='btn-btn']")