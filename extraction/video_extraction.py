import streamlit as st
import os
import tempfile
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment

def extract_text_from_video(video_file, language_code):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(video_file.read())
            temp_video_path = temp_video.name

        video = VideoFileClip(temp_video_path)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio_path = temp_audio.name
            video.audio.write_audiofile(temp_audio_path)

        video.close()

        extracted_text = extract_text_from_audio(temp_audio_path, language_code)

        os.remove(temp_video_path)  
        os.remove(temp_audio_path)

        return extracted_text

    except Exception as e:
        return f"Error: {str(e)}"


def extract_text_from_audio(audio_path, language_code):
    try:
        if not audio_path.lower().endswith(".wav"):
            audio_path = convert_to_wav(audio_path)

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        
        text = recognizer.recognize_google(audio_data, language=language_code)
        return text

    except sr.UnknownValueError:
        return "Sorry! Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from the speech recognition service: {e}"
    except Exception as e:
        return f"Error: {str(e)}"


def convert_to_wav(audio_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wav_path = temp_wav_file.name
            audio = AudioSegment.from_file(audio_file)
            audio.export(wav_path, format="wav")
        return wav_path

    except Exception as e:
        raise Exception(f"Error converting audio file to WAV: {str(e)}")