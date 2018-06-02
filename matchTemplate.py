import cv2,numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Mario.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template=cv2.imread('block.jpg',0)

Shape=template.shape
width,height=Shape[0],Shape[1]

match=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF) #匹配
threshold=match.max()*0.98 # 阈值
locations=np.where(match>=threshold) # 寻找匹配当中契合度大于阈值的地方

for pt in zip(*locations[::-1]):
    cv2.rectangle(img, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

cv2.imshow('win',img)
cv2.waitKey()

"""
在Mario的游戏图像中找到所有的问号方块。
"""
