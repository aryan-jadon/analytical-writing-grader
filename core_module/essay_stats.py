import nltk
import math
import re


def getWordCount(text):
    # split the text into words
    wordList = re.findall(r'\w+', text)

    return len(wordList)


def getSentenceCount(text):
    # split the essay into sentences
    sentList = nltk.sent_tokenize(text)

    return len(sentList)


def getParaCount(text):
    # split the text into paragraphs
    paraList = text.splitlines()
    # remove blank lines from the list of paragraphs
    paraList[:] = [element for element in paraList if element != ""]

    return len(paraList)


def getAvgSentenceLength(text):
    # split the essay into sentences
    sentList = nltk.sent_tokenize(text)

    sumSentLength = 0
    for sent in sentList:
        sumSentLength = sumSentLength + getWordCount(sent)

    return float(sumSentLength) / len(sentList)


def getStdDevSentenceLength(text):
    # split the essay into sentences
    sentList = nltk.sent_tokenize(text)

    # mean sentence length
    mean = getAvgSentenceLength(text)

    nr = 0.0
    for sent in sentList:
        nr = nr + (getWordCount(sent) - mean) ** 2

    return math.sqrt(nr / len(sentList))
