
"""
提现接口：
   所有用例的前置：登陆！
                拿到2个数据：id，token
   把前置的数据，传递给到测试用例。

   提现接口的请求数据：id
             请求头：token

遇到的问题一：充值前的用户余额：{'leave_amount': Decimal('4536202.88')}
    处理sql语句：把Decimal对应的字段值修改为字符串返回。CAST(字段名 AS CHAR)
    select CAST(member.leave_amount AS CHAR) as leave_amount from member where id=#member_id#;
    方式二：Decimal类

优化方式：
"""

import unittest
from jsonpath import jsonpath
from Common.handle_phone import get_old_phone
import json
from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.myddt import ddt, data
from Common.handle_path import datas_dir
from Common.my_logger import logger
from Common.handle_db import HandleDB
from Common.handle_data import replace_case_by_regular, EnvData,clear_EnvData_attrs

he = HandleExcel(datas_dir + "\\api_cases.xlsx", "提现")
cases = he.read_all_datas()
he.close_file()
db = HandleDB()


@ddt
class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 得到登陆的用户名和密码
        clear_EnvData_attrs()
        user, passwd = get_old_phone()
        # 登陆接口调用。
        resp = send_requests("POST", "member/login", {"mobile_phone": user, "pwd": passwd})
        # cls.member_id = jsonpath(resp.json(),"$..id")[0]
        # cls.token = jsonpath(resp.json(),"$..token")[0]
        # setattr(EnvData, "member_id", jsonpath(resp.json(), "$..id")[0])
        setattr(EnvData, "member_id", str(jsonpath(resp.json(), "$..id")[0]))
        setattr(EnvData, "token", jsonpath(resp.json(), "$..token")[0])
    def tearDown(self) -> None:
        if hasattr(EnvData,"money"):
            delattr(EnvData,"money")

    @data(*cases)
    def test_recharge(self, case):
        # 替换的数据
        if case["request_data"].find("#member_id#") != -1:
            case = replace_case_by_regular(case)

        # 数据库 - 查询当前用户的余额 - 在提现之前
        if case["check_sql"]:
            user_money_before_recharge = db.select_one_data(case["check_sql"])["leave_amount"]
            logger.info("提现前的用户余额：{}".format(user_money_before_recharge))
            # 期望的用户余额。 提现之前的余额 - 提现的钱
            recharge_money = json.loads(case["request_data"])["amount"]
            logger.info("提现的金额为：{}".format(recharge_money))
            expected_user_leave_amount = round(float(user_money_before_recharge) - recharge_money, 2)
            logger.info("提现后的金额为：{}".format(expected_user_leave_amount))
            # 更新期望的结果 - 将期望的用户余额更新到期望结果当中。
            # case = replace_mark_with_data(case, "#money#", str(expected_user_leave_amount))
            setattr(EnvData,"money",str(expected_user_leave_amount))
            case =replace_case_by_regular(case)
        # 发起请求 - 给用户提现
        response = send_requests(case["method"], case["url"], case["request_data"], token=EnvData.token)

        # 将期望的结果转成字典对象，再去比对
        expected = json.loads(case["expected"])

        # 断言
        try:
            self.assertEqual(response.json()["code"], expected["code"])
            self.assertEqual(response.json()["msg"], expected["msg"])
            if case["check_sql"]:
                self.assertEqual(response.json()["data"]["id"], expected["data"]["id"])
                self.assertEqual(response.json()["data"]["leave_amount"], expected["data"]["leave_amount"])
                # 数据库 - 查询当前用户的余额
                user_money_after_recharge = db.select_one_data(case["check_sql"])["leave_amount"]
                logger.info("提现之后的用户余额：{}".format(expected_user_leave_amount))
                self.assertEqual("{:.2f}".format(expected["data"]["leave_amount"]),
                                 "{:.2f}".format(float(user_money_after_recharge)))
        except:
            logger.exception("断言失败！")
            raise
