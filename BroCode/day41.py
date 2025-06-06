import math
import random
import time
import sys
from enum import Enum
print()

#################################################################################################
#################################################################################################

'''
# rock paper scissors
def rps():
    player_wins = 0
    computer_wins = 0
    game_ties = 0
    game_count = 0

    def play():

        nonlocal player_wins, computer_wins, game_ties, game_count

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player = input(
            'Choose...\n1. for Rock 🪨 🪨  \n2. for Paper 📃📜\n3. for Scissors ✂️ ✂️\nQ. to Quit...\n\n')
        if player.lower() == 'q':
            sys.exit('\nThanks for playing Rock Paper Scissors\n')
        player = int(player)
        if 1 < player > 3:
            print('Invalid Selection')
            return play()

        computer = random.choice('123')
        computer = int(computer)

        print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", '')}')
        print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}\n')

        game_count += 1

        # if player == 1 and computer == 2:
        #     player_wins += 1
        #     print('Player Wins 🎉🎉')
        # elif player == 2 and computer == 3:
        #     player_wins += 1
        #     print('Player Wins 🎉🎉')
        # elif player == 3 and computer == 1:
        #     player_wins += 1
        #     print('Player Wins 🎉🎉')
        # elif player == computer:
        #     game_ties += 1
        #     print('It is a Tie 🤡')
        # else:
        #     computer_wins += 1
        #     print('Computer Wins 🧑‍💻 ')

        def decide_winner(player, computer):
            if player == 1 and computer == 2:
                return 1
            elif player == 2 and computer == 3:
                return 1
            elif player == 3 and computer == 1:
                return 1
            elif player == computer:
                return 2
            else:
                return 0

        result = decide_winner(player, computer)

        if result == 1:
            player_wins += 1
            print('Player Wins 🎉🎉')
        elif result == 2:
            game_ties += 1
            print('It is a Tie 🤡')
        elif result == 0:
            computer_wins += 1
            print('Computer Wins 🧑‍💻 ')

        print()

        print('Do you want to continue? ')
        play_again = True
        while play_again:
            play_again = input('Y to continue Q to quit:  ')
            if play_again.lower() not in ['q', 'y']:
                continue
            else:
                break
        if play_again.lower() == 'y':
            print()
            return play()
        else:
            print(f'\nTotal Game Count: {game_count}')
            print(f'Player Wins: {player_wins}')
            print(f'Computer Wins: {computer_wins}')
            print(f'Game Ties: {game_ties}')
            sys.exit('\nThanks for playing Rock Paper Scissors\n')

    return play()


game = rps()
print(game)
'''

#################################################################################################
#################################################################################################


'''
# ROCK PAPER SCISSRORS == MOSH
emojis = {
    'r': '🪨 🪨',
    'p': '📃 📜',
    's': '✂️ ✂️'
}
heading = f'               🚀 ROCK PAPER SCISSORS 🚀           '
headlen = len(heading)
print(f'{headlen * "*"}')
print(f'{heading}')
print(f'{headlen * "*"}')


while True:
    choice = input('Select rock, paper or scissors (r / p / s):  ')
    choices = ['r', 'p', 's']
    if choice == 'q':
        break

    if choice not in choices:
        print('Invalid Choice!!')
        continue

    computer = random.choice(choices)

    print(f'\nYou Chose: {emojis[choice]}')
    print(f'Computer Chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 's') or
        (choice == 'r' and computer == 's') or
            (choice == 'r' and computer == 's')):
        print('You Win!! 🎉🎉')
    elif choice == computer:
        print('It is a Tie 🤡')
    else:
        print('Computer Wins!! 🧑‍💻')

    print()
    should_continue = input('Continue? (y  / n):  ').lower()
    if should_continue == 'y':
        continue
    else:
        break

print('\nThanks for Playing Rock 🪨 Paper 📜 Scissors ✂️\n')
'''


#################################################################################################
#################################################################################################
'''
def get_user_input():
    while True:
        print('---------------------------------------------------')
        choice = input('Select rock, paper or scissors (r / p / s):  ')
        if choice in choices:
            return choice
        else:
            print('Invalid Choice!! Only choose (r/p/s)')
            continue


def display_choices(choice, computer):
    print(f'\nYou Chose: {emojis[choice]}')
    print(f'Computer Chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    if ((choice == ROCK and computer == PAPER) or
        (choice == PAPER and computer == SCISSORS) or
            (choice == SCISSORS and computer == ROCK)):
        print('You Win!! 🎉🎉')
    elif choice == computer:
        print('It is a Tie 🤡')
    else:
        print('Computer Wins!! 🧑‍💻')


ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

# choices = ['r', 'p', 's']
# choices = [ROCK, PAPER, SCISSORS]
emojis = {
    ROCK: '🪨  🪨',
    PAPER: '📃  📜',
    SCISSORS: '✂️  ✂️'
}

choices = tuple(emojis.keys())

heading = f'               🚀 ROCK PAPER SCISSORS 🚀           '
headlen = len(heading)
print(f'{headlen * "-"}')
print(f'{heading}')
# print(f'{headlen * "*"}')


def game():
    while True:
        choice = get_user_input()

        computer = random.choice(choices)

        display_choices(choice, computer)

        decide_winner(choice, computer)

        print()
        should_continue = input('Continue? (y  / n):  ').lower()
        if should_continue == 'y':
            continue
        else:
            break

    print('\nThanks for Playing Rock 🪨  Paper  📜 Scissors  ✂️\n')


game()
'''

#################################################################################################
#################################################################################################
# Python Slot Machine Game

'''
def spin_row():
    symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('***********************************')
    print('     |       '.join(row))
    print('***********************************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍎':
            return bet * 8
        elif row[0] == '🍌':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 15
        elif row[0] == '🌟':
            return bet * 20
    else:
        return 0


print('---------------------------------------')
print('🎰  Python Slots Machine  🎰')
print('Symbols: 🍉  🍎  🍌  🔔  🌟')


def main():
    balance = 100
    while balance > 0:
        print('---------------------------------------')
        print(f'Your Current Balance is {balance:.2f}')
        bet = input('Enter bet amount (q to quit):  ')

        if bet.lower() == 'q':
            break
        if not bet.isdigit():
            print('Invalid Bet Amount!!')
            continue
        bet = float(bet)
        if bet > balance:
            print(f'Insufficent Balance!! Current Balance is {balance:.2f}')
            continue
        if bet == 0:
            print('Bet cannot be a 0')
            continue
        if bet < 0:
            print('Bet cannot be a NEGATIVE NUMBER\n')
            continue
        if bet < 4:
            print('Minimum bet amount is $4 ')
            continue
        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Congrats 🎉 You Won: ${payout:.2f}')
            balance += payout
        else:
            print('Sorry!! You did not win anything in this round!! ')

        if balance == 0:
            print(
                '\nYou ran out of Betting Funds  😔 !! \nBet Luck Next Time 🤞 !! \nExiting Application 👋 \n')

    print('Thanks for playing  🎰 Python Slots Machine 🎰\n')


if __name__ == "__main__":
    main()
    
'''

#################################################################################################
#################################################################################################

# Bank Application


def check_balance(balance):
    print(f'\nCurrent Account Balance is ${balance:.2f}')


def deposit():
    while True:
        amount = input('Enter the amount to deposit:    ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            return None  # Return None instead of calling main()
        if not amount.isdigit():
            print('Invalid Deposit Amount!!')
            continue
        amount = float(amount)
        if amount == 0:
            print('Deposit cannot be 0')
        elif amount <= 0:
            print('Deposit cannot be a NEGATIVE number!!')
            continue
        elif amount <= 10:
            print('Minimum deposit is $10')
            continue
        else:
            print(f'Successfully Deposited ${amount:.2f} ✅')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter the amount to withdraw:    ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            return None  # Return None instead of calling main()
        if not amount.isdigit():
            print('Invalid Withdrawal Amount!!')
            continue
        amount = float(amount)
        if amount > balance:
            print('Insufficient Funds ❌')
            continue
        if amount == 0:
            print('Withdrawal amount cannot be 0')
        elif amount <= 0:
            print('Withdrawal amount cannot be a NEGATIVE number!!')
            continue
        elif amount <= 50:
            print('Minimum withdrawal is $50')
            continue
        else:
            print(f'Successfully Withdrawn ${amount:.2f} ✅')
            return amount


print('Welcome to Python Banking Application')


def main():
    balance = 0
    while True:
        print('----------------------------------')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('\nSelect your choice (q to quit): ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice!!')
            continue
        choice = int(choice)
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            # balance += deposit()

            # result = deposit()
            # if result is None:
            #     break
            # balance += result

            result = deposit()
            if result:
                balance += result

        elif choice == 3:
            # balance -= withdraw(balance)
            result = withdraw()
            if result is None:
                break
            balance -= result

        elif choice == 4:
            break
        else:
            print('Invalid Selection!!!!')

    print('\n-------------------------------------------')
    print('🏦 Exiting Python Easy Bank Application 🪙')
    time.sleep(2)
    print('Bye  👋 👋 \n')
    print('\nThanks for using \n')


if __name__ == "__main__":
    main()
