import tkinter as tk
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
canvas = tk.Canvas(window, height=200, width=500)
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
    imgend=zong(imgF,imgS)

    cv2.imshow('contrast', imgend)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def contrast():
    img_1 = img1.get()
    img_2 = img2.get()
    ssim1=s.get()
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