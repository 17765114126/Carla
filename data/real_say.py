import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from data import use_faster_whisper, ollama_api
from util_tool import pyttsX

# 定义全局变量来存储录音数据
audio_data = []
is_recording = False
samplerate = 44100  # 采样率
stream = None  # 用于存储录音流


def start_recording():
    global is_recording, audio_data, stream
    is_recording = True
    audio_data = []  # 清空之前的录音数据
    print("开始录音...")

    def callback(indata, frames, time, status):
        if is_recording:
            audio_data.append(indata.copy())
            # print(f"录音数据长度: {len(indata)}")

    # 启动录音流
    stream = sd.InputStream(samplerate=samplerate, channels=1, callback=callback)
    stream.start()


def stop_recording_and_process():
    global is_recording, stream
    if not is_recording:
        return "请先开始录音！"

    is_recording = False
    print("停止录音.")

    # 确认是否有音频数据
    if not audio_data:
        return "没有录制到任何音频数据。"

    # 将累积的数据转换为NumPy数组
    recorded_audio = np.concatenate(audio_data, axis=0)

    # 保存录音文件
    filename = "recorded_audio.wav"
    write(filename, samplerate, (recorded_audio * 32767).astype(np.int16))  # 转换为int16

    # 调用语音识别服务
    recognized_text = use_faster_whisper.transcription(filename, "zh")
    print(f"识别的文字: {recognized_text}")

    model_name = 'llama3.1'
    messages = [{'role': 'user', 'content': recognized_text}]
    response = ollama_api.ollama_chat(model_name, messages)
    print(f"模型回复: {response}")

    # 关闭录音流
    if stream:
        stream.stop()
        stream.close()
    pyttsX.speak(response)
    return f"你说: {recognized_text}\n回复: {response}"
