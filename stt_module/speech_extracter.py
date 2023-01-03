import moviepy.editor as mp


def extract_audio_from_video():
    clip = mp.VideoFileClip(r"Frnds-S03E09-720p_FiLMin.mkv")  # specify the correct file path to your video file
    clip.audio.write_audiofile(r"audio.wav")  # this the name of the converted audio file

