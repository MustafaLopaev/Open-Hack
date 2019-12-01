from AcikHack import Translate_Text
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import requests
import re
class mainCases:
    def __init__(self, data):
        self.data = data


    def SendToCheck(self):
        data = self.data
        Translate_Text.trans(data)


if __name__ == '__main__':
    def FileGet():
        FileName = input()
        with open(FileName, 'r') as file:
            data = file.read()
        q = mainCases(data)
        q.SendToCheck()


    def TextGet():
        data = """Automatic summarization is the process of reducing a text document with a \
                computer program in order to create a summary that retains the most important points \
                of the original document. As the problem of information overload has grown, and as \
                the quantity of data has increased, so has interest in automatic summarization. \
                Technologies that can make a coherent summary take into account variables such as \
                length, writing style and syntax. An example of the use of summarization technology \
                is search engines such as Google. Document summarization is another"""
        q = mainCases(data)
        q.SendToCheck()

    Choose = 2
    if Choose == 1:
        FileGet()
    elif Choose == 2:
        TextGet()