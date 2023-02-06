# 1. visit hf.co/pyannote/speaker-diarization and accept user conditions
# 2. visit hf.co/pyannote/segmentation and accept user conditions
# 3. visit hf.co/settings/tokens to create an access token
# 4. instantiate pretrained speaker diarization pipeline
import os

os.add_dll_directory('C:\\Program Files\\Python310\\Lib\\site-packages\\torchaudio\\lib')
# os.add_dll_directory('libtorchaudio.pyd')


from pyannote.audio import Pipeline


pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1",
                                    use_auth_token="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")


# apply the pipeline to an audio file
diarization = pipeline("audio.wav")

# dump the diarization output to disk using RTTM format
with open("audio.rttm", "w") as rttm:
    diarization.write_rttm(rttm)
