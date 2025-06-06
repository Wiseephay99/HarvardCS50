import random
from enum import Enum
import sys
import random
import time
'''
# rock paper scissors
print("\nWelcome to Rock Paper Scissors")


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS.ROCK)
# print(RPS["ROCK"])
# # print((RPS(PAPER)))
# print((RPS.ROCK).name)
# print((RPS.ROCK).value)


print("\nLet's play!\n")
while True:

    choice = input(
        "Choose...\n1. for Rock🪨 🪨\n2. for Paper📃 📜\n3. for Scissors ✂️ ✂️\nQ to Quit\n\n")

    if choice.lower() == "q":
        print('\nThanks for playing Rock Paper Scissors\n')
        break
    if not choice.isdigit():
        print('\nInvalid Input! Please choose 1, 2 or 3\n')
        continue
    choice = int(choice)

    computer = random.choice('123')
    computer = int(computer)

    # print(f'\nPlayer choose: {choice}')
    # print(f'Computer choose: {computer}\n')

    print(f'\nPlayer choose: {str(RPS(choice)).replace("RPS.", "")}')
    print(f'Computer choose: {str(RPS(computer)).replace("RPS.", "")}\n')

    if choice == 1 and computer == 2:
        print('🎉🎉 Player Won 🎉🎉')
    elif choice == 2 and computer == 3:
        print('🎉🎉 Player Won 🎉🎉')
    elif choice == 3 and computer == 1:
        print('🎉🎉 Player Won 🎉🎉')
    elif choice == computer:
        print('🪢 🪢  It\'s a Tie! 🪢 🪢 ')
    else:
        print('💻💻 Computer Won! 💻💻')

    print()

    print('Do you want to play Again?')
    play_again = True
    while play_again:
        play_again = input('Y to play again, Q to quit: ')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break
    if play_again.lower() == "y":
        print()
        continue
    else:
        break

print('\nThanks for playing Rock Paper Scissors\n')
'''
##############################################################
##############################################################

'''
def play():
    player_wins = 0
    computer_wins = 0
    games_played = 0
    games_tied = 0

    print("\nWelcome to Rock Paper Scissors")
    print("Let's play!\n")

    def rps():
        nonlocal player_wins, computer_wins, games_played, games_tied

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        choice = input(
            "Choose...\n1. for Rock🪨 🪨\n2. for Paper📃 📜\n3. for Scissors ✂️ ✂️\nQ to Quit\n\n")

        if choice.lower() == "q":
            sys.exit('\nThanks for playing Rock Paper Scissors\n')
        if not choice.isdigit():
            print('\nInvalid Input! Please choose 1, 2 or 3\n')
            rps()
        choice = int(choice)

        computer = random.choice('123')
        computer = int(computer)

        # print(f'\nPlayer choose: {choice}')
        # print(f'Computer choose: {computer}\n')

        print(f'\nPlayer choose: {str(RPS(choice)).replace("RPS.", "")}')
        print(f'Computer choose: {str(RPS(computer)).replace("RPS.", "")}\n')

        def decide_winner(player, computer):
            if choice == 1 and computer == 2:
                return 1
            elif choice == 2 and computer == 3:
                return 1
            elif choice == 3 and computer == 1:
                return 1
            elif choice == computer:
                return 2
            else:
                return 3

        # Determine the winner
        result = decide_winner(choice, computer)
        games_played += 1
        if result == 1:
            player_wins += 1
            print('🎉🎉 Player Won 🎉🎉')
        elif result == 2:
            games_tied += 1
            print('🪢 🪢  It\'s a Tie! 🪢 🪢 ')
        else:
            computer_wins += 1
            print('💻💻 Computer Won! 💻💻')
        print()
        time.sleep(1)  # Adding a slight delay for better user experience
        # Ask if the player wants to play again

        print('Do you want to play Again?')
        play_again = True
        while play_again:
            play_again = input('Y to play again, Q to quit: ')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == "y":
            print()
            rps()
        else:
            print(f'\n--------- RPS Game Results ----------')
            print(f'Games Played: {games_played}')
            print(f'Player Wins: {player_wins}')
            print(f'Computer Wins: {computer_wins}')
            print(f'Games Tied: {games_tied}')
            print('\nThanks for playing Rock Paper Scissors\n')

    return rps()


play()
'''
##############################################################
##############################################################
'''
# Code with Mosh
print('\nWelcome to Rock Paper Scissors!')

choices = ("r", "p", "s")
while True:
    print('\n--------------------------------------------------------')
    choice = input('Choose rock, paper or scissors: (r/p/s) q to quit:  ')
    if choice.lower() == 'q':
        break
    if choice not in choices:
        print('Invalid choice! Please choose r, p or s.')
        continue

    computer = random.choice(choices)

    print(f'\nYou chose: {choice}')
    print(f'Computer chose: {computer}\n')

    if ((choice == "r" and computer == "s") or
            (choice == "p" and computer == "r") or
            (choice == "s" and computer == "r")):
        print('You Win! 🎉🎉')
    elif choice == computer:
        print('It\'s a Tie! 🪢 🪢  ')
    else:
        print('Computer Wins! 💻💻')
    print()

    should_continue = input('Continue playing? (y/n): ')
    if should_continue == "y":
        continue
    else:
        break

print('\nThanks for playing Rock Paper Scissors!\n')'''

###################################################################################
###################################################################################

# Code with Mosh
'''

def get_user_input():
    while True:
        print('\n--------------------------------------------------------')
        choice = input('Choose rock, paper or scissors: (r/p/s) q to quit:  ')
        if choice.lower() == 'q':
            return None
        if choice in choices:
            return choice
        else:
            print('Invalid choice! Please choose r, p or s.')
            continue


def display_choices(choice, computer):
    print(f'\nYou chose: {emojis.get(choice)}')
    print(f'Computer chose: {emojis.get(computer)}\n')


def decide_winner(choice, computer):
    global player_wins, computer_wins, games_played, games_tied
    games_played += 1
    if ((choice == ROCK and computer == SCISSORS) or
        (choice == PAPER and computer == ROCK) or
            (choice == SCISSORS and computer == PAPER)):
        player_wins += 1
        print('You Win! 🎉🎉')
    elif choice == computer:
        games_tied += 1
        print('It\'s a Tie! 🪢 🪢  ')
    else:
        computer_wins += 1
        print('Computer Wins! 💻💻')
    print()


print('\nWelcome to Rock Paper Scissors!')
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {
    ROCK: "🪨  🪨  rock",
    PAPER: "📃  📜  paper",
    SCISSORS: "✂️  ✂️  scissors"
}
# emojis = {
#     "r": "🪨  🪨  rock",
#     "p": "📃  📜  paper",
#     "s": "✂️  ✂️  scissors"
# }
# choices = ("r", "p", "s")
choices = tuple(emojis.keys())

player_wins = 0
computer_wins = 0
games_played = 0
games_tied = 0


def display_results():
    print(f'\n--------- RPS Game Results ----------')
    print(f'Games Played: {games_played}')
    print(f'Player Wins: {player_wins}')
    print(f'Computer Wins: {computer_wins}')
    print(f'Games Tied: {games_tied}')


def main():
    while True:

        choice = get_user_input()
        if choice is None:
            break

        computer = random.choice(choices)

        display_choices(choice, computer)

        decide_winner(choice, computer)

        should_continue = input('Continue playing? (y/n): ')
        if should_continue == "y":
            continue
        else:
            break

    display_results()
    print('\nThanks for playing Rock Paper Scissors!\n')


if __name__ == "__main__":
    main()
'''

###################################################################################
###################################################################################
'''
questions = (
    ("How many teeth does an adult human have?"),
    ("What is the capital of France?"),
    ("What is the Largest Planet in our Solar System?"),
    ("Which year did Kenya gain independence?"),
    ("How many bones are in the adult human body?"),
    ("How many states are there in the United States?"),
)

answers = (
    ("A. 32", "B. 28", "C. 30", "D. 26", "E. 24"),
    ("A. Paris", "B. London", "C. Berlin", "D. Madrid", "E. Rome"),
    ("A. Neptune", "B. Uranus", "C. Saturn", "D. Jupiter", "E. Mars"),
    ("A. 1966", "B. 1963", "C. 1965", "D. 1967", "E. 1968"),
    ("A. 206", "B. 205", "C. 204", "D. 203", "E. 202"),
    ("A. 54", "B. 51", "C. 50", "D. 49", "E. 52")
)

question_num = 0
guesses = []
correct_answers = ["A", "A", "D", "B", "A", "C"]
total = 0
score = 0

print("\nWelcome to Trivia Quiz!\n")

for i, question in enumerate(questions, start=1):
    print(f'------------------------------------------------')
    print(f"{i}. {question}")
    for answer in answers[question_num]:
        print(answer)
    print()

    choices = ["A", "B", "C", "D", "E"]
    while True:
        guess = input("Choose A, B, C, D or E: ").upper()

        if guess not in choices:
            print("Invalid choice! Please choose A, B, C D or E.")
            continue
        guesses.append(guess)
        if guess == correct_answers[question_num]:
            print("Correct! 🎉")
            score += 1
            break
        else:
            print(f'Incorrect Answer!')
            break

    question_num += 1

print()
print('Correct Answers:')
for answer in correct_answers:
    print(answer, end=" ")
print()
print('Your Answers:')
for guess in guesses:
    print(guess, end=" ")
print()
total = score / len(questions) * 100

print(f'\nYou Scored: {total:.2f}%\n')
'''

###################################################################################
###################################################################################
'''

class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.acc_balance = balance
        self.transactions = []

    def __str__(self):
        self.transactions.append(
            f"Account created ✅ for {self.acc_name} with initial balance: {self.acc_balance:.2f}")
        return f"Account: '{self.acc_name}', Initial Balance: {self.acc_balance:.2f} created successfully!"

    def get_balance(self):
        return f"Account: '{self.acc_name}', Balance: {self.acc_balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount
            self.transactions.append(
                f"Deposited: {amount} - New Balance: {self.acc_balance:.2f}")
            print(f'Deposited: {amount} to account: "{self.acc_name}"')
        else:
            return f'Invalid Deposit Amount. Please enter a valid Amount'

    def viableTransaction(self, amount):
        if self.acc_balance >= amount:
            return
        else:
            raise BalanceException('Insufficient Balance for this Transaction')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            print(f'--------- 🚀 Beginnng Withdrawal Process 🚀 ---------')
            print(f'Withdrawing {amount:.2f} from account: "{self.acc_name}"')
            time.sleep(1)
            print(self.get_balance())
            self.acc_balance -= amount
            self.transactions.append(
                f"Withdrawn: {amount:.2f} from account: '{self.acc_name}'")
            print(
                f"Successfully ✅ Withdrawn {amount:.2f} from account: '{self.acc_name}'")
            print(f'New Balance: {self.acc_balance:.2f}')
            print(f'--------- 🔚 Completed Withdrawal Process 🔚 ---------')
            self.transactions.append(f'New Balance: {self.acc_balance:.2f}')

        except BalanceException as e:
            print('Withdrawal Process Interrupted! ❌')
            print(e)

    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            print(f'--------- 🚀 Beginnng Transfer Process 🚀 ---------')
            time.sleep(1)
            print(
                f'Transferring {amount:.2f} from account: "{self.acc_name}" to account: "{account.acc_name}"')

            print(self.get_balance())
            # self.withdraw(amount)
            self.acc_balance -= amount
            account.deposit(amount)
            print(
                f"Successfully Transferred {amount:.2f} to account: '{account.acc_name}'")
            self.transactions.append(
                f"Transferred {amount:.2f} to account: '{account.acc_name}'")
            account.transactions.append(
                f'Received {amount:.2f} from account: "{self.acc_name}" - New Balance: {account.acc_balance:.2f}')
            print(self.get_balance())
            print(f'--------- 🚀 Completed Transfer Process 🚀 ---------')

        except BalanceException as e:
            print('Transfer Process Interrupted! ❌')
            print(e)

    def print_transactions(self):
        print(f'\nTransactions for account: {self.acc_name}')
        if not self.transactions:
            print('No Transactions Found!')
        else:
            for transaction in self.transactions:
                print(transaction)


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount + (amount * 1.05)
            self.transactions.append(
                f"Deposited: {amount:.2f} - New Balance: {self.acc_balance:.2f}")
            print(
                f'Deposited: {amount:.2f} to account: "{self.acc_name}" with interest reward of 5%')
        else:
            return 'Invalid Deposit Amount. Please enter a valid Amount.'


class SavingsAccount(BankAccount):
    def __init__(self, acc_name, acc_balance):
        super().__init__(acc_name, acc_balance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.acc_balance -= (amount + self.fee)
            self.transactions.append(
                f"Withdrawn {amount + self.fee} from account: {self.acc_name}")
            print(
                f'Withdrawn {amount + self.fee} from account: {self.acc_name}\n')
            print(self.get_balance())
        except BalanceException as e:
            print('Withdrawal Process Interrupted! ❌')
            print(e)


dave = BankAccount('Dave', 30000)
sarah = BankAccount('Sarah', 40000)

print()
print(dave)
print(sarah)

dave.get_balance()
sarah.get_balance()

print()

dave.deposit(5000)
sarah.deposit(10000)

print()
print(dave.get_balance())
print(sarah.get_balance())

print()
dave.withdraw(1000)
print()
sarah.withdraw(5000)

print()
dave.transfer(1600, sarah)
print()
sarah.transfer(2400, dave)
print()

dave.print_transactions()
print()
sarah.print_transactions()
print()

mary = InterestRewardAccount("Interest Account", 10000)
print(mary)
mary.deposit(4000)
print()
mary.print_transactions()
'''

###################################################################################
###################################################################################

'''
def spin_wheel():
    wheel = ['🍒', '🍋', '🍊', '🍉', '🍇', '🍓']
    return random.choice(wheel), random.choice(wheel), random.choice(wheel)


def check_winner(spin_result):
    if spin_result[0] == spin_result[1] == spin_result[2]:
        return "Congratulations! You've won the jackpot! 🎉"
    return "Sorry, better luck next time! 😞"


def play_slot_machine():
    spin_result = spin_wheel()
    print("Spinning the wheel...")
    print(f"Result: {spin_result}")
    print(check_winner(spin_result))


if __name__ == "__main__":
    print("Welcome to the Slot Machine Game! 🎰")
    play_slot_machine()
    while input("Do you want to play again? (y/n): ").lower() == 'y':
        play_slot_machine()
    print("Thanks for playing! Goodbye! 👋")
'''
###################################################################################
###################################################################################

'''
def show_balance(balance):
    print(f"Current Balance is {balance:.2f}")


def deposit():
    while True:
        amount = input("Enter the amount to deposit:  ")
        if amount.lower() == "q":
            print('Exiting to Main Menu')
            return None
        if not amount.isdigit():
            print('Invalid amount! Please try again!')
            continue
        amount = int(amount)
        if amount < 0:
            print('Cannot deposit a negative number')
            continue
        if amount == 0:
            print("Deposit amount cannot be zero")
            continue
        if amount < 10:
            print("Minimum Deposit amount is 10usd")
            continue
        else:
            print(f'Successfully Deposited: {amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input("Enter the amount to withdraw:  ")
        if amount.lower() == "q":
            print('Exiting to Main Menu')
            return None
        if not amount.isdigit():
            print('Invalid amount! Please try again!')
            continue
        amount = int(amount)
        if amount > balance:
            print('Insufficent Funds!...Please try a Lower amount!')
        if amount < 0:
            print('Cannot withdraw a negative number')
            continue
        if amount == 0:
            print("Withdrawal amount cannot be zero")
            continue
        if amount < 50:
            print("Minimum Withdrawal amount is 50usd")
            continue
        else:
            print(f'Successfully Withdrawn: {amount:.2f}')
            return amount


def spin_row():
    # symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    # return [random.choice(symbols) for _ in range(3)]
    symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('---------------------------------')
    print("     |     ".join(row))
    print('---------------------------------')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍎':
            return bet * 7
        elif row[0] == '🍌':
            return bet * 9
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🍉':
            return bet * 15
        elif row[0] == '🌟':
            return bet * 20
    return 0


def play(balance):

    while balance > 0:
        print(f'Current Balance is: {balance}')
        bet = input('Enter bet amount (or q to quit):  ')
        if bet.lower() == "q":
            print('Exiting to Main Menu')
            time.sleep(1)
            return balance, None
        if not bet.isdigit() or int(bet) <= 0:
            print('Invalid bet amount. Please try again!')
            continue
        bet = int(bet)
        if bet == 0:
            print('Bet amount cannot be 0.')
            continue
        if bet > balance:
            print('Insufficient Funds! ')
            continue
        if bet < 5:
            print("Minimum bet amount is 5$")
            continue
        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"Congratulations.. You won {payout:.2f}")
            balance += payout
        else:
            print('Sorry! You did not win anything this in round!')

        if balance <= 5:
            print(
                "Your balance is too low to continue playing. Please deposit more funds.")
            deposit_funds = input("Do you want to deposit more funds? (y/n): ")
            if deposit_funds.lower() == 'y':
                result = deposit()
                if result:
                    balance += result
                    print("---------------------------------------")
                    continue
            else:
                print('Exiting to Main Menu')
                return balance, None
        print('Do you want to play again? (y/n)')
        play_again = True
        while play_again:
            play_again = input('Y to play again, Q to quit:  ')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == "y":
            print()
            continue
        else:
            print('Exiting to Main Menu')
            return balance, None

    return balance, None


balance = 100


def main(balance):
    print('\n--------------------------------------------')
    print('Welcome to Python Slot Machine Game! 🎰')
    print('You can bet on a row of 3 symbols.')
    print('Symbols: 🍉, 🍎, 🍌, 🔔, 🌟')

    while True:
        print('----------- Main Menu -----------')
        print("1. Play Spin Row")
        print('2. Deposit bet amount')
        print("3. Check Balance")
        print("4. Withdraw winnings")
        print("5. Exit")

        choice = input("\nSelect your choice?  ")
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid choice! Please try again')
        choice = int(choice)

        if choice == 1:
            result = play(balance)
            if result is not None:
                balance, _ = result

        elif choice == 2:
            result = deposit()
            if result is not None:
                balance += result

        elif choice == 3:
            show_balance(balance)

        elif choice == 4:
            result = withdraw(balance)
            if result:
                balance -= result

        elif choice == 5:
            break

        else:
            print("Invalid choice! Please try again!")
            continue

    print("\nThanks for Playing Python Slots\n")


if __name__ == "__main__":
    main(balance)

'''
###################################################################################
###################################################################################
