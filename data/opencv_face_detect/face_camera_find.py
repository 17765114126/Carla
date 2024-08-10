import cv2 as cv
import utils

config = utils.read_config("data/opencv_config.json")


# 2： 摄像头下人脸检测实现
def face_detect_demo(image):
    # 输入的彩色图像image转换为灰度图像gray
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # 创建一个人脸检测器对象face_detector，使用OpenCV预训练的人脸检测模型。
    face_detector = cv.CascadeClassifier(config.data.xmlUrl)
    # 使用人脸检测器对象face_detector在灰度图像gray中检测人脸，返回一个包含人脸位置信息的列表faces。
    faces = face_detector.detectMultiScale(gray, 1.2, 6)
    for x, y, w, h in faces:
        # 在原始图像image上绘制一个红色矩形框，表示检测到的人脸。
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)


print("--------- Python OpenCV Tutorial ---------")

# 创建一个视频捕获对象capture，用于从摄像头获取视频。
capture = cv.VideoCapture(0)
# 创建一个名为"result"的窗口，并设置其大小为自动调整
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
while (True):
    # 从视频捕获对象capture中读取一帧图像，并将其存储在frame中
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)  # 将读取到的图像左右翻转。
    face_detect_demo(frame)
    # ESC键退出
    c = cv.waitKey(10)
    if c == 27:  # ESC
        break
cv.waitKey(0)
cv.destroyAllWindows()

# 同理：调整 face_detector.detectMultiScale(gray, 1.2, 6) 的参数值，效果不一样。
