import cv2
import numpy as np

# 这里是onChange函数，这里没有用到
def nothing(x):
    pass

# 创建一个黑色背景，大小是300*512
img=np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# 创建颜色滑动条，设置其可用范围
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# 开关。本质仍是一个滑块，但是取值只有0,1两种
switch = '0 : OFF \n1 : ON\n'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # 获取滑块的参数
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r] # 将img的所有元素设置为指定的颜色[b,g,r]

cv2.destroyAllWindows()
