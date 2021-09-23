from nltk.corpus import wordnet


def word_information(requested_word):
    input_query = requested_word
    wordResults = []

    word = wordnet.synsets(input_query)
    word = word[0]
    word_definition = word.definition()
    try:
        wordResults.append(word_definition)
    except:
        wordResults.append("")
        # wordResults.append("definition not found for this word")

    exampleList = []

    word_examples = word.examples()

    if len(word_examples) > 0:
        for example in word_examples:
            exampleList.append(example)
        wordResults.append(exampleList)
    else:
        wordResults.append("")
        # wordResults.append("no examples found for this word")

    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(input_query):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    if len(set(synonyms)) > 0:
        synonyms = list(set(synonyms))
        wordResults.append(synonyms)
    else:
        wordResults.append("")

        # wordResults.append("no synonyms found")

    if len(set(antonyms)) > 0:
        antonyms = list(set(antonyms))
        wordResults.append(antonyms)
    else:
        wordResults.append("")
        # wordResults.append("no antonyms found")

    return wordResults


