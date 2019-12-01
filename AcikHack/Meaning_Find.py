import wikipedia


def Meanings(newArr):
    for word in newArr:
        print(word)
    wikipedia.set_lang("tr")
    meaningList = []
    for word in newArr:
        try:
            print('\n')
            print(word)
            page = wikipedia.page(word)
            meaning = page.content
            parsedMeaning = meaning.split("\n")
            meaningList.append(parsedMeaning[0])
        except:
            print('\n')
            print(word)
            print("Not found")
    for word in meaningList:
        print(word)
