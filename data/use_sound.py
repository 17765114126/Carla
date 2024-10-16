import sounddevice as sd
import numpy as np
from pydub import AudioSegment
from simpleaudio import play_buffer
import io
# from vits.server import handle
from vits.inference_main import handle
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


def play_audio_from_stream(audio_stream):
    # 将字节流转换为 AudioSegment 对象
    audio = AudioSegment.from_file(io.BytesIO(audio_stream))

    # 获取音频数据
    raw_audio_data = audio.raw_data

    # 获取音频的采样率
    sample_rate = audio.frame_rate

    # 获取音频的通道数
    num_channels = audio.channels

    # 获取音频的位深度
    sample_width = audio.sample_width

    # 使用 simpleaudio 播放音频
    play_buffer(raw_audio_data, num_channels, sample_width, sample_rate)


def listen_for_audio(text):
    # 推理并获取字节流
    audio_stream = handle(text)
    # 直接播放字节流
    play_audio_from_stream(audio_stream.getvalue())


if __name__ == '__main__':
    listen_for_audio("天空是什么颜色呢,具体有几种呢？")
