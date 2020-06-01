"""
====================================
Author：樵夫
Time：2020/5/31    17:40
====================================
"""
from selenium.webdriver.common.by import By


class WorkLocator:
    """作业页面元素定位"""
    #   添加作业文件按钮
    add_work_btn = (By.XPATH, "//a[@class='sc-btn webuploader-container']")
    #   第一次更新提交按钮
    update_work01_btn = (By.XPATH, "(//div[@class='sc-tj fl']//a)[1]")
    #   确定编辑作业按钮
    dix_edit_work_btn = (By.XPATH, "//div[@class='layui-layer-content']//a[text()='确定']")
    #   提交作业文件按钮
    submit_work_btn = (By.XPATH, "//a[@class='tj-btn']")
    #   第二次更新提交按钮
    update_work02_btn = (By.XPATH, "(//div[@class='sc-tj fl']//a)[last()]")
    #   进入留言按钮
    get_message_btn = (By.XPATH, "//div[@class='work-message clearfix']")
    #   留言输入框
    input_message_ele = (By.XPATH, "//div[@class='work-message2 clearfix']//textarea")
    #   留言保存按钮
    sava_message_btn = (By.XPATH, "//div[@class='work-message2 clearfix']//a")
    #   提交成功弹框
    success_alert_ele = (By.XPATH, "//div[@class='weui_dialog_alert']//div[text()='作业提交成功']")
    #   点击关闭_提交成功弹框
    close_alert_btn = (By.XPATH, "//a[@class='weui_btn_dialog primary']")
    #   已留言展示元素
    message_ele = (By.XPATH, "//div[@class='work-message clearfix']//span")
    #   返回作业页面按钮
    return_ele = (By.XPATH, "//a[@class='return']")
    #   进入作业讨论按钮
    discuss_btn = (By.XPATH, "//div[@class='nav gWidth']//a[text()='作业讨论']")
    #   添加评论元素
    add_ele = (By.XPATH, "//div[@class='input-click clearfix']//p")
    #   评论输入框
    comment_ele = (By.XPATH, "//textarea[@placeholder='添加评论']")
    #   确定评论按钮
    define_comment_btn = (By.XPATH, "//div[@class='opt-btn fr']/a[text()='确定']")
    #   取消评论按钮
    cancel_comment_btn = (By.XPATH, "//div[@class='opt-btn fr']/a[text()='取消']")
