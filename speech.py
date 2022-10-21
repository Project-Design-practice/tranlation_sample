import os
from google.cloud import texttospeech
from playsound import playsound
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret-key.json'

def Text_to_Speech(sentence):
    str(sentence)
    client = texttospeech.TextToSpeechClient()
    try:
        synthesis_input = texttospeech.SynthesisInput(text=sentence)
        voice = texttospeech.VoiceSelectionParams(
            language_code="ja-JP", 
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
    except:
        print("入力が文章ではない、又は他言語の可能性があります")

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

if __name__ == "__main__":
    Text_to_Speech("Hello World!")