import os
import numpy as np
import cv2
import utils

config = utils.read_config("data/opencv_config.json")

# 人脸识别
# 前面讲得是人脸检测，即检测出图片是否含有脸。接下来完成人脸识别，即识别出当前脸是谁。
# 数据集：选取人物网图各几张。

# 训练模型并保存
# 注意：如果出现module ‘cv2.cv2’ has no attribute ‘face’ 错误信息。
# 说明没有安装opencv-contrib-python 包，这是OpenCV外带模块，外带模块是测试性能不足，所以没有一起放在opencv包里。
# 解决方法：pip install opencv-contrib-python


# 脸部检测函数
def face_detect_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(config.data.xmlUrl)
    faces = face_detector.detectMultiScale(gray, 1.2, 6)
    # 如果未检测到面部，则返回原始图像
    if (len(faces) == 0):
        return None, None
    # 目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
    (x, y, w, h) = faces[0]
    # 返回图像的脸部部分
    return gray[y:y + w, x:x + h], faces[0]


def ReFileName(dirPath):
    """
    :param dirPath: 文件夹路径
    :return:
    """
    # 对目录下的文件进行遍历
    faces = []
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
            c = os.path.basename(file)
            name = dirPath + '\\' + c
            img = cv2.imread(name)
            # 检测脸部
            face, rect = face_detect_demo(img)
            # 我们忽略未检测到的脸部
            if face is not None:
                # 将脸添加到脸部列表并添加相应的标签
                faces.append(face)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    return faces


# 胡歌照读取
huge = ReFileName("D:\opt\hg")  # 调用函数
label_huge = np.array([0 for i in range(len(huge))])  # 标签处理

# 霍建华照读取
huojianhua = ReFileName("D:\opt\hjh")  # 调用函数
label_huojianhua = np.array([1 for i in range(len(huojianhua))])  # 标签处理

# 拼接并打乱数据特征和标签
x = np.concatenate((huge, huojianhua), axis=0)
y = np.concatenate((label_huge, label_huojianhua), axis=0)

index = [i for i in range(len(y))]  # test_data为测试数据
np.random.seed(1)
np.random.shuffle(index)  # 打乱索引
train_data = x[index]
train_label = y[index]

# 分类器
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_data, train_label)
# 保存训练数据
recognizer.write(config.data.xmlUrl)
