import math
import time
from enum import Enum
import sys
import random
print()
###########################################################
###########################################################
'''
foods = []
print('---------------------------')
food = input('Enter food you like: ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like: ')
print('---------------------------')
print('The foods you like are: ')
for food in set(foods):
    print(food, end=' ')
print('\n---------------------------\n')
'''

###########################################################
###########################################################

'''foods = []
print('---------------------------')
food = input('Enter food you like: ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like: ')
print('---------------------------')
print('The foods you like are: ')
for food in set(foods):
    print(food, end=' ')
print('\n---------------------------\n')
'''

###########################################################
###########################################################
'''
foods = {}
total = 0

print('-------------------------------------')
while True:
    food = input('Enter food you like (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food)
        continue
    while True:
        price = input(f'Enter the price of {food}(q to quit): ')
        if not price.isdigit():
            print('Invalid price')
            continue
        elif price.isdigit():
            foods[food] = float(price)
            break
print('------------Your Cart---------------')
for i, (food, price) in enumerate(foods.items(), start=1):
    print(f'{i}. {food:10}: ${price:.2f}')
for price in foods.values():
    total += price
print('------------Total Cost---------------')
print(f'Total Cost of your items is: ${total:.2f}')
print('-------------------------------------\n')
'''
###########################################################
###########################################################
'''
menu = {
    'biscuits': 3.50,
    'nachos': 2.40,
    'pretzel': 3.60,
    'popcorn': 2.76,
    'chips': 1.50,
    'tea': 2.60,
    'burger': 6.75,
    'candy': 1.30,
    'coffee': 3.45
}
cart = {}
total = 0
print(f'------------ CONCERSSION STAND ------------ ')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:10} ${price:.2f}')
print('----------------------------------------------')
while True:
    food = input('Enter the food you want:  ')
    if food == 'q':
        break

    if not food:
        print('You did not select an item!')
        continue

    if menu.get(food) is not None:
        cart[food] = menu[food]
        continue
print()
print(f'------------ YOUR CART ------------ ')
if not cart:
    print('You dont have any items in your cart')
else:
    for i, (food, price) in enumerate(cart.items(), start=1):
        print(f'{i}. {food:10} ${price:.2f}')
print(f'------------ TOTAL COST ------------ ')
for price in cart.values():
    total += price
print(f'Total cost of your-= items is: ${total:.2f}')
print('----------------------------------------------')
'''
###########################################################
###########################################################

# Bank ATM application
'''
def show_balance(balance):
    print(f'\nYour Current Balance is: ${balance:.2f}\n')


def deposit():
    while True:
        amount = input('Enter the amount to deposit:  ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            return main()

        if not amount.isdigit():
            print(f'{amount} is not a valid amount')
            continue

        amount = float(amount)

        if amount < 10:
            print(f'Minimum deposit is $10')
        elif amount == 0:
            print(f'Deposit cannot be a 0')
            continue
        elif amount > 10:
            print(f'Successfully Deposited: ${amount:.2f}\n')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter the amount to withdraw:  ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            return main()

        if not amount.isdigit():
            print(f'{amount} is not a valid amount')
            continue

        amount = float(amount)

        if amount > balance:
            print('Insufficient Funds')
        elif amount == 0:
            print(f'You cannot withdraw a 0')
            continue
        else:
            print(f'Successfully Withdrawn: ${amount:.2f}\n')
            return amount


def main(balance=100):
    print('Welcome to Python Bank ATM Application')
    balance = 0
    while True:

        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')

        choice = input('Select your choice: ')
        if not choice.isdigit():
            print('Invalid Input')
            continue
        choice = int(choice)
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            break
        else:
            print('Invalid Selection')
            continue

    print('\nExiting Python Bank ATM')
    print('👋👋👋\n')


if __name__ == "__main__":
    main(balance)
'''
###########################################################
###########################################################

# Python Slots Machine Game


def spin_row():
    symbols = ['🍉', '🍌', '🍎', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))

    return results


def display_row(row):
    print('--------------------------------------------')
    print("        |         ".join(row))
    print('--------------------------------------------')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍌":
            return bet * 7
        elif row[0] == "🍎":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 15
        elif row[0] == "🌟":
            return bet * 20
    return 0


def deposit():
    while True:
        amount = input('Enter the amount to deposit:    ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            main(balance)
            return
        try:
            amount = int(amount)
            if amount == 0:
                print('Deposit can\'t be a 0.')
                continue
            elif amount < 10:
                print('Minimum deposit is $10')
                continue
            else:
                print(f'Successfully Deposited: {amount:.2f}\n')
                return amount
        except ValueError:
            print(f'{amount} is not  a valid deposit amount\n')
            continue


def withdraw(balance):
    while True:
        amount = input('Enter the amount to withdraw (q to quit):    ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            main(balance)
            return
        if not amount.isdigit():
            print(f'{amount} is not  a valid deposit amount\n')
            continue
        amount = int(amount)

        if amount == 0:
            print('You cannot withdraw 0.')
            continue
        elif amount < 10:
            print('Minimum wwithdrawal amount is $10')
            continue
        elif amount > balance:
            print('Insufficient Funds')
        else:
            print(f'Sucessfully withdrawn ${amount}')
            return amount


def playgame(balance):
    while balance > 0:
        print('--------------------------------------------')
        print(f'Current balance is: ${balance:.2f}')
        bet = input('Enter bet amount (q to quit): ')
        if bet.lower() == 'q':
            main(balance)

        if not bet.isdigit():
            print('Bet is not a valid amount...\n')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient funds..\n')
            continue
        if bet == 0:
            print('Bet cannot be be a 0\n')
            continue
        if bet <= 4:
            print('Bet amount cannot be less than $4\n')
            continue
        balance -= bet

        row = spin_row()
        display_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
            print(f'\nCongrats 🎉🎉 You Won ${payout:.2f}\n')
            # print(f'Current balance is: ${balance:.2f}')
        else:
            print('Sorry😔🙇 You did not win anything in this round..')

        should_continue = input('Continue?(Y or N):     ')
        if should_continue == 'y':
            continue
        else:
            main(balance)


def show_balance(balance):
    print(f'\nYour current balance is: ${balance:.2f}\n')


def exit_game():
    print('\n--------------------------------------------')
    print('Thanks for playing Python Slots Machine Game')
    sys.exit('Exiting\nBye 👋👋\n')


print('--------------------------------------------')
print('Welcome to Python Slots                     ')
print('Symbols: 🍉 🍋 🍌 🍍 🍎 🔔 🌟            ')

balance = 100


def main(balance):
    while True:
        print('--------------------------------------------')
        print('1. Play Game')
        print('2. Check Balance')
        print('3. Deposit')
        print('4. Withdraw Funds')
        print('5. Exit Game')
        choice = input('Select your choice(1-5):  ')
        if not choice.isdigit():
            print('Invalid selection')
            continue
        choice = int(choice)
        if choice == 1:
            playgame(balance)
        elif choice == 2:
            show_balance(balance)
        elif choice == 3:
            balance += deposit()
        elif choice == 4:
            balance -= withdraw(balance)
        elif choice == 5:
            exit_game()
        else:
            print('Invalid Selection')
            continue


if __name__ == "__main__":
    main(balance)
