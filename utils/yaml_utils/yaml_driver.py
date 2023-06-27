import re

import yaml

from config import ROOT_PATH
from utils.data_utils.extend_util import *  # 别删了


def get_data_from_yaml(path) -> dict:
    """
    获取原始测试数据
    :param path:
    :return:
    """
    result = {}
    data = __load_yaml(path)
    for i in range(len(data)):
        __format_data(data[i])
    for i in range(len(data)):
        temp = {data[i]["id"]: data[i]}
        result.update(temp)
    return result


def __load_yaml(path):
    """
    加载yaml文件
    :param path: 文件路径
    :return:
    """
    try:
        file = open(path, 'r', encoding='utf-8')
        data = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError("找不到文件")
    return data


def __format_data(data: dict):
    """
    正则替换函数
    :param data: 每一项测试数据,字典
    :return:
    """
    # data: 每一项,是一个字典
    for item_key, item_value in data.items():
        result = re.sub("{{(.*?)}}", __inner_sub, item_value)
        data[item_key] = result


def __inner_sub(temp):
    """
    替换用函数
    :param temp:
    :return:
    """
    format_raw = temp.group(1)  # function(a,b)
    try:
        return eval(format_raw)
    except NameError:
        raise NameError(f"没有该扩展功能:{format_raw}")
    except SyntaxError:
        raise SyntaxError(f"扩展功能语法错误:{format_raw}")
    except TypeError:
        raise TypeError(f"扩展功能缺少参数:{format_raw}")


if __name__ == '__main__':
    # print(re.findall("{{(.*?)}}", "asdfsdf{{function(a,b)}}"))
    # data_1 = {"a": "{{random_phone_number()}}"}
    # __format_data(data_1)
    # print(data_1)
    # print(eval("aaa(1)"))
    data = get_data_from_yaml(ROOT_PATH + "/test/home/test_home.yml")
    print(data)
