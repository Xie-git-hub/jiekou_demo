from Common.handle_data import EnvData,clear_EnvData_attrs,replace_case_by_regular
from Common.handle_extract_data_from_response import extract_data_from_response
from Common.handle_excel import HandleExcel
from Common.handle_phone import get_new_phone
from Common.handle_requests import send_requests
from Common.handle_path import datas_dir
from Common.myddt import ddt,data
import unittest
he = HandleExcel(datas_dir+"\\api_cases.xlsx","业务流")
cases = he.read_all_datas()
he.close_file()
@ddt
class TestUserBusiness(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        #
        clear_EnvData_attrs()
        new_phone = get_new_phone()
        setattr(EnvData,"phone",new_phone)
    @data(*cases)
    def test_user_business(self,case):
        replace_case_by_regular(case)
        if hasattr(EnvData,"token"):
            response = send_requests(case["method"], case["url"], case["request_data"], token=EnvData.token)
        else:
            response = send_requests(case["method"], case["url"], case["request_data"])
            # 如果有要提取数据的，提取数据。并设置为全局变量。
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"], response.json())