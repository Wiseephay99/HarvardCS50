print()

#   Python Bank Program


def show_balance(balance):
    print('*****************************')
    print(f'Your balance is: {balance:.2f}')
    print('*****************************')
    return balance


def deposit():
    print('*****************************')
    amount = float(input('Enter an amount to be deposited:   '))
    print('*****************************')

    if amount < 0:
        print('\n*****************************')
        print("That's not a valid input...\n")
        print('*****************************')
        return 0
    else:
        return amount


def withdraw(balance):
    print('*****************************')
    amount = float(input('Enter amount to be withdrawn?:  '))
    print('*****************************')

    if amount > balance:
        print('*****************************')
        print('Insufficient Funds...')
        print('*****************************')
    elif amount < 0:
        print('*****************************')
        print('Amount must be greater than 0')
        print('*****************************')
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print('*****************************')
        print('Baking Application Program')
        print('*****************************')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        print('*****************************')
        choice = input('Select your choice (1-4):  \n\n').lower()

        if choice == '1':
            balance = show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('*****************************')
            print('Invalid Choice')
            print('*****************************')

    print('*****************************')
    print(f'Thank you and have a nice day..\n\n')
    print('*****************************')


if __name__ == '__main__':
    main()
