

import cv2
import numpy as  np

__author__ = 'ypf'
__date__ = '2019/1/16,9:11'



def SaltAndPepper(img):
    coutn = 1000
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
    # cv2.namedWindow('img')
    # cv2.imshow('img', img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
cc=cv2.imread('1.jpg')
SaltAndPepper(cc)

