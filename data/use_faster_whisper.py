from faster_whisper import WhisperModel
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Faster Whisper 模型初始化
model = WhisperModel("small", device="cpu", compute_type="int8")


def transcription(audio_data, language_type):
    """
    faster_whisper 语音识别
    """
    recognized_text = ""
    segments, info = model.transcribe(audio_data, beam_size=5, language=language_type)
    # 识别结果
    for segment in segments:
        recognized_text += segment.text + " "
    return recognized_text
