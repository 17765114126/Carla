import whisper

if __name__ == '__main__':
    whisper_model = whisper.load_model("base")
    result = whisper_model.transcribe(r"D:\aupi\out.wav")
    print(", ".join([i["text"] for i in result["segments"] if i is not None]))
