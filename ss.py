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