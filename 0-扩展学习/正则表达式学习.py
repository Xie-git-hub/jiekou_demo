"""
@Title   : Selenium+python3-web自动化测试
@Author  : 小简
@Email   : lemonban_simple@qq.com
"""
"""
1、单字符匹配
   .    匹配除\n以外的任意字符
   \d   匹配1个数字字符 [0-9]
   \D   匹配一个非数字字符[^0-9]
   \w   匹配包括下划线的任何单词字符，还有中文。等价于“[A-Za-z0-9_]”。
   \W   匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。


2、多数量匹配
   *
   +
   ？
   {n}
   {n,} 匹配前一个字符至少n次
   {n,m}  匹配前一个字符至少n次，最多m次

3、贪婪模式和非贪婪模式

   默认是贪婪模式：尽可能的匹配更长
   非贪婪模式：尽可能的匹配更短。通过?修改为非贪婪模式
   
   ？ 当该字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的。
   非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
   例如，对于字符串“oooo”，“o+?”将匹配单个“o”，而“o+”将匹配所有“o”。

4、多选项匹配
   | 匹配多个规范   x|y  匹配x或者y
   [zxy]  匹配zxy中的任意字符
   [a-z]  匹配a-z范围内的任意字符  比如[0-9][a-z][A-Z]
 
5、() 匹配分组：将括号里的匹配出来


"""

import re

# case = {
#         "method": "POST",
#         "url": "http://api.lemonban.com/futureloan/member/register",
#         "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "#nick#"}'
#     }
#
# res = re.findall("#.*?#",case["request_data"])
# print(res)


resp = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 200713,
        "leave_amount": 4000.0,
        "mobile_phone": "18605671115",
        "reg_name": "美丽可爱的小简",
        "reg_time": "2020-06-29 11:52:20.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2020-07-06 21:48:53",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MDQzMzMzfQ.WJMI0-t7YZD8FtAiaYR8-SH1p58_7fJjnvS6xVw7_hYTe7eVIyxj3W2Oj7SlwR8dDZBc1T59U2ngRROXyFjx_Q"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}

import json

res_str = json.dumps(resp)
print(res_str)


# res = re.findall('"token":(.*?)}',res_str)
# print(res)

s = "**abcdeefdg123345233"
# result = re.findall("\W",s)
# print(result)

# result = re.findall("[0-9]+?",s)
# print(result)

strs = '{"loan_id":#loan_id#,"approved_or_not": True,"member":#member_id#}'
# result = re.search("#(.*?)#",strs)
# print(result)
# res = result.group(1)
# print(res)

print("888888888888888888888888888888888888")
# result = re.search("#(.*?)#",strs)
# print(result)
# res = result.group(1)
# print(res)
