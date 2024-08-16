import sounddevice as sd
import numpy as np
from playsound import playsound
from io import BytesIO
import requests

# 麦克风录音参数
SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 1  # 持续时间


def recording(duration):
    """
    录音
    """
    # duration 持续时间
    record = sd.rec(int(SAMPLE_RATE * duration), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32')
    sd.wait()  # 等待录音完成

    # 转换为numpy数组
    audio_data = np.frombuffer(record, dtype=np.float32).flatten()
    return audio_data


def is_speak(audio_data):
    """
    判断录音中是否有人说话
    """
    # 计算音频信号的绝对值
    abs_audio_data = np.abs(audio_data)

    # 计算平均振幅
    average_amplitude = np.mean(abs_audio_data)

    # 设定阈值
    threshold = 0.05  # 需要根据实际情况调整

    # 判断是否有人说话
    if average_amplitude > threshold:
        print("录音中有说话的声音")
        return True
    else:
        print("录音中没有人说话")
        return False


def listen_for_audio(text):
    # 定义请求的 URL
    url = "http://127.0.0.1:5577"

    # 定义请求的数据
    data = {
        "text": text
    }
    response = requests.post(url, json=data)
    # 检查响应是否成功
    if response.status_code == 200:
        # 将响应的内容转换为字节流
        audio_stream = BytesIO(response.content)

        # 保存音频到文件
        with open('audio.wav', 'wb') as audio_file:
            audio_file.write(audio_stream.getvalue())

        # 使用 playsound 播放音频文件
        playsound('audio.wav')


if __name__ == '__main__':
    listen_for_audio()
