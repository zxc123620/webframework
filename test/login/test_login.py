#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_login.py
# @Time      :2023/6/26 21:06
# @Author    :zhouxiaochuan
import allure
import pytest

from config import ROOT_PATH
from utils.yaml_utils.yaml_driver import get_data_from_yaml

data = get_data_from_yaml(ROOT_PATH + "/test/login/test_login.yml")


@allure.feature("首页模块")
@allure.story("登录功能")
@pytest.mark.login
class TestLogin:

    @allure.title("成功登录")
    @pytest.mark.smoke
    @pytest.mark.parametrize("login_operation", [data["成功登录"]], ids=["成功登录"], indirect=True)
    def test_login_1(self, goto_login_page, login_operation, get_title, get_user_info):
        """
        验证登录成功
        测试1：页面跳转
        测试2: 跳转后显示用户信息
        :param goto_login_page: 页面跳转
        :param login_operation: 登录
        :param get_title: 获取页面标题
        :param get_user_info:
        :return:
        """
        assert get_title == data["成功登录"]["expect_page_title"], "没有跳转到首页"
        assert get_user_info == data["成功登录"]["phone_number"], "页面跳转成功,但是用户信息没有显示在首页"

    @allure.title("成功登录并且勾选下次自动登录")
    @pytest.mark.smoke
    @pytest.mark.parametrize("login_operation", [data["成功登录并且勾选下次自动登录"]], ids=["成功登录并且勾选下次自动登录"], indirect=True)
    def test_login_2(self, goto_login_page, login_operation, get_title, get_user_info):
        """
        成功登录并且勾选下次自动登录
        测试1：页面跳转
        测试2: 跳转后显示用户信息
        :param goto_login_page: 页面跳转
        :param login_operation: 登录
        :param get_title: 获取页面标题
        :param get_user_info:
        :return:
        """
        assert get_title == data["成功登录并且勾选下次自动登录"]["expect_page_title"], "没有跳转到首页"
        assert get_user_info == data["成功登录并且勾选下次自动登录"]["phone_number"], "页面跳转成功,但是用户信息没有显示在首页"
