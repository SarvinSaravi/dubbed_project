import speech_recognition as sr
import time

start_time = time.time()


def convert_text_to_speech():
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
