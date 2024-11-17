import speech_recognition as sr
import os
from pydub import AudioSegment

def convert_to_wav(audio_file,output_dir="temp"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    wav_file = os.path.join(output_dir,"temp_audio.wav")

    #COnvert MP# to wave
    audio = AudioSegment.from_file(audio_file)
    trimmed_audio = audio[:7*1000]
    trimmed_audio.export(wav_file,format="wav")
    return wav_file

def extract_text_from_audio(audio_path):
    recognizer = sr.Recognizer()

    if not audio_path.name.lower().endswith(".wav"):
        audio_path = convert_to_wav(audio_path)

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data,language="en-US")
        return text
    
    except sr.UnknownValueError:
        return "Sorry ! Could not understand the audio"
    
    except sr.RequestError as e:
        return f"Could not request results;{e}"
# if __name__ == "__main__":
#     # Replace with the path to your MP3 or WAV file
#     audio_path = "C:\\Users\\jatin\\OneDrive\\Desktop\\my.unknown"
#     text = extract_text_from_audio(audio_path=audio_path)
#     print("Extracted Text:", text)