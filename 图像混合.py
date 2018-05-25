import cv2,numpy as np

black=np.zeros((400,400,3),np.uint8) # 纯黑
img=cv2.imread('吃猫.jpg') # 导入图像
cv2.namedWindow('merge')

cv2.createTrackbar('black level','merge',0,100,lambda x:None)
cv2.imshow('merge',img)

while 1:
    k=cv2.waitKey(1) & 0xFF
    if k==27: break
    # 获取黑色值 rate
    rate=cv2.getTrackbarPos('black level','merge')/100
    # 按比例合成图像
    merge=cv2.addWeighted(black,rate,img,1-rate,0)
    # 把合成图像显示出来
    cv2.imshow('merge',merge)
    cv2.waitKey(10)

"""
这个程序设置了一个控制"黑色"程度的滑动条。以滑动条的数值为比例合成两个图像。
"""
