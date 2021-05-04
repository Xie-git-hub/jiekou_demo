import unittest
from Common.handle_excel import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_data import EnvData,replace_case_by_regular,clear_EnvData_attrs
from Common.myddt import ddt,data
from Common.my_logger import logger
from Common.handle_requests import send_requests
from Common.handle_extract_data_from_response import extract_data_from_response
he = HandleExcel(datas_dir+"\\api_cases.xlsx","加标")
cases = he.read_all_datas()
he.close_file()
@ddt
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("************添加项目开始执行********")
        clear_EnvData_attrs()
        #清除EnvDta的属性
    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("************添加项目结束执行********")
    @data(*cases)
    def test_add(self,case):
        # 替换case
        case = replace_case_by_regular(case)
        # 如果前置sql - 得到结果后，再次替换。
        # 发送请求 - 考虑用例是否都需要token
        if hasattr(EnvData,"token"):
            #如果有token，则将token的值一起发送
            response = send_requests(case["method"], case["url"], case["request_data"], token=EnvData.token)
        else:
            #否则只发送方法地址和请求参数
            response = send_requests(case["method"], case["url"], case["request_data"])
            # 如果有提取表达式，提取数据，设置为全局变量。
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())