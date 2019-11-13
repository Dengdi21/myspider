import tesserocr

from PIL import Image


# 1. 初级识别
image = Image.open("CheckCode.aspx.jpeg")

result = tesserocr.image_to_text(image)
print(result)


# 2 转化为灰度图形
image = image.convert("L")
image.show()

# 3 二值化处理
# image = image.convert("1")
# image.show()

result2 = tesserocr.image_to_text(image)
print(result2)


# 指定二值化阈值
threshold = 80
tabel = []

for i in range(256):
    if i < threshold:
        tabel.append(0)
    else:
        tabel.append(1)

image = image.point(tabel, '1')

image.show()

