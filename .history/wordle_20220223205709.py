import random as rnd
import emoji

#creating the word list
wordFile = open('words.txt','r')
data = wordFile.read()
wordList = data.split()


correctAns = emoji.emojize(':green_square:')
closeAns = emoji.emojize(':yellow_square:')
notAns = emoji.emojize(':black_large_square:')


#choose the word
def wordOfLvl():
    num = rnd.randint(0,12971)
    
    return wordList[num]

# guess the word
def guess(wrd): #Validation
    print(wrd)
    guess = input('Type guess here: ')
    while len(guess) > 5 or len(guess) < 5: #input validation for length
        guess = input('Type a 5 letter word: ')
        print(len(guess))
    while guess not in wordList:
        guess = input('Not a valid word, retry: ') #input validation for is it is a word
    return guess


def checkAns(pguess,wrd):
    count = 1

    while count < 7: #6 attempts
        
        if pguess == wrd:
            print(correctAns*5,'\nWord get!')
            break

        for i,l in enumerate(pguess):
            if l in wrd:
                
                if l == wrd[i]:
                    print(correctAns,end='')
                    
                else:
                    print(closeAns,end='')
                    
            else:
                print(notAns,end='')
              
        count += 1
        print(f'\n{pguess}\nattempt {count-1}/6') 
      
        pguess = guess(wrd)
    if pguess == wrd:
            return print(correctAns*5,'\nWord get!')
               
    return print(f"You failed the correct word was {wrd}") 


word = wordOfLvl()
initGuess = guess(word)
checkAns(initGuess,word)



