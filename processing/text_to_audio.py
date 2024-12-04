from gtts import gTTS
import tempfile

def save_to_audio(text, filename, language="en"):
    try:
        if not text.strip():
            raise ValueError("Text cannot be empty for audio conversion.")
        
        tts = gTTS(text=text, lang=language)
        
        # Use a temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, mode='wb', suffix='.mp3') as temp_audio_file:
            tts.save(temp_audio_file.name)  # Save the audio to the temporary file
            temp_audio_file.seek(0)  # Move cursor to the beginning of the file
            return temp_audio_file.name  # Return the path of the temporary audio file
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
 