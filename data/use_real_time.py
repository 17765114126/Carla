import sounddevice as sd
import numpy as np
import threading
import time
from faster_whisper import WhisperModel
import os
from util import pyttsX
import ollama_api

# 麦克风录音参数
SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 1  # 持续时间
model_path = "C:\\Users\\1\\.cache\\modelscope\\hub\\pengzhendong\\faster-whisper" + "-small"

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Faster Whisper 模型初始化
model = WhisperModel(model_path, device="cpu", compute_type="int8")


def recording(duration):
    # duration 持续时间
    # 录音
    record = sd.rec(int(SAMPLE_RATE * duration), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='float32')
    sd.wait()  # 等待录音完成

    # 转换为numpy数组
    audio_data = np.frombuffer(record, dtype=np.float32).flatten()
    return audio_data


def speak(audio_data):
    # 判断录音中是否有人说话

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


def transcription(audio_data, language_type):
    recognized_text = ""
    # 语音识别
    segments, info = model.transcribe(audio_data, beam_size=5, language=language_type)
    # 识别结果
    for segment in segments:
        recognized_text += segment.text + " "
    return recognized_text


def listen_for_audio():
    model_name = 'llama3.1'
    while True:
        # 语音唤醒
        audio_data = recording(1)
        # 判断是否有人声
        if (speak(audio_data)):
            recognized_text = transcription(audio_data, "zh")
            print(recognized_text)
            # 检查是否识别到了关键词
            keywords = ["小C", "小夕", "小溪", "小西", "小希", "小心"]
            if any(keyword in recognized_text for keyword in keywords):
                recognized_text = ""
                # 生成音频并播放
                pyttsX.speak("我在,你说")
                # 开始对话模式
                # 语音转录文字调ollama
                conversation_start_time = time.time()
                while time.time() - conversation_start_time < 180:  # 3 分钟
                    audio_data = recording(5)
                    # 判断是否有人声
                    if speak(audio_data):
                        recognized_text = transcription(audio_data, "zh")
                        print(recognized_text)
                        # 调用API
                        ollama_txt = ollama_api.ollama_chat(model_name, recognized_text)
                        print(ollama_txt)
                        pyttsX.speak(ollama_txt)
                    else:
                        # 如果没有人声，等待一小段时间后再次尝试录音
                        time.sleep(0.3)
                # 如果三分钟内没有声音，则重新开始语音唤醒无限循环
                continue


def main():
    # 启动监听线程
    # thread = threading.Thread(target=listen_for_audio)
    # thread.start()
    # # 等待监听线程完成
    # thread.join()
    listen_for_audio()
    try:
        while True:
            time.sleep(0.1)  # 减少CPU占用
    except KeyboardInterrupt:
        print("Exiting...")


if __name__ == "__main__":
    main()
