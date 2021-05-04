"""
======================
Author: 柠檬班-小简
Time: 2020/7/6 17:32
Project: day5
Company: 湖南零檬信息技术有限公司
======================
"""
"""
文章地址： 
http://www.lemfix.com/topics/63

安装：pip install jsonpath

使用方式：jsonpath.jsonpath(字典对象,jsonpath表达式)
返回值：列表。
"""
import jsonpath

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

# $.code

# 参数：第一个：字典对象    第二个：jsonpath表达式
# 返回值：列表。存放匹配到所有值。
res = jsonpath.jsonpath(resp,"$.data.token_info.token")

print(res)