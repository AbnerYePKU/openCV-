import cv2
import numpy as np

global radius
radius=80

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global radius
    if event == cv2.EVENT_MOUSEMOVE or cv2.EVENT_LBUTTONDOWN:
        if event==cv2.EVENT_LBUTTONDOWN:radius=80
        cv2.circle(img,(x,y),radius,(255,255,0),3)
        radius=int(radius*0.99)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()