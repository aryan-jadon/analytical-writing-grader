from nltk.corpus import wordnet


def word_information(requested_word):
    input_query = requested_word
    word_results = []

    word = wordnet.synsets(input_query)
    word = word[0]
    word_definition = word.definition()
    try:
        word_results.append(word_definition)
    except Exception as e:
        word_results.append("definition not found for this word")
        print(e)

    example_list = []
    word_examples = word.examples()

    if len(word_examples) > 0:
        for example in word_examples:
            example_list.append(example)
        word_results.append(example_list)
    else:
        word_results.append("no examples found for this word")

    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(input_query):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    if len(set(synonyms)) > 0:
        synonyms = list(set(synonyms))
        word_results.append(synonyms)
    else:
        word_results.append("no synonyms found")

    if len(set(antonyms)) > 0:
        antonyms = list(set(antonyms))
        word_results.append(antonyms)
    else:
        word_results.append("no antonyms found")

    return word_results
