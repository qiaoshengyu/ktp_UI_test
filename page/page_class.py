"""
====================================
Author：樵夫
Time：2020/6/1    9:52
====================================
"""
from common.base_pase import BasePage
from locator.course_locator import CourseLocator


class PageClass(BasePage):

    def get_class_name(self):
        """获取班级名称"""
        return self.get_element_text(CourseLocator.class_ele, "班级页面，获取班级名称")

    def click_get_index(self):
        """点击返回课程首页"""
        self.click_element(CourseLocator.index_btn, "班级页面，返回课堂首页")

    def click_get_work(self):
        """点击进入作业页面"""
        self.click_element(CourseLocator.work_ele, "班级页面，点击进入作业页面")

    def get_view_work(self):
        """获取作业提交状态"""
        return self.get_element_text(CourseLocator.view_work_ele, "班级_作业，获取作业状态")

    def click_work_title_href(self):
        """点击作业标题进入作业页面"""
        self.click_element(CourseLocator.work_href_ele, "班级_作业，点击作业标题进入作业页面")
