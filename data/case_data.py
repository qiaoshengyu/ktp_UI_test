"""
====================================
Author：樵夫
Time：2020/5/31    16:49
====================================
"""
from common.handle_config import config


class Letter_data:
    """私信页面测试数据"""

    #   发送私信成功数据
    letter_success_case = [{"title": "发送私信成功", "data": "自动化测试_发送信息", "expected": "自动化测试_发送信息"}]

    #   发送私信失败数据
    letter_error_case = [{"title": "发送失败：私信内容为空", "data": "", "expected": "私信内容不能为空"}]


class Course_data:
    """课程测试数据"""

    #   加入课程成功
    join_course_success_case = [{"title": "加入课堂成功", "data": config.get("test_data", "code"), "expected": "加入课堂成功"}]

    #   加入课程失败
    join_course_error_case = [{"title": "加课码不存在", "data": "1111111", "expected": "该加课码不存在或者已经失效"},
                              {"title": "加课码不足6位", "data": "111", "expected": "加课验证码必须是6位字符"},
                              {"title": "已经选过此课程", "data": config.get("test_data", "code"), "expected": "你已经选过此课程"}]

    #   退出课程成功
    drop_course_success_case = [{"title": "退出课堂成功", "data": config.get("test_data", "pwd"), "expected": "课程退课成功"}]

    #   退出课程失败
    drop_course_error_case = [{"title": "退出课堂失败", "data": "123456", "expected": "密码错误"}]

    #   进入班级成功
    ender_class_success_case = [{"title": "进入班级成功", "expected": "python-web项目实战- 考核项目"}]


class Work_data:
    """作业测试用例"""

    #   上传作业成功
    update_work_success_case = [
        {"title": "上传作业成功", "data": config.get("test_data", "filename"), "expected": "作业提交成功"}]

    #   作业留言成功
    massage_success_case = [
        {"title": "作业留言成功", "data": "自动化留言测试", "expected": "自动化留言测试"}]

    #   作业提交成功查看状态
    view_work_success_case = [{"title": "作业已提交状态", "expected": "已提交"}]
