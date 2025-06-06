from enum import Enum
import math
import random

import sys
print()
######################################################################
######################################################################
######################################################################
'''
play = True
while play:

    player = input(
        'Choose...\n1. for Rock 🪨 🪨\n2. for Paper 📜📃\n3. for scissors ✂️ ✂️...\n\n')
    if player not in ['1', '2', '3']:
        print('You must enter 1 2 or 3 only')
        continue

    player = int(player)

    computer = random.choice('123')
    computer = int(computer)

    print(f'\nPlayer chose: {player}')
    print(f'Computer chose: {computer}\n')

    if player == 1 and computer == 3:
        print(f'🎉🎉 Player Wins')
    elif player == 2 and computer == 1:
        print(f'🎉🎉 Player Wins')
    elif player == 3 and computer == 2:
        print(f'🎉🎉 Player Wins')
    elif player == computer:
        print(f'😲😲😲 It is a tie')
    else:
        print(f'🐍🐍 Python Wins')
    print()

    playagain = input('Playagain?\nY to continue\nN to quit \n')
    if playagain.lower() == 'y':
        print()
        continue
    else:
        print(f'\n🎉🎉🎉🎉🎉🎉')
        print('Thanks for playing rps')
        print('Bye 👋👋\n')
        play = False
'''
######################################################################
######################################################################
######################################################################
'''
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print((RPS.ROCK))
# print((RPS.ROCK.value))
# print((RPS(2)))
# print((RPS['ROCK']))
# sys.exit()

play = True
while play:

    player = input(
        'Choose...\n1. for Rock 🪨 🪨\n2. for Paper 📜📃\n3. for scissors ✂️ ✂️...\n\n')
    if player not in ['1', '2', '3']:
        print('You must enter 1 2 or 3 only')
        continue

    player = int(player)

    computer = random.choice('123')
    computer = int(computer)

    print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", '')}')
    print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}\n')

    if player == 1 and computer == 3:
        print(f'🎉🎉 Player Wins')
    elif player == 2 and computer == 1:
        print(f'🎉🎉 Player Wins')
    elif player == 3 and computer == 2:
        print(f'🎉🎉 Player Wins')
    elif player == computer:
        print(f'😲😲😲 It is a tie')
    else:
        print(f'🐍🐍 Python Wins')
    print()

    playagain = input('Playagain?\nY to continue\nN to quit \n')
    if playagain.lower() == 'y':
        print()
        continue
    else:
        print(f'\n🎉🎉🎉🎉🎉🎉')
        print('Thanks for playing rps')
        print('Bye 👋👋\n')
        play = False
'''

######################################################################
######################################################################
######################################################################
'''
game_count = 0
player_wins = 0
python_wins = 0
ties = 0


def rps():
    global game_count, player_wins, python_wins, ties

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player = input(
        'Choose...\n1. for Rock 🪨 🪨\n2. for Paper 📜📃\n3. for scissors ✂️ ✂️...\n\n')
    if player.lower() == 'q':
        sys.exit('Thanks for playing RPS')

    if player not in ['1', '2', '3']:
        print('You must enter 1 2 or 3 only')
        return rps()
    
    # if not player.isdigit():
    #     print(f'{player} is not a valid selection')
    #     return rps()
    # if player < 1 or player > 2:
    #     print(f'{player} is invalid selection')
    #     return rps()

    player = int(player)
    computer = random.choice('123')
    computer = int(computer)

    print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", '')}')
    print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}\n')

    def decide_winner(player, computer):
        global game_count, player_wins, python_wins, ties
        if player == 1 and computer == 3:
            player_wins += 1
            return f'🎉🎉 Player Wins'
        elif player == 2 and computer == 1:
            player_wins += 1
            return f'🎉🎉 Player Wins'
        elif player == 3 and computer == 2:
            player_wins += 1
            return f'🎉🎉 Player Wins'
        elif player == computer:
            ties += 1
            return f'😲😲😲 It is a tie'
        else:
            python_wins += 1
            return f'🐍🐍 Python Wins'

    game_count += 1

    result = decide_winner(player, computer)
    print(result)
    print()

    print('Do you want to playagain? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue...N to quit \n').lower()
        if play_again not in ['y', 'n', 'q']:
            print()
            continue
        else:
            break

    if play_again.lower() == 'y':
        print()
        return rps()
    else:
        print('-----------------------------------')
        print(f'Game count: {game_count}')
        print(f'Player Wins: {player_wins}')
        print(f'Python Wins: {python_wins}')
        print(f'Game Ties: {ties}')
        print('-----------------------------------')
        print(f'\n🎉🎉🎉🎉🎉🎉')
        print('Thanks for playing rps')
        print('Bye 👋👋\n')
        sys.exit()

play_rps()
'''
######################################################################
######################################################################
######################################################################

'''
def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    ties = 0

    def play_rps():
        nonlocal game_count,  player_wins, python_wins, ties

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player = input(
            'Choose...\n1. for Rock 🪨 🪨\n2. for Paper 📜📃\n3. for scissors ✂️ ✂️...\n\n')
        if player.lower() == 'q':
            sys.exit('Thanks for playing RPS')

        if player not in ['1', '2', '3']:
            print('You must enter 1 2 or 3 only')
            return rps()

        # if not player.isdigit():
        #     print(f'{player} is not a valid selection')
        #     return rps()
        # if player < 1 or player > 2:
        #     print(f'{player} is invalid selection')
        #     return rps()

        player = int(player)
        computer = random.choice('123')
        computer = int(computer)

        print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", '')}')
        print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}\n')

        def decide_winner(player, computer):
            nonlocal game_count
            nonlocal player_wins
            nonlocal python_wins
            nonlocal ties

            if player == 1 and computer == 3:
                player_wins += 1
                return f'🎉🎉 Player Wins'
            elif player == 2 and computer == 1:
                player_wins += 1
                return f'🎉🎉 Player Wins'
            elif player == 3 and computer == 2:
                player_wins += 1
                return f'🎉🎉 Player Wins'
            elif player == computer:
                ties += 1
                return f'😲😲😲 It is a tie'
            else:
                python_wins += 1
                return f'🐍🐍 Python Wins'
        game_count += 1

        result = decide_winner(player, computer)
        print(result)
        print()

        print('Do you want to playagain? ')
        play_again = True
        while play_again:
            play_again = input('Y to continue...N to quit \n').lower()
            if play_again not in ['y', 'n', 'q']:
                print()
                continue
            else:
                break

        if play_again.lower() == 'y':
            print()
            return play_rps()
        else:
            print('\n-----------------------------------')
            print(f'Total Games Played: {game_count}')
            print(f'Player Wins: {player_wins}')
            print(f'Python Wins: {python_wins}')
            print(f'Ties: {ties}')
            print('-----------------------------------')
            print(f'\n🎉🎉🎉🎉🎉🎉')
            print('Thanks for playing rps')
            print('Bye 👋👋\n')
            sys.exit()
    play_rps()


game = rps()
game()
'''

######################################################################
######################################################################
######################################################################
