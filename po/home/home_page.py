#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :home_page.py
# @Time      :2023/6/24 16:20
# @Author    :zhouxiaochuan
import allure

from po.base_page import BasePage
from po.home.home_locator import *


class HomePage(BasePage):
    """
    主页: http://novel.hctestedu.com/
    """

    @allure.step("获取用户名称")
    def get_username(self):
        """
        获取用户名称
        :return:
        """
        return self.get_text(*user_name)

    @allure.step("输入搜索内容")
    def input_search_text(self, content):
        """
        搜索框输入
        :param content: 搜索关键字
        :return:
        """
        self.input(content, *search_text)

    @allure.step("点击搜索按钮")
    def click_search(self):
        """
        点击搜索按钮
        :return:
        """
        self.click_element(*search_btn)

    @allure.step("搜素业务")
    def search(self, content):
        """
        搜索业务: 输入搜索 -> 点击
        :param content:
        :return:
        """
        self.input_search_text(content)
        self.click_search()

    @allure.step("获取搜索到的结果书籍")
    def get_result_books(self):
        """
        获取搜索到的结果书籍
        :return:
        """
        return self.locates(*search_re_books)

    @allure.step("获取搜索到的结果书籍名称")
    def get_result_books_name(self):
        """
        获取搜索到的结果书籍名称
        :return:
        """
        result_elements = self.locates(*search_re_book_name)
        return [result_element.text for result_element in result_elements]


if __name__ == '__main__':
    print(HomePage.__class__)
