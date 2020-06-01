"""
====================================
Author：樵夫
Time：2020/6/1    11:20
====================================
"""
import os

os.environ['DISPLAY'] = ':0'
import time
from common.base_pase import BasePage
from locator.work_locator import WorkLocator
import pyautogui


class PageWork(BasePage):

    def submit_file_01(self):
        """第一次点击更新提交作业按钮"""
        time.sleep(1)
        self.click_element(WorkLocator.update_work01_btn, "作业页面，第一次点击更新提交作业")

    def click_dix_edit_work(self):
        """点击确定编辑作业按钮"""
        self.click_element(WorkLocator.dix_edit_work_btn, "作业页面，点击确定编辑作业按钮")

    def add_file(self, filename):
        """添加作业文件"""
        self.click_element(WorkLocator.add_work_btn, "作业页面，添加作业文件")
        time.sleep(2)
        pyautogui.write(filename)
        pyautogui.press('enter', 2)
        time.sleep(3)

    def submit_file_02(self):
        """第二次点击更新提交作业按钮"""
        self.click_element(WorkLocator.update_work02_btn, "作业页面，第二次点击更新提交作业")

    def get_success_alert_info(self):
        """获取提交成功弹框信息"""
        return self.get_element_text(WorkLocator.success_alert_ele, "作业页面，获取提交成功弹框信息")

    def close_success_alert(self):
        """关闭提交成功的弹框"""
        self.click_element(WorkLocator.close_alert_btn, "作业页面，点击关闭提交成功的弹框")

    def get_message(self):
        """进入留言输入框"""
        self.click_element(WorkLocator.get_message_btn, "作业页面，点击进入留言输入框")

    def input_message(self, text_value):
        """清空留言，输入新留言信息"""
        self.get_element(WorkLocator.input_message_ele, "作业页面，清空留言信息").clear()
        self.input_text(WorkLocator.input_message_ele, text_value, "作业页面，输入留言信息")

    def save_message(self):
        """保存留言"""
        self.click_element(WorkLocator.sava_message_btn, "作业页面，点击保存留言")

    def get_message_info(self):
        """获取已留言信息"""
        return self.get_element_text(WorkLocator.message_ele, "作业页面，获取已留言信息")

    def click_return_work(self):
        """点击返回作业页面"""
        self.click_element(WorkLocator.return_ele, "作业页面，点击返回课程-作业页面")

    def get_discuss(self):
        """进入作业谈论页面"""
        self.click_element(WorkLocator.discuss_btn, "作业页面，点击进入作业讨论")
