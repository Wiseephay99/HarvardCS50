import time
import random
import sys
from enum import Enum
print()

# ROCK PAPER SCISSORS
'''
choice = input(
    'Choose...\n1. for Rock \n2. for Paper\n3. for Scissors\nQ to Quit..\n\n')

computer = random.choice("123")
computer = int(computer)

print(f'\nPlayer chose: {choice}')
print(f'Computer chose: {computer}\n')

if choice.lower() == "q":
    sys.exit(f'Exiting the Program...Bye\nThanks for playing RPS\n')

if choice == "1" and computer == "2":
    print('Player Wins 🎉🎉')
elif choice == "2" and computer == "3":
    print('Player Wins 🎉🎉')
elif choice == "3" and computer == "1":
    print('Player Wins 🎉🎉')
elif choice == computer:
    print('It is a Tie!!')
else:
    print('Ciomputer Wins 💻🧑‍💻')
print()
'''
################################################################################
################################################################################
'''
computer = random.choice("123")
computer = int(computer)

while True:
    print('-----------------------------')
    choice = input(
        'Choose...\n1. for Rock \n2. for Paper\n3. for Scissors\nQ to Quit..\n\n')

    print(f'\nPlayer chose: {choice}')
    print(f'Computer chose: {computer}\n')

    if choice.lower() == "q":
        break

    if choice == "1" and computer == "2":
        print('Player Wins 🎉🎉')
    elif choice == "2" and computer == "3":
        print('Player Wins 🎉🎉')
    elif choice == "3" and computer == "1":
        print('Player Wins 🎉🎉')
    elif choice == computer:
        print('It is a Tie!!')
    else:
        print('Computer Wins 💻🧑‍💻')
    print()

    print(f'Do you want to continue? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue Q to Quit..  ')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break
    if play_again.lower() == "y":
        print()
        continue
    else:
        print('\nExiting Application!')
        break

print('\nThanks for playing ROCK PAPER SCISSORS!!\n')'''

################################################################################
################################################################################

'''
def play():
    player_wins = 0
    computer_wins = 0
    ties = 0
    game_count = 0

    def rps():
        nonlocal player_wins, computer_wins, game_count, ties

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        print('-----------------------------')
        choice = input(
            'Choose...\n1. for Rock \n2. for Paper\n3. for Scissors\nQ to Quit..\n\n')

        if choice.lower() == "q":
            rps()
        if not choice.isdigit():
            print('Invalid choice...Only choose 1 2 or 3')
            rps()
        choice = int(choice)

        computer = random.choice("123")
        computer = int(computer)

        print(f'\nPlayer chose: {str(RPS(choice)).replace("RPS.", ' ')}')
        print(f'Computer chose: {str(RPS(computer)).replace("RPS.", ' ')}\n')

        # if choice == 1 and computer == 2:
        #     print('Player Wins 🎉🎉')
        # elif choice == 2 and computer == 3:
        #     print('Player Wins 🎉🎉')
        # elif choice == 3 and computer == 1:
        #     print('Player Wins 🎉🎉')
        # elif choice == computer:
        #     print('It is a Tie!!')
        # else:
        #     print('Computer Wins 💻🧑‍💻')
        # print()
        def decide_winner(choice, computer):
            if choice == 1 and computer == 2:
                return 1
            elif choice == 2 and computer == 3:
                return 1
            elif choice == 3 and computer == 1:
                return 1
            elif choice == computer:
                return 2
            else:
                return 0

        result = decide_winner(choice, computer)
        game_count += 1
        if result == 1:
            player_wins += 1
            print('Player Wins 🎉🎉')
        elif result == 2:
            ties += 1
            print('It is a Tie!!')
        else:
            computer_wins += 1
            print('Computer Wins 💻🧑‍💻')

        print(f'Do you want to continue? ')
        play_again = True
        while play_again:
            play_again = input('Y to continue Q to Quit..  ')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == "y":
            print()
            rps()
        else:
            print('\n------------------ RESULTS -----------------')
            print(f'Total Game Count: {game_count}')
            print(f'Total Player and Computer Ties: {ties}')
            print(f'Total Player Wins: {player_wins}')
            print(f'Total Computer Wins: {computer_wins}')

            print('\nThanks for playing ROCK PAPER SCISSORS!!\n')

    return rps()


play()'''

################################################################################
################################################################################

# ROCK PAPER SCISSORS

'''choices = ['r', 'p', 's']
choice = input('choose rock paper or scissors (r p s):  ')
if choice not in choices:
    print('Invalid choice! Only choose  r p  or s! ')

computer = random.choice(choices)

print(f'\nYou chose: {choice}')
print(f'Computer chose: {computer}\n')

if choice == 'r' and computer == "p":
    print('You Win 🎉🎉')
elif choice == "p" and computer == 's':
    print('You Win 🎉🎉')
elif choice == 's' and computer == 'r':
    print('You Win 🎉🎉')
elif choice == computer:
    print('It is a Tie 🪢 🪢 ')
else:
    print('Computer Wins 🧑‍💻  🧑‍💻')
print()'''

################################################################################
################################################################################
'''
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    ROCK: '🪨 🪨',
    PAPER: '📃 📜',
    SCISSORS: '✂️ ✂️',
}
# choices = [ROCK, PAPER, SCISSORS]
# choice = ['r', 'p', 's']

choices = tuple(emojis.keys())
while True:
    choice = input('choose rock paper or scissors (r p s):  ')
    if choice not in choices:
        print('Invalid choice! Only choose  r p  or s! ')

    computer = random.choice(choices)

    print(f'\nYou chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')

    if choice == ROCK and computer == PAPER:
        print('You Win 🎉🎉')
    elif choice == PAPER and computer == SCISSORS:
        print('You Win 🎉🎉')
    elif choice == SCISSORS and computer == ROCK:
        print('You Win 🎉🎉')
    elif choice == computer:
        print('It is a Tie 🪢 🪢 ')
    else:
        print('Computer Wins 🧑‍💻  🧑‍💻')
    print()

    should_continue = input('Continue (y / n): ').lower()
    if should_continue == "y":
        print()
        continue
    elif should_continue == "n":
        break

print('\nThanks for playing Rock Paper Scissors!!\n')'''


################################################################################
################################################################################
'''
def get_user_input():

    while True:
        print('--------------------------------------------')
        choice = input('choose rock paper or scissors (r p s):  ')
        if choice not in choices:
            print('Invalid choice! Only choose  r p  or s! ')
            continue
        else:
            return choice


def display_choices(choice, computer):
    print(f'\nYou chose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    global player_wins, computer_wins, game_count, ties
    game_count += 1
    if choice == ROCK and computer == PAPER:
        player_wins += 1
        print('You Win 🎉🎉')
    elif choice == PAPER and computer == SCISSORS:
        player_wins += 1
        print('You Win 🎉🎉')
    elif choice == SCISSORS and computer == ROCK:
        player_wins += 1
        print('You Win 🎉🎉')
    elif choice == computer:
        ties += 1
        print('It is a Tie 🪢 🪢 ')
    else:
        computer_wins += 1
        print('Computer Wins 🧑‍💻  🧑‍💻')
    print()


ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    ROCK: '🪨 🪨',
    PAPER: '📃 📜',
    SCISSORS: '✂️ ✂️',
}
# choices = [ROCK, PAPER, SCISSORS]
# choice = ['r', 'p', 's']
choices = tuple(emojis.keys())
player_wins = 0
computer_wins = 0
game_count = 0
ties = 0


def main():

    while True:

        choice = get_user_input()

        computer = random.choice(choices)

        display_choices(choice, computer)

        decide_winner(choice, computer)

        should_continue = input('Continue (y / n): ').lower()
        if should_continue == "y":
            print()
            continue
        elif should_continue == "n":
            print('\n------------------ RESULTS -----------------')
            print(f'Total Game Count: {game_count}')
            print(f'Total Player and Computer Ties: {ties}')
            print(f'Total Player Wins: {player_wins}')
            print(f'Total Computer Wins: {computer_wins}')
            break

    print('\nThanks for playing Rock Paper Scissors!!\n')


if __name__ == "__main__":
    main()'''


################################################################################
################################################################################

'''def rps():
    while True:
        choice = input(
            "What\'s your choice? rock 'r' paper 'p' or scissors 's': ").lower()
        if choice == "q":
            break
        if choice not in ['r', 'p', 's']:
            rps()

        computer = random.choice(['r', 'p', 's'])
        if choice == computer:
            return f"It is a Tie"

        elif is_win(choice, computer):
            return f'You Win'

        return f'Computer Wins'

    return f'\nThanks for playing Rock Paper Scissors\n'


def is_win(player, computer):
    if ((player == 'r' and computer == "p") or
            (player == 'r' and computer == "p") or
            (player == 'r' and computer == "p")):
        return True


result = rps()
print(result)


'''
################################################################################
################################################################################

# Guess a random number
'''
def guess(x):
    low = 1
    high = x
    user_input = " "
    random_num = random.randint(low, high)
    while user_input != random_num:
        user_input = int(input(f'Guess a number between {low} and {high}:  '))
        if user_input > random_num:
            print('Too High! Try guessing a lower number!! \n')
        elif user_input < random_num:
            print('Too Low!! Try Guessing a Higher number!! \n')

    print('Hurray!! Yay!! You guessed the correct number!! \n')


guess(10)'''

################################################################################
################################################################################
'''

def computer(x):
    low = 1
    high = x
    computer_num = random.randint(low, high)
    user_num = 0
    while user_num != 'C' and user_num != computer_num:
        user_num = input(
            f'Is {computer_num} too high (H), too low (L) or correct (C): ').upper()
        if user_num == 'L':
            low = computer_num + 1
            computer_num = random.randint(low, high)
        elif user_num == 'H':
            high = computer_num - 1
            computer_num = random.randint(low, high)

    print('Yay..Computer Guessed your number right..Correct Guess!\n')


computer(300)'''

################################################################################
################################################################################

'''def guess(x):
    low = 1
    high = x
    user_num = 0
    rand_num = random.randint(low, high)
    while user_num != rand_num:
        try:
            print('---------------------------------------')
            user_num = int(input(f'Guess a number between {low} and {high}: '))
            if low < user_num > high:
                print(f'Only choose between {low}  and {high} \n')
            elif user_num > rand_num:
                print('Too High!! \n')
            elif user_num < rand_num:
                print('Too Low!! \n')
        except ValueError:
            print(f'Invalid Input..Only Choose between {low} and {high} \n')

    print(f'Yay you guesses it right!! Random num is {rand_num}\n')


guess(20)'''
################################################################################
################################################################################

'''def computer(x):
    low = 1
    high = x
    rand_num = random.randint(low, high)
    choice = ""
    while choice != 'C':
        choice = input(
            f'Is {rand_num} it Too High H, too Low L, or Correct C?:  ').upper()
        if choice == 'L':
            low = rand_num + 1
            rand_num = random.randint(low, high)
        elif choice == 'H':
            high = rand_num + 1
            rand_num = random.randint(low, high)

    print(f'\nYay...Computer Guessed it Right...Random Number is {rand_num}\n')


computer(200)'''

################################################################################
################################################################################

# Python BVank Application

'''
def show_balance(balance):
    return f'Current Account Balance is {balance:.2f}\n'


def deposit():
    while True:
        amount = input('Enter amount to deposit:  ')
        if amount.lower() == 'q':
            print('Exiting to Main')
            return None
        if not amount.isdigit():
            print('Invalid amount!! ')
            continue
        amount = int(amount)
        if amount < 50:
            print(f'Minimum Deposit is $50\n')
            continue
        elif amount < 0:
            print('Amount cannot be  Negative Number \n')
            continue
        elif amount == 0:
            print('Deposit caanot be a 0\n')
            continue
        else:
            print(f'Successfully Deposited ✅ {amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw:  ')
        if amount.lower() == 'q':
            print('Exiting to Main')
            return None
        if not amount.isdigit():
            print('Invalid amount!! ')
            continue
        amount = int(amount)
        if amount > balance:
            print('Insufficent Funds...!)
            continue
        if amount < 50:
            print(f'Minimum Withdrawal amount is $50 \n')
            continue
        elif amount < 0:
            print('Withdrawal amount cannot be  Negative Number \n')
            continue
        elif amount == 0:
            print('Withdrawal amount cannot be a 0\n')
            continue
        else:
            print(f'Successfully Withdrawn 🤑🤑 {amount:.2f}')
            return amount


def main():
    print('Welcome to Python Bank Application')
    balance = 0
    while True:
        print('----------------------------')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit or Q to Quit')

        choice = input('\nSelect your choice: ')
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid Option.. Only choose 1 2 3 or 4')
            continue
        choice = int(choice)
        if choice == 1:
            print(show_balance(balance))
        elif choice == 2:
            result = deposit()
            if result:
                balance += result

        elif choice == 3:
            result = withdraw(balance)
            if result:
                balance -= result

        elif choice == 4:
            break
        else:
            print('Invalid choice! OnLy choose 1 - 4\n')

    print('\nThanks for using Python Bank Application\n')


if __name__ == "__main__":
    main()
   '''

################################################################################
################################################################################
#   Python slots machine
'''
print('Welcome to Python Slots Machine')
print('Symbols: 🍉 🍎 🍌 🔔 🌟')


def main():
    balance = 100
    while True:
        print('------------------------------')
        print('1. Play Python Slots Game')
        print('2. Deposit Bet Amount')
        print('3. Withdraw Winnings')
        print('4. Show Balance')
        print('0. Q to Quit or Exit')
        print('------------------------------')

        choice = input('\nSelect your choice: ')
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid choice!! Only choose 1 2 3 or 4')
            continue
        choice = int(choice)
        if choice == 1:
            result = play(balance)
            if result is not None:
                balance, _ = result
        elif choice == 2:
            result = deposit()
            if result:
                balance += result
        elif choice == 3:
            result = withdraw()
            if result:
                balance -= result

        elif choice == 4:
            print(show_balance(balance))
        elif choice == 0:
            break
        else:
            print('Invalid Input!! .. Only Choose 1 2 3 4 or 5')
            continue

    print('\nThanks for using Python Slots Machine!\n')


def show_balance(balance):
    return f"Current balance is {balance:.2f}"


def deposit():
    while True:
        amount = input('Enter amount to deposit:  ')
        if amount.lower() == "q":
            print('Exiting to Main')
            return None
        if not amount.isdigit():
            print('Invalid Amount!! ')
            continue
        amount = int(amount)
        if amount == 0:
            print('Deposit cannot be 0')
        elif amount < 10:
            print('Minimum Deposit is $10')
            continue
        elif amount < 0:
            print('Deposit cannot be a Ngetive Number!! ')
            continue
        else:
            print(f'Successfully Deposited ✅ {amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw:  ')
        if amount.lower() == "q":
            print('Exiting to Main')
            return None
        if not amount.isdigit():
            print('Invalid Amount!! ')
            continue
        amount = int(amount)
        if amount > balance:
            print('Insufficient Funds!! ')
            continue
        if amount == 0:
            print('Withdraw cannot be 0')
        elif amount < 50:
            print('Minimum waithdrawal is $50')
            continue
        elif amount < 0:
            print('Withdrawal amount cannot be a Ngetive Number!! ')
            continue
        else:
            print(f'Successfully Withdrawan ✅ {amount:.2f}')
            return amount


def spin_row():
    symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('-------------------------')
    print('   |    '.join(row))
    print('-------------------------')


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
    return 0


def play(balance):

    print('------------------------------')
    print('Python Slots Game')
    print('------------------------------')
    start = input('Start Game (y /n):  ')
    if not start == "y":
        return None

    while True:
        print(f'\nCurrent Balance is {balance:.2f}')
        bet = input('Enter bet amount:  ')
        if bet.lower() == "q":
            print('\nExiting to Main')
            break

        if not bet.isdigit():
            print('Enter valid bet amount!! ')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficent Funds!! ')
            continue
        if bet == 0:
            print('Balance cannot be a 0!! ')
            continue
        if bet < 9:
            print('Minimum bet amount is $9\n')
            continue
        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Congrats.. You won {payout:.2f}')
            balance += payout
        else:
            print('Sorry You did not win anything in this round!! \n')

        if balance <= 9:
            print('You ran out od betting funds...')
            should_deposit = input('Deposit to continue (y /n):  ')
            if should_deposit == "y":
                result = deposit()
                if result:
                    balance += result
            else:
                break
        print('Do you want to continue?  ')
        play_again = True
        while play_again:
            play_again = input('Y to continue.. Q to Quit:  ')
            if play_again not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == "y":
            continue
        else:
            print('Thanks for playing Python Slots Machine Game!')
            break

    return balance, None


if __name__ == "__main__":
    main()'''

################################################################################
################################################################################

'''
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.status = False  # Track if the book is borrowed

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            self.status = True
            return f"You Borrowed '{self.title}' by {self.author}"
        return f"'{self.title}' is currently not available in the library"

    def return_book(self):
        self.copies += 1
        self.status = False
        return f"You returned the book '{self.title}' "

    def __str__(self):
        return f"Book Title: '{self.title}' by {self.author}. Copies Available: {self.copies}\n"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        return f"Added ✅ Book of '{title}' by '{author}' "

    def borrow(self, title):
        if title in self.books:
            self.borrowed_books[title] = self.books[title]
            return self.books[title].borrow()
        return f"The Book Titled '{title}' is currently not available"

    def return_book(self, title):
        if title in self.books:
            return self.books[title].return_book()
        return f"Book '{title}' does not belong in this library"

    def view_books(self):
        if not self.books:
            return 'No books currently in the library'
        return "\n".join(str(book) for book in self.books.values())

    def view_borrowed_books(self):
        return "\n".join(f"Book Title: '{book.title}', status: {'Borrowed' if book.status else 'Available'}, Number of Copies: {book.copies}" for book in self.books.values())


def main():
    library = Library()
    print('Welcome to Python Library')
    while True:
        print('---------------------------')
        print('1. Add Book')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. View Books in Library')
        print('5. View Borrowed Books')
        print('0. Q to Quit or Exit')
        print('---------------------------')

        choice = input('\nSelect your choice:  ')
        if choice.lower() == "q":
            break
        if choice == "1":
            title = input('Enter Book Title:  ')
            author = input(f'Enter author name of {title}:  ')
            copies = int(input('Enter number of copies of the book:  '))
            print(library.add_book(title, author, copies))

        elif choice == "2":
            title = input('Enter Book Title:  ')
            print(library.borrow(title))

        elif choice == "3":
            title = input('Enter Book Title:  ')
            print(library.return_book(title))

        elif choice == "4":
            print(library.view_books())

        elif choice == "5":
            print(library.view_borrowed_books())

        elif choice == "0":
            break
        else:
            print('Invalid Option!! Please Try Again!! ')
            continue

    print('\nThanks for using Python Library\n')


if __name__ == "__main__":
    main()
'''

################################################################################
################################################################################


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, name, balance):
        self.acc_name = name
        self.balance = balance

    def __str__(self):
        return f"Account 'name' Created ✅ Balance is {self.balance:.2f}"

    def get_balance(self):
        return f"Account '{self.acc_name}' Balance: {self.balance:.2f}"

    def deposit(self, amount):
        if amount > 50:
            self.balance += amount
            return f"Deposited {amount:.2f} to account '{self.acc_name}'"
        return f'Cannot Deposit {amount:.2f}'

    def viableTransaction(self, amount):
        if amount < self.balance:
            return amount
        else:
            raise BalanceException(f'Insufficent Funds..')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            time.sleep(1)
            print('------🚀 Beggining Withdrawal Process 🚀------\n')
            print(self.get_balance())
            self.balance -= amount
            print(
                f"You have withdrawn {amount:.2f} from Account '{self.acc_name}' ")
            print(self.get_balance())
            time.sleep(1)
            print('\n------🚀 Ended Withdrawal Process 🚀------')

        except BalanceException as e:
            print('------ Withdrawal Process Interrupted ❌❌')
            print(e)

    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            time.sleep(1)
            print('------ ⚡⚡ Beggining Transfer Process ⚡⚡ ------ \n')
            print(
                f"Transferring {amount:.2f} from Acc: '{self.acc_name}' to '{account.acc_name}' ")
            print(self.get_balance())
            self.balance -= amount
            print(account.get_balance())
            account.deposit(amount)

            print(
                f"Transferred {amount} to '{account.acc_name}' Balance: {account.balance}' ")
            self.get_balance()
            time.sleep(1)
            print('\n------ ⚡⚡ Ended Transfer Process ⚡⚡ ------\n')

        except BalanceException as e:
            print('------ Transfer Process Interrupted ❌❌')


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit complete')
        self.get_balance()


class SavingsFee(InterestRewardsAccount):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw Completed')
            self.get_balance()
        except BalanceException as error:
            print(f'\n\nWithdraw Interrupted: {error}')


dave = BankAccount('Dave', 10000)
sarah = BankAccount('Sarah', 20000)
print(dave)
print()

print(dave.get_balance())
print()

print(dave.deposit(1000))
print()

print(dave.get_balance())
print()

dave.withdraw(3000)
print()

dave.transfer(1000, sarah)

################################################################################
################################################################################


################################################################################
################################################################################


################################################################################
################################################################################


################################################################################
################################################################################
