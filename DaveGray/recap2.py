import sys
import random
from enum import Enum

print()


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print()
# print(RPS(2))
# print(RPS.PAPER)
# print(RPS.PAPER.name)
# print(RPS.PAPER.value)
# print(RPS['PAPER'])
# print(RPS['PAPER'].value)
# print(RPS(2).name)
# print(RPS(2).value)


print()

playerchoice = input(
    'Enter...\n1 for Rock🪨 🪨..\n2 for Paper📃📜📄..\n3 for Scissors✂️ ✂️:..\n\n')
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit(f'You must enter 1, 2 or 3.. ')

computerchoice = random.choice("123")

computer = int(computerchoice)

# print(f'\nYou chose: {player}')
# print(f'Computer chose: {computer}..\n')
print(f'\nYou chose: {str(RPS(player)).replace('RPS.', '')}')
print(f'Computer chose: {str(RPS(computer)).replace('RPS.', '')}..\n')


if player == "1" and computer == '3':
    print(f'Player Wins! 🎉🎉🎉🎉 \n')
elif player == "2" and computer == "1":
    print(f'Player Wins! 🎉🎉🎉🎉 \n')
elif player == "3" and computer == "2":
    print(f'Player Wins! 🎉🎉🎉🎉 \n')
elif player == computer:
    print(f'Player and Computer Tied! 🪢🪢🪢🪢 \n')
else:
    print('Computer Wins! 🐍🐍🐍🐍 \n')
