import random
import math
import sys

print()

'''
    Ask the user ro make a choice
    if choice is not valid...print an error  
    let the compter to make a choice   
    print choices (emojis)
    determine the winner 
    Ask the user if they want to continue 
    If not .....Terminate
'''

'''

choices = ('r', 'p', 's')  # Convert to a tuple..bcz it is immutable...
emojis = {'r': '🪨', 'p': '📜📃', 's': '✂️'}    # Dict to map: 'Key': "Value"

while True:
    player = input('Enter rock,paper or scissors (r/p/s)..  ').lower()

    if player not in choices:
        print(f'Invalid Input..')
        continue

    computer_choice = random.choice(choices)

    print(f'\nPlayer chose: {emojis[player]}')
    print(f'Computer chose: {emojis[computer_choice]}\n')

    if ((player == 'r' and computer_choice == 'p') or
        (player == 'p' and computer_choice == 's') or
            (player == 's' and computer_choice == 'r')):
        print(f'Player Wins!🎉🎉🎉🎉')
    elif player == computer_choice:
        print('It\'s a Tie')
    else:
        print('You Loose')

    should_continue = input('\nContinue? (y/n):    ')
    print()
    if should_continue.lower() == 'y':
        continue
    else:
        break

'''

# Modularisation
# DRY Dont Repeat Yourself
# =========================================================================
# =========================================================================

# choices = ('r', 'p', 's')  # Convert to a tuple..bcz it is immutable...
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

# Dict to map: 'Key': "Value"
emojis = {ROCK: '🪨', PAPER: '📜📃', SCISSORS: '✂️'}
print(emojis.keys())   # we want a tuple
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        print()
        player = input('Enter rock,paper or scissors (r/p/s)..  ').lower()
        if player in choices:
            return player
        elif player == 'q':
            sys.exit(f'\nBye... Thanks for Playing RPS..\n')
        else:
            print(f'Invalid Choice..\n')


def display_choices(player, computer_choice):
    print(f'\nPlayer chose: {emojis[player]}')
    print(f'Computer chose: {emojis[computer_choice]}\n')


def determine_winner(player, computer_choice):
    if ((player == ROCK and computer_choice == PAPER) or
            (player == PAPER and computer_choice == SCISSORS) or
            (player == SCISSORS and computer_choice == ROCK)):
        print(f'Player Wins!🎉🎉🎉🎉')
    elif player == computer_choice:
        print('It\'s a Tie')
    else:
        print('You Loose')


def play_game():
    while True:
        player = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(player, computer_choice)

        determine_winner(player, computer_choice)

        should_continue = input('\nContinue? (y/n):    ')
        print()
        if should_continue.lower() == 'y':
            continue
        else:
            break


play_game()
