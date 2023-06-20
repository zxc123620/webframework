import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import ROOT_PATH
from my_exception.page_exception import ElementNotFound
from utils.page_utils.other_function import identify_the_captcha


class BasePage:
    def __init__(self):
        """
        初始化driver对象
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.window_handles = []

    @allure.step("前往页面")
    def go_to(self, url):
        """
        访问页面
        :param url: 页面url
        :return:
        """
        self.driver.get(url)
        self.update_window_handle()  # 更新handle信息

    @allure.step("更新handle信息")
    def update_window_handle(self):
        """
        更新窗口信息,最先打开的在最前面,最后打开的在最后面
        :return:
        """
        handles = self.driver.window_handles
        if len(handles) == 1:
            self.window_handles.append(handles[0])
        else:
            for window_handle in handles:
                if window_handle not in self.window_handles:
                    self.window_handles.append(window_handle)

    @allure.step("定位单个元素")
    def locate(self, *locator) -> WebElement:
        """
        定位元素操作
        :param locator: 元祖,形如(BY.id, "xxx")
        :return: webElement
        """
        try:
            web_element = self.driver.find_element(*locator)
            self.locator_station(web_element)
            return web_element
        except Exception as e:
            raise ElementNotFound("元素找不到: %s" % e.args)

    @allure.step("元素截图")
    def save_element_image(self, *locator):
        """
        元素截图
        :param locator:
        :return:
        """
        file_path = ROOT_PATH + "/temp/temp.png"
        self.locate(*locator).screenshot(file_path)
        return file_path

    @allure.step("识别验证码")
    def get_captcha_number(self, path):
        """
        识别验证码
        :param: path 图片路径
        :return:
        """
        return identify_the_captcha(path)

    @allure.step("定位多个元素")
    def locates(self, *locator) -> list:
        """
        定位多个元素
        :param locator:
        :return: webElement
        """
        try:
            web_elements = self.driver.find_elements(*locator)
            for web_element in web_elements:
                self.locator_station(web_element)
            return web_elements
        except Exception as e:
            raise ElementNotFound("元素找不到: %s" % e.args)

    @allure.step("输入内容")
    def input(self, content, *locator):
        """
        输入内容
        :param content:
        :param locator:
        :return:
        """
        self.locate(*locator).send_keys(content)

    @allure.step("切换页面")
    def switch_frame(self, *locator):
        """
        切换内嵌frame
        :param locator:
        :return:
        """
        self.driver.switch_to_frame(self.locate(*locator))

    @allure.step("点击操作")
    def click_element(self, *locator):
        """
        点击事件
        :param locator:
        :return:
        """
        self.locate(*locator).click()

    def switch_window_by_title(self, title):
        """
        根据页面标题切换页面
        :param title:页面所属title
        :return:
        """
        for window_handle in self.driver.window_handles:
            self.driver.switch_to_window(window_handle)
            if self.driver.title == title:
                break

    def switch_window_by_index(self, index: int):
        """
        根据页面所属位置切换页面
        :param index:页面所属位置
        :return:
        """
        if index < 0 or index > len(self.window_handles):
            raise IndexError(f"根据页面所属位置切换页面,页面位置不正确,没有该位置: {index}")
        self.driver.switch_to_window(self.window_handles[index])

    def locator_station(self, element):
        """
        框出元素
        :param element:
        :return:
        """
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid green;"
        )


if __name__ == '__main__':
    base_page = BasePage()
    base_page.go_to("http://novel.hctestedu.com/user/register.html")
    base_page.save_element_image(By.ID, "chkd")
    print(base_page.get_captcha_number())
