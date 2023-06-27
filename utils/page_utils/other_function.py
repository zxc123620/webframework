import allure
import ddddocr


@allure.step("识别图片中的数字和字母")
def identify_the_captcha(file_path) -> str:
    """
    识别图片数字和字母
    :param file_path: 图片路径
    :return: 识别结果
    """
    ocr = ddddocr.DdddOcr()
    with open(file_path, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return str(res)


# print(identify_the_captcha(r"D:\Tmp\gitTest\webframework\temp.png"))
