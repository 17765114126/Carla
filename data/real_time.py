import time
from util_tool import pyttsX
from data import use_sound, use_faster_whisper, ollama_api


def listen_for_audio():
    model_name = 'llama3.1'
    while True:
        # 语音唤醒
        audio_data = use_sound.recording(1)
        # 判断是否有人声
        if use_sound.is_speak(audio_data):
            recognized_text = use_faster_whisper.transcription(audio_data, "zh")
            print(recognized_text)
            # recognized_text = "小夕"
            # 检查是否识别到了关键词
            keywords = ["小C", "小夕", "小溪", "小西", "小希", "小心"]
            if any(keyword in recognized_text for keyword in keywords):
                recognized_text = ""
                # 生成音频并播放
                # pyttsX.speak("我在,你说")
                use_sound.listen_for_audio("我在,你说")
                # 开始对话模式
                # 语音转录文字调ollama
                conversation_start_time = time.time()
                while True:
                    audio_data = use_sound.recording(5)
                    # 判断是否有人声
                    if use_sound.is_speak(audio_data):
                        recognized_text = use_faster_whisper.transcription(audio_data, "zh")
                        print(recognized_text)
                        messages = [
                            {
                                'role': 'user',
                                'content': recognized_text
                            },
                        ]
                        # 调用API
                        ollama_txt = ollama_api.ollama_chat(model_name, messages)
                        print(ollama_txt)
                        # pyttsX.speak(ollama_txt)
                        use_sound.listen_for_audio(ollama_txt)
                        # 重置计时器
                        conversation_start_time = time.time()
                    elif time.time() - conversation_start_time >= 180:
                        # 如果三分钟内没有声音，则退出对话模式
                        break
                    else:
                        # 如果没有人声，等待一小段时间后再次尝试录音
                        time.sleep(0.3)
                # 如果三分钟内没有声音，则重新开始语音唤醒无限循环
                continue


# 实时对话
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
