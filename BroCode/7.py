import random
import sys
import math
from enum import Enum
print()

'''
def rps():

    # rock paper scissors
    # choices = ['1', '2', '3']
    print('*****************************************')
    print(f'    Welcome to Rock Paper Scissors      ')
    print('*****************************************')

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS.PAPER)
    # print(RPS(2))
    # print(RPS['PAPER'])
    # print(RPS.ROCK.PAPER)

    player = input(
        f'Choose...\n1 for Rock...\n2 for Paper...\n3 for Scissors...\n\n')
    computer = random.choice('123')
    computer = int(computer)
    if player.lower() == 'q':
        sys.exit(f'Thanks for playing Rock,Paper scissors....\n')

    # if player not in choices:
    if player not in ['1', '2', '3']:
        print(f'Invalid choice..\n')
        rps()
    player = int(player)
    # print(f'\nPlayer Chose: {player}')
    # print(f'Computer chose: {computer}\n')
    print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", "")}')
    print(f'Computer chose: {str(RPS(computer)).replace('RPS.', '')}\n')

    def decide_winner():
        if player == '1' and computer == '2':
            return f'Plaer Wins!....\n'
        elif player == '2' and computer == '3':
            return f'Plaer Wins!....\n'
        elif player == '3' and computer == '3':
            return f'Plaer Wins!....\n'
        elif player == computer:
            return f'It is a Tie...\n'
        else:
            return f'Computer Wins..\n'

    result = decide_winner()
    print(result)

    print(f'Do you want to playagain?   ')
    playagain = True
    while playagain:
        playagain = input('Y to continue...\nQ to Quit...\n\n')
        if playagain.lower() not in ['q', 'exit', 'y']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        rps()
    # elif playagain.lower() == 'q' or playagain.lower() == 'exit':
    else:
        print(f'Thanks for Using RPS..\n')
        playagain = False


rps()
'''

# ========================================================================
# ========================================================================
# ========================================================================

choices = ['r', 'p', 's']

emojis = {'r': '🪨🪨', 'p': '📃📜', 's': '✂️✂️'}


def get_user_choice():
    global count
    choice = input('choose rock, paper or scissors (r, p, s): ').lower()
    if choice in ['q', 'exit']:
        display_results()
    if choice not in choices:
        print('Invalid choice!\n')
    else:
        count += 1
    return choice


def display_choices(choice, computer):
    print(f'\nYou chose: {choice}')
    print(f'Computer chose: {computer}\n')


def decide_winner(choice, computer):
    global count, player_wins, computer_wins, game_ties
    if ((choice == 'r' and computer == 'p') or
        (choice == 'p' and computer == 's') or
            (choice == 's' and computer == 'r')):
        player_wins += 1
        print('You Win...\n')
    elif choice == computer:
        game_ties += 1
        print(f'It is a Tie...\n')
    else:
        computer_wins += 1
        print('Computer Wins!!....\n')


def display_results():
    global count, player_wins, computer_wins, game_ties
    print(f'Total Game count is: {count}')
    print(f'Player Won: {player_wins} time(s)')
    print(f'Computer Won: {computer_wins} time(s)')
    print(f'You and Computer tied {game_ties} time(s)')
    print(f'Thanks for playing Rock paper scissors..\n')


player_wins = 0
computer_wins = 0
game_ties = 0
count = 0


def main():

    print('\n*******************************')
    print('      ROCK PAPER SCISSORS     ')
    print('*******************************\n')
    choice = get_user_choice()
    computer = random.choice(choices)

    display_choices(choice, computer)
    decide_winner(choice, computer)

    should_continue = True
    while should_continue:
        should_continue = input('\nY to continue..\nQ to quit...\n\n')
        if should_continue == 'y':
            main()
        else:
            should_continue = False

    display_results()


if __name__ == "__main__":
    main()
