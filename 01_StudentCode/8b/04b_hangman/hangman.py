# Hangman Game by Jamaal Smith II, v0.0
import random
words = 'run ran rock roll lean drank vamp black opium purple blurple golden destroy autumn wafflestomper '.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = [' ' '
    +---+
        |
        |
        |
    ======== ''', '''
    +---+
    o   |
        |
        |
    ======== ''', '''
    +---+
    o   |
    |   |
        |
    ======== ''', '''
    +---+
    o   |
   /|   |
        |
    ======== ''', '''
    +---+
    o   |
   /|\  |
        |
    ======== ''', '''
    +---+
    o   |
   /|\  |
   /    |
    ======== ''', '''
    +---+
    o   |
   /|\  |
   / \  |
    ======== ''', ''']

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0, len(wordlist) - 1)
    # len(listNmae) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS
    return wordList[wordIndex]

def display(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blank = '_' * len(secretWord)

    # Replace Blanks with Correct Letters 
    for i in range (len(secretWord)):
        if secretWord [i] in correctLetters: 
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 

    for letter in blanks: 
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True: 
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed: 
            print('Letter has been guessed alreadym try again.')
        elif guess not on 'abcdefghijklmnopqrstuvwxyz':
             print('Please guess a LETTER from the Englush alphabet.')
        else:
            return guess
        
def playAgain():
    print('Do you want to play again? Yes or No?')
    return input().lower().startswith(y)

# i = 0
# while i < 100:
#      word = getRandomWord(words)
#      print(word)
