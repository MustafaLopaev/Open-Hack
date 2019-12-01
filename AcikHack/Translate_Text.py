from googletrans import Translator
from AcikHack import Keywords_Finder


def trans(data):
    translator = Translator(service_urls=[
          'translate.google.com'
        ])
    translations = translator.translate([data], dest='en')
    q = []
    for translation in translations:
        q.append(translation.text)
    data = ''.join(q)
    Keywords_Finder.Key_words(data)
