import cv2 as cv
import numpy as np
import os
import random
import tensorflow as tf
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# 加载数据集
def load_dataset(dataset_path):
    images = []
    labels = []

    for folder in os.listdir(dataset_path):
        if not folder.startswith('.'):
            label = int(folder.split('_')[0])
            folder_path = os.path.join(dataset_path, folder)
            for file in os.listdir(folder_path):
                if file.endswith('.jpg'):
                    file_path = os.path.join(folder_path, file)
                    image = cv.imread(file_path)
                    image = cv.resize(image, (128, 128))
                    images.append(image)
                    labels.append(label)

    return np.array(images), np.array(labels)

# 数据预处理
def preprocess_data(images, labels):
    images = images.astype('float32') / 255.0
    labels = tf.keras.utils.to_categorical(labels, num_classes=len(set(labels)))
    return images, labels

# 创建模型
def create_model(input_shape, num_classes):
    model = Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# 训练模型
def train_model(model, X_train, y_train, epochs=20, batch_size=32):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)


# 保存模型
def save_model(model, file_name):
    model.save(file_name)


# 加载数据集
dataset_path = "D:\opt\hg"
X, y = load_dataset(dataset_path)

# 数据预处理
X, y = preprocess_data(X, y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建模型
input_shape = (128, 128, 3)
num_classes = len(set(y))
model = create_model(input_shape, num_classes)

# 训练模型
train_model(model, X_train, y_train)

# 保存模型
save_model(model, "face_recognition_model.h5")