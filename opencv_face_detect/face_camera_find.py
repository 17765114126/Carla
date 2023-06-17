import cv2 as cv
import utils

config = utils.read_config("data/opencv_config.json")


# 2： 摄像头下人脸检测实现
def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier(config.data.xmlUrl)
    faces = face_detector.detectMultiScale(gray, 1.2, 6)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)


print("--------- Python OpenCV Tutorial ---------")

capture = cv.VideoCapture(0)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
while (True):
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)  # 左右翻转
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27:  # ESC
        break
cv.waitKey(0)
cv.destroyAllWindows()

# 同理：调整 face_detector.detectMultiScale(gray, 1.2, 6) 的参数值，效果不一样。
