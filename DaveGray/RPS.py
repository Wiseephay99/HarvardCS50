
import sys
import random
from enum import Enum

print()
print('--------------------------------------------')  
print('|            Rock Paper Scissors Game       |')
print('--------------------------------------------')  

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# print(RPS(2))
# print(RPS['ROCK'])
# print(RPS.ROCK)
# print(RPS.ROCK.value)
# sys.exit()
playagain = True
while playagain:
    playerchoice = input('Enter ...\n1. for Rock 🪨,\n2. for Paper 📃 , or\n3. for Scissors ✂️:\n\n')
    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit('You must enter 1,2, or 3.')

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print('-----------------------------------')
    # print(f'You chose: {playerchoice}')
    # print(f'Python chose: {playerchoice}')
    print(f'You chose: {str(RPS(player)).replace('RPS.','')}')
    print(f'Python chose: {str(RPS(computer)).replace('RPS.','')}')
    print('-----------------------------------')

    if player == 1 and computer == 3:
        print('🏆🏆 You Win! 🏆🏆\n')
    elif player == 2 and computer == 1:
        print('🏆🏆 You Win! 🏆🏆\n')
    elif player == 3 and computer == 2:
        print('🏆🏆 You Win! 🏆🏆\n')
    elif player == computer:
        print('😲 Tie Game! 🤓\n')
    else:
        print('🐍 Python Wins!\n')
    
    playagain = input('\nPlay again? \nY for Yes or \nQ to Quit \n\n')
    if playagain.lower() == 'y':
        continue
    else:
        print(f'\n🎉🎉🎉🎉🎉')
        print('Thank You for playing!')
        playagain = False

sys.exit(f'Bye!👋👋 \n')


