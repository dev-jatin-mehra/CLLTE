from gtts import gTTS
import tempfile

def save_to_audio(text, filename, language="en",accent="us"):
    try:
        if not text.strip():
            raise ValueError("Text cannot be empty for audio conversion.")
        
        if accent == "us":
            tts = gTTS(text=text, lang=language, tld="com")  # U.S. English accent
        elif accent == "uk":
            tts = gTTS(text=text, lang=language, tld="co.uk")  # U.K. English accent
        elif accent == "au":
            tts = gTTS(text=text, lang=language, tld="com.au")  # Australian English accent
        elif accent == "ca":
            tts = gTTS(text=text, lang=language, tld="ca")  # Canadian English accent
        else:
            tts = gTTS(text=text, lang=language)
        
        with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.mp3') as temp_audio_file:
            tts.save(temp_audio_file.name)
            temp_audio_file.seek(0)
            return temp_audio_file.name
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
 