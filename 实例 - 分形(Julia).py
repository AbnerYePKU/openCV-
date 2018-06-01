import math,cv2,numpy as np

phi=(math.sqrt(5)+1)/2

# 复数类
class Complex:
    def __init__(self,x=0.0,y=0.0):
        self.re=x
        self.im=y
    def __add__(self, other):
        return Complex(self.re+other.re,self.im+other.im)
    def __mul__(self, other):
        return Complex(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)
    def __repr__(self):
        return "({},{})".format(self.re,self.im)
    def module(self):
        return self.re**2+self.im**2

# 图像规格
width=1200 # 宽
height=1200 # 高
max_interations=300 # 最大迭代次数
max_module=4 # 模长的阈值
X_max=1.6;X_min=-1.6;Y_max=1.6;Y_min=-1.6 # 坐标的范围

delta_X=(X_max-X_min)/width
delta_Y=(Y_max-Y_min)/height

img=np.zeros((height,width,1),dtype=np.uint8) # 初始化图形

def Color(iteration):
    if iteration==max_interations:
        return 0 # black
    else:
        return int(math.sqrt(iteration/max_interations)*255)

c_list=[Complex(1-phi),Complex(phi-2,phi-1),Complex(0.285,0.01),Complex(-0.70176,-0.3842),Complex(-0.8,0.156),Complex(-0.7269,0.1889)]

count=0
for c in c_list:
    # 绘制图像
    for col in np.arange(0,width):
        for row in np.arange(0,height):
            iteration=0 # 计算给定点的迭代次数
            z=Complex(X_min+col*delta_X,Y_min+row*delta_Y)
            while iteration < max_interations and z.module()<max_module:
                z=z*z+c # Julia 集合迭代
                iteration+=1
            if iteration >= max_interations:
                iteration=max_interations
            img[row,col]=Color(iteration)
    count+=1;print(count)
    cv2.imwrite('Julia{}.jpg'.format(count),img)
