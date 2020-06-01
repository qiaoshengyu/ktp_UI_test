"""
====================================
Author：樵夫
Time：2020/5/31    19:09
====================================
"""
import pytest
from data.case_data import Work_data
from common.handle_log import log


@pytest.mark.work
class TestWork:
    """作业测试类"""

    @pytest.mark.work_update
    @pytest.mark.parametrize("case", Work_data.update_work_success_case)
    def test_update_work_success(self, case, work_fixture):
        """上传作业文件成功测试用例"""
        class_page, work_page = work_fixture
        #   点击进入作业页面
        class_page.click_work_title_href()
        #   第一次点击更新提交页面
        work_page.submit_file_01()
        #   点击确定编辑作业按钮
        work_page.click_dix_edit_work()
        #   点击添加作业文件
        work_page.add_file(case["data"])
        #   第二次点击更新提交页面
        work_page.submit_file_02()
        #   获取提交成功弹框信息
        res = work_page.get_success_alert_info()
        #   点击关闭提交成功弹框
        work_page.close_success_alert()
        #   预期结果
        expected = case["expected"]
        try:
            assert expected == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))
        #   返回课程-作业页面
        work_page.click_return_work()

    @pytest.mark.work_message
    @pytest.mark.parametrize("case", Work_data.massage_success_case)
    def test_work_message_success(self, case, work_fixture):
        """作业留言成功测试用例"""
        class_page, work_page = work_fixture
        #   点击进入作业页面
        class_page.click_work_title_href()
        #   第一次点击更新提交页面
        work_page.submit_file_01()
        #   点击确定编辑作业按钮
        work_page.click_dix_edit_work()
        #   点击进入留言框
        work_page.get_message()
        #   清空留言，输入留言信息
        work_page.input_message(case["data"])
        #   保存留言
        work_page.save_message()
        #   第二次点击更新提交页面
        work_page.submit_file_02()
        #   点击关闭提交成功弹框
        work_page.close_success_alert()
        #   获取已留言信息
        res = work_page.get_message_info()
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
        #   返回课程-作业页面
        work_page.click_return_work()

    @pytest.mark.work_view
    @pytest.mark.parametrize("case", Work_data.view_work_success_case)
    def test_work_view_success(self, case, work_fixture):
        """获取作业状态成功测试用例"""
        class_page = work_fixture[0]
        #   获取作业提交状态
        res = class_page.get_view_work()
        #   预期结果
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
