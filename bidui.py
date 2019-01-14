import time

__author__ = 'ypf'
__date__ = '2019/1/4,9:58'
# import cv2
# import numpy as np
# img4 = cv2.imread('1.jpg')
# img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)
# print(img4)

# img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
import numpy as np
from skimage.measure import compare_ssim
import cv2
class CompareImage():
    def compare_image(self, path_image1, path_image2):
        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)
        if imageA is None:
           return print("图片1路径有问题")
        elif imageB is None:
           return print("图片2路径有问题")
        else:
            crop_size = (600, 400)
            rayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            rayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
            grayA= cv2.resize(rayA, crop_size, interpolation = cv2.INTER_CUBIC)
            grayB = cv2.resize(rayB, crop_size, interpolation=cv2.INTER_CUBIC)
            (score, diff) = compare_ssim(grayA, grayB, full=True)
            print("SSIM: {}".format(score))
            if score>0.8:
                return print("相似")
compare_image = CompareImage()
compare_image.compare_image("1.jpg", "2.jpg")


def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)
    return histImg

def detil_image(self,name):
    original_img = cv2.imread(name)
    img = cv2.resize(original_img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)
    crop_size=(200,200)
    histImgB = calcAndDrawHist(b, [255, 0, 0])
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])
    histImgB=  cv2.resize(histImgB, crop_size, interpolation = cv2.INTER_CUBIC)
    histImgG = cv2.resize(histImgG, crop_size, interpolation=cv2.INTER_CUBIC)
    histImgR = cv2.resize(histImgR, crop_size, interpolation=cv2.INTER_CUBIC)
    cv2.imshow("%sImgB"%(name), histImgB)
    cv2.imshow("%sImgG"%(name), histImgG)
    cv2.imshow("%sImgR"%(name), histImgR)
    cv2.imshow("Img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

import tkinter as tk
from tkinter import  messagebox
# from skimage.measure import compare_ssim
# import cv2
# class CompareImage():
#     def compare_image(self, path_image1, path_image2):
#        try:
#            imageA = cv2.imread(path_image1)
#            imageB = cv2.imread(path_image2)
#            crop_size = (320, 480)
#            rayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
#            rayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
#            grayA = cv2.resize(rayA, crop_size, interpolation=cv2.INTER_CUBIC)
#            grayB = cv2.resize(rayB, crop_size, interpolation=cv2.INTER_CUBIC)
#            (score, diff) = compare_ssim(grayA, grayB, full=True)
#            return score
#        except:
#            return 0
# compare_image = CompareImage()



# window = tk.Tk()
# window.title('Welcome to Mofan Python')
# window.geometry('450x300')
# l = tk.Label(window, bg='yellow', width=20, text='Vision')
# l.pack()
#
# # welcome image
# canvas = tk.Canvas(window, height=200, width=500)
# image_file = tk.PhotoImage(file='logo.png')
# image = canvas.create_image(0,0, anchor='nw', image=image_file)
# canvas.pack(side='top')
#
# # user information
# tk.Label(window, text='图片地址1:').place(x=50, y= 150)
# tk.Label(window, text='图片地址2: ').place(x=50, y= 190)
#
# img1 = tk.StringVar()
# img1.set('')
# entry_img1 = tk.Entry(window, textvariable=img1)
# entry_img1.place(x=160, y=150)
# img2 = tk.StringVar()
# entry_img2 = tk.Entry(window, textvariable=img2)
# entry_img2.place(x=160, y=190)
#
# def contrast():
#     img_1 = img1.get()
#     type(img_1)
#     img_2 = img2.get()
#     jieguo=compare_image.compare_image(img_1, img_2)
#     if jieguo==0:
#         tk.messagebox.showinfo(title='出错了', message='检查图片路径')
#     else:
#         tk.messagebox.showinfo(title='对比结果', message='SSIM:%d' % (jieguo))
#         if  jieguo>0.8:
#             l.config(bg='green',text='ok')
#         else:
#             l.config( bg='red',  text='wrong')
# # login and sign up button
# btn_login = tk.Button(window, text='对比', command=contrast)
# btn_login.place(x=200, y=230)
#
# if __name__ == '__main__':
#     window.mainloop()