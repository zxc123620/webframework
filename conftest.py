import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from my_exception.page_exception import PageNotFound
from po.sub_page import SubPage

driver = None


@pytest.fixture(autouse=True, scope="class")
def initial_driver() -> WebDriver:
    """
    初始化driver
    :return:
    """
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def get_pages():
    """
    获取page页面对象
    :return:
    """
    pages = {}
    clss = SubPage.__bases__  # (<class 'po.home.home_page.HomePage'>, <class 'po.registry.registry_page.RegistryPage'>
    for i in clss:
        pages[i.__name__] = [i, None]

    def inner(page_name):
        if page_name in pages:
            if pages[page_name][1] is not None:
                return pages[page_name][1]
            else:
                new_page_obj = pages[page_name][0](driver)
                pages[page_name][1] = new_page_obj
                return new_page_obj
        else:
            raise PageNotFound(f"没有找到{page_name}实例,确保该实例正确注册")

    return inner


@pytest.fixture
def delete_cookie(initial_driver):
    """
    删除cookie操作
    :return:
    """
    yield
    initial_driver.delete_all_cookies()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    result = yield
    report = result.get_result()
    if report.when in ('setup', 'call') and report.outcome == "failed":
        with allure.step("失败截图"):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


if __name__ == '__main__':
    pytest.main(['-s', '-q'])
