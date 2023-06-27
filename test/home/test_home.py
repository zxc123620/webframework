#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_home.py
# @Time      :2023/6/25 21:33
# @Author    :zhouxiaochuan
import allure
import pytest

from config import ROOT_PATH
from utils.yaml_utils.yaml_driver import get_data_from_yaml

data = get_data_from_yaml(ROOT_PATH + "/test/home/test_home.yml")


@allure.feature("首页模块")
@allure.story("搜索功能")
@pytest.mark.search
class TestHome:
    @allure.title("模糊搜索我的")
    @pytest.mark.parametrize("search_operation", [data["模糊搜索我的"]], ids=["模糊搜索我的"], indirect=True)
    @pytest.mark.smoke
    def test_search_1(self, search_operation, get_result_books, get_url):
        """
        测试 模糊搜索我的
        1、测试1 搜素到的书籍中是否都包含我的
        2、测试2 搜索页面是否跳转到“全部作品"
        :param search_operation:
        :param get_result_books:
        :param get_url:
        :return:
        """
        assert get_result_books, "页面没有跳转到结果页"
        assert data["模糊搜索我的"]["url"] in get_url, "页面没有跳转到全部作品页"
        for book_name in get_result_books:
            assert data["模糊搜索我的"]["content"] in book_name, f"搜索书籍中有书籍({book_name})没有关键字f{data['content']}"

    @allure.title("搜索结果>20条")
    @pytest.mark.parametrize("search_operation", [data["搜索结果>20条"]], ids=["搜索结果>20条"], indirect=True)
    @pytest.mark.smoke
    def test_search_2(self, search_operation, get_result_books):
        """
        测试搜索结果>20条,查看是否按照20条一页排序
        1、测试1 一页20条
        2、测试2 结果中都有关键字
        :param search_operation:
        :param get_result_books:
        :return:
        """
        assert get_result_books, "页面没有跳转到结果页"
        assert 20 == len(get_result_books), f"搜索结果({len(get_result_books)})不为20条"
        for book_name in get_result_books:
            assert data["搜索结果>20条"]["content"] in book_name, f"搜索书籍中有书籍({book_name})没有关键字f{data['content']}"
