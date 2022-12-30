import moviepy.editor as mp


def extract_audio_from_video():
    clip = mp.VideoFileClip(r"video2.mp4")  # specify the correct file path to your video file
    clip.audio.write_audiofile(r"converted_mp3.wav")  # this the name of the converted audio file
