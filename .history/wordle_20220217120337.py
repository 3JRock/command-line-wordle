import random as rnd

#creating the word list
wordFile = open('words.txt','r')
data = wordFile.read()
wordList = data.split()
# print(wordList)
print(len(wordList))
#choose the word
def wordOfLvl():
    rnd.randrange(0,12972)
print(wordList[12972])    