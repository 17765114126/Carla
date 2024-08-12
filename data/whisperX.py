import whisper
import pyaudio
import wave
import numpy as np
import librosa

# Whipser 推出了 tiny、base、small、medium、large 5 个档次的模型。转录效果依次增加，但相应花费的时间也会增加。

# ### 模型文件位置：Windows：C:\Users\<你的用户名>\.cache\whisper

# Whisper 使用了 Python 开发，安装后，在文件所在目录打开终端，运行 whisper audio.mp3 即可进行转录。

# 想要自定义设置的话，则可以在后面追加命令参数，具体包括：

# whisper audio.mp3 --命令参数

# --task
#
# 指定转录方式，默认使用 --task transcribe 转录模式，--task translate 则为翻译模式，目前只支持英文。
#
# --model
#
# 指定使用模型，默认使用 --model small，Whisper 还有英文专用模型，就是在名称后加上 .en，这样速度更快。
#
# --language
#
# 指定转录语言，默认会截取 30 秒来判断语种，但最好指定为某种语言，比如指定中文是 --language Chinese。
#
# --device
#
# 指定硬件加速，默认使用 auto 自动选择，--device cuda 则为显卡，cpu 就是 CPU， mps 为苹果 M1 芯片。
# 加载模型
model = whisper.load_model("small")
# mp3Url = "audio (4).wav"
mp3Url = "G:\\Install_package\\python_source\\GPT-SoVITS\\adam.godigital\\2\\output_1.mp3"

# 设置音频参数
FORMAT = pyaudio.paInt16  # 16-bit PCM
CHANNELS = 1  # 单声道
# RATE = 44100 # 采样率，这里是44.1kHz
RATE = 16000
CHUNK = 1024  # 数据块大小
RECORD_SECONDS = 5  # 录制5秒

# 初始化pyaudio
audio = pyaudio.PyAudio()


# 音频转文字
def file_to_text(mp3Url):
    # result = model.transcribe(mp3Url, language="Chinese")
    result = model.transcribe(mp3Url)

    print(", ".join([i["text"] for i in result["segments"] if i is not None]))


if __name__ == '__main__':
    mp3Url = "G:\\JJ\\3\\output_1.mp3"

    file_to_text(mp3Url)
    # real_time()

# if __name__ == '__main__':
#     file_to_text()
THRESHOLD = 0.1  # 自定义的特征能量阈值


# 音频数据处理
def audio_data_dispose(audio_data):
    # 将音频数据转换为NumPy数组
    audio_samples = np.frombuffer(b''.join(audio_data), dtype=np.int16)

    # 将音频数据转换为浮点数
    audio_data_float = librosa.util.buf_to_float(audio_samples, n_bytes=2, dtype=np.float32)

    # # 降噪
    audio_data_denoised = librosa.effects.remix(audio_data_float,
                                                intervals=librosa.effects.split(audio_data_float, top_db=20))

    # # Librosa部分：特征提取与判断
    # y = audio_samples / 32768.0  # 将int16数据归一化至-1~1之间
    # mfcc = librosa.feature.mfcc(y=y, sr=RATE)
    #
    # # 简单的能量阈值判断（实际VAD会更复杂）
    # energy = np.mean(np.abs(mfcc).flatten())  # 可以选择其他特征能量衡量方式
    # if energy > THRESHOLD:
    #     print("可能有人声")
    # else:
    #     print("可能无人声或主要是噪音")

    # 如果没有检测到人声，返回空数组
    # if len(voice_segments) == 0:
    #     voice_segments = np.array([], dtype=int)

    # 将降噪后的音频数据转换回整数
    audio_data_denoised_int = np.round(audio_data_denoised * 32767).astype(np.int16)
    return audio_data_denoised_int


def save_file(audio_data):
    # 音频数据处理
    audio_data_denoised_int = audio_data_dispose(audio_data)
    # 保存录制的音频数据
    with wave.open("output.wav", "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(audio_data_denoised_int.tobytes())


# 录制音频5秒（一次性）
def record_audio(stream):
    # 初始化音频数据列表
    audio_data = []
    print("开始录制--------------------")
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        audio_data.append(data)
    print("结束录制--------------------")
    # 音频保存为wav文件
    save_file(audio_data)
    # 音频文件转文字
    file_to_text()


# 录制音频每5秒转换文字一次
def for_record_audio(stream):
    while True:
        # 初始化音频数据列表
        audio_data = []
        print("5秒开始录制--------------------")
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            audio_data.append(data)
        print("5秒结束录制--------------------")
        # 音频保存为wav文件
        save_file(audio_data)
        # 音频文件转文字
        file_to_text()


def real_time():
    # 打开音频流
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    # 录制音频转化文字
    record_audio(stream)
    # 录制音频转化文字每5秒
    # for_record_audio(stream)
    # 关闭音频流
    stream.stop_stream()
    stream.close()
    # 关闭pyaudio
    audio.terminate()


def to_text1():
    # load audio and pad/trim it to fit 30 seconds
    # 载入音频并填充/修剪以适应 30 秒
    audio = whisper.load_audio(mp3Url)
    audio = whisper.pad_or_trim(audio)
    # make log-Mel spectrogram and move to the same device as the model
    # log-Mel光谱图,并移动到与模型相同的设备
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    # 检测语言
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")
    lang = max(probs, key=probs.get)
    # decode the audio
    # 解码音频
    options = whisper.DecodingOptions(beam_size=5)
    result1 = whisper.decode(model, mel, options)

    print(result1.text)
    # return lang, result.text
