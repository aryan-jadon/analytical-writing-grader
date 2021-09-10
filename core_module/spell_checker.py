from spellchecker import SpellChecker
import re


def checkSpellings(text):
    spell = SpellChecker(distance=1)
    regex = '[a-zA-Z0-9 ]'
    Sentence = text
    match = "".join(re.findall(regex, Sentence))
    Misspelled = spell.unknown(match.split(' '))
    Misspelled = list(Misspelled)

    try:
        Misspelled.remove('')
    except:
        pass

    return len(Misspelled), Misspelled
