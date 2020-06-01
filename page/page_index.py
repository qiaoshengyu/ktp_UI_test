"""
====================================
Author：樵夫
Time：2020/5/31    19:17
====================================
"""
from common.base_pase import BasePage
from locator.index_locator import IndexLocator


class PageIndex(BasePage):

    def click_letter(self):
        """点击进入私信页面"""
        self.click_element(IndexLocator.letter_btn, "首页_点击进入私信页面")

    def click_course(self):
        """点击进入班级页面（python_web项目实战）"""
        self.click_element(IndexLocator.course_ele, "首页，点击进入python_web项目实战课程")

    def click_join_course(self):
        """点击加入课程"""
        self.click_element(IndexLocator.join_course_btn, "首页，点击加入课程")

    def input_course_code(self, code):
        """输入课程验证码"""
        self.input_text(IndexLocator.course_code_ele, code, "首页，输入课程验证码")

    def clear_course_code(self):
        """输入课程验证码"""
        self.get_element(IndexLocator.course_code_ele, "首页，清空课程验证码").clear()

    def add(self):
        """输完课程码加入"""
        self.click_element(IndexLocator.add_btn, "首页，输完验证码加入")

    def get_success_alert_info(self):
        """获取正确弹框信息"""
        return self.get_element_text(IndexLocator.success_tip_ele, "首页，获取正确弹框信息")

    def get_error_alert_info(self):
        """获取错误弹框信息"""
        return self.get_element_text(IndexLocator.error_tip_ele, "首页，获取错误弹框信息")

    def click_course_more(self):
        """点击课程选项_更多"""
        self.click_element(IndexLocator.course_more_ele, "首页，点击课程选项_更多")

    def click_course_drop(self):
        """点击课程更多选项_退课"""
        self.click_element(IndexLocator.course_drop_ele, "首页，点击课程更多选项_退课")

    def input_drop_course_pwd(self, pwd):
        """删除课程输入密码"""
        self.input_text(IndexLocator.pwd_ele, pwd, "首页,删除课程输入密码")

    def click_drop_course(self):
        """密码输入后点击删除"""
        self.click_element(IndexLocator.dele_btn,"首页，密码输入后点击删除")

    def ref_page(self):
        """刷新页面"""
        self.driver.refresh()