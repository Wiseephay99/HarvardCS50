import string
import sys
import random
import time
from enum import Enum
print()
#################################################################
'''
# rock paper scissors


print("Welcome to ROCK PAPER SCISSORS")


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


while True:
    player = input(
        'Choose....\n1. for ROCK...\n2. PAPER...\n3. for SCISSORS...\nQ to quit...\n\n')
    if player.lower() == 'q':
        break
    if player not in ['1', '2', '3']:
        sys.exit(f'\nInvalid input!! Choose 1 2 or 3')
    player = int(player)

    computer = random.choice('123')
    computer = int(computer)

    print(f'\nPlayer Chose: {str(RPS(player)).replace("RPS.", " ")}')
    print(f'Computer Chose: {str(RPS(computer)).replace("RPS.", " ")}\n')

    if player == 1 and computer == 2:
        print('Player Wins 🎉🎉')
    elif player == 2 and computer == 3:
        print('Player Wins 🎉🎉')
    elif player == 3 and computer == 1:
        print('Player Wins 🎉🎉')
    elif player == computer:
        print('It is a Tie...\n')
    else:
        print('Computer Wins 🧑‍💻🧑‍💻\n')

sys.exit('\nThanks for playing Rock Paper Scissors...\n')
print()

'''
#################################################################

'''
# rock paper scissors

print('--------------------------------')
print("Welcome to ROCK PAPER SCISSORS")


def play():

    player_wins = 0
    computer_wins = 0
    gamecount = 0
    game_ties = 0

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    def rps():

        nonlocal player_wins, computer_wins, gamecount, game_ties

        print('--------------------------------')
        player = input(
            'Choose....\n1. for ROCK...\n2. for PAPER...\n3. for SCISSORS...\nQ to quit...\n\n')
        if player.lower() == 'q':
            sys.exit('\nThanks for playing Rock Paper Scissors...\n')

        if player not in ['1', '2', '3']:
            print(f'\nInvalid input!! Choose 1 2 or 3')
            return rps()

        player = int(player)

        computer = random.choice('123')
        computer = int(computer)

        print(f'\nPlayer Chose: {str(RPS(player)).replace("RPS.", " ")}')
        print(f'Computer Chose: {str(RPS(computer)).replace("RPS.", " ")}\n')

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

        gamecount += 1
        result = decide_winner(player, computer)
        if result == 1:
            player_wins += 1
            print('Player Wins 🎉 🎉 ')
        elif result == 2:
            game_ties += 1
            print('It is a Tie 🪢 🪢')
        else:
            computer_wins += 1
            print('Computer Wins 🧑‍💻 🧑‍💻')

        print('Do you want to continue playing? ')
        play_again = True
        while play_again:
            play_again = input('Y to continue playing..Q to quit:  ')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == 'y':
            print()
            return rps()
        else:
            print(f'\nTotal Gamecount {gamecount}')
            print(f'Total Game Ties: {game_ties}')
            print(f'Total Player Wins: {player_wins}')
            print(f'Total Computer Wins: {computer_wins}\n')
            print('Thanks for playing Rock Paper Scissors...\n')

    return rps()


play()
'''
#################################################################

'''# rock paper scissors

choices = ['r', 'p', 's']
while True:
    print('\n--------------------------------')
    choice = input('Choose rock paper or scissors (r / p / s):  ')
    if choice.lower() == 'q':
        break

    if choice not in choices:
        print('Invalid Choice!! Only choose r p or s')
    computer = random.choice(choices)

    print(f'\nYou chose: {choice}')
    print(f'Computer chose: {computer}\n')

    if ((choice == 'r' and computer == 's') or
        (choice == 'p' and computer == 'r') or
            (choice == 's' and computer == 'p')):
        print('You Win...🎉🎉')
    elif choice == computer:
        print('It is a Tie 🪢')
    else:
        print(f'Computer Wins!! 🏆')
    print()

    should_continue = input('Continue (Y or N): ').lower()
    if should_continue == 'y':
        continue
    else:
        print()
        break

print('Thanks for playing Rock Paper Scissors!!\n')'''

#################################################################


'''
# rock paper scissors


def get_user_input(choices):
    while True:
        print('\n------------------------------------------------')
        choice = input('Choose rock paper or scissors (r / p / s):  ')
        if choice.lower() == 'q':
            break

        if choice in choices:
            return choice
        else:
            print('Invalid Choice!! Only choose r p or s')
            continue


def display_choices(emojis, choice, computer):
    print(f'\nYou chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):

    if ((choice == ROCK and computer == SCISSORS) or
        (choice == PAPER and computer == ROCK) or
            (choice == SCISSORS and computer == PAPER)):
        print('You Win...🎉🎉')
    elif choice == computer:
        print('It is a Tie 🪢')
    else:
        print(f'Computer Wins!! 🏆')
    print()


# choices = ['r', 'p', 's']
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {
    ROCK: "🪨  🪨 ",
    PAPER: "📃  📄  📜",
    SCISSORS: '✂️ ✂️'
}
choices = tuple(emojis.keys())

player_wins = 0
computer_wins = 0
gamecount = 0
game_ties = 0


def play():
    player_wins, computer_wins, gamecount, game_ties

    while True:
        choice = get_user_input(choices)

        computer = random.choice(choices)

        display_choices(emojis, computer, choice)
        decide_winner(choice, computer)

        should_continue = input('Continue (Y or N): ').lower()
        if should_continue == 'y':
            continue
        else:
            print()
            break

    print('Thanks for playing Rock Paper Scissors!!\n')


play()

'''
#################################################################

'''# rock paper scissors


def play():
    while True:
        print('-------------------------------------------------------------------')
        choice = input(
            "What\'s your choice? 'r' for Rock, 'p' for paper or 's' for scissors?:   ")
        if choice not in (['r', 'p', 's']):
            print('Invalid choice Only choose "r", "p", "s" !!')
            return play()
        computer = random.choice(['r', 'p', 's'])

        print(f'\nYou choose: {choice}')
        print(f'Computer chose: {computer}\n')

        if choice == computer:
            return 'It is a Tie 🪢🪢\n'

        elif is_win(choice, computer):
            return 'Player Wins!! 🎉 🎉\n'

        else:
            return 'Computer Wins 🧑‍💻 🧑‍💻\n'


def is_win(player, opponent):
    if ((player == 'r' and opponent == 'p') or (player == 'r' and opponent == 'p') or (player == 'r' and opponent == 'p')):
        return True


result = play()
print(result)
'''
#################################################################

'''
#   python slots machine game
print('Welcome to Python Slots Machine')
print('Symnbols: 🍉  🍌  🍎  🔔  🌟')


def spin_row():
    symbols = ['🍉',  '🍌',  '🍎',  '🔔',  '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('----------------------------------------')
    print('         |       '.join(row))
    print('----------------------------------------')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍌':
            return bet * 7
        elif row[0] == '🍎':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 7
        elif row[0] == '🌟':
            return bet * 7
    return 0


def main():
    balance = 100
    while balance > 0:
        print('----------------------------------------')
        print(f'Current balance is {balance:.2f}')
        bet = input('Enter bet amount (q to quit):   ')
        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print('Invalid Bet amount!! ')
            continue
        bet = int(bet)
        if bet == 0:
            print('Bet amount cannot be 0')
            continue
        if bet < 0:
            print('Bet amount cannot be a NEGATIVE NUMBER!!')
            continue
        if bet < 4:
            print('Minimum bet amount is $4')
            continue

        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Congrats!! You won ${payout:.2f}')
            balance += payout
        else:
            print('Sorry 😔😥 You did not win anything in this round')

    print('\nThanks for using python Slots Machine\n')


if __name__ == "__main__":
    main()
'''

#################################################################

'''
#   Python Easy Banking application
print('-----------------------------------------------------------------')
print('Welcome to 🏦  Python Easy Banking 🏦 Application')


def show_balance(balance):
    print(f'\nCurrrent Balance 💰 ${balance:.2f}')


def deposit():
    while True:
        amount = input('Enter the amount to deosit (q to quit):   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            time.sleep(2)
            return None
        if not amount.isdigit():
            print('Invalid Deposit Amount!! ❌')
            continue
        amount = int(amount)
        if amount < 0:
            print('Deposit cannot be a Ngetive Number!! ❌')
            continue

        elif amount == 0:
            print('Deposit amount cannot be 0 ❌')
            continue

        elif amount < 50:
            print('Minimum Deposit is $50')
            continue
        else:
            print(f'Successfully Deposited ${amount:.2f} ✅')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter the amount to deosit (q to quit):   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            time.sleep(2)
            return None
        if not amount.isdigit():
            print('Invalid Withdrawal Amount!!')
            continue
        amount = int(amount)
        if amount > balance:
            print('Imsufficient Funds!! ❌')
            continue

        if amount < 0:
            print('Withdraw amount cannot be a Negative Number!! ❌')
            continue

        elif amount == 0:
            print('Withdrawal amount cannot be 0 ❌')
            continue

        elif amount < 50:
            print('Minimum Withdrawal amount is $50')
            continue

        else:
            print(f'Successfully Withdrawn ${amount:.2f} ✅')
            return amount


def main():
    balance = 0
    while True:
        print('\n----------- Main Menu ------------')
        print('1. Check Balance 💳 💵')
        print('2. Deposit Funds 💰')
        print('3. Withdraw Funds 🤑')
        print('4. Exit or Q to quit')

        choice = input('\nSelect your choice ( 1-4 ): ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid choice!!')
            continue
        choice = int(choice)
        if choice == 1:
            show_balance(balance)
        elif choice == 2:

            result = deposit()
            if result is not None:
                balance += result

        elif choice == 3:

            result = withdraw(balance)
            if result is not None:
                balance -= result

        elif choice == 4:
            break
        else:
            print('Invalid Choice')
            continue

    print('\nThanks for using Python 🏦 🏦 🏦  Easy Banking  🏦 🏦 🏦 Application\n')


if __name__ == "__main__":
    main()
'''

#################################################################
'''
# Combined Project

#   python slots machine game

print('Welcome to Python Slots Machine')
print('Symnbols: 🍉  🍌  🍎  🔔  🌟')


def spin_row():
    symbols = ['🍉',  '🍌',  '🍎',  '🔔',  '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('----------------------------------------')
    print('         |       '.join(row))
    print('----------------------------------------')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍌':
            return bet * 7
        elif row[0] == '🍎':
            return bet * 7
        elif row[0] == '🔔':
            return bet * 7
        elif row[0] == '🌟':
            return bet * 7
    return 0


def deposit():
    while True:
        amount = input('Enter the amount to deosit (q to quit):   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            time.sleep(2)
            return None
        if not amount.isdigit():
            print('Invalid Deposit Amount!! ❌')
            continue
        amount = int(amount)
        if amount < 0:
            print('Deposit cannot be a Ngetive Number!! ❌')
            continue

        elif amount == 0:
            print('Deposit amount cannot be 0 ❌')
            continue

        elif amount < 50:
            print('Minimum Deposit is $50')
            continue
        else:
            print(f'Successfully Deposited ${amount:.2f} ✅')
            return amount


def show_balance(balance):
    print(f'\nCurrrent Balance 💰 ${balance:.2f}')


def withdraw(balance):
    while True:
        amount = input('Enter the amount to deosit (q to quit):   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            time.sleep(2)
            return None
        if not amount.isdigit():
            print('Invalid Withdrawal Amount!!')
            continue
        amount = int(amount)
        if amount > balance:
            print('Imsufficient Funds!! ❌')
            continue

        if amount < 0:
            print('Withdraw amount cannot be a Negative Number!! ❌')
            continue

        elif amount == 0:
            print('Withdrawal amount cannot be 0 ❌')
            continue

        elif amount < 50:
            print('Minimum Withdrawal amount is $50')
            continue

        else:
            print(f'Successfully Withdrawn ${amount:.2f} ✅')
            return amount


def play(balance):
    if balance < 4:
        print('You have Insufficient funds to play the game...')
        print('Please Top up to continue playing...\n')
        time.sleep(2)
        print('Exiting to Main Menu\n')
        return balance, None

    while balance > 0:
        print('----------------------------------------')
        print(f'Current balance is {balance:.2f}')
        bet = input('Enter bet amount (q to quit):   ')
        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print('Invalid Bet amount!! ')
            continue
        bet = int(bet)
        if bet == 0:
            print('Bet amount cannot be 0')
            continue
        if bet < 0:
            print('Bet amount cannot be a NEGATIVE NUMBER!!')
            continue
        if bet < 4:
            print('Minimum bet amount is $4')
            continue

        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Congrats!! You won ${payout:.2f}')
            balance += payout
        else:
            print('Sorry 😔😥 You did not win anything in this round')

        if balance < 4:
            print('\nYou ran out of funds...Please top Up to continue playing!')
            while True:
                should_continue = input('Do you want to deposit (y /n):    ')
                if should_continue.lower() not in ['y', 'n']:
                    continue
                else:
                    break

            if should_continue.lower() == 'y':
                result = deposit()
                if result is not None:
                    balance += result
            elif should_continue.lower() == 'n':
                break
            else:
                print('Exiting to Main Menu')
                return None

    return balance, None


def main():
    balance = 100
    while True:
        print('\n----------- Main Menu ------------')
        print('1. Play Python slots 🎭 ▶️ 🎰')
        print('2. Check Balance 💳  💵')
        print('3. Deposit Soiining Funds 💰')
        print('4. Withdraw Winnings 🤑')
        print('5. Exit or Q to quit')

        choice = input('\nSelect your choice ( 1-5 ): ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid choice!!')
            continue

        choice = int(choice)
        if choice == 1:
            balance, _ = play(balance)
        elif choice == 2:
            show_balance(balance)
        elif choice == 3:
            result = deposit()
            if result is not None:
                balance += result

        elif choice == 4:

            result = withdraw(balance)
            if result is not None:
                balance -= result

        elif choice == 5:
            break
        else:
            print('Invalid choice!! Only choose (1-4)')
            continue

    print('\nThanks for using python Slots Machine\n')


if __name__ == "__main__":
    main()

'''
#################################################################

'''
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance
        self.account_history = []

    def __str__(self):
        self.account_history.append(f"Account '{self.acc_name}' created ✅")

        return f"Account '{self.acc_name}' created ✅ Current Balance 🤑: {self.balance}\n"

    def get_balance(self):
        print(f"{self.acc_name}\'s account Balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        print('-------------🚀 Deposit  Process 🚀-------------')
        self.get_balance()
        time.sleep(3)
        print(f'Depositing {amount:.2f} to account {self.acc_name}')
        if amount > 0:
            self.balance += amount

            print(f"Successfuly Deposited {amount:.2f} to '{self.acc_name}' ")

            self.get_balance()
            self.account_history.append(
                f"Deposited: {amount:.2f} to account {self.acc_name}'")

            print('-------------🚀 Deposit  Process Complete 🚀-------------\n')
        else:
            print('Invalid deposit amount!')

    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(f'Insufficient Funds!! ❌')

    def withdraw(self, amount):
        try:
            print('-------------🚀 Withdraw  Process 🚀-------------')
            self.get_balance()
            print(f'Withdrawing {amount:.2f} from account {self.acc_name}')
            time.sleep(2)
            self.viableTransaction(amount)
            self.balance -= amount

            self.account_history.append(
                f"Withdrawn: {amount:.2f} from account {self.acc_name}'")

            print(f'Successfuly Withdrawn {amount:.2f} from {self.acc_name}')
            self.get_balance()
            print('-------------🚀 Withdraw Process Complete 🚀-------------')
        except BalanceException as error:
            print(f'Withdrawal Process Interrupted!!')
            print(error)

    def transfer(self, account, amount):
        try:
            print('-------------⚡⚡ Transfer  Process ⚡⚡-------------\n')
            print(
                f"Transfering {amount:.2f} from '{self.acc_name}' to '{account.acc_name}' ")

            time.sleep(2)
            self.viableTransaction(amount)
            self.withdraw(amount)
            print()

            account.deposit(amount)
            print()

            self.get_balance()
            self.account_history.append(
                f"Transferred {amount:.2f} from '{self.acc_name}' to '{account.acc_name}' ")
        except BalanceException as error:
            print(error)
            print('\n-------------⚡⚡ Transfer  Process Interrupted ⚡⚡-------------')

    def get_account_history(self):

        print('--------- ⚜️ 🔱 Account Transaction 🔱 ⚜️ ---------')
        if not self.account_history:
            print('No Account History')
        else:
            for item in self.account_history:
                print(item)
        print()


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('Deposit Complete ✅')
        self.get_balance()


class InterestRewaardAccount(BankAccount):
    def __init__(self, acc_name, initial_amount):
        super().__init__(acc_name, initial_amount)
        self.fee = 5

    def withdraw(self, amount):
        # return super().withdraw(amount)
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount - self.fee)
            print('Withdraw Complete ✅')
            print(f'Savings Account Balance: ${self.fee:.2f}')
            self.get_balance()
        except BalanceException as error:
            print('Withdrwal Process Interrupted!!')
            print(f'{error}')


dave = BankAccount('Dave', 1000)
sarah = BankAccount('Sarah', 2000)

print(dave.__str__())

dave.get_balance()
print()

dave.deposit(2000)
print()

dave.withdraw(500)
print()

dave.transfer(sarah, 1500)
print()

dave.get_account_history()
print()

'''

#################################################################
