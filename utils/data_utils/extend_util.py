import random
from functools import reduce

import allure


@allure.step("生成随机电话号码")
def random_phone_number():
    """
    生成随机电话号码
    中国电信号段：133，153， 180，181，189，173， 177，149
    中国联通号段：130，131，132，155，156，185，186，145，176，185
    中国移动号段：134，135，136，137，138，139，150，151，152，158，159，182，183，184，147，178
    11位
    第一位 ：1
    第二位：3，4，5，7，8
    第三位：根据第二位来确定
        3 + 【0-9】
        4 + 【5，7，9】
        5 + 【0-9】 ！4
        7 + 【0-9】！ 4and9
        8 + 【0-9】
    后8位： 随机生成8个数字
    :return:
    """
    first = "1"
    second = str(random.choice(["3", "4", "5", "7", "8"]))
    third = {
        3: str(random.randint(0, 9)),
        4: ["5", "7", "9"][random.randint(0, 2)],
        5: [str(i) for i in range(10) if i != 4][random.randint(0, 8)],
        7: [str(i) for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: str(random.randint(0, 9))
    }[int(second)]
    last = [random.randint(0, 9) for i in range(8)]
    random.shuffle(last)
    last = list(map(lambda x: str(x), last))
    last = reduce(lambda x, y: x + y, last)
    phone = first + second + third + last
    return phone


def aaa(a, b):
    return str(a) + str(b)
