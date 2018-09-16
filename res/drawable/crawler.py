import requests
from bs4 import BeautifulSoup
import os

def urlFromName(name):
    name = name.split('.',1)[0]
    url =  "https://codepoints.net/U+"+name
    #print(url)
    return url


def getH1(url):
    getUrl = requests.get(url)
    getText = getUrl.text
    BSoup = BeautifulSoup(getText, "html.parser")
    emojiName = BSoup.find('h1')
    emojiName = emojiName.get_text()
    #print(emojiName)
    return emojiName


def getEmojiNameFromFileName(fileName):
    url = urlFromName(fileName)
    h1 = getH1(url)
    finalName = h1.split(' ', 1)[1]
    #print("Split= "+finalName)

    finalName = finalName.lower()
    #print("Lower= "+finalName)
    finalName = finalName.replace(" ", "_")
    return finalName


def iterateOverFiles():
    for fileName in os.listdir("."):
        if fileName.startswith('1') or fileName.startswith('2'):
            newName = getEmojiNameFromFileName(fileName) + ".png"
            if newName != "not_found.png":
                os.rename(fileName, newName)
                print(fileName +" -> "+newName)


if __name__ == '__main__':
    iterateOverFiles()
