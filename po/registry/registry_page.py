#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :registry_page.py
# @Time      :2023/6/24 9:25
# @Author    :zhouxiaochuan
import allure

from po.base_page import BasePage
from po.registry.registry_locator import *


class RegistryPage(BasePage):

    @property
    @allure.step("获取错误文本")
    def error_text(self):
        """
        获取错误文本
        :return:
        """
        return self.get_text(*error_span)

    @allure.step("输入手机号")
    def input_phone_number(self, phone_number: str):
        """
        输入手机号
        :param phone_number:
        :return:
        """
        self.input(phone_number, *phone_text)

    @allure.step("输入密码")
    def input_password(self, password: str):
        """
        输入密码
        :param password:
        :return:
        """
        self.input(password, *pwd_text)

    @allure.step("识别验证码")
    def identify_code(self):
        """
        识别验证码
        :return: 验证码
        """
        return self.get_captcha_number(self.save_element_image("identify_code_pic", *code_pic))  # 得到验证码

    @allure.step("输入验证码")
    def input_code(self, code: str):
        """
        输入验证码
        :param code:
        :return:
        """
        self.input(code, *code_input)

    @allure.step("自动输入验证码")
    def auto_input_code(self):
        """
        自动输入验证码
        :return:
        """
        self.input_code(self.identify_code())

    @allure.step("点击注册按钮")
    def click_registry(self):
        """
        点击注册按钮
        :return:
        """
        self.click_element(*registry_btn)

    @allure.step("进行注册业务")
    def registry_operation(self, phone_number, password):
        """
        注册业务
        :param phone_number: 电话号码
        :param password: 密码
        :return:
        """
        self.input_phone_number(phone_number)
        self.input_password(password)
        self.auto_input_code()
        self.click_registry()

    @allure.step("进行注册业务-不加验证码")
    def registry_operation_no_code(self, phone_number, password):
        """
        进行注册业务-不加验证码
        :param phone_number: 电话号码
        :param password: 密码
        :return:
        """
        self.input_phone_number(phone_number)
        self.input_password(password)
        self.click_registry()

    @allure.step("进行注册业务-自己填写验证码")
    def registry_operation_on_code(self, phone_number, password, registry_code):
        """
        进行注册业务-自己添加验证码
        :param registry_code: 验证码
        :param phone_number: 电话号码
        :param password: 密码
        :return:
        """
        self.input_phone_number(phone_number)
        self.input_password(password)
        self.input_code(registry_code)
        self.click_registry()
