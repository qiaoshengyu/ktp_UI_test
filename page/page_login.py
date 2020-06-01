"""
====================================
Author：樵夫
Time：2020/5/31    18:48
====================================
"""
from common.base_pase import BasePage
from common.handle_config import config
from locator.login_locator import LoginLocator


class PageLogin(BasePage):
    url = config.get("env", "base_url") + config.get("url", "login_url")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.url)

    def login(self, name, pwd):
        """输入账号密码登录"""
        self.input_text(LoginLocator.name_ele, name, "登录_输入账号")
        self.input_text(LoginLocator.pwd_ele, pwd, "登录_输入密码")
        self.click_element(LoginLocator.login_btn, "登录_点击登录")