# import allure
import ddddocr


# @allure.step("识别验证码")
def identify_the_captcha(file_path):
    ocr = ddddocr.DdddOcr()
    with open(file_path, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)
    return res


print(identify_the_captcha(r"D:\Tmp\gitTest\webframework\temp.png"))