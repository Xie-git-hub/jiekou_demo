"""
======================
Author: 柠檬班-小简
Time: 2020/7/20 20:11
Project: day10
Company: 湖南零檬信息技术有限公司
======================
"""
"""
json: 是什么样就直接转换，没有计算
eval: python表达式去计算
"""
import json

sss = '{"member_id":round(float(202+1),2),"title":null,"amount":2000,"loan_rate":12.0,"loan_term":3,"loan_date_type":1,"bidding_days":5}'

if sss.find("null") != -1:
    sss = sss.replace("null","None")

# s = json.loads(sss)
s = eval(sss)
print(s)
