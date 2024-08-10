import face_recognition
import pickle


# 保存人脸数据
def save_train(inputName):
    # 从摄像头采集图像并检测人脸
    # cap = cv2.VideoCapture(0)
    while True:
        # ret, frame = cap.read()
        img_path = "D:\\opt\\hg\\x.jpg"
        frame = face_recognition.load_image_file(img_path)  # 加载图片
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if len(face_locations) > 0:
            break

        # 提示用户为每个人脸输入名称并保存人脸数据
    face_encodings = []
    face_names = []
    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        face_img = rgb_frame[top:bottom, left:right]
        face_encoding = face_recognition.face_encodings(face_img)
        name = inputName
        # name = input(f"Enter the name for face {i + 1}: ")
        face_encodings.append(face_encoding)
        face_names.append(name)

    # 将人脸数据和名称保存到文件中
    face_data = {"encodings": face_encodings, "names": face_names}
    with open('face_data.pkl', 'wb') as f:
        pickle.dump(face_data, f)
    print("--------------->保存人脸数据成功")


# 增量保存人脸数据
def increment_train(inputName):
    # 尝试加载已保存的人脸数据
    try:
        with open('face_data.pkl', 'rb') as f:
            face_data = pickle.load(f)
    except FileNotFoundError:
        face_data = {"encodings": [], "names": []}

        # 从摄像头采集图像并检测人脸
    # cap = cv2.VideoCapture(0)
    while True:
        # ret, frame = cap.read()
        img_path = "D:\opt\hjh\OIP-C.jpg"
        frame = face_recognition.load_image_file(img_path)  # 加载图片
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        if len(face_locations) > 0:
            break

            # 提示用户为每个人脸输入名称并保存人脸数据
    for i, face_location in enumerate(face_locations):
        top, right, bottom, left = face_location
        face_img = rgb_frame[top:bottom, left:right]
        face_encoding = face_recognition.face_encodings(face_img)[0]
        # name = input(f"Enter the name for face {i + 1}: ")
        name = inputName

        # 检查名称是否已经存在，如果存在则跳过
        if name in face_data["names"]:
            print(f"Name '{name}' already exists. Skipping...")
            continue

        face_data["encodings"].append(face_encoding)
        face_data["names"].append(name)

        # 将更新后的人脸数据保存到文件中
    with open('face_data.pkl', 'wb') as f:
        pickle.dump(face_data, f)
    print("--------------->增量保存人脸数据成功")


# 查询人脸数据名称是否已存在
def select_face(name):
    # 尝试加载已保存的人脸数据
    try:
        with open('face_data.pkl', 'rb') as f:
            face_data = pickle.load(f)
    except FileNotFoundError:
        face_data = {"encodings": [], "names": []}
    # 检查名称是否已经存在，如果存在则跳过
    if name in face_data["names"]:
        print(f"Name '{name}' 已存在...")
    else:
        print(f"Name '{name}' 不存在...")


# 删除已保存的人脸数据
def del_face(name_to_delete):
    # 加载已保存的人脸数据
    with open('face_data.pkl', 'rb') as f:
        face_data = pickle.load(f)

        # 删除指定名称的人脸数据
    # 要删除的人脸数据名称
    if name_to_delete in face_data["names"]:
        index = face_data["names"].index(name_to_delete)
        del face_data["encodings"][index]
        del face_data["names"][index]

        # 将更新后的人脸数据保存到文件中
    with open('face_data.pkl', 'wb') as f:
        pickle.dump(face_data, f)
    print("--------------->删除指定人脸数据成功")


if __name__ == '__main__':
    # 查询人脸数据名称是否已存在
    select_face("HuGe")
    # 保存人脸数据
    # save_train("HuGe")
    # 增量保存人脸数据
    # increment_train("Hjh")
    # 删除已保存的人脸数据
    # del_face("Hjh")