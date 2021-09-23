from nltk.corpus import stopwords
import re
from collections import Counter


def check_vocab(text):
    stop_word_list = stopwords.words('english')
    stop_word_set = set(stop_word_list)
    document = text

    regex = '[a-zA-Z0-9 ]'
    filteredSentence = "".join(re.findall(regex, document))
    notCommonWords = []

    for word in filteredSentence.split():
        if word.lower() not in stop_word_set:
            notCommonWords.append(word.lower())

    counts = Counter(notCommonWords)

    return counts.most_common(4)

