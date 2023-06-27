#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2023/6/26 21:05
# @Author    :zhouxiaochuan
import pytest

from po.url import LOGIN_URL


@pytest.fixture(scope="class")
def init_login_page(initial_driver, get_pages):
    """
    初始化注册页面
    :param get_pages:
    :param initial_driver:
    :return:
    """
    return get_pages("LoginPage")


@pytest.fixture
def goto_login_page(init_login_page, delete_cookie):
    """
    打开网址
    :param delete_cookie:
    :param init_login_page:
    :return:
    """
    login_page= init_login_page
    login_page.go_to(LOGIN_URL)
    return init_login_page


@pytest.fixture
def login_operation(goto_login_page, request):
    """
    登录操作
    :param goto_login_page:
    :param request:
    :return:
    """
    login_page = goto_login_page
    data = request.param
    login_page.login_operation(data["phone_number"], data["password"], data["auto_login"])
