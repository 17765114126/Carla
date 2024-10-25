# 支持的视频格式
video_type = ["mp4", "avi", "flv", "mkv", "mpeg"]
# 支持的音频格式
audio_type = ["mp3", "wav", "aac", "flac", "m4a"]
whisper_model = [
    "tiny",
    "base",
    "small",
    "medium",
    "large"
]
whisper_device = ["cpu", "cuda"]
whisper_language = [
    "auto",
    "zh",
    "en",
    "ru",
    "fr",
    "de",
    "ko",
    "ja"
]
translator_language = [
    "zh",
    "en",
    "ru",
    "fr",
    "de",
    "ko",
    "ja",
    "ar",
    "es"
]
translator_engine = [
    "bing",
    "sogou",
    "alibaba",
    "caiyun",
    "deepl",
    "ollama"
]
ollama_translate_model = "qwen"
# vits = {
#     "cnhubert_path": "D:\\develop\\project\\GPT-SoVITS\\GPT_SoVITS\\pretrained_models\\chinese-hubert-base",
#     "bert_path": "D:\\develop\\project\\GPT-SoVITS\\GPT_SoVITS\\pretrained_models\\chinese-roberta-wwm-ext-large",
#     "sovits_path": "D:\\develop\\project\\carla\\vits\\hutao\\hutao1_e8_s160.pth",
#     "gpt_path": "D:\\develop\\project\\carla\\vits\\hutao\\hutao1-e15.ckpt",
#     "default_refer_path": "D:\\develop\\project\\carla\\vits\\hutao\\39.胡桃的爱好…_天清海阔，皓月凌空，此情此景，正适合作诗一首。.mp3",
#     "default_refer_text": "天清海阔，皓月凌空，此情此景，正适合作诗一首。",
#     "default_refer_language": "zh",
#     "is_half": false
# }