import speech_recognition as sr
print(sr.__version__)
# 创建语音识别器对象
r = sr.Recognizer()

# 读取词库，将词库中的词语转换为小写字母
word_list = ['北京', '四川']
word_list = [word.lower() for word in word_list]

# 选择使用系统默认的麦克风
with sr.Microphone() as source:
    print("请开始说话：")
    # 麦克风录入语音，使用语音识别器进行语音转文本
    audio = r.listen(source)

try:
    # 使用语音识别器识别语音并转换为文本
    text = r.recognize_google(audio, language='zh-CN')
    text = text.lower()
    # 输出转换后的文本
    print("你说的是：" + text)

    # 匹配词库，输出匹配结果
    for word in word_list:
        if word in text:
            print("匹配成功，识别结果为：" + word)
            break
    else:
        print("没有匹配到任何结果")
except sr.UnknownValueError:
    print("无法识别语音")
except sr.RequestError as e:
    print("请求失败：{0}".format(e))