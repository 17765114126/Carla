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