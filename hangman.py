debugMode = False
from random import choice
#Creating word
wordsList = ["monkey","elephant","serval","giraffe","viper","macaw","parrot","bear","ferret","tapir",
             "kingfisher","baboon","vulture","lemur"]
wordsListLen = len(wordsList)
hiddenWordString = choice(wordsList)
hiddenWordLettersCount = int(len(hiddenWordString))
dashesSource = '-------------------------'
unhiddenWordString = dashesSource[:hiddenWordLettersCount]
if debugMode == True:
    print (hiddenWordString)
    print (unhiddenWordString)

hiddenWordGuessesCount = int (0)

#word input and output

print ("The word you are guessing is an animal and has " + str(hiddenWordLettersCount) + " letters")
print ("You have made " + str(hiddenWordGuessesCount) + " Guesses")

while hiddenWordString != unhiddenWordString:
    guessInput = input("What is your guess? ")

#Checking guess code
#Confirm guess input is valid
    if debugMode == True:
        print ("guessed letter = " + guessInput)
    if len(guessInput) == 1:
        guessInputValid = True
    else:
        guessInputValid = False
        print ("Your Guess is invalid")
    guessInputIncluded = False
    #Checking each letter in turn
    loopCount = 0
    while loopCount < hiddenWordLettersCount:
        if hiddenWordString[loopCount] == guessInput: 
            print ("You guessed letter " + str((loopCount + 1)) + " correctly")
            unhiddenWordString = unhiddenWordString[:loopCount] + guessInput + unhiddenWordString[(loopCount+1):]
            guessInputIncluded = True
        loopCount += 1
    if guessInputIncluded == False:
        print ("Sorry, your guess was not in the word")
        hiddenWordGuessesCount += 1
    print (unhiddenWordString)    
    if hiddenWordString == unhiddenWordString:
        print ("congratulations, you correctly guessed the word with " + str(hiddenWordGuessesCount) + " incorrect guesses")
      