#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_registry.py
# @Time      :2023/6/24 11:43
# @Author    :zhouxiaochuan
import allure
import pytest

from config import ROOT_PATH
from utils.yaml_utils.yaml_driver import get_data_from_yaml

data = get_data_from_yaml(ROOT_PATH + "/test/registry/test_registry.yml")


# print(data)


@allure.feature("注册模块")
@allure.story("注册功能")
@pytest.mark.registry
class TestRegistry:
    @allure.title("注册成功")
    @pytest.mark.parametrize("registry_operation", [data["注册成功"]], ids=["注册成功"], indirect=True)
    @pytest.mark.smoke
    def test_registry_ok(self, registry_operation, get_homepage_username):
        assert get_homepage_username  # 判断跳转到首页没有
        assert data['注册成功']["phone_number"] == get_homepage_username

    @allure.title("注册失败-电话号码不准确")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-电话号码不准确"]], ids=["注册失败-电话号码不准确"], indirect=True)
    def test_registry_fail1(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-电话号码不准确']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-电话号码被注册")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-电话号码被注册"]], ids=["注册失败-电话号码被注册"], indirect=True)
    def test_registry_fail2(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-电话号码被注册']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-手机号为空")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-手机号为空"]], ids=["注册失败-手机号为空"], indirect=True)
    def test_registry_fail3(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-手机号为空']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-密码为空")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-密码为空"]], ids=["注册失败-密码为空"], indirect=True)
    def test_registry_fail4(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-密码为空']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-没输入验证码")
    @pytest.mark.parametrize("registry_operation_no_code", [data["注册失败-没输入验证码"]], ids=["注册失败-没输入验证码"], indirect=True)
    def test_registry_fail5(self, registry_operation_no_code, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-没输入验证码']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-密码小于6位")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-密码小于6位"]], ids=["注册失败-密码小于6位"], indirect=True)
    def test_registry_fail6(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-密码小于6位']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-密码大于20位")
    @pytest.mark.parametrize("registry_operation", [data["注册失败-密码大于20位"]], ids=["注册失败-密码大于20位"], indirect=True)
    def test_registry_fail8(self, registry_operation, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-密码大于20位']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"

    @allure.title("注册失败-验证码错误")
    @pytest.mark.parametrize("registry_operation_on_code", [data["注册失败-验证码错误"]], ids=["注册失败-验证码错误"], indirect=True)
    def test_registry_fail9(self, registry_operation_on_code, get_error_info):
        assert get_error_info, "能够注册成功"  # 判断跳转到首页没有
        assert data['注册失败-验证码错误']["expect_msg"] == get_error_info, "手机号注册失败,但是提示信息有误"
