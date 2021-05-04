"""
======================
Author: 柠檬班-小简
Time: 2020/7/15 21:25
Project: day8
Company: 湖南零檬信息技术有限公司
======================
"""
# 替换请求数据当中，
from Common.handle_data import EnvData
from Common.handle_config import conf

setattr(EnvData,"member_id","12345678900000")
setattr(EnvData,"user_money","2500")

import re
# data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'

# res = re.findall("#(.*?)#",data) # 如果没有找到，返回的是空列表。
# print(res)
#
# # 标识符对应的值，来自于：1、环境变量  2、配置文件
# if res:
#     for item in res:
#         # 得到标识符对应的值。
#         try:
#             value = conf.get("data",item)
#         except:
#             value = getattr(EnvData,item)
#         print(value)
#         # 再去替换原字符串
#         data = data.replace("#{}#".format(item),value)
#     print(data)

def replace_by_regular(data):
    res = re.findall("#(.*?)#", data)  # 如果没有找到，返回的是空列表。
    # 标识符对应的值，来自于：1、环境变量  2、配置文件
    if res:
        for item in res:
            # 得到标识符对应的值。
            try:
                value = conf.get("data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    # value = "#{}#".format(item)
                    continue
            print(value)
            # 再去替换原字符串
            data = data.replace("#{}#".format(item), value)
    return data

data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'

data2 = {
    "url":"http://api.lemonban.com/futureloan/member/#member_id#/register",
    "request_data":"{\"member_id\": #member_id#,\"amount\":#money#,'mobile_phone': '18605671115', 'pwd': '123456789'}"
}
import json

data2_str = json.dumps(data2)


res = replace_by_regular(data2_str)
print(res)

new_data2 = json.loads(res)
print(new_data2)

