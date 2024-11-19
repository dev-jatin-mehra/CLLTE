import moviepy.editor as mp
from audio_extraction import extract_text_from_audio

def extract_text_from_video(video_file):
    video = mp.VideoFileClip(video_file)
    audio_path = "../temp/temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    return extract_text_from_audio(audio_path=audio_path)