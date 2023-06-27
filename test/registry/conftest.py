#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2023/6/24 12:09
# @Author    :zhouxiaochuan
import pytest

from my_exception.page_exception import KeyFoundException
from po.home.home_page import HomePage
from po.registry.registry_page import RegistryPage
from po.url import REGISTRY_URL


@pytest.fixture(scope="class")
def init_registry_page(initial_driver, get_pages) -> RegistryPage:
    """
    初始化注册页面
    :param get_pages:
    :param initial_driver:
    :return:
    """
    return get_pages("RegistryPage")


@pytest.fixture
def goto_registry_page(init_registry_page, delete_cookie) -> RegistryPage:
    """
    打开网址
    :param delete_cookie: 删除cookie前后置操作
    :param init_registry_page:
    :return:
    """
    page = init_registry_page
    page.go_to(REGISTRY_URL)
    return page


@pytest.fixture
def registry_operation(goto_registry_page, request):
    """
    注册操作
    :param request: 参数
    :param goto_registry_page: fixture
    :return:
    """
    data = request.param
    registry_page = goto_registry_page
    keys = data.keys()
    if ("phone_number" in keys) and ("password" in keys):
        registry_page.registry_operation(data["phone_number"], data["password"])
        return registry_page
    else:
        raise KeyFoundException(f"数据中有key不存在: {data}")


@pytest.fixture
def registry_operation_no_code(goto_registry_page, request):
    """
    注册操作-不输入验证码
    :param request: 参数
    :param goto_registry_page: fixture
    :return:
    """
    data = request.param
    registry_page = goto_registry_page
    keys = data.keys()
    if ("phone_number" in keys) and ("password" in keys):
        registry_page.registry_operation_no_code(data["phone_number"], data["password"])
        return registry_page
    else:
        raise KeyFoundException(f"数据中有key不存在: {data}")


@pytest.fixture
def registry_operation_on_code(goto_registry_page, request):
    """
    注册操作-错误
    :param request: 参数
    :param goto_registry_page: fixture
    :return:
    """
    data = request.param
    registry_page = goto_registry_page
    keys = data.keys()
    if ("phone_number" in keys) and ("password" in keys) and ("code" in keys):
        registry_page.registry_operation_on_code(data["phone_number"], data["password"], data["code"])
        return registry_page
    else:
        raise KeyFoundException(f"数据中有key不存在: {data}")


# --------------------------------------------------------
@pytest.fixture
def get_homepage_username(goto_registry_page):
    """
    获取主页的用户名称(电话号码)
    :param goto_registry_page:
    :return:
    """
    if goto_registry_page.title == "会员注册_读书屋":
        # 没有跳转过去
        return False
    else:
        home_page = HomePage(goto_registry_page.driver)
        return home_page.get_username()


@pytest.fixture
def get_error_info(goto_registry_page):
    """
    获取错误信息
    :param goto_registry_page:
    :return:
    """
    if goto_registry_page.title != "会员注册_读书屋":
        # 没有跳转过去
        return False
    else:
        return goto_registry_page.error_text
#
# if __name__ == '__main__':
#     data = {"phone_number": "1", "password": "2"}
#     print("phone_number" in data.keys())
#     print("password" in data.keys())
