import sys
from enum import Enum
import time
import random
import math
print()
'''

class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, account_name, initial_amount):
        self.account_name = account_name
        self.balance = initial_amount
        print(
            f"Account: '{self.account_name}' created. Balance: {self.balance}")

    def get_balance(self):
        print(f'Account {self.account_name}: Balance: ${self.balance:.2f}')

    def deposit(self, amount):
        print('------------------------------------------')
        self.balance += amount
        print(
            f"Successfully Deposited: ${amount:.2f} to account '{self.account_name}' ")
        self.get_balance()
        print('------------------------------------------')

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            print('------------------------------------------')
            raise BalanceException(
                f'Insufficient Funds. \nAccount {self.account_name} balance is ${self.balance:.2f}')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('Withdrawal Complete ✅')
            print(
                f"Withdrawn: ${amount:.2f} from account '{self.account_name}' ")
            self.get_balance()
            print('------------------------------------------')
        except BalanceException as error:
            print('Withdrawal Inturrupted! ❌')
            print(f'{error}')


dave = BankAccount('Dave', 10000)
sarah = BankAccount('Sarah', 20000)

# print(dave)
# print(sarah)
print()
dave.get_balance()
sarah.get_balance()

print()
dave.deposit(100)
print()
sarah.deposit(200)

print()
dave.withdraw(20000)

print()
'''
###########################################################################
###########################################################################
###########################################################################

'''print('----------------------------------------------')


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, acc_name, initial_amount):
        self.balance = initial_amount
        self.acc_name = acc_name
        print(
            f"Account 🏦 🪙: '{self.acc_name}' created ✅ \nAccount Balance = {self.balance:.2f}\n")

    def get_balance(self):

        print(f"{self.acc_name}\'s Account 🏦  Balance 💰 is ${self.balance:.2f} \n")

    def deposit(self, amount):
        self.balance += amount
        # print('----------------------------------------------')
        print('Deposit Process Complete ✅')
        self.get_balance()

    def viable_Transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Insufficient Funds..\nAccount '{self.acc_name}' Balance = ${self.balance:.2f}  ")

    def withdraw(self, amount):
        try:
            self.viable_Transaction(amount)
            # print('----------------------------------------------')
            print('Withdrawal Process Complete ✅')
            self.get_balance()
        except BalanceException as error:
            print('Withdrawal Process Interrupted ❌')
            print(f'{error}')

    def transfer(self, amount, account):
        try:
            print('----------------------------------------------')
            print(f'Transfer Process 🚀 ✅ \n')
            self.viable_Transaction(amount)
            # self.withdraw(amount)
            print(
                f"Transferring {amount} from Account '{self.acc_name}' to '{account.acc_name}'\n")
            account.deposit(amount)

            self.balance -= amount
            self.get_balance()
            print('----------------------------------------------')
        except BalanceException as error:
            print('Transfer Interrupted ❌')
            print(f'{error}')


class InterestRewardsAcount(BankAccount):
    def deposit(self, amount):
        # return super().deposit(amount)
        self.balance = self.balance + (amount * 1.05)
        print('Deposit Complete ❇️')
        self.get_balance()


class SavngsAccount(InterestRewardsAcount):
    def __init__(self, acc_name, initial_amount):
        super().__init__(acc_name, initial_amount)
        self.fee = 5

    def withdraw(self, amount):
        # return super().withdraw(amount)()
        try:
            self.viable_Transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('Withdraw Complete ❇️')
            print(f'Savings Account balance is : {self.fee:.2f}')
            self.get_balance()
        except BalanceException as error:
            print(f'Withdraw Interrupted ❌')
            print(f'{error}')


dave = BankAccount('Dave', 20000)
sarah = BankAccount('Sarah', 10000)

dave.get_balance()
sarah.get_balance()

dave.deposit(500)
sarah.deposit(1000)

dave.transfer(600, sarah)
print()
sarah.transfer(10000, dave)

wise = InterestRewardsAcount('Wise', 30000)
wise.deposit(1000)
peter = InterestRewardsAcount('Peter', 30000)
peter.deposit(1000)

peter.transfer(2000, wise)
john = SavngsAccount('John', 20000)
john.get_balance()
john.withdraw(2000)
print()'''

###########################################################################
###########################################################################
###########################################################################

'''
# Python Slots Machine Game

print('Welcome To Python Slot Machine')
print('Symbols: 🍉 🍎 🍌 🔔 🌟')
print('----------------------------------------------')


def spin_row():
    symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    results = []
    print('----------------------------------')
    print('           Spinnng Row         ')
    time.sleep(1)
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('*******************************')
    print("    |       ".join(row))
    print('*******************************')


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


def main():
    balance = 100
    while balance > 0:
        print(f'Current Balance: ${balance}')
        bet = input('Enter bet amount (q to quit):  ')
        if bet. lower() == 'q':
            break
        if not bet.isdigit():
            print('Enter a valid bet amount')
            continue
        bet = int(bet)

        if bet > balance:
            print(f'Insufficient Funds. Account Balance: ${balance:.2f}\n')
            continue
        elif bet <= 4:
            print('Minimum ⚠️ bet amount is $4\n')
            continue
        elif bet == 0:
            print('Bet cannot be a 0\n')
            continue
        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
            print(
                f'🎉🎉 Congrats 🥳🥳 You Won ${payout:.2f} New Balance is ${balance:.2f}')
        else:
            print('Sorry 😔😢 You did not win anything in this round\n')

        if balance <= 4:
            print(
                'Sorry,...You ran out betting funds...\nExiting Python Slots  Better Luck next time\n')
            break

    print(f'\nBye..👋 Exiting Python Slots Machine\n')


if __name__ == "__main__":
    main()'''


###########################################################################
###########################################################################
###########################################################################
'''
# concession stand
menu = {
    'nachos': 2.50,
    'pretzel': 3.00,
    'chips': 2.00,
    'popcorns': 6.50,
    'soda': 3.65,
    'burger': 4.00,
    'coffee': 2.65
}
cart = {}
items = []
total = 0
print(f'--------- MENU --------- ')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {(food.capitalize()):10}: ${price:.2f}')
print('---------------------------')

while True:
    food = input('Enter food you want (q to quit):      ')
    if food.lower() == 'q':
        break
    if menu.get(food) is None:
        items.append(food)
    else:
        cart[food] = menu[food]
print()
print('--------- FOODS NOT IN MENU --------- ')
for food in items:
    print(food.capitalize(), end=' ')
print()
print()
print(f'--------- YOUR CART MENU --------- ')
for i, (food, price) in enumerate(cart.items(), start=1):
    print(f'{i}. {(food.capitalize()):10}: ${price:.2f}')

print()
print()
print(f'--------- TOTAL CART COST --------- ')
for price in cart.values():
    total += price
print(f'Total cost of {i} food items is {total:.2f}')
print('------------------------------------')
'''
###########################################################################
###########################################################################
###########################################################################

'''# concession stand
menu = {
    'nachos': 2.50,
    'pretzel': 3.00,
    'chips': 2.00,
    'popcorns': 6.50,
    'soda': 3.65,
    'burger': 4.00,
    'coffee': 2.65
}
foods = []
total = 0

print(f'--------- MENU --------- ')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {(food.capitalize()):10}: ${price:.2f}')
print('---------------------------')

while True:
    food = input('Enter food you want (q to quit):      ')
    if food.lower() == 'q':
        break
    if menu.get(food) is not None:
        foods.append(food)

print()


print(f'--------- YOUR CART MENU --------- ')
for food in foods:
    print(food, end=" ")
print()

print()

print(f'--------- TOTAL CART COST --------- ')
for food in foods:
    total += menu.get(food, 0)
print(f'Total cost of {len(foods)} food items is {total:.2f}')
print('------------------------------------')'''

###########################################################################
###########################################################################
###########################################################################
'''

menu = {"apple": 3, "banana": 2}
foods = ["apple", "orange", "banana"]

total = 0
for food in foods:
    total += menu.get(food, 0)  # Use 0 if the food is not in the menu

print(total)  # Output: 5 (3 for apple + 0 for orange + 2 for banana)

'''
###########################################################################
###########################################################################
###########################################################################

'''
foods = []
food = input('Enter food you want (q to quit): ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')

print()
print('The foods you like are: ')
for food in foods:
    print(food, end=' ')
print()
'''
###########################################################################
###########################################################################
###########################################################################

'''foods = []
food = input('Enter food you want (q to quit): ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')

print()
print('The foods you like are: ')
for food in foods:
    print(food, end=' ')
print()
'''
###########################################################################
###########################################################################
###########################################################################

'''foods_price = {}
total = 0
while True:
    food = input('Enter food you want (q to quit): ')
    if food.lower() == 'q':
        break
    price = input(f'Enter the price of {food}: ')
    foods_price[food] = float(price)


print()
print('--------------Your Food Menu Items--------------')
for food, price in foods_price.items():
    print(f'{food:10}: Ksh{price:.2f}')
print()
for price in foods_price.values():
    total += price
print(f'Your Total amount is: Ksh{total:.2f}')
print('--------------------------------------------------------')
'''
###########################################################################
###########################################################################
###########################################################################

# Python Bank Application


def check_balance(balance):
    print(f'Current account balance is: ${balance:.2f}')


def deposit():
    while True:
        amount = input('Enter amount to deposit q to quit():   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu\n')
            return None  # Return None instead of calling main()
        elif not amount.isdigit():
            print('Deposit amount must be a valid number')
        amount = int(amount)
        if amount == 0:
            print('Deposit cannot be a 0')
            continue
        elif amount <= 10:
            print('Minimum deposit is $10')
            continue
        else:
            print(f'Successfully Deposited {amount:.2f}\n')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw q to quit():   ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            return None  # Return None instead of calling main()
        elif not amount.isdigit():
            print('Withdraw amount must be a valid number')
        amount = int(amount)
        if amount == 0:
            print('Withdraw amount cannot be a 0')
        elif amount <= 10:
            print('Minimum withdrawal is $10')
        elif amount > balance:
            print('Insufficient Funds')
            continue
        else:
            print(f'Successfully Deposited {amount:.2f}')
            return amount


print('Welcome to Python Bank 🏦 Easy Application 💵')


def main():
    balance = 0

    while True:
        print('1. Check Balance 💰')
        print('2. Deposit Funds 💵')
        print('3. Withdraw Funds 🤑')
        print('4  Exit or Q to Quit App ❌')
        print()
        choice = input('Select your choice (1-4):   ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice')
            continue
        choice = int(choice)
        if choice == 1:
            check_balance(balance)

        elif choice == 2:

            # balance += deposit()
            result = deposit()
            if result is None:
                break
            balance += result

        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            break
        else:
            print('Invalid choice..select 1 2 3 4 or Q to Quit')
            continue

    print(f'\nExiting 👋👋 Python Bank Application\n')


if __name__ == "__main__":
    main()
