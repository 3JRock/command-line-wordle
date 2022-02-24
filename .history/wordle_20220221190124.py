from __future__ import print_function
import random as rnd
import emoji

#creating the word list
wordFile = open('words.txt','r')
data = wordFile.read()
wordList = data.split()



#choose the word
def wordOfLvl():
    num = rnd.randint(0,12971)
    print(wordList[num])
    return wordList[num]

# guess the word
def guess(wrd):
    print(wrd)
    count = 0
    guess = input('Type guess here: ')
    while len(guess) >= 5 or len(guess) <= 5:
        guess = input('Type guess here: ')
