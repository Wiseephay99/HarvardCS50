from enum import Enum
import time
import random
import sys
print()

'''
class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, acc_name, initial_amount):
        self.acc_name = acc_name
        self.balance = initial_amount

    def __str__(self):
        return f"Account '{self.acc_name}' Created. ❇️ 'Balance 💰: ${self.balance:.2f}"

    def get_balance(self):
        print(f"{self.acc_name}'s Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 50:
            self.balance += amount
            self.get_balance()
        else:
            print(f'Minimum Deposit is {self.balance:.2f}')

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Insufficient Funds.\n{self.acc_name}'s Balance = {self.balance} ")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            self.get_balance()
        except BalanceException as error:
            print('Withdrwal Process Interrupted!!')
            print(f'{error}')

    def transfer(self, amount, account):
        try:
            amount = float(input("Enter the amount to deposit: "))
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            self.get_balance()
        except BalanceException as error:
            print('Transfer Pocesss Interrrupted')
            print(f'{error}')

    def create_account(self):
        print('Create account by Entering your name and initial deposit.')
        name = input('Enter your name: ')
        amt = float(input('Enter initial amount:  '))
        print()
        account = BankAccount(name, amt)
        print(str(account))
        # name.get_balance()
        # print()
        # print('Account Created Successfully!')
        # print('Account Name: ', name.acc_name)
        # print('Account Balance: ', name.balance)
        # print()
        return account


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


def main():
    print('Welcome to Easy Banking\n')
    while True:
        print('1. Create Account')
        print('2. Deposit')
        print('3  Withdraw')
        print('4. Check Balance')
        print('5. Transfer')
        print('6. Exit')

        print()
        choice = input('Select your option (1-5):   ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice')
            continue
        choice = int(choice)
        if choice == 1:
            # Create a default account instance
            account = BankAccount("Default", 0)
            account = account.create_account()
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            account.get_balance()
        elif choice == 5:
            account = input('Enter the name of the account to transfer to: ')
            amount = float(
                input(f'Enter the amount to transfer to {account}: '))
            # Assuming account is an instance of BankAccount or InterestRewardsAccount
            # You need to create the account instance first
            # For example, you can create a new account instance here or pass an existing
            # account instance to the transfer method
            # account = BankAccount(account, 0)  # Create a new account instance
            # or use an existing account instance
            # account = InterestRewardsAccount(account, 0)  # Create a new account instance
            account = BankAccount(account, 0)
            account.transfer(amount, account)

        elif choice == 5:
            break
        elif choice == 5:
            break
        else:
            print('Invalid Choice')
            break

    print('\nThanks for using Bank Application\n')


if __name__ == "__main__":
    main()
'''

########################################################################################
########################################################################################
########################################################################################

'''
class BankException(Exception):
    pass  # Bank Exception to handle class exceptions


class BankAccount():
    no_of_count = 0  # class varibale to count the number of accounts created

    def __init__(self, acc_name, initial_amount, acc_type):
        self.balance = initial_amount
        self.acc_name = acc_name
        self.acc_type = acc_type
        BankAccount.no_of_count += 1  # Increment the account count

    def __str__(self):
        return f"Account '{self.acc_name}' created ❇️  Account Type: '{self.acc_type}' Balance 💰: ${self.balance:.2f}"

    def get_balance(self):
        print(f'{self.acc_name}\'s Balance 💵: ${self.balance:.2f}')

    def deposit(self, amount):
        try:
            if amount > 50:
                self.balance += amount
                print('Deposit Complete ✅')
            else:
                print('Minimum Deposit is $50.00')
        except ValueError:
            print('Invalid Input ❌')

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BankException(
                f'Insufficient Funds.\n{self.acc_name}\'s has a balance of 💵: ${self.balance:.2f}')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print('Withdraw Complete ✅')
            self.get_balance()
        except BankException as error:
            print('Withdrawal Process Interrupted ❌')
            print(f'{error}')
        except ValueError:
            print('Invalid Amount ❌')
        except Exception as error:
            print('An unexpected error occurred ❌')
            print(f'{error}')

    def Transfer(self, amount, account):
        try:
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer Commplete ✅')
            self.get_balance()

        except BankException as error:
            print('Transfer Process Interrupted ❌')
            print(f'{error}')
        except ValueError:
            print('Invalid Amount ❌')
        except Exception as error:
            print('An unexpected error occurred ❌')
            print(f'{error}')


def create_account():
    print('-------------------------------------------------')
    print('Create an account')
    print('Enter your name, Initial Deposit and Account Type')
    name = input('Enter your name: ')

    initial_amount = float(input('Enter initial amount: '))

    if initial_amount < 50:
        print('Minimum Deposit is 50.00 ❌')
        return None

    account_type = input('Enter the type of account (Savings/Checking): ')
    # Create a default account instance
    account = BankAccount(name, initial_amount, 'Default')
    # Check the account type and create the appropriate account instance

    if account_type.lower() == 'savings':
        account = BankAccount(name, initial_amount, 'Savings')
    elif account_type.lower() == 'checking':
        account = BankAccount(name, initial_amount,  'Checking')
    # elif account_type.lower() == 'interest':
    #     account = InterestRewardsAccount(name, initial_amount, 'Interest')
    # elif account_type.lower() == 'interest rewards':
    #     account = InterestRewardsAccount(name, initial_amount, 'Interest Rewards')
    # elif account_type.lower() == 'interest rewards account':
    #     account = InterestRewardsAccount(name, initial_amount, 'Interest Rewards Account')
    else:
        print('Invalid Account Type ❌')
        return None

    account_list.append(account)

    return account, account_list


def display_accounts(account_list):
    if not account_list:
        print("No accounts available to display ❌")
    else:
        print("\nList of Accounts:")
        for account in account_list:
            print('--------------------------------------------------------')
            # print(account)
            print(
                f"Account Name: {(account.acc_name).upper()} Account Type: '{account.acc_type}' Balance: ${account.balance:.2f}")


def find_account(account_list, name):
    account_found = None
    for account in account_list:
        if account.acc_name == name:
            return account
    if not account_found:
        print(f'{name} does not exist')
        return None


account_list = []


def main():
    print('Welcome to Easy Banking\n')

    while True:
        print('---------------------------------------')
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Check Balance')
        print('5. Transfer Money')
        print('6. Display Accounts')
        print('7. Exit or Q to Quit')
        print('---------------------------------------')
        print()
        choice = input('Select your option (1-7): ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid choice ❌')
            continue
        choice = int(choice)
        if choice == 1:
            account, account_list = create_account()
            print(str(account))
            print('Account Created Successfully! ✅ ')

        elif choice == 2:
            name = input('Enter account to deposit: ')
            account = find_account(account_list, name)
            amount = float(input('Enter the amount to deposit: '))
            account = account.deposit(amount)

        elif choice == 3:
            name = input('Enter account to withdraw: ')
            account = find_account(account_list, name)
            amount = float(input('Enter the amount to withdraw: '))
            account.withdraw(amount)
        elif choice == 4:
            name = input('Enter the account name to check balance:')
            account = find_account(account_list, name)
            account.get_balance()
        elif choice == 5:
            pass
        elif choice == 6:
            display_accounts(account_list)
        elif choice == 7:
            break
        else:
            print('Invalid choice ❌')
            continue

    print('\n---------------------------------------')
    print('Thanks for Using Easy Banking\n')


if __name__ == "__main__":
    main()
'''

########################################################################################
########################################################################################
########################################################################################


'''

foods = []
food = input('Enter food you like (q to quit ): ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like q to quit:  ')

print()
print('----------------------------')
print('The foods you like are: ')
for food in foods:
    print(food, end=" ")

print()
print()

'''
########################################################################################

'''

foods = []
food = input('Enter food you like (q to quit ): ')
while food != 'q':
    if food.lower() == 'q':
        break
    foods.append(food)
    food = input('Enter another food you like q to quit:  ')

print()
print('----------------------------')
print('The foods you like are: ')
for food in foods:
    print(food, end=" ")

print()
print()

'''

########################################################################################

'''
foods_price = {}
total = 0

while True:
    print('----------------------------------------------')
    food = input('Enter food you want (q to quit): ')
    if food.lower() == 'q':
        break
    price = input(f'Enter price of {food}:  ')
    foods_price[food] = float(price)

print()
print('---------------------YOUR MENU--------------------')
for food in foods_price.keys():
    print(food, end=" ")
for price in foods_price.values():
    total += price
print()
print(f'Your Total = {total:.2f}')
print('----------------------------------------------')
'''
########################################################################################
########################################################################################
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
cart = []
total = 0

print('--------------------------------------------------')
print('                 CONCESSION STAND                 ')
print('---------------------YOUR MENU--------------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:10}:{price:.2f}')
print('----------------------------------------------')

print()

while True:
    food = input('Select your food (q to quit):   ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not select an item')
        continue
    if menu.get(food) is not None:
        cart.append(food)

print()
print('------------------------ CART -----------------------')
if not cart:
    print(f'No items select in your cart')
for food in cart:
    total += menu.get(food)
    print(f"{food}", end=" ")
print()
print(f'Your Total Bill = {total:.2f}')
print('--------------------------------------------------')

'''
########################################################################################
########################################################################################
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

print('--------------------------------------------------')
print('                 CONCESSION STAND                 ')
print('---------------------YOUR MENU--------------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:10}:{price:.2f}')
print('----------------------------------------------')

print()

while True:
    food = input('Select your food (q to quit):   ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not select an item')
        continue
    if menu.get(food) is not None:
        cart[food] = menu[food]

print()
print('------------------------ CART -----------------------')
if not cart:
    print(f'No items select in your cart')

for i, (food, price) in enumerate(cart.items(), start=1):
    print(f'{i}. {food:10}: {price:.2f}')

print()
for price in cart.values():
    total += price
print(f'Your Toal Bill = {total:.2f}')
print('--------------------------------------------------')
'''
########################################################################################
########################################################################################

'''
foods_prices = {}
total = 0
while True:
    print('---------------------------------------------------')
    food = input('Enter the food you like (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food')
        continue

    while True:
        price = input(f'Enter price of {food} (q to quit):  ')
        if price.lower() == 'q':
            break
        if not price.isdigit():
            print('Invalid Price Amount')
            continue
        foods_prices[food] = float(price)
        break


print()
print('******************** YOUR MENU ********************')
if not foods_prices:
    print(F'You did not select any food')
for i, (food, price) in enumerate(foods_prices.items(), start=1):
    print(f'{i}. {food:10}: {price:.2f}')

print()

if not foods_prices:
    total = 0
for price in foods_prices.values():
    total += price
print(f'Your Total is: {total:.2f}')
print('*****************************************************')
'''

##################################################################################### _###
########################################################################################

'''
# Days Converter

def days_to_hours(no_of_days):
    return f'{no_of_days} Days to Hours is {no_of_days * 24} Hours\n'


def evaulate_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nThanks for using Days Converter\n')

    days = days.split(',')
    days = [day.strip() for day in days]
    days = [day for day in days if day]  # Remove empty strings
    for day in days:
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(days_to_hours(day))
            elif day == 0:
                print(f'You entered a 0 ..pls don\'t ruin the program..\n')
            elif day <= 0:
                print(f'You entered a NEGATIVE NUMBER so no conversion for you\n')
        else:
            print('Invalid Number of Days\n')


while True:
    print('--------------------------------------------------------------')
    days = input(
        f'Enter # as a list separated by comma (",") and I\'ll convert to hours:  ')
    evaulate_and_excute(days)
'''

########################################################################################
########################################################################################

'''
# Days Converter List
def days_to_hours(no_of_days):
    return f'{no_of_days} Days to Hours is {no_of_days * 24} Hours\n'


def evaulate_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nThanks for using Days Converter\n')

    days = days.split(',')
    days = [day.strip() for day in days]
    days = [day for day in days if day]  # Remove empty strings
    for day in days:
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(days_to_hours(day))
            elif day == 0:
                print(f'You entered a 0 ..pls don\'t ruin the program..\n')
            elif day <= 0:
                print(f'You entered a NEGATIVE NUMBER so no conversion for you\n')
        else:
            print('Invalid Number of Days\n')


while True:
    print('--------------------------------------------------------------')
    days = input(
        f'Enter # as a list separated by comma (",") \nand I\'ll convert to hours:\n\n')
    evaulate_and_excute(days)
'''

########################################################################################
########################################################################################

'''
# Days Converter  Dictionary


def days_to_hours(no_of_days, units):
    if units == 'hours':
        return f'{no_of_days} Days to Hours is {no_of_days * 24} Hours\n'
    elif units == 'minutes':
        return f'{no_of_days} Days to Minutes is {no_of_days * 24 * 60} Minutes\n'
    elif units == 'seconds':
        return f'{no_of_days} Days to Seconds is {no_of_days * 24 * 3600} Seconds\n'
    else:
        return f'Invalid unit'


def evaulate_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nThanks for using Days Converter\n')

    days = days.split(':')
    days = [day.strip() for day in days]
    days = [day for day in days if day]  # Remove empty strings
    days_units = {'days': days[0], 'units': days[1]}
    days = days_units['days']
    units = days_units['units']

    if days.isdigit():
        days = int(days)
        if days > 0:
            print(days_to_hours(days, units))
        elif days == 0:
            print(f'You entered a 0 ..pls don\'t ruin the program..\n')
        elif days <= 0:
            print(f'You entered a NEGATIVE NUMBER so no conversion for you\n')
    else:
        print('Invalid Number of Days\n')


while True:
    print('--------------------------------------------------------------')
    days = input(
        f"Enter # of days and units seprated by comma (':') \nand I\'ll convert to units:\n\n")
    evaulate_and_excute(days)
'''


########################################################################################
########################################################################################
# Bank Application

'''
def show_balance(balance):
    return f'Your Balance 🤑 is Ksh {balance:.2f}'


def deposit():
    while True:
        amount = input('Enter amount to Deposit 💵 Ksh:  ')
        if amount.lower() == 'q':
            print('Exiting  to Main Main Ⓜ️')
            return None
        if not amount.isdigit():
            print('Invalid mount ❌ ')
            continue
        amount = float(amount)
        if amount <= 10:
            print('Minimum Deposit is $10.00 ❌')
            continue
        elif amount == 0:
            print('Deposit cannot be 0 ❌')
            continue
        elif amount < 0:
            print('Deposit cannot be a NEGATIVE amount ❌')
            continue
        else:
            print('----------------------------------------')
            print('Deposit Complete ✅')
            print(f'Sucessfully Deposited: Ksh {amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to Withdraw 💵 Ksh:  ')
        if amount.lower() == 'q':
            print('Exiting  to Main Main Ⓜ️')
            return None
        if not amount.isdigit():
            print('Invalid mount ❌ ')
            continue
        amount = float(amount)
        if amount > balance:
            print('Insufficient Funds ❌')
            continue
        elif amount > 1000:
            print('Maximum Withdrawal amount is $1000.00 ❌')
            continue
        if amount <= 50:
            print('Minimum Withdrawal amount is $50.00 ❌')
            continue
        elif amount == 0:
            print('Amount to withdraw cannot be 0 ❌')
            continue
        elif amount < 0:
            print('Withdrawal amount cannot be a NEGATIVE amount ❌')
            continue
        else:
            print('----------------------------------------')
            print('Withdrawal Process Complete ✅')
            print(f'Sucessfully Withdrawn: Ksh {amount:.2f}')
            return amount


print('Welcome to Python 🐍 Easy 🏦 Banking 🏦\n')


def main():
    balance = 0
    while True:
        print('----------------------------------------')
        print('1. Show Balance 🤑 ')
        print('2. Deposit 🏧 ')
        print('3. Withdraw 💰 ')
        print('4. Exit or Q to Quit ❌ ')
        print('----------------------------------------')
        print()
        choice = input('Select your option: (1-4): ')
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid Choice')
            continue

        choice = int(choice)

        if choice == 1:
            print(show_balance(balance))
        elif choice == 2:

            result = deposit()
            if result:
                balance += result

        elif choice == 3:

            result = withdraw()
            if result:
                balance -= result

        elif choice == 4:
            break
        else:
            print('Invalid Option')
            continue

    print('\nThanks for using Python 🐍 Easy Banking 🏦 \n')


if __name__ == "__main__":
    main()

'''

########################################################################################
########################################################################################

'''
# Python  Slots Machine Game

def spin_row():
    symbols = ['🍓', '🍇', '🍉', '🍌', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))

    return results


def display_row(row):
    print("---------------------------------------")
    print('                 Spinning...           ')
    print("---------------------------------------")
    print('         |       '.join(row))
    print("---------------------------------------")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍓':
            return bet * 5
        elif row[0] == '🍇':
            return bet * 7
        elif row[0] == '🍉':
            return bet * 8
        elif row[0] == '🍌':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 15
        elif row[0] == '🌟':
            return bet * 20
    return 0


def deposit():
    while True:
        amount = input('Enter amount to Deposit 💵 Ksh:  ')
        if amount.lower() == 'q':
            print('Exiting  to Main Main Ⓜ️')
            return None
        if not amount.isdigit():
            print('Invalid mount ❌ ')
            continue
        amount = float(amount)
        if amount <= 10:
            print('Minimum Deposit is $10.00 ❌')
            continue
        elif amount == 0:
            print('Deposit cannot be 0 ❌')
            continue
        elif amount < 0:
            print('Deposit cannot be a NEGATIVE amount ❌')
            continue
        else:
            print('----------------------------------------')
            print('Deposit Complete ✅')
            print(f'Sucessfully Deposited: Ksh {amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to Withdraw 💵 Ksh:  ')
        if amount.lower() == 'q':
            print('Exiting  to Main Main Ⓜ️')
            return None
        if not amount.isdigit():
            print('Invalid mount ❌ ')
            continue
        amount = float(amount)
        if amount > balance:
            print('Insufficient Funds ❌')
            continue
        elif amount > 1000:
            print('Maximum Withdrawal amount is $1000.00 ❌')
            continue
        if amount <= 50:
            print('Minimum Withdrawal amount is $50.00 ❌')
            continue
        elif amount == 0:
            print('Amount to withdraw cannot be 0 ❌')
            continue
        elif amount < 0:
            print('Withdrawal amount cannot be a NEGATIVE amount ❌')
            continue
        else:
            print('----------------------------------------')
            print('Withdrawal Process Complete ✅')
            print(f'Sucessfully Withdrawn: Ksh {amount:.2f}')
            return amount


def play_game(balance):
    while balance > 0:
        print('---------------------------------------')
        print(f'Current Balance is: $ {balance:.2f}')
        bet = input('Enter bet amount: $    ')
        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print('Invalid bet amount! ❌ ')
            continue
        bet = float(bet)

        if bet > balance:
            print('Insuffcient Balance ❌')
            continue
        elif bet < 0:
            print('Bet amount cannot be a NEGATIVE amount ❌ ')
            continue
        elif bet == 0:
            print('Bet amount cannot be 0 ❌ ')
            continue
        elif bet <= 4:
            print('Minimum Bet amount is $4.00 ❌')
            continue
        balance -= bet

        row = spin_row()

        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'🎉🎉 You Won 🎉🎉 ${payout:.2f}')
            balance += payout
        else:
            print('Sorry 😔😔 You didn\'t win anythong in this round!')

        if balance <= 5:
            print(
                'You ran out of betting money.Please Deposit more money to continue playing.')
            deposit_money = input('Do you want deposit more money? (y/n): ')
            if deposit_money.lower() == 'y':
                deposit()
            elif deposit_money.lower() == 'q' or deposit_money.lower() == 'n':
                break

    print('Exiting to Main Menu ')
    return balance, None


def show_balance(balance):
    print(f'Your Balance 🤑 is Ksh {balance:.2f}')


print('--------------------------------------------------')
print('Welcome to Python Slots Machine ')
print('Symbols: 🍓 🍇 🍉 🍌 🔔 🌟 ')
print()


def main():
    balance = 100
    while True:
        print('------------------------------------')
        print('1. Play Slots Machine Game 🎰 ')
        print('2. Depsoit Money 💰 ')
        print('3. Withdraw Money 🤑 ')
        print('4. Check Balance 💵')
        print('5. Exit or Q to Quit ❌ ')
        print('------------------------------------')

        choice = input('Select your choice: (1-5): ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice ❌ ')
            continue
        choice = int(choice)
        if choice == 1:
            result = play_game(balance)
            if result is not None:
                balance, _ = result
        elif choice == 2:
            # balance += deposit()
            result = deposit()
            if result:
                balance += result

        elif choice == 3:
            result = deposit()
            if result:
                balance += result

        elif choice == 4:
            show_balance(balance)
        elif choice == 5:
            break
        else:
            print('Invalid Option ❌ ')

    print('\nThanks for Playing Slots Machine Game')
    print('Bye 👋👋👋 ...\n')


if __name__ == "__main__":
    main()
'''

########################################################################################
########################################################################################
# rock paper scissors game
'''
print('-------------------------------------')
print('ROCK PAPER SCISSORS GAME')
print('-------------------------------------\n')

while True:
    player = input(
        'Choose...\n1. for Rock 🪨 🪨, \n2. for Paper 📃📜\n3. for Scissors ✂️ ✂️:\n\n')

    python = random.choice('123')
    python = int(python)

    if player not in ['1', '2', '3']:
        print('Invalid  Choice ❌')
        break

    player = int(player)

    print(f'\nPlayer Chose: {player}')
    print(f'Python Chose: {python}\n')

    if player == 1 and python == 2:
        print('Player Win 🎉🎉')
    elif player == 2 and python == 3:
        print('Player Win 🎉🎉')
    elif player == 3 and python == 1:
        print('Player Win 🎉🎉')
    elif player == python:
        print('It is a Tie 🪢  🪢  ')
    else:
        print('Python Wins 🐍🐍 ')

    print()

print('\n-------------------------------------')
print('Thanks for playing Rock Paper Scissors Game')
'''

########################################################################################
########################################################################################


# rock paper scissors game
'''
print('-------------------------------------')
print('ROCK PAPER SCISSORS GAME')
print('-------------------------------------\n')

count = 0
player_wins = 0
python_wins = 0
game_ties = 0


def rps():
    global count, player_wins, python_wins, game_ties

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print()
    # print(RPS(2))
    # print(RPS.PAPER)
    # print(RPS.PAPER.value)
    # print(RPS['PAPER'])
    # print(RPS['PAPER'].value)
    # print(RPS['PAPER'].name)
    # print(RPS['PAPER'].name, RPS['PAPER'].value)

    # print()
    # print()RPS.ROCK.name, RPS.ROCK.value)

    player = input(
        'Choose...\n1. for Rock 🪨 🪨, \n2. for Paper 📃📜\n3. for Scissors ✂️ ✂️:\n\n')

    if player.lower() == 'q':
        print('\n-------------------------------------')
        sys.exit('Thanks for playing Rock Paper Scissors Game')

    python = random.choice('123')
    python = int(python)

    if not player.isdigit():
        print('Invalid Choice ❌')
        sys.exit()

    player = int(player)

    if player < 1 or player > 3:
        print('Invalid Choice ❌')
        sys.exit()

    print(f'\nPlayer Chose: {str(RPS(player)).replace('RPS.', '')}')
    print(f'Python Chose: {str(RPS(python)).replace('RPS.', '')}\n')

    def decide_winner(player, python):
        global count, player_wins, python_wins, game_ties
        if player == 1 and python == 2:
            return 1
        elif player == 2 and python == 3:
            return 1
        elif player == 3 and python == 1:
            return 1
        elif player == python:
            return 2
        else:
            return 0

    result = decide_winner(player, python)
    count += 1
    if result == 1:
        player_wins += 1
        print(f'Player Wins 🎉🎉')
    elif result == 2:
        game_ties += 1
        print(f'It is a Tie 🪢  🪢  ')
    elif result == 0:
        python_wins += 1
        print(f'Python Wins 🐍🐍 ')

    print()

    print('Do you want to play again? \n')
    play_again = True
    while play_again:
        play_again = input('Y to continue Q to quit: ')
        if play_again.lower() not in ['y', 'q']:
            continue
        else:
            break
    if play_again.lower() == 'y':
        print()
        rps()

    else:
        print('\n-------------------------------------')
        print(f'Game Count: {count}')
        print(f'Player Wins: {player_wins}')
        print(f'Python Wins: {python_wins}')
        print(f'Game Ties: {game_ties}')
        sys.exit('Thanks for playing Rock Paper Scissors Game\n')

    print()


rps()
'''


########################################################################################
########################################################################################

# Version 2

'''
choices = ['r', 'p', 's']

print('*******************************************************')
choice = input('choose rock, paper or scissors (r/p/s): ')

if choice not in choices:
    print(f'Invalid Choice ❌\n')
    sys.exit()

computer = random.choice(choices)

print(f'\nYou Chose: {choice}')
print(f'Computer Chose: {computer}\n')


if ((choice == 'r' and computer == 'p') or
    (choice == 'p' and computer == 's') or
        (choice == 's' and computer == 'r')):
    print('You Win 🎉🎉')
elif choice == computer:
    print('It is a Tie 🪢  🪢  ')
else:
    print('Computer Wins 👨‍💻')

print()'''

# =========================================================================
# =========================================================================
# =========================================================================


# Version 3
'''
choices = ['r', 'p', 's']

while True:
    print('*******************************************************')
    choice = input('choose rock, paper or scissors (r/p/s): ')

    if choice not in choices:
        print(f'Invalid Choice ❌\n')
        sys.exit()

    computer = random.choice(choices)

    print(f'\nYou Chose: {choice}')
    print(f'Computer Chose: {computer}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'p' and computer == 's') or
            (choice == 's' and computer == 'r')):
        print('You Win 🎉🎉')
    elif choice == computer:
        print('It is a Tie 🪢  🪢  ')
    else:
        print('Computer Wins 👨‍💻')
    print()

    should_continue = input('Continue (y/n): ').lower()
    if should_continue == 'y':
        print()
        continue
    else:
        break

print('\nThanks for playing Rock Paper Scissors Game\n')
'''
# =========================================================================
# =========================================================================
# =========================================================================

'''emojis = {
    'r': '🪨 🪨',
    'p': '📃 📃',
    's': '✂️ ✂️'
}

choices = ['r', 'p', 's']

while True:
    print('*******************************************************')
    choice = input('choose rock, paper or scissors (r/p/s): ')

    if choice not in choices:
        print(f'Invalid Choice ❌\n')
        sys.exit()

    computer = random.choice(choices)

    print(f'\nYou Chose: {emojis[choice]}')
    print(f'Computer Chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'p' and computer == 's') or
            (choice == 's' and computer == 'r')):
        print('You Win 🎉🎉')
    elif choice == computer:
        print('It is a Tie 🪢  🪢  ')
    else:
        print('Computer Wins 👨‍💻')
    print()

    should_continue = input('Continue (y/n): ').lower()
    if should_continue == 'y':
        print()
        continue
    else:
        break

print('\nThanks for playing Rock Paper Scissors Game\n')'''

# =========================================================================
# =========================================================================
# =========================================================================


def get_user_input():
    global player_wins, gamecount, computer_wins, game_ties

    while True:
        print('*******************************************************')
        choice = input('choose rock, paper or scissors (r/p/s): ')
        if choice.lower() == 'q':
            sys.exit(f'Thanks for playing Rock,Paper Scissors...\n')
        if choice not in choices:
            print(f'Invalid Choice ❌\n')
            continue
        elif choice in choices:
            return choice
        else:
            print(f'{choice} is an Invalid Input....\n')
            continue


def display_choices(choice, computer, emojis):
    return f'\nYou Chose: {emojis[choice]} \nComputer Chose: {emojis[computer]}\n'


def decide_winner(choice, computer):
    global player_wins, gamecount, computer_wins, game_ties
    gamecount += 1
    if ((choice == 'r' and computer == 'p') or
        (choice == 'p' and computer == 's') or
            (choice == 's' and computer == 'r')):
        player_wins += 1
        print('You Win 🎉🎉')
    elif choice == computer:
        game_ties += 1
        print('It is a Tie 🪢  🪢  ')
    else:
        computer_wins += 1
        print('Computer Wins 👨‍💻')
    print()


emojis = {
    'r': '🪨 🪨',
    'p': '📃 📃',
    's': '✂️ ✂️'
}

choices = ['r', 'p', 's']
gamecount = 0
player_wins = 0
computer_wins = 0
game_ties = 0


def main():
    while True:
        choice = get_user_input()

        computer = random.choice(choices)

        result = display_choices(choice, computer, emojis)
        print(result)

        decide_winner(choice, computer)

        should_continue = input('Continue (y/n): ').lower()
        if should_continue == 'y':
            print()
            main()

        elif should_continue == 'n':
            print('------------------------------------')
            print(f'Game Count: {gamecount}')
            print(f'Player Wins: {player_wins}')
            print(f'Computer Wins: {computer_wins}')
            print(f'Game Ties: {game_ties}')
            break
        else:
            continue

    print('\nThanks for playing Rock Paper Scissors Game\n')


if __name__ == "__main__":
    main()
