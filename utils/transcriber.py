import whisper

# Load Whisper model
model = whisper.load_model("base")

def transcribe_audio(path):
    try:
        result = model.transcribe(path)
        return result['text']
    except Exception as e:
        return f"Transcription failed: {str(e)}"