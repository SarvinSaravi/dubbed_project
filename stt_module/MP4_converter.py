import os
import moviepy.editor as movpy
import time
from pathlib import Path

start_time = time.time()
start_dir = Path.cwd()


def mkv_to_mp4_converter():
    for path, folder, files in os.walk(start_dir):
        print("*")
        for file in files:
            print('....')
            if file.endswith('.mkv'):
                print("Found file: %s" % file)
                # convert_to_mp4(os.path.join(start_dir, file))

                clip = movpy.VideoFileClip(file)  # Reading .mkv file
                clip.write_videofile("video2.mp4", codec="libx264", audio_codec="aac")  # Writing .mp4 file
            else:
                pass

        print()
        print("--- %s seconds ---" % (time.time() - start_time))
