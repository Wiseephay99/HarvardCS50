import math
print()

# Bank Application
# show/check balance
# deposit
# withdraw
# exit


def check_balance(balance):
    print(f'Current Account balance is: ${balance}\n')
    return balance


def deposit(balance):
    try:
        amount = float(input('Enter amount to deposit:    '))
        if amount > 0:
            balance += amount
            print(f'Successfully Deposited ${amount:.2f} to your account..\n')
            return balance
        elif amount <= 0:
            print(f'Amount cannot be negative number...\n')
            return 0
    except ValueError:
        print(f'{amount} is an invalid amount')


def withdraw(balance):
    while True:
        try:
            amount = float(input('Enter the amount you want to withdraw:  '))
            if amount > balance:
                print('Insufficient Funds🏦...\n')
            elif amount <= balance:
                balance -= amount
                print(f'Withdrawn ${amount:.2f}💷💷 from your account..\n')
                return balance
            else:
                print(f'{amount} is invalid...\n')
        except ValueError:
            print(f'{amount} is an invalid amount')


def main():

    balance = 100
    is_running = True

    print(f'***********************************')
    print(f'        🏦 BANK PROGRAM 🏦         ')
    print(f'***********************************')

    print('1. Check Balance💳')
    print('2. Deposit💰')
    print('3. Withdraw 🏧🤑')
    print('4. Exit Program👋🏧')
    print(f'***********************************\n')

    while is_running:
        choice = input('Select your choice (1-4):  \n\n').lower()
        if choice == '1':
            balance = check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            is_running = False
            break
        else:
            print('Invalid Choice')
            continue
    print(f'Thanks for using 🏦 Bank 💴 Easy Application 💳 🏧...\n')


main()
