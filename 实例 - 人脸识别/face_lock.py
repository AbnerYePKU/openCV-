import cv2,requests,json
import numpy as np

# 获取人脸分类器
faceCascade = cv2.CascadeClassifier('/Users/abneryepku/Desktop/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml') # xml文件的地址

# 我的密钥
API_KEY = 'jjX9vUdUJf69_3G843d5BjMU8srKbCzG'
API_SECRET = '2PxJdklBAm_Lze8JOtE2PHkqDmXr3lnu'
data={"api_key": API_KEY, "api_secret": API_SECRET,"return_landmark":"1"}
BASE_URL = 'https://api-cn.faceplusplus.com/facepp/v3/'

### 人脸区域检测
def detect_face(path):
    count=0 # 已经捕获到的图像的数量
    # 打开电脑上的摄像头
    capInput=cv2.VideoCapture(0)
    if not capInput.isOpened(): print('无法打开您的摄像头')

    while count==0:
        ret,img=capInput.read() # 截图
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 转化为灰度值
        width,height=gray.shape[1],gray.shape[0]
        faces=faceCascade.detectMultiScale(gray,1.3,5) # 获取脸部信息
        if len(faces): # 在摄像头中捕获到类图像信息
            for x,y,w,h in faces:
                count=1
                cv2.imwrite(path,img[max(y-20,0):min(y+h+20,height),max(x-20,0):min(x+w+20,width)]) # 写入脸部图像
                break

    capInput.release() # 结束摄像
    cv2.destroyAllWindows()

### 向 face++ 发送数据，然后将信息存储在 face.json 当中
def upload_img(path):
    URL=BASE_URL+'detect' # 探测
    # 使用Requests上传图片
    files = {"image_file":open(path,"rb")}
    r = requests.post(URL,data=data,files = files)
    # 如果读取到图片中的头像则输出他们，其中的'face_id'就是我们所需要的值
    faces = r.json() # faces 是存储面部信息的 dict
    wfile=open('face.json','w',encoding='utf-8')
    json.dump(faces,wfile)
    wfile.close()

### 比较图像的相似度，返回相似的可信度(confidence)
def compare_img(path1,path2):
    URL=BASE_URL+'compare' # 比较
    files={"image_file1":open(path1,"rb"),"image_file2":open(path2,"rb")}
    r=requests.post(URL,data=data,files=files)
    faces=r.json()
    confidence=faces.get('confidence')
    wfile=open('compare.json','w',encoding='utf-8')
    json.dump(faces,wfile)
    wfile.close()
    return confidence

### 获取 faceID
def get_face():
    detect_face('faceID.jpg')
    print("faceID 已经录入成功！")

### 验证 faceID
def verify_face():
    detect_face('face1.jpg')  # 从摄像头读入头像，然后存储为 face1.jpg
    confidence=compare_img('faceID.jpg','face1.jpg') # 匹配可信度
    if confidence and confidence>75:
        print("认证成功！")
    else:
        print("认证失败！")
