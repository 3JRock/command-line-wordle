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
def guessCheck(wrd):
    print(wrd)
    count = 0
    guess = input('Type guess here: ')
    while guess != wrd:
        for i,l in enumerate(guess):
            if (l in wrd) and (l == wrd[i]):
                print(':white_check_mark:',end='')
            elif (l in wrd):
                print(':large_orange_diamond:',end='')
            else:
                 print(':black_circle:',end='')   
            
        count += 1
        guess = input('Try again: ')

guessCheck(wordOfLvl())
