import speech_recognition as sr

print(sr.__version__)


# 文件语音识别
def audio_voice(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    print(type(audio))
    output = r.recognize_sphinx(audio, language='zh-cn')

    print(output)
    with open(r'sound2Txt.txt', 'w') as f:
        f.write(output)
# https://www.cnblogs.com/zhe-hello/p/13273523.html
# https://blog.csdn.net/Zbreakzhong/article/details/109127837
# 参考：https://blog.csdn.net/qq_41891021/article/details/90737715

# pip install SpeechRecognition -i https://mirror.baidu.com/pypi/simple
# pip install PocketSphinx -i https://mirror.baidu.com/pypi/simple
# 要下wheel（和python版本及系统对应，兼容性肯定差）：https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx
# 进入.whl所在的文件夹，执行以下代码（pip install）
# pip install C:\AH_TOOLS\AH_PythonCode\Detect_Silence\sound2txt\pocketsphinx-0.1.15-cp38-cp38-win_amd64.whl
# 要下普通话包：https://sourceforge.net/projects/cmusphinx/files/Acoustic and Language Models/Mandarin/


# 音频语音识别
def record_voice():
    r = sr.Recognizer()

    with sr.Microphone() as live_phone:
        r.adjust_for_ambient_noise(live_phone)

        print("I'm trying to hear you: ")
        audio = r.listen(live_phone)

        # 这里尝试一下降噪或许可以优化一下

        try:
            output = r.recognize_sphinx(audio, language='zh-cn')
            with open('sound2Txt.txt', 'w') as file:
                file.write(output)
            print('the last sentence you spoke was saved in sound2Txt.txt')
            return output
        except sr.UnknownValueError:
            return "I didn't understand what you said"


if __name__ == '__main__':
    # audio_voice("D:\aupi\out.wav")
    record_voice()


