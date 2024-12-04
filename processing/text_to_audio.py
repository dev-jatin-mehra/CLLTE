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
        
        # Use a temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.mp3') as temp_audio_file:
            tts.save(temp_audio_file.name)  # Save the audio to the temporary file
            temp_audio_file.seek(0)  # Move cursor to the beginning of the file
            return temp_audio_file.name  # Return the path of the temporary audio file
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
 