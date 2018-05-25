import cv2,numpy as np

img=cv2.imread('吃猫.jpg')
back=cv2.imread('花与女孩.jpg')
back_cut=back[0:400,0:400]
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 彩色图像变成灰白

# mask 选择灰度值高于252的部分(选取白色部分)
ret,mask=cv2.threshold(img_gray,252,255,cv2.THRESH_BINARY) # 指示背景部分
mask_inv=cv2.bitwise_not(mask) # 指示图片部分
part_1=cv2.bitwise_and(back_cut,back_cut,mask=mask) # 完成背景部分
part_2=cv2.bitwise_and(img,img,mask=mask_inv) # 完成图片部分
result_cut=part_1+part_2 # 图片组合
back[0:400,0:400]=result_cut # 图片替换
cv2.imwrite('组合.jpg',back)

"""
将一个图片的白色部分去掉，然后粘在另一个图片上。
"""
