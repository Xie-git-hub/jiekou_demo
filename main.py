"""
======================
Author: 柠檬班-小简
Time: 2020/7/1 20:36
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""

import unittest
import os
from BeautifulReport import BeautifulReport

from Common.handle_path import cases_dir,reports_dir

# 收集用例

s = unittest.TestLoader().discover(cases_dir)

# 生成报告
br = BeautifulReport(s)
br.report("py30-注册用例自动化", "report_.html",reports_dir)
