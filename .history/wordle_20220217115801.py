import random   


wordFile = open('words.txt','r')

data = wordFile.read()

wordList = data.split()
print(wordList)