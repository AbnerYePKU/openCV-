import cv2,numpy as np
from matplotlib import pyplot as plt

# 设置绘制字体和格式
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.figure(facecolor='#F6F8FA',dpi=600)

label_list=[r'$c=1-\varphi$',
            r'$c=\varphi-2+(\varphi-1)\mathrm{i}$',
            r'$c=0.285+0.01\mathrm{i}$',
            r'$c=-0.70176-0.3842\mathrm{i}$',
            r'$c=-0.8+0.156\mathrm{i}$',
            r'$c=-0.7269+0.1889\mathrm{i}$']

for i in range(1,7):
    img=cv2.imread('Julia/Julia{}.jpg'.format(i),0)
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8)) # CLAHE 直方图均衡算法
    output=clahe.apply(img)
    plt.subplot(2,3,i)
    plt.imshow(output,'gray')
    plt.xticks([]);plt.yticks([])
    plt.xlabel(label_list[i-1],fontsize=10)

plt.show()
