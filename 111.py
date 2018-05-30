import cv2
import numpy as np

nThresh = 100
nMaxThresh = 255

img = cv2.imread('star_and_square.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # 转化为黑白
gray=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)[1] # 阈值调节
gray = cv2.blur(gray, (3,3)) # 模糊处理，舍弃图像的过多细节
cv2.namedWindow('img', cv2.WINDOW_NORMAL) # 使得窗口的大小可调节
cv2.imshow('img', img) # 原图

cannyImg = cv2.Canny(gray, nThresh, nThresh*2, 3) # 获取图像边缘(canny)
_, contours, hierarchy = cv2.findContours(cannyImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 得到的contours是许多contour的序列

# mu是每一段contour的moment(矩)字典
mu = []
mc = []
retval = np.array([])
for i in range(0, np.array(contours).shape[0]):
    retval = cv2.moments(contours[i], False) # 获取矩
    mu.append(retval)
mu = np.array(mu)

thetas = []
for i in range(0, np.array(contours).shape[0]):
    if mu[i]['m00'] == 0.0:
        a=0
        b=0
    else:
        a = mu[i]['m10'] / mu[i]['m00']  #质心x坐标
        b = mu[i]['m01'] / mu[i]['m00']  #质心y坐标

        #根据二阶矩计算物体形状的方向
        r1 = mu[i]['m20'] / mu[i]['m00'] - a*a
        r2 = 2.0*(mu[i]['m11'] / mu[i]['m00'] - a*b)
        r3 = mu[i]['m02'] / mu[i]['m00'] - b*b

        if r1-r3==0:
            theta = np.pi / 2
        else:
            theta = np.arctan(r2/(r1-r3)) / 2
        thetas.append(theta)
    mc.append([a,b]) # mc为质心list
mc = np.array(mc)
drawing = np.zeros(img.shape, dtype = np.uint8)
for i in range(0, mc.shape[0]):
    c1 = np.random.randint(0, 256)
    c2 = np.random.randint(0, 256)
    c3 = np.random.randint(0, 256)
    cv2.drawContours(drawing, contours, i, (c1, c2, c3), 2, 8)
    cv2.circle(drawing, (int(round(mc[i][0])), int(round(mc[i][1]))), 4, (c1, c2, c3), -1, 8, 0)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.imshow('img2', drawing)
cv2.waitKey(0)

"""
这个程序能够获取每一个几何图形的轮廓，然后求出这些几何图形的重心。
主要利用了findContours和drawContours函数。
这些函数能够找出并绘制图形的轮廓。moments函数帮助对每一个轮廓求出它的重心。
"""