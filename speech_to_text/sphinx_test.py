import speech_recognition as sr

print(sr.__version__)

r = sr.Recognizer()
with sr.AudioFile(r"D:\aupi\out.wav") as source:
    audio = r.record(source)
print(type(audio))
output = r.recognize_sphinx(audio)
print(output)
with open(r'sound2Txt.txt', 'w') as f:
    f.write(output)

# https://blog.csdn.net/Zbreakzhong/article/details/109127837

#参考：https://blog.csdn.net/qq_41891021/article/details/90737715

# pip install SpeechRecognition -i https://mirror.baidu.com/pypi/simple
# pip install PocketSphinx -i https://mirror.baidu.com/pypi/simple
# 要下wheel（和python版本及系统对应，兼容性肯定差）：https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx
# 进入.whl所在的文件夹，执行以下代码（pip install）
# pip install C:\AH_TOOLS\AH_PythonCode\Detect_Silence\sound2txt\pocketsphinx-0.1.15-cp38-cp38-win_amd64.whl
# 要下普通话包：https://sourceforge.net/projects/cmusphinx/files/Acoustic and Language Models/Mandarin/