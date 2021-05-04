"""
======================
Author: 柠檬班-小简
Time: 2020/7/15 20:05
Project: day8
Company: 湖南零檬信息技术有限公司
======================
"""
"""
字符串：正则表达式
http://www.lemfix.com/topics/393
https://www.cnblogs.com/Simple-Small/p/9150947.html

字符串匹配、提取
regular

正则表达式手册：https://tool.oschina.net/uploads/apidocs/jquery/regexp.html

单个匹配表达式
.	匹配除“\n”之外的任何单个字符
\d	匹配一个数字字符。等价于[0-9]。
\D	匹配一个非数字字符。等价于[^0-9]
\w	匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”。
\W	匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
[xyz]  字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”
[a-z] 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
x|y  匹配x或者y

数量上的匹配：
{m}  n是一个非负整数。匹配前一个字符的n次
{n,m} 匹配前一个字符至少n次，最多m次
{n,} 匹配前一个字符至少n次

*  匹配前一个字符，0次或多次。
+  匹配前一个字符，1次或多次。
?  匹配前一个字符，0次或1次。

贪婪模式：尽可能匹配更多更长。默认的贪婪模式。
非贪婪模式：尽可能匹配更少。
    改成非贪婪模式，在限定数量表达式后面加上?

边界字符
^ 	匹配输入字符串的开始位置。
$   匹配输入字符串的结束位置。

5、() 匹配分组：将括号里的匹配出来


"""
import re

s = "sdk11fj12333445fga000000009abcdffda111a%^&*=---柠檬班。sfsfd"
data = '{"member_id": #member_id#,"amount":600,money:#user_money#,username:"#user#"}'

res = re.findall("#(.*?)#",data)
print(res)

# ()提取
# res = re.findall("a(\d+)a",s)
# print(res)

# res = re.findall("a(.*?)a",s)
# print(res)

# 数量上的匹配：
# res = re.findall("\d+",s)
# print(res)
# res = re.findall("1.*",s)
# print(res)
# res = re.findall("^[a-z]+",s)
# print(res)
# res = re.findall("[a-z]$",s)
# print(res)

# res = re.findall("\d{3,5}",s)
# print(res)
# res = re.findall("\d{3,5}?",s)
# print(res)
# res = re.findall("\d{3,}",s)
# print(res)
# res = re.findall("\d{3}",s)
# print(res)


# 单字符匹配
# res = re.findall(".",s)
# print(res)
# res = re.findall("\d",s)
# print(res)
# res = re.findall("\D",s)
# print(res)
# res = re.findall("\W",s)
# print(res)
# res = re.findall("[abcd]",s)
# print(res)
# res = re.findall("[A-Za-z0-9]",s)
# print(res)
# res = re.findall("abc|123|11",s)
# print(res)



