from __future__ import division
import os
import re
import sys
from google.cloud import speech
from google.cloud import texttospeech

#音声再生用
import pyaudio
import wave

from playsound import playsound
import winsound

#作成したモジュール
import sample_texttospeech
import sample_speechtotext
import sample_translation

def main():
    print("start translation")
    sentence_before = sample_speechtotext.module_speechtotext("ja-JP")
    print("---------------------")
    sentence_after = sample_translation.translation_api(sentence_before, 'en')
    print(sentence_after)
    sample_texttospeech.Text_to_Speech(sentence_after)
    '''
    try:
        #playsound("output.wav")
        #winsound.PlaySound("output.wav", winsound.SND_FILENAME)
       
    except FileNotFoundError:
        print("音声を再生できません.")
    '''


if __name__ == "__main__":
    main()    