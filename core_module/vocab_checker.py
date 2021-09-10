from nltk.corpus import stopwords
import re
from collections import Counter


stop_word_list = stopwords.words('english')
stop_word_set = set(stop_word_list)

document = '''It is no doubt that music is an integral part of today's youth . With the proliferation of music players such as iPods and the increased capabilities of technology to integrate music into other gadgets like mobile phones and even game consoles , it shows that today's young generation have embedded music deeply into their lives . The youth use music to express themselves - and couple that with information technology and advancements in the internet and you will get a bless world where all the young people share and swap music in cyberspace
Why music though? The appeal of music does not only apply to the youth - music has persisted since the beginning of time . During ancient times music was used for rituals and rites to cover important and sacred events , bringing together the community in their harvest , celebration and praiase of a god , even a death of a king . Music is also an important element in the arts , used to accompany poetry and plays even in Hellenistic Greece . Even today , music plays a central role in ethnic communities like the tribes in Africa
Music is a primary vehicle for self-expression because it can be both exclusive and inclusive . An individual can create music a whole community can share music . It promotes both individuality and a sense of community . It allows the musician , the artist , the individual various modes of exerpression , thus we have the many differing genres in music , We have classical , neo-classical , power metal , heavy metal , progressive rock , rock`n 'roll , ballads , hip hop , rap , bossa nova , goth , ska , emo and pop
Further , music is pleasing - it is different from noise , although what kind of music is pleasing can be very subjective . Music can evoke emotions , set a mood , bring back memories , and trigger sentiments . Music even with the absence of accompanying lyrics can be a powerful tool to bring people together , to suggest an identity or a shared value Consider the national anthem - even without the lyrics an American will surely recognize it anywhere , even if the tempo was altered . It can spur nationalistic and patriotic sentiments . It can bring people together especially in times of tragedy . It is because of music's subtle power that it is used in propaganda . To harp on people's support , the govment may play the national anthem . In the same way , politicians employ catchy music during campaigns to make a mark on people's memories . Commercials and TV ads use easy to remember jingles to encourage brand recall
Music is also an important element in films - consider how scoring and sound effects greatly render emotions on the big screen . Music is used to heighten sensory illusions , to increase suspense , intensify drama enhance ambiance
But more than for its entertainment value or for its use in self-expression , music is integral because it is a reflection of man's rhythm , the movements of his body , mind and soul . Music is always present because man's spirit communicates mood and emotions through rhythm...'
'''

regex = '[a-zA-Z0-9 ]'
filteredSentence = "".join(re.findall(regex, document))
notCommonWords = []

for word in filteredSentence.split():    
    if word.lower() not in stop_word_set:
        notCommonWords.append(word.lower())

counts = Counter(notCommonWords)
print(counts.most_common(4))