"""
======================
Author: 柠檬班-小简
Time: 2020/7/1 20:21
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
"""
null None
"""
import json

ss = '{"mobile_phone":"18600001112","pwd":"123456789","type":1,"reg_name":"美丽可爱的小简","flag":null}'

# json字符串转换成字典
ss_dict = json.loads(ss)
print(ss_dict)

dict_ss = {'mobile_phone': '18600001112', 'pwd': '123456789', 'type': 1, 'reg_name': '美丽可爱的小简', 'flag': None}
# 将字典转换成json字符串
ss_json = json.dumps(dict_ss,ensure_ascii=False)
print(ss_json)

