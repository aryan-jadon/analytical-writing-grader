import re
from collections import Counter
import spacy
from sklearn.feature_extraction import stop_words
import warnings

warnings.filterwarnings('ignore')
import pandas as pd


def suggest_words(analyzetext):
    from nltk.corpus import stopwords
    from nltk.corpus import wordnet

    stopwordsSpacy = spacy.load("en_core_web_sm")

    stopwords1 = sorted(list(stop_words.ENGLISH_STOP_WORDS))
    stopwords2 = sorted(list(stopwordsSpacy.Defaults.stop_words))
    stopwords3 = stopwords.words('english')

    stopwords = stopwords1 + stopwords2 + stopwords3
    stop_word_set = set(stopwords)
    document = analyzetext

    regex = '[a-zA-Z0-9 ]'

    filteredSentence = "".join(re.findall(regex, document))

    notCommonWords = []

    for word in filteredSentence.split():
        if word.lower() not in stop_word_set:
            notCommonWords.append(word.lower())

    counts = Counter(notCommonWords)

    word_DataFrame = []

    for word, count in counts.items():
        if count >= 3:
            synonyms = []

            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())

            synonyms = list(set(synonyms))

            try:
                synonyms.remove(word)
            except:
                pass

            otherwords = ", ".join(synonyms)

            word_DataFrame.append((word, count, otherwords))

    word_DataFrame = pd.DataFrame(word_DataFrame, columns=["Word", "Count", "Synonyms"])

    return word_DataFrame, notCommonWords
