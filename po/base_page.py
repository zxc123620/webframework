from selenium import webdriver


class BasePage:
    def __init__(self):
        """
        初始化driver对象
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def go_to(self, url):
        """
        访问页面
        :param url: 页面url
        :return:
        """
        self.driver.get(url)

    def locate(self, *locate):
        pass


if __name__ == '__main__':
    BasePage()
