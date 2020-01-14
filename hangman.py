
import random
from collections import Counter

# This function replaces the '_' with the guessed correct letter
def removeLetterFromWord(guess, word, text_display):
    list_positions = text_display.copy()
    for i in range(len(word)):
        if word[i] == guess:
            list_positions[i] = guess
    return list_positions

# Declare gameMode Function. Easy or Hard.
def gameMode(text_display, secret_word, letter_position, game_mode_choice):
    strike = 0
    guess_attempts = []
    while True:
        
        print(*text_display)
        guess = str(input('\nTake your guess: ')).upper()
        while True:
            if len(guess) < 1 or len(guess) > 1:
                guess = str(input('\nInvalid Guess. Please try again: ')).upper()
            else:
                break
        
        validate_guess = int(secret_word.find(guess))
        guess_attempts.append(guess)


        if validate_guess != -1:
            text_display = removeLetterFromWord(guess, letter_position, text_display)
        else: 
            strike += 1
            if game_mode_choice == 1:
                 print(f'\nPlease try again! \n\n\n')
                 print(f'Attempts: {strike}')
            else:
                print(f'\nStrike {strike}!!! You got { 3 - strike } attempts left! \n\n\n')

        if game_mode_choice == 2:
            if strike == 3:
                print('\nToo bad! You are OUT!\n')
                break
        
        if text_display == letter_position:
            if game_mode_choice == 1:
                print('\n')
                print(*text_display)
                text_display = ''.join(text_display)
                print(f'\nCONGRATULATIONS! It took you {strike} attempts. Word: {text_display} \n')
                break
            else:    
                print('\n')
                print(*text_display)
                print('\nCONGRATULATIONS! You are the MASTER of Hangman!\n')
                break
        print(guess_attempts)

# Open file to get the word
with open('./Hangman/words.txt') as my_file:
    words = my_file.read().splitlines()

secret_word = random.choice(words).upper()
wordsize = len(secret_word)

text_display = []
letter_position = []

for i in range(wordsize):
    text_display += '_'
    letter_position += secret_word[i]

print('''

Welcome to HANGMAN in Python!! v1.0

Your WORD OF FAITH has been chosen!

The words are random! Good luck!

Choose your level:

1- Easy Mode
    (Unlimited attempts)
2- Hard Mode
    (3 Strikes and you are OUT!)
''')

game_mode_choice = int(input('Type your game mode: '))

while True: 
    if game_mode_choice > 0 < 3:
       # pdb.set_trace()
        gameMode(text_display, secret_word, letter_position, game_mode_choice)
        break
    else:
        game_mode_choice = int(input('Incorrect Game mode. Type your game mode: '))





