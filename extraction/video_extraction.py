# import moviepy.editor as mp
# from .audio_extraction import extract_text_from_audio

# def extract_text_from_video(video_file):
#     video = mp.VideoFileClip(video_file)
#     audio_path = "../temp/temp_audio.wav"
#     video.audio.write_audiofile(audio_path)
#     return extract_text_from_audio(audio_path=audio_path)

import os
import moviepy.editor as mp
from .audio_extraction import extract_text_from_audio

def extract_text_from_video(video_file):
    # Ensure the temp directory exists
    temp_dir = "./temp"
    os.makedirs(temp_dir, exist_ok=True)

    # Define the audio output path
    audio_path = os.path.join(temp_dir, "temp_audio.wav")

    try:
        # Load the video file
        video = mp.VideoFileClip(video_file)

        # Check if the video contains an audio stream
        if video.audio is None:
            raise ValueError("The video file does not contain an audio stream.")

        # Extract the audio and save it as a WAV file
        video.audio.write_audiofile(audio_path)

        # Extract text from the audio
        extracted_text = extract_text_from_audio(audio_path=audio_path)

        return extracted_text

    except Exception as e:
        raise IOError(f"Error processing video: {e}")

    finally:
        # Clean up the temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)
