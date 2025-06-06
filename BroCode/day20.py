import random
import sys


print(f'--------------------------------------------------')
print(f'|       Welcome to Guess Number🔢 Game           |')
print(f'--------------------------------------------------\n')

print(f'\nThis is Guess Number Game..\nYou Enter a range of two numbers and python will \nselect a random number which you will guess...\nif you guess right...you win , otherwise you loose...\n')
ready = input(
    'Are you ready to start?.. (Y to Enter Game ..Q to Quit()..\n\n')
if ready.lower() in ['Q', 'q']:
    sys.exit(F'\nBye!👋\n')

playagain = True
while playagain:
    try:
        num1 = float(
            input(f'\nEnter 1st range of number python to choose from:  '))
        num2 = float(
            input(f'Enter 2nd range of number python to choose from:  '))
    except ValueError:
        print('\nEnter a valid choice!\n')
        continue
    except (KeyboardInterrupt, EOFError, SystemExit, Exception) as e:
        print('\n\nExiting the game...\n')
        print('\nBye!👋\n')
        sys.exit()

    if num1 > num2:
        print(f'First Number should be less than Second Number!')
        continue
    elif num1 == num2:
        print(f'Both numbers are the same!')
        continue
    elif num1 < 0 or num2 < 0:
        print(f'Negative numbers are not allowed!')
        continue
    elif num1 == 0 or num2 == 0:
        print(f'Number range should not be zero!!')
        continue
    elif num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)

    python_num = random.randint(num1, num2)

    play = True
    while play:
        user_num = input(
            f'\nGuess a random Number between {num1} and {num2}?..   ')
        if user_num.lower() in ['q', 'Q']:
            print('\nExiting the game...\n')
            print('\nBye!👋\n')
            sys.exit()
        try:
            user_num = float(user_num)
        except ValueError:
            print('\nEnter a valid choice!\n')
            continue

        user_num = int(user_num)

        if user_num < num1 or user_num > num2:
            print(f'{user_num} is out of your choosen range!')
            print(f'Please try again with a number between {num1} and {num2}')
            continue
        elif user_num == python_num:
            print(
                f'\nCorrect Guess! You won!..\nGuessed number was {python_num}..\n')
            playagain = False
            progress = input(f'Want to play again? (Y/N):  ').lower()
            if progress == 'y':
                playagain = True
            elif progress == "n":
                play = False
                playagain = False
            else:
                continue
        elif user_num != python_num:
            if user_num < python_num:
                print(f'\nIncorrect Guess! Try Guessing a Higher Number\n')
            elif user_num > python_num:
                print(f'\nIncorrect Guess! Try Guessing a Lower Number\n')

else:
    print(f'Exiting the game...\n')
    print('\nBye!👋\n')
    sys.exit()
