
# Hangman as learned from 'Invent Your Own Games with Python' (Al Sweigart)

import random
HANGMANPICS = ['''

    +---+    
    |   |
        |
        |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
        |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
    |   |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|   |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========''']

words = 'ant baboon badger bat bear'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
        print()
    blanks = '_' * len(secretWord)

# Replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]


# Show secret word with spaces in between each letter            
    for letter in blanks:
        print(letter, end=' ')

# Returns letter player entered. This function makes sure the player entered a single letter and not anything else
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input(' > ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

# Function returns True if players want to play again            
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
    
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
            
# Ask if they want to play again, only if game is done
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break