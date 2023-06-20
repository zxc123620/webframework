import os

# 项目根路径ROOT_PATH
__current_path = os.getcwd()
ROOT_PATH = __current_path[:__current_path.find("webFramework") + len("webFramework")]
# 变量
ALL_VALUE = {}


def get_all_value() -> dict:
    return ALL_VALUE


def set_all_value(value: dict):
    ALL_VALUE.update(value)


# mysql
MYSQL_HOST = "shop-xo.hctestedu.com"
MYSQL_port = 3306
MYSQL_USERNAME = "api_test"
MYSQL_PASSWORD = "Aa9999!"
MYSQL_DB = "shopxo_hctested"

if __name__ == '__main__':
    print(__current_path)
    print(ROOT_PATH)
