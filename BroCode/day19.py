import sys
from enum import Enum
import math
import time
import random

'''
print()
# Python slot machine program
# python bank app

print()


def spin_row():
    symbols = ['🍉', '🍎', '🍍', '🍌', '🔔', '⭐']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    time.sleep(2)
    print('Spinning 🔃 🔃')
    time.sleep(2)
    return results


def display_row():
    print('--------------------')
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍎':
            return bet * 6
        elif row[0] == '🍍':
            return bet * 7
        elif row[0] == '🍌':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 15
        elif row[0] == '⭐':
            return bet * 20
    else:
        return 0


balance = 100
print('-------------------------------------')
print('Welcome to Python Slot Machine Game 🎰')
print('Symbols:  🍉 🍎 🍍 🍌 🍉 🔔 ⭐ ')

while balance > 0:
    print('-------------------------------------')
    print(f'Current Balance is: ${balance:.2f}')
    bet = input('Enter bet amount (q to quit):  ')

    if bet.lower() == 'q':
        break
    if not bet.isdigit():
        print('Invalid bet amount! Enter a valid bet amount...')
        continue

    bet = int(bet)

    if bet > balance:
        print(f'Insufficient Funds')
        continue
    elif bet <= 0:
        print('Bet amount cannot be less than 0')
        continue
    balance -= bet

    row = spin_row()

    display_row()

    payout = get_payout(row, bet)
    # print(payout)
    if payout > 0:
        balance += payout
        print(f'Congradulations..You Won: {payout:.2f}')
    else:
        print('Sorry... You lost in this round')

print('\n-------------------------------------')
print(f'Game Over 🧸🧸 Current Balance: ${balance:.2f}')
print('-------------------------------------')

'''
# =================================================================
# =================================================================
'''
# Python Bank Application


def check_balance(balance):
    print(f'Your current balance is: ${balance:.2f}')


def deposit():
    while True:
        amount = input('Enter amount to deposit:    ')
        if not amount.isdigit():
            print('Invalid deposit amount.')
            continue

        amount = float(amount)

        if amount <= 10:
            print('Deposit amount must be greater than $10')
        else:
            print(f'You have successfully deposited ${amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        try:
            amount = input('Enter amount to withdraw:(q to quit)    ')
            if amount.lower() == 'q':
                break

            amount = float(amount)

            if amount > balance:
                print('Insufficient Funds ')
                continue
            if amount <= 10:
                print('Withdrawal amount must be greater $10')
                continue
            else:
                print(f'You have successfully withdrawn ${amount:.2f}')
                return amount
        except ValueError:
            print('Invalid withdrawal amount.')
            continue


def main():
    balance = 0

    while True:
        print('--------------------')
        print('Bank Application')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        print('--------------------')

        choice = input('\nSelect your choice (1-4)(q to quit): ')

        if choice.lower() == 'q':
            break

        choice = int(choice)

        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            balance += deposit()

        elif choice == 3:
            balance -= withdraw(balance)

        elif choice == 4:
            break

    print(f'\nExiting Bank Application..Goodbye!!!\n')


if __name__ == "__main__":
    main()
'''
# =================================================================
# =================================================================
'''
# while loop

# rock paper scissors
print('-----------------------------------')
print('ROCK 🪨  PAPER 📜 SCISSORS ✂️  GAME')
print('-----------------------------------')


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


while True:

    player = input(
        'Choose...\n1. for Rock\n2. for Paper\n3. for Scissors\nQ to quit...\n\n')
    computer = random.choice('123')
    computer = int(computer)
    if player.lower() == 'q':
        break

    elif not player.isdigit():
        print(f'{player} is an Invalid Option..')
        continue

    player = int(player)

    if player < 1 or player > 3:
        break

    print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", " ")}')
    print(f'Computer chose: {str(RPS(computer)).replace("RPS.", " ")}\n')

    if player == 1 and computer == 2:
        print(f"🏆 🏆 Player Won 🏆 🏆")
    elif player == 2 and computer == 3:
        print(f"🏆 🏆 Player Won 🏆 🏆")
    elif player == 3 and computer == 1:
        print(f"🏆 🏆 Player Won 🏆 🏆")
    elif player == computer:
        print(f'🪢 🪢  It is a Tie 🪢 🪢 ')
    else:
        print(f"👨‍💻👨‍💻 Computer Wins 👨‍💻🧑‍💻")
    print()


print('\nGame Over...Exiting Rock🪨  Paper 📜  Scissors ✂️ \n')
'''
# =================================================================
# =================================================================

'''
# functions

# rock paper scissors
print('-----------------------------------')
print('ROCK 🪨  PAPER 📜 SCISSORS ✂️  GAME')
print('-----------------------------------')

player_wins = 0
computer_wins = 0
game_count = 0
player_and_computer_ties = 0


def play():
    global player_wins, computer_wins, player_and_computer_ties, game_count

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player = input(
        'Choose...\n1. for Rock 🪨 \n2. for Paper 📜 \n3. for Scissors ✂️ \nQ to quit...\n\n')
    computer = random.choice('123')
    computer = int(computer)
    if player.lower() == 'q':
        sys.exit('\nGame Over...Exiting Rock🪨  Paper 📜  Scissors ✂️ \n')

    elif not player.isdigit():
        print(f'{player} is an Invalid Option..\n')
        return play()

    player = int(player)

    if player < 1 or player > 3:
        play()

    def display_choices():
        print(f'\nPlayer chose: {str(RPS(player)).replace("RPS.", " ")}')
        print(
            f'Computer chose: {str(RPS(computer)).replace("RPS.", " ")}\n')

    display_choices()

    def decide_winner():
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

    result = decide_winner()

    game_count += 1

    if result == 1:
        player_wins += 1
        print(f"🏆 🏆 Player Won 🏆 🏆")
    elif result == 2:
        player_and_computer_ties += 1
        print(f'🪢 🪢  It is a Tie 🪢 🪢 ')
    elif result == 0:
        computer_wins += 1
        print(f"👨‍💻👨‍💻 Computer Wins 👨‍💻🧑‍💻")

    print()
    print('Do you want to continue playing? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue Q to Quit:    ')
        if play_again not in ['q', 'y']:
            continue
        else:
            print(f'\nTotal Game Count: {game_count}')
            print(f'Player won: {player_wins} round(s)')
            print(f'Computer won: {computer_wins} round(s)')
            print(
                f'Player and Computer Tied: {player_and_computer_ties} round(s)')
            break
    if play_again.lower() == 'y':
        print()
        return play()
    else:
        print('\n👋 👋 🎉 🎉 🎉 🎉 🎉')
        print('Thanks for playing ROCK,PAPER, SCISSORS!\n')
        sys.exit(f'Bye!👋')


play()
'''

# =================================================================
# =================================================================
# python rock paper scissors
'''
emojis = {
    'r': '🪨 🪨',
    'p': '📜 📜',
    's': '✂️ ✂️'
}
emojis.keys()
choices = ['r', 'p', 's']

while True:
    print('--------------------------------------------')
    choice = input('choose rock paper or scissors(r/p/s):  ').lower()
    if choice.lower() == 'q':
        break

    if choice not in choices:
        print('Invalid choice')
        continue
    computer = random.choice(choices)

    # print(f'\nPlayer chose: {emojis.get(choice)}')
    # print(f'Computer chose: {emojis.get(computer)}\n')
    print(f'\nPlayer chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        print('Player Won')
    elif choice == computer:
        print('It is a tie')
    else:
        print('Computer Wins')

    print()

    should_continue = input('Continue? (y/n):')
    if should_continue == 'y':
        continue
    else:
        break

print('\nGame Over...Exiting Rock, Paper Scissors\n')

'''

# =================================================================
# =================================================================

# python rock paper scissors


def get_user_input():

    while True:
        print('\n--------------------------------------------')
        choice = input('choose rock paper or scissors(r/p/s):  ').lower()
        if choice.lower() == 'q':
            break

        elif choice not in choices:
            print('Invalid choice')
            continue

        return choice


def display_choices(choice, computer):
    print(f'\nPlayer chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    global player_wins, gamecount, computer_wins, game_ties
    gamecount += 1
    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        player_wins += 1
        print('Player Won')
    elif choice == computer:
        game_ties += 1
        print('It is a tie')
    else:
        computer_wins += 1
        print('Computer Wins')

    print()


emojis = {
    'r': '🪨 🪨',
    'p': '📜 📜',
    's': '✂️ ✂️'
}
emojis.keys()
choices = ['r', 'p', 's']

player_wins = 0
gamecount = 0
player_wins = 0
computer_wins = 0
game_ties = 0


def play_rps():
    global player_wins, gamecount, computer_wins, game_ties

    while True:
        choice = get_user_input()

        computer = random.choice(choices)

        display_choices(choice, computer)

        decide_winner(choice, computer)

        should_continue = input('Continue? (y/n):')
        if should_continue == 'y':
            play_rps()
        elif should_continue == "n":
            break
        else:
            continue

    print(f'\n--------------------------------------------------')
    print(f'Game Count: {gamecount}')
    print(f'Player won: {player_wins} time(s)')
    print(f'Computer won: {computer_wins} time(s)')
    print(f'Player and Computer Tied: {game_ties} times(s)')

    print('\nGame Over...Exiting Rock, Paper Scissors\n')


if __name__ == "__main__":
    play_rps()
