"""
======================
Author: 柠檬班-小简
Time: 2020/7/1 20:53
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例路径
cases_dir = os.path.join(base_dir,"TestCases")
# 测试数据的路径
datas_dir = os.path.join(base_dir,"TestDatas")
# 测试报告
reports_dir = os.path.join(base_dir,"Outputs\\reports")
# 日志的路径
logs_dir = os.path.join(base_dir,"Outputs\\logs")
# 配置文件路径
conf_dir = os.path.join(base_dir,"Conf")