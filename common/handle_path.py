"""
====================================
Author：樵夫
Time：2020/5/31    16:44
Email：1161909073@qq.com
Company：烽台科技（北京）有限公司
====================================
"""
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMON_PATH = os.path.join(PROJECT_PATH, "common")
CONF_PATH = os.path.join(PROJECT_PATH, "conf")
DATA_PATH = os.path.join(PROJECT_PATH, "data")
LOCATOR_PATH = os.path.join(PROJECT_PATH, "locator")
PAGE_PATH = os.path.join(PROJECT_PATH, "page")

RESULT_PATH = os.path.join(PROJECT_PATH, "result")
ALLURE_REPORT_PATH = os.path.join(RESULT_PATH, "allure_report")
ERROR_IMAGE_PATH = os.path.join(RESULT_PATH, "error_image")
LOGS_PATH = os.path.join(RESULT_PATH, "logs")

TESTCASES_PATH = os.path.join(PROJECT_PATH, "testcases")
