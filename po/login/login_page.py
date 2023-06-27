#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_page.py
# @Time      :2023/6/24 9:24
# @Author    :zhouxiaochuan
import allure

from po.base_page import BasePage
from po.login.login_locator import *


class LoginPage(BasePage):
    @allure.step("登录操作")
    def login_operation(self, phone_number, password, is_auto_login):
        """
        登录操作
        :param phone_number:
        :param password:
        :param is_auto_login:
        :return:
        """
        with allure.step(f"输入用户名: {phone_number}"):
            self.input(phone_number, *phone_number_text)
        with allure.step(f"输入密码: {password}"):
            self.input(password, *password_loc)
        if str(is_auto_login) == "1":
            with allure.step(f"勾选自动登录"):
                self.click_element(*auto_login_checkbox)
        with allure.step(f"点击登录"):
            self.click_element(*login_btn)
