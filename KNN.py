import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

## 预备工作：随机分组

# 建立25个随机(x,y)序列(范围是 0,100)
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

# 随机分类，红色是0，蓝色是1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

# 打印红色三角形
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

# 打印蓝色正方形
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

## KNN: 分类
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv.ml.KNearest_create() # 建立KNN问题
knn.train(trainData, cv.ml.ROW_SAMPLE, responses) # 设置训练数据
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3) # 选择K，然后根据neighbor进行分类

print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )
plt.show()

"""
红色三角形和蓝色正方形的分类
"""
