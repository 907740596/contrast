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
import os

import copy
import tkinter as tk
from tkinter import  messagebox
from PIL import Image, ImageTk
from skimage.measure import compare_ssim
import cv2
import  numpy as  np
class CompareImage():
    # 图片ssim对比函数
    def compare_image(self, path_image1):
       try:
           imageA = cv2.imread(path_image1)
           imageB = SaltAndPepper(imageA)
           detil_image(imageA,imageB)
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
window.geometry('1000x630')
# 禁止拉伸页面
window.resizable(0,0)
# label  标签
l = tk.Label(window, bg='#F5F5DC', width=30, text='Vision',justify='left')
l.place(x=0,y=0)
jd = tk.Label(window, bg='#F5F5DC', width=30, text='SSIM标准:',justify='left')
jd.place(x=500,y=0)
l1=tk.Label(window)
l1.pack(side='bottom')
# welcome image
# canvas = tk.Canvas(window, height=443, width=800)
# image_file = tk.PhotoImage(file='logo.png')
# image = canvas.create_image(0,0, anchor='nw', image=image_file)
# canvas.pack(side='bottom')
tk.Label(window, text='测试块:').place(x=760, y= 0)
img1 = tk.StringVar()
entry_img1 = tk.Entry(window, textvariable=img1,bg='#E6E6FA')
entry_img1.place(x=820, y=0)
def print_selection(v):
    # 拉动条  ssim对比值
    jd.config(text='SSIM:' + v)
    return v
s=tk.Scale(window,from_=0,to=1,tickinterval=0.1,orient=tk.HORIZONTAL,
           length=300,showvalue=True,resolution=0.1,command=print_selection,bg='#E6E6FA',width=5)
s.set(value=0.9)
s.place(x=200,y=0)

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
    macrop_size = (480, 350)   #   大图片尺寸
    crop_size = (160, 200)     #小图片尺寸
    original_img = name
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
    original_img1 = name1
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
    FW=cv2.imwrite("end.png", imgend, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    return FW

def SaltAndPepper(yuan):
    # 定义添加椒盐噪声的函数
    coutn = 100000
    img=copy.deepcopy(yuan)
    for k in range(0, coutn):
        # get the random point
        xi = int(np.random.uniform(0, img.shape[1]))
        xj = int(np.random.uniform(0, img.shape[0]))
        # add noise
        if img.ndim == 2:
            img[xj, xi] = 255
        elif img.ndim == 3:
            img[xj, xi, 0] = 25
            img[xj, xi, 1] = 20
            img[xj, xi, 2] = 20
    return img

def contrast():
    # 对比函数
    # 获取图片地址
    img_1 = img1.get()
    ssim1=s.get()
    # 进行对比
    jieguo=compare_image.compare_image(img_1)
    jieguo=round(jieguo,2)
    if jieguo==0 or float(ssim1)==False:
        tk.messagebox.showinfo(title='出错了', message='检查图片路径或者ssim值是否有误')
    else:
        image2 = Image.open('end.png')
        photo2 = ImageTk.PhotoImage(image2)
        l1.config(image=photo2)
        l1.image = photo2
        # tk.messagebox.showinfo(title='对比结果', message=f'SSIM:{jieguo}')
        if  jieguo>float(ssim1):
            l.config(bg='green',text=f'ok   {jieguo}')
        else:
            l.config( bg='red',  text=f'wrong  {jieguo}')

# 测试按钮函数
btn_login = tk.Button(window, text='加噪测试', command=contrast,bg='#D8BFD8')
btn_login.place(x=700, y=0)


if __name__ == '__main__':
    window.mainloop()

