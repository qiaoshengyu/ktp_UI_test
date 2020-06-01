"""
====================================
Author：樵夫
Time：2020/5/31    19:10
====================================
"""
import pytest
from data.case_data import Letter_data
from common.handle_log import log


@pytest.mark.letter
class TestLetter:
    """私信测试类"""

    @pytest.mark.letter_success
    @pytest.mark.parametrize("case", Letter_data.letter_success_case)
    def test_send_letter_success(self, case, letter_fixture):
        """发送私信成功测试用例"""
        letter_page = letter_fixture
        #   输入发送信息
        letter_page.input_info(case["data"])
        #   点击发送按钮
        letter_page.send_info()
        #   获取聊天框自己发送的信息
        res = letter_page.get_self_send_info()
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

    @pytest.mark.letter_error
    @pytest.mark.parametrize("case", Letter_data.letter_error_case)
    def test_send_letter_error(self, case, letter_fixture):
        """发送私信失败测试用例"""
        letter_page = letter_fixture
        #   输入发送信息
        letter_page.input_info(case["data"])
        #   点击发送按钮
        letter_page.send_info()
        #   获取失败弹框信息
        res = letter_page.get_error_alert_info()
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
