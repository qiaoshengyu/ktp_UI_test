"""
====================================
Author：樵夫
Time：2020/5/31    17:01
====================================
"""
from selenium.webdriver.common.by import By


class IndexLocator:
    """首页页面元素定位"""
    #   加入课程按钮
    join_course_btn = (By.XPATH, "//div[text()='+ 加入课程']")
    #   课程验证码输入框
    course_code_ele = (By.XPATH, "//input[@placeholder='请输入课程加课验证码']")
    #   加入按钮
    add_btn = (By.XPATH, "//a[text()='加入']")
    #   正确信息弹框
    success_tip_ele = (By.XPATH, "//div[@id='show-tip']//span")
    #   错误信息弹框
    error_tip_ele = (By.XPATH, "//div[@id='error-tip']//span")
    #   课程标题元素_进入班级
    course_ele = (By.XPATH, "//a[text()='python-web项目实战- 考核项目']")
    #   课程选项_更多
    course_more_ele = (By.XPATH, "//dl[@data-id='MDAwMDAwMDAwMLR2vd6Gz8mw']//span[text()='更多']")
    #   课程更多选项_退课
    course_drop_ele = (By.XPATH, "//dl[@data-id='MDAwMDAwMDAwMLR2vd6Gz8mw']//a[text()='退课']")
    #   删除课程验证_密码输入框
    pwd_ele = (By.XPATH, "//input[@type='password']")
    #   删除课程验证_删除按钮
    dele_btn = (By.XPATH, "//div[@class='deletebot cl']//a[text()='退课']")
    #   进入私信按钮
    letter_btn = (By.XPATH, "//a[@href='/Letter/index.html']")
