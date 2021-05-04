"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 21:18
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
from configparser import ConfigParser
import os

from Common.handle_path import conf_dir

class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")



file_path = os.path.join(conf_dir, "nmb.ini")
conf = HandleConfig(file_path)


if __name__ == '__main__':
    conf = HandleConfig("nmb.ini")
    conf.get("log","name")
