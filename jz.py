import os
import random

import cv2
import numpy
import numpy as  np

__author__ = 'ypf'
__date__ = '2019/1/16,9:11'



# def SaltAndPepper(img):
#     coutn = 1000
#     for k in range(0, coutn):
#         # get the random point
#         xi = int(np.random.uniform(0, img.shape[1]))
#         xj = int(np.random.uniform(0, img.shape[0]))
#         # add noise
#         if img.ndim == 2:
#             img[xj, xi] = 255
#         elif img.ndim == 3:
#             img[xj, xi, 0] = 25
#             img[xj, xi, 1] = 20
#             img[xj, xi, 2] = 20
#     return img
#     # cv2.namedWindow('img')
#     # cv2.imshow('img', img)
#     # cv2.waitKey()
#     # cv2.destroyAllWindows()
# cc=cv2.imread('1.jpg')
# SaltAndPepper(cc)
def tupianshengcheng():
    randomByteArray = bytearray(os.urandom(300 * 400))
    flatNumpyArray = numpy.array(randomByteArray)
    bgrImage = flatNumpyArray.reshape(100, 400, 3)
    cv2.imwrite('RandomColor.png', bgrImage)

# def draw_circle(event, x, y, flags, param):
#     # 鼠标左键双击
#     if event == cv2.EVENT_LBUTTONDOWN:
#         # 每次点击，都是一种 新颜色
#         r = random.randint(0, 255)
#         g = random.randint(0, 255)
#         b = random.randint(0, 255)
#         cv2.circle(img, (x, y), 100, (b, g, r), -1)
#
#
# img = np.zeros((600, 1000, 3), np.uint8)
# cv2.namedWindow('draw circles')
# # 鼠标点击的位置 = 传入函数的圆心
# cv2.setMouseCallback('draw circles', draw_circle)

from PIL import Image
# def createcolor():
#     img = Image.open("D:\shiju\contrast\color.jpg")#读取图片
#     img = img.convert("RGB")
#     width = img.size[0]#长度
#     height = img.size[1]#宽度
#     for i in range(0, width):  # 遍历所有长度的点
#         for j in range(0, height):  # 遍历所有宽度的点
#             data = img.getpixel((i, j))  # i,j表示像素点
#             if (data[0] == 255 and data[1] == 255 and data[2] == 255):
#                 m = random.randint(100, 190)  # 取160-190的颜色随机值
#                 print("m=", m)
#                 img.putpixel((i, j), (m, m, m))  # 颜色改变
#     # img = img.convert("L")  # 把图片转成灰度图
#     img.save("D:\shiju\contrast\color.jpg")  # 保存修改像素点后的图片
# createcolor()
def creatcolor():
    black=cv2.imread(r"D:\shiju\contrast\black.jpg")
    blue=cv2.imread(r"D:\shiju\contrast\blue.jpg")
    orange=cv2.imread(r"D:\shiju\contrast\orange.jpg")
    red=cv2.imread(r"D:\shiju\contrast\red.jpg")
    list1=[black,blue,orange,red]
    random.shuffle(list1)
    imagecolor = cv2.hconcat(list1)
    return imagecolor
creatcolor()
