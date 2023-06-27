#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sub_page.py
# @Time      :2023/6/25 22:07
# @Author    :zhouxiaochuan
from po.home.home_page import HomePage
from po.login.login_page import LoginPage
from po.registry.registry_page import RegistryPage
import po


class SubPage(HomePage, RegistryPage, LoginPage):
    pass
