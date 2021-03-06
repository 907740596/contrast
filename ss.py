import cv2

__author__ = 'ypf'
__date__ = '2019/1/11,14:32'


import  numpy as np

def duibi(image1,image2):
    h1,w1,c1 = image1.shape
    h2,w2,c2 = image2.shape
    if c1 != c2:
        print("channels NOT match, cannot merge")
        return
    else:
        if w1 > w2:
            tmp = np.zeros([h2,w1-w2,c1])
            image3 = np.hstack([image2,tmp])
            image3 = np.vstack([image1,image3])
            cv2.imshow('666',image3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        elif w1 == w2:
            image3 = np.vstack([image1,image2])
            cv2.imshow('666',image3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            tmp = np.zeros([h1,w2-w1,c2])
            image3 = np.hstack([image1,tmp])
            image3 = np.vstack([image3,image2])
            cv2.imshow('666',image3)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    return image3
img1=cv2.imread('1.jpg')
img2=cv2.imread('1.jpg')

# duibi(img1,img2)
image3=cv2.hconcat([img2,img1])  #  横向拼接
image4=cv2.vconcat([img2,img1]) #  纵向拼接
cv2.imshow('666',image3)
cv2.imshow('66',image4)
cv2.waitKey(0)
cv2.destroyAllWindows()

def heng(img1,img2,img3,imgtop):
    # 横向拼接,再纵向拼接函数
    imgh = cv2.hconcat([img1,img2,img3])
    imgF = cv2.vconcat([imgtop,imgh ])
    return imgF
def zong(img1,img2):
    # 拼接两个图
    imgend = cv2.hconcat([img1,img2])
    return imgend



''''''''''''''''''''''''
# 原来版本
"""
SSIM参数
        一种衡量两幅图像相似度的新指标，其值越大越好，最大为1，经常用到图像处理中，
        特别在图像去噪处理中在图像相似度评价上全面超越SNR（signal to noise ratio）和PSNR（peak signal to noise ratio）。
        结构相似性理论认为，自然图像信号是高度结构化的，即像素间有很强的相关性，特别是空域中最接近的像素，
        这种相关性蕴含着视觉场景中物体结构的重要信息；HVS的主要功能是从视野中提取结构信息，
        可以用对结构信息的度量作为图像感知质量的近似。
        结构相似性理论是一种不同于以往模拟HVS低阶的组成结构的全新思想，与基于HVS特性的方法相比，
        最大的区别是自顶向下与自底向上的区别。这一新思想的关键是从对感知误差度量到对感知结构失真度量的转变。
        它没有试图通过累加与心理物理学简单认知模式有关的误差来估计图像质量，而是直接估计两个复杂结构信号的结构改变，
        从而在某种程度上绕开了自然图像内容复杂性及多通道去相关的问题。作为结构相似性理论的实现，
        结构相似度指数从图像组成的角度将结构信息定义为独立于亮度、对比度的，反映场景中物体结构的属性
        ，并将失真建模为亮度、对比度和结构三个不同因素的组合。用均值作为亮度的估计，标准差作为对比度的估计，
        协方差作为结构相似程度的度量。
"""

import tkinter as tk
from random import random
from tkinter import  messagebox
from skimage.measure import compare_ssim
import cv2
import  numpy as  np
class CompareImage():
    # 图片ssim对比函数
    def compare_image(self, path_image1, path_image2):
       try:
           imageA = cv2.imread(path_image1)
           imageB = cv2.imread(path_image2)
           crop_size = (320, 480)
           rayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
           rayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
           grayA = cv2.resize(rayA, crop_size, interpolation=cv2.INTER_CUBIC)
           grayB = cv2.resize(rayB, crop_size, interpolation=cv2.INTER_CUBIC)
           (score, diff) = compare_ssim(grayA, grayB, full=True)
           return score
       except:
           return 0
compare_image = CompareImage()


#   窗口化
window = tk.Tk()
window.title('Welcome Vision')
window.geometry()
l = tk.Label(window, bg='yellow', width=20, text='Vision')
l.pack()
jd = tk.Label(window, bg='yellow', width=20, text='SSIM标准:')
jd.pack()


# welcome image
canvas = tk.Canvas(window, height=443, width=800)
image_file = tk.PhotoImage(file='logo.png')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='right')

# user information
tk.Label(window, text='图片地址1:').place(x=50, y= 150)
img1 = tk.StringVar()
entry_img1 = tk.Entry(window, textvariable=img1)
entry_img1.place(x=160, y=150)
tk.Label(window, text='图片地址2: ').place(x=50, y= 190)
img2 = tk.StringVar()
entry_img2 = tk.Entry(window, textvariable=img2)
entry_img2.place(x=160, y=190)
# 拉动条  ssim对比值
def print_selection(v):
    jd.config(text='SSIM:' + v)
    return v
s=tk.Scale(window,label='SSIM:',from_=0,to=1,tickinterval=0.1,orient=tk.HORIZONTAL,
           length=300,showvalue=True,resolution=0.1,command=print_selection)
s.set(value=0.9)
s.pack()

def calcAndDrawHist(image, color):
    # 直方图
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)
    return histImg
# def cut(name):
#     修改名字
#     name=str(name)
#     c = name.split("\\")
#     return c[-1]
def heng(img1,img2,img3,imgtop):
    # 横向拼接,再纵向拼接函数
    imgh = cv2.hconcat([img1,img2,img3])
    imgF = cv2.vconcat([imgtop,imgh ])
    return imgF
def zong(img1,img2):
    # 拼接两个图
    imgend = cv2.hconcat([img1,img2])
    return imgend
def detil_image(name,name1):
    # 图片对比  生成直方图
    macrop_size = (600, 400)   #   大图片尺寸
    crop_size = (200, 200)     #小图片尺寸
    original_img = cv2.imread(name)
    img = cv2.resize(original_img, macrop_size, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)

    histImgB = calcAndDrawHist(b, [255, 0, 0])
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])
    histImgB = cv2.resize(histImgB, crop_size, interpolation=cv2.INTER_CUBIC)
    histImgG = cv2.resize(histImgG, crop_size, interpolation=cv2.INTER_CUBIC)
    histImgR = cv2.resize(histImgR, crop_size, interpolation=cv2.INTER_CUBIC)
    imgF=heng(histImgB,histImgG,histImgR,img)



    #   第二个图片操作
    original_img1 = cv2.imread(name1)
    img1 = cv2.resize(original_img1, macrop_size, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img1)
    hist1ImgB = calcAndDrawHist(b, [255, 0, 0])
    hist1ImgG = calcAndDrawHist(g, [0, 255, 0])
    hist1ImgR = calcAndDrawHist(r, [0, 0, 255])
    hist1ImgB = cv2.resize(hist1ImgB, crop_size, interpolation=cv2.INTER_CUBIC)
    hist1ImgG = cv2.resize(hist1ImgG, crop_size, interpolation=cv2.INTER_CUBIC)
    hist1ImgR = cv2.resize(hist1ImgR, crop_size, interpolation=cv2.INTER_CUBIC)
    imgS = heng(hist1ImgB, hist1ImgG, hist1ImgR, img1)
    # 合并两张图片
    imgend=zong(imgF,imgS)

    cv2.imshow('contrast', imgend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






#定义添加椒盐噪声的函数
def SaltAndPepper(src,percetage):
    SP_NoiseImg=src
    SP_NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(SP_NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            SP_NoiseImg[randX,randY]=0
        else:
            SP_NoiseImg[randX,randY]=255
    return SP_NoiseImg

def contrast():
    # 获取图片地址
    img_1 = img1.get()
    img_2 = img1.get()
    # 获取选定ssim值
    ssim1=s.get()
    # 进行对比
    jieguo=compare_image.compare_image(img_1, img_2)
    if jieguo==0 and float(ssim1)==False:
        tk.messagebox.showinfo(title='出错了', message='检查图片路径或者ssim值是否有误')
    else:
        tk.messagebox.showinfo(title='对比结果', message=f'SSIM:{jieguo}')
        if  jieguo>float(ssim1):
            l.config(bg='green',text='ok')
        else:
            l.config( bg='red',  text='wrong')
    detil_image(img_1,img_2)
# login and sign up button
btn_login = tk.Button(window, text='对比', command=contrast)
btn_login.place(x=200, y=230)

if __name__ == '__main__':
    window.mainloop()