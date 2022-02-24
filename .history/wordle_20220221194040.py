from __future__ import print_function
from itertools import count
import random as rnd
import emoji

#creating the word list
wordFile = open('words.txt','r')
data = wordFile.read()
wordList = data.split()

print(emoji.emojize('Python is :thumbs_up:'))

#choose the word
def wordOfLvl():
    num = rnd.randint(0,12971)
    
    return wordList[num]

# guess the word
def guess(wrd): #Validation
    print(wrd)
    guess = input('Type guess here: ')
    while len(guess) > 5 or len(guess) < 5: #input validation for length
        guess = input('Type 5 letter word: ')
        print(len(guess))
    while guess not in wordList:
        guess = input('Not a valid word, retry: ') #input validation for is it is a word
    return guess


def checkAns(guess,wrd):
    count = 0
    while count < 7:
        if guess == wrd:
            print(f'correct! it took {count} attempts')# emojis?
        for l in guess:
            if l in guess:
                print('g')