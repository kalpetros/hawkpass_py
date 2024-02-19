import os

from enum import Enum


class Wordlist(Enum):
    ADJECTIVE = 'adjective'
    ARTICLE = 'article'
    CZECH = 'cs'
    DANISH = 'da'
    DUTCH = 'nl'
    EFF = 'en_eff'
    FINISH = 'fi'
    FRENCH = 'fr'
    GERMAN = 'de'
    GREEK = 'el'
    ITALIAN = 'it'
    LATIN = 'la'
    MALAY = 'ms'
    NORWEGIAN = 'no'
    NOUN = 'noun'
    ORIGINAL = 'original'
    PINYIN = 'zh'
    PORTUGUESE = 'pt'
    ROMAJI = 'ja'
    SWEDISH = 'sv'
    TURKISH = 'tr'
    VERB = 'verb'


def get_wordlist(token: Wordlist = Wordlist.EFF) -> list:
    path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'wordlists')
    )

    wordlist = open(f'{path}/{token.value}.txt', 'r')

    words = []
    for word in wordlist:
        words.append(word.strip())

    wordlist.close()
    
    return words