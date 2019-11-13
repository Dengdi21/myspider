"""
思路
1.模拟点击验证按钮
2.识别滑动缺口位置
3.模拟拖动滑块
"""
import time
from io import BytesIO
from telnetlib import EC

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# 1. 模拟点击按钮

EMAIL = "test@test.com"
PASSWORD = '123456'

class CrackGeetest():
    """
    a.初始化
        以极验的管理后台登录页面为例
    """
    def __init__(self):

        self.url == "https://account.geetest.com/login"

        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=option)

        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    """
    b. 模拟点击
        先获取按钮，使用显示等待
    """
    def get_geetest_botton(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        from telnetlib import EC
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_rader_tip')))

        return button

    # 点击按钮，第一步完成
    button = get_geetest_botton()
    button.click()


    # 2. 识别缺口
    """
        获取前后两张图片的进行对比，二者不一样的地方即为缺口
        获取不带缺口的图片，利用selenium选取图片元素，得到其所在位置的宽高，然后获取整个网页的截图，图片裁剪处理
    """

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))

        return screenshot


    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元祖,左上角和右下角
        """

        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)

        location = img.location

        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']

        return (top, bottom, left, right)


    def get_geetest_image(self, name = 'captcha.png'):
        """
        获取验证码图片
        :param name:
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()

        print('验证码位置',  top, bottom, left, right)

        screeshot = self.get_screenshot()
        captcha = screeshot.crop(top, bottom, right, bottom)

        return captcha


    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """

        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))

        return slider

    # 点按呼唤出缺口
    slider = get_slider()
    slider.click()

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置1
        :param y: 位置2
        :return: 像素是否相同
        """

        # 取两个图的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 60


        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True

        else:
            return False


    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1:不带口图片
        :param image2: 带缺口图片
        :return:
        """

        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left

        return left

    # 3.模拟拖动

    # 模拟人的行为，先加速后减速

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :return: 移动轨迹
        """

        # 移动轨迹
        track = []

        # 当前位移
        current = 0

        # 减速阈值
        mid = distance * 4/5

        # 计算间隔
        t = 0.2

        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 先加速， 加速度为正
                a = 2

            else:
                # 后减速，加速度为负
                a = -3

            # 初速度
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 当前距离
            move = v0 * t + 1/2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))

        return track


    def move_to_gap(self, slider, tracks):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        """

        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()

        time.sleep(0.5)
        ActionChains(self.browser).release().perform()









