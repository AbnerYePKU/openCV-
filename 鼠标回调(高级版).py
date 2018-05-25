import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

drawing = False # 判断是否正在作图
mode = True # 是否正在绘制矩形。点击'm'切换模式
ix,iy = -1,-1

# 鼠标-回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    # 1. 鼠标按下，开始绘制(set drawing to True)
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    # 2. 鼠标移动，作图
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == False:
                cv2.circle(img,(x,y),2,(0,0,255),-1)

    # 3. 鼠标按起，结束绘制
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            cv2.circle(img,(x,y),2,(0,0,255),-1)

cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode # 切换模式
    elif k == 27:
        break

cv2.destroyAllWindows()
