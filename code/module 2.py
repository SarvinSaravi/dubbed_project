import speech_recognition as sr
import moviepy.editor as mp
import time

start_time = time.time()

# clip = mp.VideoFileClip(r"video2.mp4")  # specify the correct file path to your video file
# clip.audio.write_audiofile(r"converted_mp3.wav")  # this the name of the converted audio file

r = sr.Recognizer()
audio = sr.AudioFile(r"converted_mp3.wav")  # give the audio file name here
with audio as source:
    audio_file = r.record(source)

result = r.recognize_google(audio_file)

with open('recognized_text_file.txt', mode='w') as file:
    file.write("speech recognized")
    file.write("\n")
    file.write(result)
    print("Now the file is ready")

with open('recognized_text_file.txt') as file:
    lines = file.readlines()
    print(lines)

print()
print("--- %s seconds ---" % (time.time() - start_time))
