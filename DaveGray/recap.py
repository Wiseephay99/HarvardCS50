from enum import Enum
import sys
import random

print()

# ****************************************************************
# ****************************************************************
'''greeting = 'Hello Wise'
print(greeting)
line01 = '***********************'
line02 = '*                     *'
line03 = '*        Welcome      *'

print(line01)
print(line02)
print(line03)
print(line02)
print(line01)

meaning = 42
# If else:
if meaning > 10:
    print("\nRight On!\n")
else:
    print('\nNot Today!\n')
# Tenary Operator
print("\nRight On!\n") if meaning > 10 else print('\nNot Today!\n')


'''


# ****************************************************************

'''print(f'\nRock,Paper,Scissors\n')

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# print(RPS(2))
# print(RPS['ROCK'])
# print(RPS['PAPER'])
# print(RPS.ROCK)
# print((RPS.ROCK.value))

print()
user = input(
    'Choose..\n1. for Rock 🪨 ...\n2. for Paper 📃 ..\n3. for Scissors ✂️ ..\n\n')
user = int(user)

if user < 1 or user > 3:
    sys.exit('\nOnly Enter 1, 2 or 3 🔢..\n')

python = random.choice('123')
python = int(python)

# print(f'\nYou chose: {user}')
# print(f'Python chose: {python}\n')
print(f'\nYou chose: {str(RPS(user)).replace('RPS.', '')}')
print(f'Python chose: {str(RPS(python)).replace('RPS.', '')}\n')

if user == '1' and python == "2":
    print(f'🏆🏆You Won!!🎉🎉\n')
elif user == "2" and python == "3":
    print(f'🏆🏆You Won!!🎉🎉\n')
elif user == "3" and python == "1":
    print(f'🏆🏆You Won!!🎉🎉\n')
elif user == python:
    print(f'It\'s a Tie 🪢\n')
else:
    print(f'🐍 Python Wins!\n')
'''
# ****************************************************************

print(f'\nRock,Paper,Scissors.\n'.upper().center(100, "="))


def rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playagain = True
    while playagain:
        user = input(
            '\nChoose..\n1. for Rock 🪨 ...\n2. for Paper 📃 ..\n3. for Scissors ✂️ ..\n\n')

        # if user < 1 or user > 3:
        #     sys.exit('\nOnly Enter 1, 2 or 3 🔢..\n')

        if user not in ['1', '2', '3']:
            print('\nOnly Enter 1, 2 or 3 🔢..\n')
            return rps()

        user = int(user)

        python = random.choice('123')
        python = int(python)

        # print(f'\nYou chose: {user}')
        # print(f'Python chose: {python}\n')
        print(f'\nYou chose: {str(RPS(user)).replace('RPS.', '')}')
        print(f'Python chose: {str(RPS(python)).replace('RPS.', '')}\n')

        if user == '1' and python == "2":
            print(f'🏆🏆You Won!!🎉🎉\n')
        elif user == "2" and python == "3":
            print(f'🏆🏆You Won!!🎉🎉\n')
        elif user == "3" and python == "1":
            print(f'🏆🏆You Won!!🎉🎉\n')
        elif user == python:
            print(f'It\'s a Tie 🪢\n')
        else:
            print(f'🐍 Python Wins!\n')

        # playagain = input(
        #     'Do you want to play again?..\nY to continue..\nQ to Quit..\n\n')
        # if playagain.lower() == 'y':
        #     continue
        # else:
        #     print(f'\n🎉🎉🎉🙌🙌🎉🎉🎉🥳🥳')
        #     print('Thanksfor playing Rock, Paper, Scissors!')
        #     sys.exit('Bye! 👋🌊👋\n')

        print(f'Do you want to play again?..')
        playagain = input('\nY to continue..\nQ to Quit..\n\n')
        if playagain.lower() == 'y':
            return rps()
        else:
            print(f'\n🎉🎉🎉🙌🙌🎉🎉🎉🥳🥳')
            print('Thanksfor playing Rock, Paper, Scissors!')
            sys.exit('Bye! 👋🌊👋\n')


rps()
