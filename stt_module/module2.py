import time
import moviepy.editor as mp

start_time = time.time()


def convert_text_to_speech():
    clip = mp.VideoFileClip(r"video2.mp4")  # specify the correct file path to your video file
    clip.audio.write_audiofile(r"converted_mp3.wav")  # this the name of the converted audio file
