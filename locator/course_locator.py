"""
====================================
Author：樵夫
Time：2020/5/31    17:36
====================================
"""
from selenium.webdriver.common.by import By


class CourseLocator:
    """课程页面元素定位"""
    #   作业按钮
    work_ele = (By.XPATH, "//div[@id='third-nav']/a[text()='作业']")
    #   上传作业按钮
    update_work_btn = (By.XPATH, "//div[@class='work-new-r fl ']//a[text()='上传作业']")
    #   作业状态
    view_work_ele = (By.XPATH, "(//a[@class='view-work'])[1]")
    #   作业标题链接
    work_href_ele = (By.XPATH, "(//h3//a)[1]")
    #   班级名称元素
    class_ele = (By.XPATH, "//div[@class='topm cl']//h1")
    #   返回课堂首页按钮
    index_btn = (By.XPATH, "//a[text()='课堂 ']")