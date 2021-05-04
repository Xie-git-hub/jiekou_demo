"""
======================
Author: 柠檬班-小简
Time: 2020/7/6 20:19
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、一条用例涉及到数据当中，有url、request_data、check_sql

"""
import re
from Common.handle_config import conf
class EnvData:
    """
    存储用例要使用到的数据。
    """
    pass

def clear_EnvData_attrs():
    # 清理 EnvData里设置的属性
    values = dict(EnvData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
            pass
        else:
            delattr(EnvData, key)


def replace_case_by_regular(case):
    """
    对excel当中，读取出来的整条测试用例，做全部替换。
    包括url,request_data,expected,check_sql
    """
    for key,value in case.items():
        if value is not None and isinstance(value, str):  # 确保是个字符串
            case[key] = replace_by_regular(value)
    return case

    # # 把case字典(从excel读取出来的一条用例数据)转换成字符串
    # case_str = json.dumps(case)
    # # 替换
    # new_case = replace_by_regular(case_str)
    # # 把替换的的字符串，转换成字典。
    # case_dict = json.loads(new_case)
    # return case_dict

def replace_by_regular(data):
    """
    将字符串当中，匹配#(.*?)#部分，替换换对应的真实数据。
    真实数据只从2个地方去获取：1个是配置文件当中的data区域 。另1个是，EvnData的类属性。
    data: 字符串
    return: 返回的是替换之后的字符串

    ps： 1个是配置文件当中的data区域 。另1个是，EvnData的类属性。必须都是字符串类型。
    """
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


def replace_mark_with_data(case,mark,real_data):
    """
    遍历一个http请求用例涉及到的所有数据，如果说每一个数据有需要替换的，都会替换。
    case: excel当中读取出来一条数据。是个字典。
    mark: 数据当中的占位符。#值#
    real_data: 要替换mark的真实数据。
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str): # 确保是个字符串
            if value.find(mark) != -1: # 找到标识符
                case[key] = value.replace(mark,real_data)
    return case

if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }
    if case["request_data"].find("#phone#") != -1:
        case = replace_mark_with_data(case, "#phone#", "123456789001")
    for key,value in case.items():
        print(key,value)

