"""
====================================
Author：樵夫
Time：2020/5/26    15:37
====================================
"""
from selenium.webdriver.remote.webdriver import WebDriver

import os, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_log import log
from common.handle_path import ERROR_IMAGE_PATH


class BasePage:
    """把页面一些常见的功能操作封装进来"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        driver.maximize_window()
        driver.implicitly_wait(30)

    def wait_element_visibility(self, locator, image_info, timeout=15, poll_frequency=0.5):
        """等待元素可见"""
        #   等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            #   输出日志
            log.error("元素--{}--等待可见超时".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            #   元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def wait_element_clickable(self, locator, image_info, timeout=15, poll_frequency=0.5):
        """等待元素可点击"""
        #   等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as e:
            #   输出日志
            log.error("元素--{}--等待点击超时".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            #   元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待点击成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def wait_element_presence(self, locator, image_info, timeout=15, poll_frequency=0.5):
        """等待元素被加载"""
        #   等待元素之前获取当前的时间
        start_time = time.time()
        try:
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            #   输出日志
            log.error("元素--{}--等待加载超时".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            #   元素等待之后获取时间
            end_time = time.time()
            log.info("元素--{}--等待加载成功,等待时间{}秒".format(locator, end_time - start_time))
            return ele

    def get_element_text(self, locator, image_info):
        """获取元素文本"""
        try:
            text = self.driver.find_element(*locator).text
        except Exception as e:
            #   输出日志
            log.error("元素--{}--获取文本失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("获取元素--{}--文本成功".format(locator))
            return text

    def get_element_attrbute(self, locator, attr_name, image_info):
        """获取元素属性"""
        try:
            ele = self.driver.find_element(*locator)
            attr_value = ele.get_attribute(attr_name)
        except Exception as e:
            #   输出日志
            log.error("元素--{}--获取元素属性失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("获取元素--{}--属性成功".format(locator))
            return attr_value

    def click_element(self, locator, image_info):
        """点击元素"""
        try:
            self.driver.find_element(*locator).click()
        except Exception as e:
            #   输出日志
            log.error("元素--{}--点击失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("元素--{}--点击成功".format(locator))

    def input_text(self, locator, text_value, image_info):
        """输入文本"""
        try:
            self.driver.find_element(*locator).send_keys(text_value)
        except Exception as e:
            #   输出日志
            log.error("元素--{}--输入文本失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("元素--{}--输入文本成功".format(locator))

    def get_element(self, locator, image_info):
        """获取元素"""
        try:
            ele = self.driver.find_element(*locator)
        except Exception as e:
            #   输出日志
            log.error("元素--{}--获取失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("元素--{}--获取成功".format(locator))
            return ele

    def save_screen_image(self, image_info):
        """获取页面截图"""
        start_time = time.time()
        filename = "{}_{}.png".format(image_info, start_time)
        filepath = os.path.join(ERROR_IMAGE_PATH, filename)
        self.driver.save_screenshot(filepath)
        log.info("错误页面截图成功，图表保存的路径：{}".format(filepath))

    def move_window(self, locator, image_info):
        """移动窗口至元素可见"""
        try:
            move_ele = self.get_element(locator, "获取元素")
            js = """
            var move_ele = arguments[0];
            move_ele.scrollIntoView();
            """
            self.driver.execute_script(js, move_ele)
        except Exception as e:
            #   输出日志
            log.error("窗口移至元素--{}--失败".format(locator))
            log.exception(e)
            #   对当前页面截图
            self.save_screen_image(image_info)
            raise e
        else:
            log.info("窗口移至元素--{}--成功".format(locator))
