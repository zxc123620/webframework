#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2023/6/24 16:29
# @Author    :zhouxiaochuan
import allure
import pytest

from my_exception.page_exception import KeyFoundException, ElementNotFound
from po.home.home_page import HomePage
from po.url import PROJECT_BASE_URL


@pytest.fixture(scope="class")
def init_home_page(initial_driver, get_pages) -> HomePage:
    """
    初始化注册页面
    :param get_pages:
    :param initial_driver:
    :return:
    """
    return get_pages("HomePage")


@pytest.fixture
def goto_home_page(init_home_page) -> HomePage:
    """
    打开网址
    :param init_home_page:
    :return:
    """
    page = init_home_page
    page.go_to(PROJECT_BASE_URL)
    return page


@pytest.fixture
def search_operation(goto_home_page, request) -> HomePage:
    """
    搜索操作
    :param request:
    :param goto_home_page:
    :return:
    """
    data = request.param
    page = goto_home_page
    if "content" not in data:
        raise KeyFoundException(f"数据中有key不存在: {data}")
    page.search(data["content"])
    return page


@pytest.fixture
def get_result_books(search_operation):
    """
    获取搜索到的书籍
    :param search_operation:
    :return:
    """
    page = search_operation
    try:
        return page.get_result_books_name()
    except ElementNotFound:
        return False


@pytest.fixture
def get_url(search_operation):
    """
    获取url
    :param search_operation:
    :return:
    """
    page = search_operation
    with allure.step("获取到当前地址"):
        return page.url


@pytest.fixture
def get_title(get_pages):
    """
    获取title
    :return:
    """
    return get_pages("HomePage").title


@pytest.fixture
def get_user_info(get_pages):
    """
    获取用户信息
    :return:
    """
    return get_pages("HomePage").get_username()
