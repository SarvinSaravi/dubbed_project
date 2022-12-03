import os
import moviepy.editor as movpy
import time

start_time = time.time()

# start_dir = os.getcwd()
start_dir = 'D:\\Python\\dubbed_project\\code'

# def convert_to_mp4(mkv_file):
#     name, ext = os.path.splitext(mkv_file)
#     # print(name, ext)
#     out_name = name + ".mp4"
#     ffmpeg.input(mkv_file).output(out_name).run()
#
#     # ffmpeg.input(mkv_file).output(out_name).overwrite_output().run_async(pipe_stdin=True)
#     print("Finished converting {}".format(mkv_file))


for path, folder, files in os.walk(start_dir):
    print("*")
    for file in files:
        print('....')
        if file.endswith('.mkv'):
            print("Found file: %s" % file)
            # convert_to_mp4(os.path.join(start_dir, file))

            clip = movpy.VideoFileClip(file.title())  # Reading .mkv file
            clip.write_videofile("video2.mp4", codec="libx264", audio_codec="aac")  # Writing .mp4 file
        else:
            pass

print()
print("--- %s seconds ---" % (time.time() - start_time))
