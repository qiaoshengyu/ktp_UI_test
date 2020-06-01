"""
====================================
Author：樵夫
Time：2020/5/31    19:09
====================================
"""
import pytest
from data.case_data import Course_data
from common.handle_log import log


@pytest.mark.course
class TestCourse:
    """课程测试类"""

    # @pytest.mark.skip
    @pytest.mark.course_join
    @pytest.mark.parametrize("case", Course_data.join_course_success_case)
    def test_join_courese_success(self, case, course_fixture):
        """加入班级成功测试用例"""
        index_page = course_fixture[0]
        #   点击加入课程
        index_page.click_join_course()
        #   输入课程验证码
        index_page.input_course_code(case["data"])
        #   点击加入按钮
        index_page.add()
        #   获取成功信息框信息
        res = index_page.get_success_alert_info()
        #   预取结果
        expected = case["expected"]
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   刷新页面
        index_page.ref_page()

    @pytest.mark.course_join
    @pytest.mark.parametrize("case", Course_data.join_course_error_case)
    def test_join_courese_error(self, case, course_fixture):
        """加入班级失败测试用例"""
        index_page = course_fixture[0]
        #   点击加入课程
        index_page.click_join_course()
        #   输入课程验证码
        index_page.input_course_code(case["data"])
        #   点击加入按钮
        index_page.add()
        #   获取失败信息框信息
        res = index_page.get_error_alert_info()
        #   预取结果
        expected = case["expected"]
        #   刷新页面
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   刷新页面
        index_page.ref_page()

    @pytest.mark.ender_class
    @pytest.mark.parametrize("case", Course_data.ender_class_success_case)
    def test_enter_class_success(self, case, course_fixture):
        """进入班级成功测试用例"""
        index_page, class_page = course_fixture
        #   点击班级名称进入班级
        index_page.click_course()
        #   获取班级页面名称
        res = class_page.get_class_name()
        #   预取结果
        expected = case["expected"]
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   返回课堂首页
        class_page.click_get_index()

    @pytest.mark.course_drop
    @pytest.mark.parametrize("case", Course_data.drop_course_error_case)
    def test_drop_course_error(self, case, course_fixture):
        """退出班级失败测试用例"""
        index_page = course_fixture[0]
        #   点击课程更多按钮
        index_page.click_course_more()
        #   点击课程退课按钮
        index_page.click_course_drop()
        #   输入登录密码
        index_page.input_drop_course_pwd(case["data"])
        #   点击退课按钮
        index_page.click_drop_course()
        #   获取错误信息框信息
        res = index_page.get_error_alert_info()
        #   获取预取结果
        expected = case["expected"]
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   刷新页面
        index_page.ref_page()

    @pytest.mark.parametrize("case", Course_data.drop_course_success_case)
    def test_drop_course_success(self, case, course_fixture):
        """退出班级成功测试用例"""
        index_page = course_fixture[0]
        #   点击课程更多按钮
        index_page.click_course_more()
        #   点击课程退课按钮
        index_page.click_course_drop()
        #   输入登录密码
        index_page.input_drop_course_pwd(case["data"])
        #   点击退课按钮
        index_page.click_drop_course()
        #   获取成功信息框信息
        res = index_page.get_success_alert_info()
        #   获取预取结果
        expected = case["expected"]
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   刷新页面
        index_page.ref_page()