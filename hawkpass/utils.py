import hashlib
import random

from dataclasses import dataclass
from enum import Enum

from .config import NUMBER_REPLACEMENT, SYMBOL_REPLACEMENT
from .wordlist import Wordlist


class Case(Enum):
    LOWERCASE = 'lowercase'
    UPPERCASE = 'uppercase'
    CAPITALIZE = 'capitalize'


@dataclass
class Options:
    length: int = 5
    numbers: bool = False
    symbols: bool = False
    spaces: bool = False
    case: Case = Case.LOWERCASE

    def __post_init__(self):
        self.length = Options.length if not self.length else self.length
        self.numbers = Options.numbers if not self.numbers else self.numbers
        self.symbols = Options.symbols if not self.symbols else self.symbols
        self.spaces = Options.spaces if not self.spaces else self.spaces
        self.case = Options.case if not self.case else self.case


def get_wordlist_enum(wordlist: str = Wordlist.EFF.value) -> Wordlist:
    wordlists = []
    for member in Wordlist:
        if wordlist == member.value:
            return member
        
        if member not in [Wordlist.ADJECTIVE, Wordlist.ARTICLE, Wordlist.NOUN, Wordlist.VERB]:
            wordlists.append(member.value)

    raise ValueError(
        f'Invalid wordlist value. Please provide one of the following {wordlists}.'
    )


def get_case_enum(case: str = Case.LOWERCASE.value) -> Case:
    """Converts a string to a Case enum value."""
    cases = []
    for member in Case:
        if case == member.value:
            return member
        
        cases.append(member.value)

    raise ValueError(f'Invalid case value. Please provide one of the following {cases}.')


def replace_character(replacements, passphrase):
    chars = [*passphrase] # split passphrase into chars
    i = None
    # Loop until random finds a character in replacements dict
    while i is None:
        random_int = random.randint(0, len(chars) - 1)
        if chars[random_int].lower() in replacements.keys():
            i = random_int

    # Replace random found character with value
    # from replacements dict
    chars[i] = replacements[chars[i].lower()]
    passphrase = ''.join(chars)
    return passphrase


def get_template(wordlist: str, length: int = Options.length) -> list:
    """Get template."""
    keys = [
        Wordlist.ARTICLE,
        Wordlist.ADJECTIVE,
        Wordlist.NOUN,
        Wordlist.VERB
    ];
    template = []

    for idx in range(0, length - 1):
        key = keys[idx % len(keys)]
        if not wordlist:
            template.append(key)
        else:
            wordlist_enum = get_wordlist_enum(wordlist)
            template.append(wordlist_enum)

    return template


def get_random_word(haystack: list) -> str:
    """Get a random word from the haystack."""
    m = hashlib.sha256()
    word = haystack[random.randint(0, len(haystack) - 1)]
    return word


def get_passphrase(options: dict, sentence: list) -> None:
    if options.case == Case.LOWERCASE:
        sentence = [s.lower() for s in sentence]

    if options.case == Case.UPPERCASE:
        sentence = [s.upper() for s in sentence]

    if options.case == Case.CAPITALIZE:
        sentence = [s[0].upper() + s[1:] for s in sentence]

    passphrase: str = ''.join(sentence)

    if options.spaces:
        passphrase = ' '.join(sentence)

    if options.numbers:
        passphrase = replace_character(NUMBER_REPLACEMENT, passphrase)

    if options.symbols:
        passphrase = replace_character(SYMBOL_REPLACEMENT, passphrase)
    
    return passphrase
