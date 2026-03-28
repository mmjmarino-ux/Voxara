from gtts import gTTS
import os

# Text to Speech only (voice input is now handled by the browser)
def text_to_speech(text, language='en'):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("output.mp3")
        os.system("start output.mp3")
        return "Audio played successfully"
    except Exception as e:
        return f"Speech error: {str(e)}"

def speech_to_text():
    return "Voice input is handled by the browser"