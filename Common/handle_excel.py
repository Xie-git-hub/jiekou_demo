"""
======================
Author: 柠檬班-小简
Time: 2020/6/17 20:09
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
excel类，你的需求是实现是什么?
1、读取表头
2、读取数据 - 读取表头以外的所有数据。 - 返回值：列表，成员是每一行数据

初始化工作？  加载一个excel,打开一个表单。

"""
from openpyxl import load_workbook
import json


class HandleExcel:

    def __init__(self,file_path,sheet_name):
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  # 遍历第1行当中每一列
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行
            values = []
            for val in item:  # 获取每一行的值
                values.append(val.value)
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
            all_datas.append(res)
        return all_datas


    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    import os
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
    exc = HandleExcel(file_path,"login")
    cases = exc.read_all_datas()
    exc.close_file()
    for case in cases:
        print(case)