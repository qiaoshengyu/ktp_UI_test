"""
====================================
Author：樵夫
Time：2020/5/31    19:13
====================================
"""
from locator.letter_locator import LetterLocator
from common.base_pase import BasePage


class PageLetter(BasePage):

    def input_info(self, text_value="test"):
        """输入发送的信息"""
        self.input_text(LetterLocator.info_ele, text_value, "私信页面，输入发送的信息")

    def update_file(self):
        """上传附件"""
        self.click_element(LetterLocator.file_btn, "私信页面，上传附件")

    def send_info(self):
        """点击确定，发送信息"""
        self.click_element(LetterLocator.info_btn, "私信页面，点击确定发送信息")

    def get_success_alert_info(self):
        """获取正确弹框信息"""
        return self.get_element_text(LetterLocator.success_tip_ele, "私信页面，获取正确弹框信息")

    def get_error_alert_info(self):
        """获取错误弹框信息"""
        return self.get_element_text(LetterLocator.error_tip_ele, "私信页面，获取错误弹框信息")

    def get_self_send_info(self):
        """获取自己已发送的信息"""
        try:
            ele = self.wait_element_visibility(LetterLocator.self_send_info, "私信页面，获取自己已发送的信息")
        except:
            return "发送信息失败"
        else:
            return ele.text