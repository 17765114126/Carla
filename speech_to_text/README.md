# Speech-to-Text Converter

This Python script converts the Speech input into Text using NLP (Natural Langauge Processing).

### Requirements

**Installation Required** :

* Python Speech Recognition module:

    `pip install speechrecognition`

* PyAudio:
  * Use the following command for linux users

    `sudo apt-get install python3-pyaudio`

  * Windows users can install pyaudio by executing the following command in a terminal

    `pip install pyaudio`

* Python pyttsx3 module:

    `pip install pyttsx3`

### How to run the script

-   Enter the audio input by speaking into the microphone.
-   Run converter_terminal.py script
-   Output Text will be displayed

## pyaudio安装失败的解决方法

Windows在 安装pyaudio-0.2.11时报错，显示有文件未安装，在linux下可以安装portaudio解决，但是windows下未找到安装方式，遂用其他办法解决

python3.7版本不支持pip安装pyaudio
解决方法：
方法一 下载pyaudio的whl文件，然后使用pip进行安装，具体步骤如下
1.下载pyaudio
whl下载地址：https://github.com/intxcc/pyaudio_portaudio/releases
2.进入文件所在目录进行安装
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
3. 检验安装的情况


## *Author Name*
<!--Remove the below lines and add yours -->
[Paulo Henrique](https://github.com/chavarera/python-mini-projects
