from stt_module.MP4_converter import mkv_to_mp4_converter
from stt_module.speech_extracter import extract_audio_from_video
from stt_module.text_converter import audio_slicer, convert_speech_to_text


def main():
    # mkv_to_mp4_converter()
    # extract_audio_from_video()
    # audio_slicer()
    convert_speech_to_text(r"chunk1.wav")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

