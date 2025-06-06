import math
import random
import time
import sys

#######################################################################
#######################################################################

# Python Bank Easy Application


def show_balance(balance):
    print(f'\nCurrent Account Balance Ksh 💴 ${balance:.2f}\n')


def deposit():
    while True:
        amount = input('Enter amount to deposit 💸 (q to quit):  ')
        if amount.lower() == 'q':
            return main()
        if not amount.isdigit():
            print('Invalid deposit amount')
            continue
        amount = int(amount)
        if amount == 0:
            print('Deposit cannot be 0❌ ')
            continue
        elif amount <= 10:
            print('Minimum deposit amount is $10  Ⓜ️ ')
            continue
        else:
            print(f'Successfully Deposited ${amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw 💸 (q to quit):  ')
        if amount.lower() == 'q':
            return main()
        if not amount.lower():
            print('Invalid withdrawal amount')
            continue
        amount = int(amount)
        if amount == 0:
            print('You cannot withdraw a 0 ❌')
            continue
        elif amount <= 10:
            print('Minimum withdrawal amount is $10 Ⓜ️ ')
            continue
        elif amount > balance:
            print('Insufficient Funds ')
            continue
        else:
            print(f'Successfully withdrawal ${amount:.2f}')
            return amount


print('\nWelcome to Python Bank 🏦 Easy Application 🪙 ')


def main():
    balance = 0

    while True:
        print('-------------------------------------------')
        print('1. Show Balance 💰')
        print('2. Deposit Funds 💴')
        print('3. Withdraw Funds 💶')
        print('4. Exit or Q to Quit ❌')
        print('-------------------------------------------')

        choice = input('\nSelect your choice 🔢 (1-4):   ')

        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid Selection')
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

    print('\n-------------------------------------------')
    print('🏦 Exiting Bank Application 🪙')
    time.sleep(2)
    print('Bye  👋 👋 \n')


if __name__ == "__main__":
    main()
