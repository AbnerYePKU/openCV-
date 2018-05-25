import cv2
import numpy as np

global radius # 全局变量radius设置为圆的半径
radius=80

# 鼠标点击时的回调函数
def draw_circle(event,x,y,flags,param):
    global radius
    if event == cv2.EVENT_MOUSEMOVE or cv2.EVENT_LBUTTONDOWN:
        if event==cv2.EVENT_LBUTTONDOWN:radius=80
        cv2.circle(img,(x,y),radius,(0,0,200),3)
        radius=int(radius*0.99)

# 建立例程运行窗口，以及其中回调函数的设置
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

# 设定循环的时间间隔
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

"""
鼠标移动时，将在窗口中画出一族半径逐渐减小的圆。点击时半径radius恢复为80。
"""
