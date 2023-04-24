import random
#find All module implemented and imported
from findAll import findAll

#show word user found
def showAlreadyFound(alreadyFound):
    print(alreadyFound)
    
#ask for new input
def askLetter():
    return input("Guess a letter\n")
    

print('============= HANGMAN GAME VERSION 1   =======================')

wordDictionnary= ['everywhere','apple', 'banana', 'cherry', 'date','day']
lossChance = 6
alreadyFound = []
lettersUsed = []

wordToGuess = random.choice(wordDictionnary)
alreadyFound = ['_']* len(wordToGuess)

print("Guess the word with {} letters".format(len(alreadyFound)))
print('You are allowed to lose 6 times')

while(lossChance>0 and alreadyFound!= list(wordToGuess)):

    showAlreadyFound(alreadyFound)
    letter = askLetter()
    
    if(letter not in lettersUsed):
            lettersUsed.append(letter)
            if(wordToGuess.find(letter)!=-1):
                for i in findAll(wordToGuess,letter):
                    alreadyFound[i] = letter
            else:
                print('Letter not found')
                lossChance -=1
                print('you have {} chances to lose'.format(lossChance))

    else:
            print('This letter has already been used')
    
#final status
if(alreadyFound== list(wordToGuess)):
     print('You WIN')
else : 
     print('GAME OVER. You loose')
    


