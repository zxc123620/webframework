class PageException(Exception):
    pass


class ElementNotFound(PageException):
    pass


class PageNotFound(PageException):
    pass


class YamlException(Exception):
    pass


class KeyFoundException(YamlException):
    """
    数据中字典与实际参数名不一样
    """
    pass
