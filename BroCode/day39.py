from enum import Enum
import random
import sys
import time
print()

#########################################################################

'''foods = []
food = input('Enter food you like (q to quit):  ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')

print()
if not foods:
    print('You did not enter any food you like!! \n')
foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=" ")'''

#########################################################################

'''foods = []
food = input('Enter food you like (q to quit):  ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')

print()
if not foods:
    print('You did not enter any food you like!! \n')
foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=" ")'''

#########################################################################

'''
foods_price = {}
total = 0
while True:
    food = input('Enter the food you like (q to quit):   ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food!')
        continue
    while True:
        price = input(f'Enter the price of {food}:   ')
        if price.isdigit():
            foods_price[food] = float(price)
            print(f'{food} Added ✅')
            break
        else:
            print('Invalid price amount')
            continue
print()
print('---------------YOUR MENU---------------')
for food, price in foods_price.items():
    # total += foods_price[food]
    total += foods_price.get(food)
    print(f'{food:10}:  {price:.2f}')
print()
print(f'Total Bill ${total:.2f}')
print('---------------------------------------------')
'''

#########################################################################

'''menu = {
    'nachos': 200,
    'pretzel': 300,
    'chips': 400,
    'sweets': 600,
    'popcorn': 350,
    'milk': 200,
    'burger': 300,
    'soda': 200,
    'water': 250,
    'lemonade': 100,
    'biscuit': 300
}
cart = []
total = 0

# display Menu

print('------------------- CONCESSION STAND -------------------')

for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {(food).capitalize():10}:  ${price:.2f}')
print()

while True:
    food = input('Choose food you want (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print(f'You did not select and food! ')
        continue
    if menu.get(food) is not None:
        cart.append(food)
        print(f'{food} Added to Cart ✅ ')
    else:
        print(f'{food} Not in Menu ')
        continue

print()

if not cart:
    print('No item added to cart 🛒')
    total = 0
else:
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")
print()
print(f'Total Bill is ${total:.2f}')

print('---------------------------------------------------------')
'''

#########################################################################
'''
menu = {
    'nachos': 200,
    'pretzel': 300,
    'chips': 400,
    'sweets': 600,
    'popcorn': 350,
    'milk': 200,
    'burger': 300,
    'soda': 200,
    'water': 250,
    'lemonade': 100,
    'biscuit': 300
}
cart = {}
total = 0

# display Menu

print('------------------- CONCESSION STAND -------------------')

for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {(food).capitalize():10}:  ${price:.2f}')
print()

while True:
    food = input('Choose food you want (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print(f'You did not select and food! ')
        continue
    if menu.get(food) is not None:
        cart[food] = menu[food]
        print(f'{food} Added to Cart ✅ ')
    else:
        print(f'{food} Not in Menu ')
        continue

print()

if not cart:
    print('No item added to cart 🛒')
    total = 0
else:
    print(f'------------------🛒 YOUR CART 🛒------------------')
    for i, (food, price) in enumerate(cart.items()):
        total += price
        print(f'{i}. {food:10}  ${price:.2f}')
print()
print(f'Total Bill is ${total:.2f}')

print('---------------------------------------------------------')

'''
#########################################################################


class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, account_name, initial_balance):
        self.account_name = account_name
        self.balance = initial_balance

    def __str__(self):
        return f"Account name: '{self.account_name}' created. Balance: ${self.balance:.2f}"

    def get_balance(self):
        print(f"Account '{self.account_name}' Balance => ${self.balance:.2f} ")

    def deposit(self, amount):
        if amount > 10:
            self.balance += amount
            print('Deposit Complete ✅')
            print(f"Deposited ${amount:.2f} to account '{self.account_name}' ")
            self.get_balance()
        else:
            print('Minimum Deposit is $10')

    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(
                f"Insufiicent Funds ❌ '{self.account_name}\'s balance is ${self.balance:.2f} ' ")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('Withdrawal Process Complete ✅')
            print(
                f"Withdrawn ${amount:.2f} from account '{self.account_name}' ")
            self.get_balance()
        except BalanceException as e:
            print('Withdraw Process Interrupted ❌')
            print(e)

    def transfer(self, account, amount):
        try:
            print(f'\n------------- Transfer Process 🚀 ---------------\n')
            print(
                f"Transferring ${amount:.2f} from Account '{self.account_name}' to '{account.account_name}' \n")
            self.viableTransaction(amount)
            self.withdraw(amount)
            print()
            account.deposit(amount)
            print('\nTransfer Process Complete ✅')
            print(
                f"Transfered ${amount:.2f} to account '{account.account_name}'")
            print(f'\n------------- End of Transfer Process 🚀 ---------------\n')
        except BalanceException as e:
            print('Transfer Process Interrupted ❌')
            print(e)


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        if amount > 10:
            self.balance = self.balance + (amount * 1.05)
            print('Deposit Complete ✅')
            print(f"Deposited ${amount:.2f} to account '{self.account_name}' ")
            self.get_balance()
        else:
            print('Minimum Deposit is $10')


class SavingsFee(InterestRewardAccount):
    def __init__(self, account_name, initial_balance):
        super().__init__(account_name, initial_balance)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount - self.fee)
            print('Withdrawal Process Complete ✅')
            print(
                f"Withdrawn ${amount:.2f} from account '{self.account_name}' ")
            print(f'Savings Fee => ${self.fee:.2f}')
            self.get_balance()
        except BalanceException as e:
            print('Withdraw Process Interrupted ❌')
            print(e)


dave = BankAccount('Dave', 300)
sarah = BankAccount('Sarah', 600)
paul = InterestRewardAccount('Paul', 500)
witney = SavingsFee('Witney', 1000)

print(dave)
dave.get_balance()
print()

dave.deposit(4000)
print()

dave.get_balance()
print()

dave.withdraw(500)
print()


dave.get_balance()
print()

dave.transfer(sarah, 800)

print(paul)
print(witney)
paul.get_balance()
witney.get_balance()
witney.withdraw(300)
witney.get_balance()

print()
