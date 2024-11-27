# import gtts

# def save_to_audio(text,filename,language="en"):
#     tts = gtts.gTTS(text,lang=language)
#     tts.save(filename)
#     return filename

from gtts import gTTS
import os

def save_to_audio(text, filename, language="en"):
    try:
        if not text.strip():
            raise ValueError("Text cannot be empty for audio conversion.")

        tts = gTTS(text=text, lang=language)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
