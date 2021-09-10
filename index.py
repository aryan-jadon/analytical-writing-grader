from core_module.word_information import word_information
from core_module.spell_checker import checkSpellings
from core_module.coherence_checker import getCoherenceMeasure
from core_module.essay_stats import get_wordcount, getSentenceCount, \
    getParaCount, getAvgSentenceLength, getStdDevSentenceLength

essay = ''' 
Although agreements have value, the juxtaposition of different ideas in a conflict inevitably leads to more significant progress and evolution. What scientific progress would we have, for example, if it weren’t for intellectual debate? None—intellectual debate leads to scientific progress. The reformation of outdated political ideas and concepts is also marked by struggle. Finally, in the words of Friedrich Nietzsche, “What doesn’t kill us makes us stronger.” This quotation captures the sentiment that personal growth arises from conflict.
First, historically, scientific progress has been inspired by conflicts of ideas. In the sixteenth century, for example, a great debate arose because Copernicus vehemently challenged the notion that the earth is the center of the solar system. Although he paid a price both socially and politically for this remonstration, Copernicus disabused a long-held belief, much to the chagrin of the Catholic Church and other astronomers of his day. Because of this conflict, humankind eventually gained a new understanding of astronomy.
Second, sociohistorical evolution rarely comes about without turmoil and unrest. For example, prior to the 1860s in the United States, it was legally acceptable to enslave other human beings and to view them as “property” with few rights. This view led several states to secede from the Union, which, in turn, led to the Civil War, a violent conflict that threatened to destroy the nation. After the war, though, slavery was abolished, and the Fourteenth Amendment to the Constitution essentially made discrimination on the basis of race illegal. As a result, the United States grew stronger as a nation. To advance takes constant questioning of the status quo.
Third, conflict can lead to personal growth. Adversity helps make us stronger. People who have not known some type of conflict or difficulty tend to be immature and spoiled. Americans so believe this sentiment about adversity that they have institutionalized it as an oft-repeated saying: If at first you don’t succeed, try, try again. This saying emphasizes the way overcoming difficulty helps us grow as individuals: Each time we fail, we must pick ourselves up and try again. We shouldn’t expect life to be easy. Sometimes the value of struggle is in the struggle, meaning that such conflicts, whether internal or external, give us perspective and insight.
Clearly, conflict has been responsible for several upward surges of humankind in diverse respects. In the areas of science, history, and individual character, progress requires struggle. Rather than avoiding conflict at all costs, we should accept conflict as a necessary—and beneficial—part of the human condition, whether the conflicts arise among scholars or states. Conflict permits true transformation and growth.
'''

print("-----------------------")
print("Word Count is " + str(get_wordcount(essay)))
print("-----------------------")

print("Sentence Count is " + str(getSentenceCount(essay)))
print("-----------------------")

print("Paragraph Count is " + str(getParaCount(essay)))
print("-----------------------")

print("Average Sentence Length is " + str(getAvgSentenceLength(essay)))
print("-----------------------")

print("Standard Dev. Sentence Length is " + str(getStdDevSentenceLength(essay)))

print("-----------------------")
print(getCoherenceMeasure(essay))
print("-----------------------")

SpellingInformation = checkSpellings(essay)

print("Number of Wrong Spellings - " + str(SpellingInformation[0]))
print("-----------------------")
print("Wrong Spellings - " + str(", ".join(SpellingInformation[1])))
print("-----------------------")

# Add grammar Code Here

Hard_Word_Information = word_information("Naive")
print("Definiton - " + str("".join(Hard_Word_Information[0])))
print("Examples - " + str(", ".join(Hard_Word_Information[1])))
print("Synonyms - " + str(", ".join(Hard_Word_Information[2])))
print("Antonyms - " + str(", ".join(Hard_Word_Information[3])))
print("-----------------------")
