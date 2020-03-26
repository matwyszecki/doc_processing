import nltk
from nltk.book import *
from nltk import bigrams
from nltk.corpus import brown
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

texts = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
sentences = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8, sent9]

##### 1. Lexical diversity
def lexical_div(text):
    print(text)
    print("liczba słów: ", len(text))
    print("słowa różne: ", len(set(text)))
    print("lexical_div: ", len(set(text)) / len(text))
    print("\n")


# for text in texts:
#     lexical_div(text)

#### 2. Find four letter words
def fourWords(text):
    V = set(text)
    fourWords = [w for w in V if len(w) == 4]
    print(len(fourWords))

# fourWords(text1)

#### 3. Shared dictionary for sentences
def sharedDict():
    comDic = []
    for sent in sentences:
        comDic = comDic + sent
    comDicSort = sorted(comDic)
    print("Słownik wspólny: ", comDicSort)

#### 4. Count the number of specific words in the category "adventure" of the gutenberg corpus
def adventure():
    adv = brown.words(categories='adventure')
    fdist = nltk.FreqDist(w.lower() for w in adv)
    words = ['mountains', 'ocean']
    for w in words:
        print(w + ":", fdist[w], end=' ')
    fdist2 = nltk.FreqDist(x for x in bigrams(adv))
    words2 = ['Bungee jump']
    for x in words2:
        print(x + ":", fdist[x], end=' ')

#### 5. Count non-stopwords
def nonStop():
    stopwords = stopwords.words('english')
    for text in texts:
        words = text
        noStop = []
        for word in words:
            if word not in stopwords:
                noStop.append(word)
        lenStop = len(words)
        lenNoStop = len(noStop)
        perCent = round((lenNoStop/lenStop)*100, 2)
        print(text, perCent,"%")

#### 6. Sentiment polarity of words
def senti():
    words = ['journalist.n.01', 'writer.n.01', 'actor.n.01', 'singer.n.01', 'kill.v.01', 'love.v.01']
    for word in words:
        senti = swn.senti_synset(word)
        print(senti)

#### 7. Check semantic similarity of words

def semantic():
    boy=wn.synset('boy.n.01')
    lad=wn.synset('lad.n.01')

    journey=wn.synset('journey.n.01')
    voyage=wn.synset('voyage.n.01')

    coast=wn.synset('coast.n.01')
    hill=wn.synset('hill.n.01')

    monk=wn.synset('monk.n.01')
    slave=wn.synset('slave.n.01')

    food=wn.synset('food.n.01')
    fruit=wn.synset('fruit.n.01')

    car=wn.synset('car.n.01')

    def sim(firstWord, secondWord):
        print(firstWord,"-", secondWord, firstWord.path_similarity(secondWord))

    pairs = [[boy, lad], [journey, voyage], [coast, hill], [monk, slave], [food, fruit], [journey, car]]
    for pair in pairs:
        sim(pair[0], pair[1])

#### 8. Analysis of the gutenberg corpus

    # Average word length
def gutenWordLen():
    for text in gutenberg.fileids():
        words = gutenberg.words(text)
        average = round(sum(len(word) for word in words) / len(words), 2)
        print("Name:", text, "Average word length:", average)

    # Average number of words in a sentence
def guteWordNum():
    for text in gutenberg.fileids():
        sents = gutenberg.sents(text)
        average = round(sum(len(sent) for sent in sents) / len(sents), 2)
        print("Name:", text, "Average word number in a sentence:", average)

    # Average number of repetitions of the same word
def gutenRep():
    for text in gutenberg.fileids():
        words = gutenberg.words(text)
        words = set(words)
        repetitions = 0
        for word in words:
            repetitions += text.count(word)
        average = repetitions/len(set(words))
        print("Name:", text, "Average number of repetitions of the same word:", average)

#### 9. Most common parts of speech
def POS():
    brown_tagged_words = brown.tagged_words(fileids='cg48',tagset='universal')
    tag = nltk.FreqDist(tag for (word, tag) in brown_tagged_words)
    print(tag.most_common())

#### 10. Look for [verb + "to" + verb] pattern in a sentence
def pattern():
    from nltk import word_tokenize
    sent1 = nltk.pos_tag(word_tokenize("Can you try to help him?"))
    sent2 = nltk.pos_tag(word_tokenize("It's time to go."))
    sent3 = nltk.pos_tag(word_tokenize("Stop lying to me."))
    sent4 = nltk.pos_tag(word_tokenize("I aim to reduce the pollution."))
    sent5 = nltk.pos_tag(word_tokenize("He wants to be a cowboy."))


    def threeGram(sentence):
        for (word1, tag1), (word2, tag2), (word3, tag3) in nltk.trigrams(sentence):
                if (tag1.startswith('VB') and tag2 == 'TO' and tag3.startswith('VB')):
                    print(word1, word2, word3)

    threeGram(sent1)
    threeGram(sent2)
    threeGram(sent3)
    threeGram(sent4)
    threeGram(sent5)
