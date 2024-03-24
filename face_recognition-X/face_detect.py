import face_recognition
import pickle
import cv2

# 加载已保存的人脸数据
with open('face_data.pkl', 'rb') as f:
    face_data = pickle.load(f)

# 从摄像头采集图像并检测人脸
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # frame = face_recognition.load_image_file("D:\\opt\\hg\\y.jpg")  # 加载图片
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    if len(face_locations) > 0:
        break

    # 对检测到的人脸进行识别
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_img = rgb_frame[top:bottom, left:right]
    face_encoding = face_recognition.face_encodings(face_img)[0]
    matches = face_recognition.compare_faces(face_data["encodings"], face_encoding)
    name = "Unknown"
    if True in matches:
        match_index = matches.index(True)
        name = face_data["names"][match_index]
        print("识别到图片中人物为："+name)
    cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

# 显示识别结果并等待用户按下 'q' 键退出程序
while True:
    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cap.release()
cv2.destroyAllWindows()