import speech

"""
speech

也是一款强大的语音模块，依赖于pywin32，而且它最适合做语音启动程序了。

"""


def speak(audioString):
    # 生成音频
    speech.say(audioString)


if __name__ == '__main__':
    speak("Hello World")
