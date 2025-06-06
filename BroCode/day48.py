import sys
import random
import time
from enum import Enum

############################################################################
############################################################################

# rock paper scissors
print('\nWelcome to Rock Paper Scissors\n')
while True:
    choice = input(
        'Choose...\n1. for Rock...\n2. for Paper...\n3. for Scissors...\nQ to Quit...\n\n')

    if choice == "q":
        break

    choice = int(choice)
    computer = random.choice("123")
    computer = int(computer)

    print(f'\nYou chose: {choice}')
    print(f'Python chose: {computer}\n')

    if choice == 1 and computer == 2:
        print('You win!')
    elif choice == 2 and computer == 3:
        print("You Win!")
    elif choice == 3 and computer == 1:
        print("You Win!")
    elif choice == computer:
        print('It is a Tie')
    else:
        print('Python Wins')

    print()
    print('Do you want to play again? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue..Q to Quit...  ')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break
    if play_again.lower() == "y":
        print()
        continue
    else:
        break

print("\nThanks for playing Rock Paper Scissors\n")
