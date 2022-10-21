import os
from google.cloud import translate_v2 as translate
from googletrans import Translator
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret-key-translation.json'

# googletransを使用した簡易な翻訳
def translation(sentence, lang_be, lang_af):
    tr = Translator()
    
    #result = tr.translate("I am John.", src="en", dest="ja").text
    result = tr.translate(sentence, src= lang_be, dest=lang_af).text

    return result

# google.cloud_APIを使用した翻訳
def translation_api(sentence, lang):
    translate_client = translate.Client()

    #result_api = translate_client.translate("hello",target_language='ja')
    result_api = translate_client.translate(sentence,target_language=lang)

    return result_api['translatedText']

#print(translation("hello", "en", "ja"))
#print(translation_api("hello", 'ja'))