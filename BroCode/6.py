'''

# Python Slot Machine

# Python Bank Program

# check balance
# deposit
# withdraw
# exit

def check_balance(balance):
    print(f'\nCurrent Account Balance is: ${balance:.2f}\n')
    return balance


def deposit(deposit_amount):
    while True:
        deposit_amount = input('Enter amount you want to deposit_amount:  ')
        try:
            deposit_amount = int(deposit_amount)
            if deposit_amount > 10:
                balance += deposit_amount
                print(f'Successfully ✅ deposited ${deposit_amount}')
                return deposit_amount
            elif deposit_amount > 0 and deposit_amount < 10:
                print(f'Deposit must be greater than $10...\n')
            elif deposit_amount < 0:
                return 0

        except ValueError:
            print('Please enter a valid amount..\n')
            continue


def withdraw(balance):
    while True:
        withdraw_amount = input('Enter amount you want to withdraw?:    ')
        try:
            withdraw_amount = int(withdraw_amount)
            if withdraw_amount > balance:
                balance -= withdraw_amount
                print(f'Successfully ✅ withdrawn ${withdraw_amount}')
                return withdraw_amount
            elif withdraw_amount < 0:
                return 0
        except ValueError:
            print(f'Please enter a valid amount ')


def main():
    balance = 100
    is_running = True
    while is_running:
        print('\nWelcome to 🏦 ATM BANK 🏧 ')
        print('1. Show Balance💶')
        print('2. Deposit💸')
        print('3. Withdraw🏧')
        print('4. Exit')

        choice = input('Select a choice (1-4):  ')
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            break
        else:
            print('\nInvalid Choice..')
            continue

    print('\nBye...Thanks for using BANK ATM..\n')


if __name__ == "__main__":
    main()
    
'''


def check_balance(balance):
    print(f'Bank Account Balance is: ${balance:.2f}\n')
    return balance


def deposit(balance):
    while True:
        deposit = input('Enter amount to deposit?   ')
        try:
            deposit = int(deposit)
            if deposit > 0:
                balance += deposit
                print(
                    f'Successfully deposited💸💶💴 ${deposit:.2f} to your account..\n')
                return balance
        except ValueError:
            print(f'{deposit} is not a valid amount..')


def withdraw(balance):
    while True:
        withdraw = input('Enter the amount to withdraw:    ')
        try:
            withdraw = int(withdraw)
            if withdraw > balance:
                print(f'Insufficent Funds....\n')
            elif withdraw <= balance:
                balance -= withdraw
                return balance
        except ValueError:
            print(f'{withdraw} is not a valid amount...\n')


def main():
    balance = 100
    is_running = True
    while is_running:

        print(f'**************************************')
        print('     🏦 Bank ATM Application  🏦      ')
        print(f'**************************************')
        print(f'1. Show Balance')
        print(f'2. Deposit Money')
        print(f'3. Withdraw Money')
        print(f'4. Exit\n')

        choice = input('Select your choice?     ')
        print()
        if choice == '1':
            balance = check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == '4':
            is_running == False
        else:
            print(f'Invalid choice')

    print(f'Thanks for using Bank ATM Application..\n')


if __name__ == '__main__':
    main()
