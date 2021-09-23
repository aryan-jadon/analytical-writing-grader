from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import re
import networkx as nx
import math


def getRelatedWords(word):
    relWords = set()
    for synset in wn.synsets(word):
        relWords |= set([name.replace("_", "-") for name in synset.lemma_names()])
        relWords |= set(name.replace("_", "-") for name in
                        [lemma.name() for subsynset in synset.hyponyms()
                         for lemma in subsynset.lemmas()])

    return relWords


def makeWordGraph(essay):
    stopwordsList = stopwords.words('english')
    wordList = [word for word in re.findall(r'\w+', essay) if word.lower() not in stopwordsList]
    graph = nx.Graph()

    # make every word a node in the graph
    graph.add_nodes_from(wordList)

    # consider every word in the word list
    for word in wordList:
        # get a list of related words
        relatedWords1 = getRelatedWords(word)
        # if the related word is present in the essay, increase the degrees by 2
        for relWord1 in relatedWords1:
            if relWord1 in graph:
                graph.add_edge(word, relWord1, weight=2)

            # finding the related words in the second level
            # if the related word is present in the essay, increase the degrees by 1
            relatedWords2 = getRelatedWords(relWord1)
            for relWord2 in relatedWords2:
                if relWord2 in graph:
                    graph.add_edge(word, relWord2, weight=1)

    return graph


def getScore(clustCoffList, graph):
    rangeList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    average = 0.0

    for ele in clustCoffList:
        rangeList[int(math.floor(clustCoffList[ele] * 10))] = rangeList[int(math.floor(clustCoffList[ele] * 10))] + 1

    for i in range(len(rangeList)):
        rangeList[i] = rangeList[i] / float(len(graph))

    i = 1
    for i in range(len(rangeList) - 1):
        average = average + rangeList[i]

    if rangeList[0] <= 0.3 and rangeList[10] <= 0.10:
        return 'completely relevant'
    elif (rangeList[0] > 0.3 or rangeList <= 0.4) and rangeList[10] <= 0.10:
        return 'moderately relavant'
    else:
        return 'irrelevant'


def getCoherenceMeasure(essay):
    graph = makeWordGraph(essay)
    # obtain clustering coefficient
    clustCoeffList = nx.clustering(graph)

    # print(getScore(clustCoeffList,graph))
    # print(nx.average_clustering(graph))

    return getScore(clustCoeffList, graph)
