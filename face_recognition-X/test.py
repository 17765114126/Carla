import face_recognition
import cv2  # opencv读取图像的格式BGR（图像的格式RGB）
import numpy as np


# 提取图像中所有人脸
def facePosition():
    img_path = "D:\Testspace\carla\opencv_face_detect\img\me.jpg"
    img = face_recognition.load_image_file(img_path)  # 加载图片
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR转换为RGB
    face_locations = face_recognition.face_locations(img)  # 提取人脸位置
    print("I found {} face(s) in this photograph.".format(len(face_locations)))  # 打印图像中的人脸数
    #######################################################
    # 提取图像中所有人脸
    for face_location in face_locations:
        top, right, bottom, left = face_location
        start = (left, top)
        end = (right, bottom)
        cv2.rectangle(img, start, end, color=(255, 255, 255), thickness=3)
    #######################################################
    # 显示识别结果
    cv2.namedWindow("face_recognition")
    cv2.imshow("face_recognition", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 人脸检测与识别
def faceSpot():
    # （1）自定义已知面孔及标签
    video_capture = cv2.VideoCapture(0)  # cv2.VideoCapture可以捕获摄像头，用数字来控制不同的设备

    obama_image = face_recognition.load_image_file("D:\opt\me.jpg")  # 自定义已知面孔1
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    biden_image = face_recognition.load_image_file("D:\\opt\hjh\\th.jpg")  # 自定义已知面孔2
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    known_face_encodings = [obama_face_encoding, biden_face_encoding]  # 创建已知人脸编码（数组）
    known_face_names = ["zf", "hjh"]  # 创建已知人脸的名称（数组）
    #########################################################
    # 参数初始化
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        #########################################################
        # 人脸检测与识别（匹配两张面孔的距离）
        ret, frame = video_capture.read()  # 循环读取视频的每一帧（图像）
        if process_this_frame:  # 为了节省时间，每隔一帧视频就处理一次
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 调整视频帧的大小为1/4大小，以更快的人脸识别处理
            rgb_small_frame = small_frame[:, :, ::-1]  # 将图像从BGR颜色(OpenCV使用)转换为RGB颜色(face_recognition使用)
            face_locations = face_recognition.face_locations(rgb_small_frame)  # 查找当前视频帧中的所有人脸位置
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # 查找当前视频帧中的所有人脸编码

            face_names = []
            for face_encoding in face_encodings:
                name = "Unknown"  # 若新面孔与已知面孔不同，则显示“ 未知”
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  # 看这张脸是否与已知的脸匹配
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)  # 计算与新面孔与已知面孔的距离
                best_match_index = np.argmin(face_distances)  # 计算与新面孔与已知面孔的最小距离
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
        process_this_frame = not process_this_frame  # 为了节省时间，每隔一帧视频就处理一次
        #########################################################
        # 框出人脸并显示标签
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # 由于我们检测到的帧被缩放到1/4大小，所以将面位置缩小
            top *= 4;
            right *= 4;
            bottom *= 4;
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # 在脸周围画一个方框
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)  # 在脸下方画一个有名字的标签
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # 27 表示退出键（Esc）
            break
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    faceSpot()
    # facePosition()