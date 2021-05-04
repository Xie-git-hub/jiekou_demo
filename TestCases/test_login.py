import unittest
from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.myddt import ddt,data
from Common.handle_path import datas_dir
from Common.my_logger import logger
from Common.handle_db import HandleDB

he = HandleExcel(datas_dir+"\\api_cases.xlsx","登陆")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("开始执行登录用例")
    @classmethod
    def tearDown(self) -> None:
        logger.info("登录用例执行结束")
    @data(*cases)
    def test_login(self,case):
        logger.info("*********   执行用例{}：{}   *********".format(case["id"],case["title"]))
        # 步骤 测试数据 - 发起请求
        response = send_requests(case["method"], case["url"], case["request_data"])

        # 期望结果，从字符串转换成字典对象。
        expected = eval(case["expected"])

        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
        except AssertionError:
            logger.exception("断言失败！")
            raise