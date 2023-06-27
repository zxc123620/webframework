#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :registry_locator.py
# @Time      :2023/6/24 9:25
# @Author    :zhouxiaochuan
from selenium.webdriver.common.by import By

# 手机号
phone_text = (By.ID, "txtUName")
# 密码
pwd_text = (By.ID, "txtPassword")
# 验证码输入框
code_input = (By.ID, "TxtChkCode")
# 验证码图片
code_pic = (By.ID, "chkd")
# 注册按钮
registry_btn = (By.ID, "btnRegister")
# 错误文本
error_span = (By.ID, "LabErr")
