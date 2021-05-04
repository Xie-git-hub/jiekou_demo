import jsonpath
from Common.handle_data import EnvData
from Common.my_logger import logger


def extract_data_from_response(extract_exprs,response_dict):
    """
       根据jsonpath提取表达式，从响应结果当中，提取数据并设置为环境变量EnvData类的类属性，作为全局变量使用。
       :param extract_exprs: 从excel当中读取出来的，提取表达式的字符串。
       :param response_dict: http请求之后的响应结果。
       :return:Nonoe
       """
    # 将提取表达式转换成字典
    extract_exprs= eval(extract_exprs)
    logger.info("要转换成字典的表达式是：\n".format(extract_exprs))
    # 遍历字典，key作为全局变量名，value是jsonpath提取表达式。
    for key,value in extract_exprs.items():
        # 提取
        res = str(jsonpath.jsonpath(response_dict,value)[0])
        logger.info("设置环境变量，key:{},value:{}".format(key,res))
        #设置为环境变量
        setattr(EnvData,key,res)
if __name__ == '__main__':
     ss = '{"member_id":"$..id","token":"$..token"}'
     response = {'code': 0, 'msg': 'OK',
                 'data': {'id': 200713, 'leave_amount': 8555405.44, 'mobile_phone': '18200009057',
                          'reg_name': '美丽可爱的小简', 'reg_time': '2020-06-29 11:52:20.0', 'type': 1,
                          'token_info': {'token_type': 'Bearer', 'expires_in': '2020-07-08 21:33:05',
                                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwMDcxMywiZXhwIjoxNTk0MjE1MTg1fQ.9oTx_KSOwjEg4V9Ez_P6QV-3aBk3QCCFRZk3OlTnGDElkVanMLFK_H5wgI_9xolnjBNZE9TMI7e1nSOPKWj2HA'}},
                 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}

     extract_data_from_response(ss,response)
     print(EnvData.__dict__)

