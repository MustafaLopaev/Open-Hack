from AcikHack.Keyword_Search.summa import summarizer
from googletrans import Translator
from AcikHack import Meaning_Find
import itertools


def Find_Summarize(data, qTR, q1TR):
    data = summarizer.summarize(data)
    print('\n')
    print(data)
    text = data
    translator = Translator(service_urls=[
        'translate.google.com'
    ])
    translations = translator.translate([data], dest='tr')
    q = []
    for translation in translations:
        q.append(translation.text)
    data = ''.join(q)
    print(data)

    def genarate(list1, list2, text):
        founds = []
        for word in list1:
            founds.append(word)
        for word in list2:
            founds.append(word)
        for word1 in list1:
            for word2 in list2:
                founds.append(word1 + " " + word2)

        for word in founds:
            if word not in text:
                founds.remove(word)

        return founds
    Meaning_Find.Meanings(genarate(qTR, q1TR, text))
