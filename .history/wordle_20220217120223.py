import random   

#creating the word list
wordFile = open('words.txt','r')
data = wordFile.read()
wordList = data.split()
# print(wordList)
print(len(wordList))
#choose the word
#def wordOfGame():
