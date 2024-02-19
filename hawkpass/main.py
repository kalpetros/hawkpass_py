from .utils import (
    get_case_enum,
    get_passphrase,
    get_random_word,
    get_template,
    Options
)
from .wordlist import get_wordlist


def passphrase(
    length: int = None,
    numbers: int = None,
    symbols: int = None,
    spaces: bool = None,
    case: str= None,
    wordlist: str = None,
) -> str:
    """Diceware"""
    sentence = []
    case_enum = get_case_enum(case)

    options = Options(
        length=length,
        numbers=numbers,
        symbols=symbols,
        spaces=spaces,
        case=case_enum,
    )

    template = get_template(wordlist, options.length)

    for token in template:
        haystack = get_wordlist(token)
        random_word = get_random_word(haystack)
        sentence.append(random_word)

    passphrase = get_passphrase(options, sentence)

    return passphrase
