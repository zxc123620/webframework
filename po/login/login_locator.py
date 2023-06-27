#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_locator.py
# @Time      :2023/6/24 9:25
# @Author    :zhouxiaochuan
from selenium.webdriver.common.by import By

# 手机号
phone_number_text = (By.ID, "txtUName")
# 密码
password_loc = (By.ID, "txtPassword")
# 自动登录复选框
auto_login_checkbox = (By.ID, "autoLogin")
# 登录按钮
login_btn = (By.ID, "btnLogin")