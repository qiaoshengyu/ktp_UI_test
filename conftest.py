"""
====================================
Author：樵夫
Time：2020/5/31    18:51
====================================
"""
import pytest
from common.handle_config import config
from selenium import webdriver
from page.page_login import PageLogin
from page.page_index import PageIndex
from page.page_letter import PageLetter
from page.page_class import PageClass
from page.page_work import PageWork


def get_option():
    """浏览器模式配置"""
    if config.get("env", "headless") == "True":
        """设置浏览启动的选项：无头模式"""
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        return opt
    else:
        return None


def login_success_fixture():
    """测试账号登录"""
    driver = webdriver.Chrome(options=get_option())
    #   获取登录页面
    login_page = PageLogin(driver)
    login_page.login(name=config.get("test_data", "name"), pwd=config.get("test_data", "pwd"))
    return driver


@pytest.fixture(scope="class")
def work_fixture():
    #   登录测试账号
    login_success_fixture()


@pytest.fixture(scope="class")
def letter_fixture():
    #   登录测试账号
    driver = login_success_fixture()
    #   获取私信页面
    letter_page = PageLetter(driver)
    #   获取首页页面
    index_page = PageIndex(driver)
    #   点击打开私信页面
    index_page.click_letter()
    #   切换进入私信页面
    driver.switch_to.window(driver.window_handles[-1])
    yield letter_page
    driver.quit()


@pytest.fixture(scope="class")
def course_fixture():
    #   登录测试账号
    driver = login_success_fixture()
    #   获取课程页面
    index_page = PageIndex(driver)
    #   获取班级页面
    class_page = PageClass(driver)
    yield index_page, class_page
    driver.quit()


@pytest.fixture(scope="class")
def work_fixture():
    #   登录测试账号
    driver = login_success_fixture()
    #   获取课程页面
    index_page = PageIndex(driver)
    #   点击加入课程
    index_page.click_join_course()
    #   输入课程验证码
    index_page.input_course_code(config.get("test_data", "code"))
    #   点击加入按钮
    index_page.add()
    #   点击进入班级
    index_page.click_course()
    #   获取班级页面
    class_page = PageClass(driver)
    #   点击进入班级_作业页面
    class_page.click_get_work()
    #   获取作业页面
    work_page = PageWork(driver)
    yield class_page, work_page
    #   点击课程更多按钮
    index_page.click_course_more()
    #   点击课程退课按钮
    index_page.click_course_drop()
    #   输入登录密码
    index_page.input_drop_course_pwd(config.get("test_data", "pwd"))
    #   点击退课按钮
    index_page.click_drop_course()
    driver.quit()
