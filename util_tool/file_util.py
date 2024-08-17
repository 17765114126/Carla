import os
import subprocess
import base64


# 打开文件夹
def open_folder():
    # 获取当前脚本所在的文件夹路径
    # current_folder = os.path.dirname(os.path.abspath(__file__))
    # Windows系统中"C盘/下载"文件夹的通用路径
    download_path = os.path.join('C:\\Users', os.getlogin(), 'Downloads')
    subprocess.run(['explorer', download_path])


def check_folder(target_file):
    # 分离文件路径和文件名
    folder_path, _ = os.path.split(target_file)
    # 检查文件夹是否存在,不存在返回False
    if not os.path.exists(folder_path):
        return False
    # 检查目标文件是否存在,不存在返回False
    if not os.path.exists(target_file):
        return False
    return True


def images_to_base64(image_paths):
    """
    转换为 base64 编码并存储在一个数组中

    image_paths 示例: ["path/to/your/image1.jpg", "path/to/your/image2.jpg"]
    """
    # 创建一个空列表来存储 base64 编码的图片
    base64_images = []
    for image_path in image_paths:
        # 读取图片文件
        with open(image_path, "rb") as image_file:
            # 读取图片的二进制内容
            binary_data = image_file.read()
            # 使用 base64 编码
            base64_encoded = base64.b64encode(binary_data)
            # 解码为字符串
            base64_string = base64_encoded.decode('utf-8')
            # 添加到列表中
            base64_images.append(base64_string)
    return base64_images


# 保存转录结果为SRT文件
def out_srt_file(segments, output_srt_file):
    with open(output_srt_file, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            start_time = segment['start']
            end_time = segment['end']
            start_str = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
            end_str = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"
            subtitle_text = segment["text"].strip()
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_str} --> {end_str}\n")
            srt_file.write(f"{subtitle_text}\n\n")


# 将segments转换为SRT格式
def segments_to_srt(segments, output_srt_file):
    with open(output_srt_file, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(segments, start=1):
            start_time = segment.start
            end_time = segment.end
            start_str = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
            end_str = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"
            subtitle_text = segment.text.strip()
            srt_file.write(f"{i}\n")
            srt_file.write(f"{start_str} --> {end_str}\n")
            srt_file.write(f"{subtitle_text}\n\n")
