from enum import Enum
import sys
import random
print()

# ******************************************************************************
# ******************************************************************************
# ******************************************************************************

'''
Day 14 of programming
Rock, Paper, Scissors Game
Objective: Write a program where the user plays "rock, paper, scissors" against the computer.
Steps:
Use random.choice() to have the computer randomly choose rock, paper, or scissors.
Compare the player's choice with the computer's choice to determine the winner.

'''
#   ROCK PAPER SCISSORS
'''
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = input('Enter rock , paper, or scissors:   ').lower()
if user_choice == computer_choice:
    print(f'Both chose {user_choice}. Its a Tie!!..')
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
    print(f'You win! {user_choice} beats {computer_choice}')
else:
    print(f'You Lost! {computer_choice} beats {user_choice}')
'''
# ******************************************************************************
# ******************************************************************************
# ******************************************************************************
print(f'--------------------------------------------------')
print(f'            Welcome To Rock, Paper, Scissors       ')
print(f'--------------------------------------------------')
gamecount = 0
player_wins = 0
python_wins = 0
ties = 0


def rps():

    python = random.choice('123')
    python = int(python)

    player = input(
        '\nChoose..\n1 for ROCK..\n2 for PAPER...\n3. for SCISSORS..\nQ to quit()..\n\n')
    if player not in ['1', '2', '3', 'q']:
        print('Choice not in options..\n')
        return rps()
    if player.lower() == "q":
        sys.exit('\nBye!!.. \n')
    print(f'\nPython chose: {python}')
    print(f'You chose:  {player}\n')

    def decide_winner():

        global gamecount
        global player_wins
        global ties
        global python_wins

        gamecount += 1

        if player == '1' and python == '3':
            player_wins += 1
            return f'Player wins..\n'
        elif player == "2" and python == "1":
            player_wins += 1
            return f'Player wins..\n'
        elif player == '3' and python == '2':
            player_wins += 1
            return f'Player wins..\n'
        elif player == python:
            ties += 1
            return f"It's a Tie!!.."
        else:
            python_wins += 1
            return f'Python Wins!!..\n'

    result = decide_winner()
    print(result)

    print(f'Do you want to playagain?   ')
    playagain = True
    while playagain:
        play = input('Y to continue playing...\nQ to quit..\n\n')
        if play.lower() not in ['q', 'y']:
            continue
        else:
            break
    if play.lower() == 'y':
        return rps()
    else:
        print('🎉🎉🎉🎉🎉🎉')
        print(f'Thanks for playing Rock, Paper, Scissors!!..')
        print(f'Bye..\n')
        playagain = False

    print(f'\n----------------------------------------')
    print(f'Total game count: {gamecount} times')
    print(f'Your won: {player_wins} times')
    print(f'Python wins: {python_wins} times')
    print(f'Player and Python tied: {ties} times')
    sys.exit(f'------------------------------------------\n')


rps()
