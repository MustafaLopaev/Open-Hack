from AcikHack import TextRank1, Summarize_Finder
from AcikHack.Keyword_Search.summa import keywords
from googletrans import Translator


def Key_words(text):
    tr4w = TextRank1.TextRank4Keyword()
    tr4w.analyze(text, candidate_pos=['NOUN', 'PROPN'], window_size=4, lower=False)
    q = tr4w.get_keywords(10)
    t = []
    q1 = []
    for word in keywords.keywords(text):
        if word != '\n':
            t.append(word)
        else:
            q1.append(''.join(t))
            t = []
    print(q)
    print(q1)
    translator = Translator(service_urls=[
        'translate.google.com'
    ])
    qTR = []
    q1TR = []
    trans = []
    for word in q:
        translations = translator.translate([word], dest='tr')
        for translation in translations:
            trans.append(translation.text)
        trans = ''.join(trans)
        qTR.append(trans)
        trans = []

    for word in q1:
        translations = translator.translate([word], dest='tr')
        for translation in translations:
            trans.append(translation.text)
        trans = ''.join(trans)
        q1TR.append(trans)
        trans = []

    print(qTR)
    print(q1TR)

    Summarize_Finder.Find_Summarize(text, qTR, q1TR) #degistircez turkce koy
