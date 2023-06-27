#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :home_locator.py
# @Time      :2023/6/24 16:20
# @Author    :zhouxiaochuan
from selenium.webdriver.common.by import By

# 用户名称
user_name = (By.XPATH, '//span[@class="user_link"]/a')

# 搜索框
search_text = (By.ID, 'searchKey')

# 搜索按钮
search_btn = (By.ID, 'btnSearch')

# 所有结果展示的书籍 (多个)
search_re_books = (By.XPATH, '//tbody[@id="bookList"]')

# 定位结果展示的书名(多个)
search_re_book_name = (By.XPATH, '//tbody[@id="bookList"]/tr/td[@class="name"]')
