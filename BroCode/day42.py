from enum import Enum
import math
import random
import sys
import time
print()


##########################################################################
##########################################################################

'''foods = []
food = input('Enter foood you like (q to quit):  ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')


print()
if not foods:
    print('You did not enter any food')
else:
    print('The foods you like are: ')
    foods = [food.strip() for food in foods]
    for food in foods:
        print(food, end=" ")
    print()
print()'''

##########################################################################
##########################################################################

'''foods = []
food = input('Enter foood you like (q to quit):  ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')


print()
if not foods:
    print('You did not enter any food')
else:
    print('The foods you like are: ')
    foods = [food.strip() for food in foods]
    for food in foods:
        print(food, end=" ")
    print()
print()'''

##########################################################################
##########################################################################
'''
foods = []
while True:
    print('---------------------------------------------')
    food = input('Enter the food you like (q to quit):   ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food! ')
        continue
    foods.append(food)

print()
if not foods:
    print('You dont have any food you like')
else:
    print('The foods you like are: ')
    foods = [food.strip() for food in foods]

    for food in foods:
        print(food, end='  ')
    print()
print()'''

##########################################################################
##########################################################################

'''foods_prices = {}
total = 0
while True:
    print('----------------------------------------')
    food = input('Enter the food you like (q to quit):  ')
    if food.lower() == 'q':
        break
    while True:
        try:
            price = float(input(f'Enter the price of {food}:  '))
            if price < 0:
                print('Price caanot be a negative number!!')
                continue
            foods_prices[food] = price
            break
        except ValueError:
            print('Invalid price amount')
            continue
print()
if not foods_prices:
    print(f'You did not enter any foods!! ')
else:
    print('------------------ YOUR FOODS ------------------')
    for i, (food, price) in enumerate(foods_prices.items(), start=1):
        # total += foods_prices.get(food)
        total += foods_prices[food]
        print(f'{i}. {(food.capitalize()):10}: ${price:.2f} ')
    print()
print(f'Total Bill: ${total:.2f} \n')

print('----------------------------------------')'''


##########################################################################
##########################################################################

'''menu = {
    'nachos': 3.56,
    'pretzel': 4.00,
    'sugar': 3.90,
    'coffee': 2.50,
    'sweets': 1.60,
    'popcorns': 2.40,
    'chips': 3.00,
    'burger': 4.60,
    'pizza': 2.78,
}
total = 0
cart = []

# display menu
# ask user for item
# display cart , total
print(f'---------------- CNCERSSION STAND  ----------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food.capitalize():10}: $ {price:.2f}')
print()
print()

while True:
    food = input('Enter the food you want (q to quit)? ')
    if food.lower() == 'q':
        break
    if menu.get(food) is not None:
        print(f'{food} Added ✅')
        cart.append(food)
    else:
        print(f'{food} not in menu ❌')
        continue
print()
if not cart:
    print('You have not choosen any items!')
else:
    print(f'---------------- Foods selected are:  ----------------')
    for food in cart:
        total += menu.get(food)
        print(f'{(food.capitalize()):10}: {menu.get(food):.2f}')
    print()
print(f'Total Bill: ${total:.2f}')
print('----------------------------------------')'''

##########################################################################
##########################################################################


'''menu = {
    'nachos': 3.56,
    'pretzel': 4.00,
    'sugar': 3.90,
    'coffee': 2.50,
    'sweets': 1.60,
    'popcorns': 2.40,
    'chips': 3.00,
    'burger': 4.60,
    'pizza': 2.78,
}
cart = {}
total = 0

# display menu
# ask user for item
# display cart , total

print(f'---------------- CNCERSSION STAND  ----------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food.capitalize():10}: $ {price:.2f}')
print()
print()

while True:
    food = input('Enter the food you want (q to quit)? ')
    if food.lower() == 'q':
        break

    if menu.get(food) is not None:
        cart[food] = menu[food]
        print(f'{food} Added ✅ to  Cart 🛒')
    else:
        print(f'{food} not in menu ❌')
        continue


print()
if not cart:
    print('You have not choosen any items!')
else:
    print(f'---------------- Foods selected are:  ----------------')

    for i, (food, price) in enumerate(cart.items(), start=1):
        total += price
        print(f'{i}. {food.capitalize():10}: ${price:.2f}')
    print()
print(f'Total Bill: ${total:.2f}')
print('----------------------------------------')'''


##########################################################################
##########################################################################

'''random_number = random.randint(1, 10)
while True:
    print('-------------------------------------------')
    guess = input('Guess a number between 1 and 10 (q to quit): ')
    if guess.lower() == 'q':
        break
    if not guess.isdigit():
        print('Invalid Number!! ❌')
        continue
    guess = int(guess)
    if 1 < guess > 10:
        print('Only Guess between 1 and 20!!')
        continue
    if guess <= 0:
        print('Guess between 1 and 10!! ')
    elif guess > random_number:
        print('Sorry!! Too High!! Wrong Guess')
    elif guess < random_number:
        print('Sorry!! Too Low!! Wrong Guess')
    else:
        print('Yay!!! Correct Guess!! \n')
        break
'''
##########################################################################


'''def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        try:
            guess = int(input(f'Guess a number beteen 1 and {x}: '))
            if 1 < guess > x:
                print(f'Guess only between 1 and {x}')
                continue
            elif guess > random_number:
                print('Sorry!! Guess again. Too High!!')
            elif guess < random_number:
                print('Sorry!! Guess again. Too Low!!')
        except ValueError:
            print('Invalid guess Number!!')

    print(
        f'\nYay!! Congrats. You Guessed the Correct Number!! {random_number}\n')


guess(20)'''


'''def computer(x):
    low = 1
    high = x
    feedback = ''
    print('Guess a number I am thinking about 🤔 ?')
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high

        feedback = input(
            f"Is {guess} too high 'H', too low 'L' , or correct 'C'?    ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print('\nWow... You got it Right comouter!!\n')


computer(30)'''

##########################################################################

# ''' rock paper scissors

'''
def play():
    user = input(
        "What\'s your choice?  'r' for rock, 'p' for paper, or 's' for scissors:  \n")
    if user not in (['r', 'p', 's']):
        print('Only choose r p or s')
        return play()

    computer = random.choice(['r', 'p', 's'])

    print(f'\n Player chose {user}')
    print(f'Computer chose {computer} \n')

    if user == computer:
        return 'It\'s a Tie\n'

    # # r > s, s > p, p > r
    if is_win(user, computer) == True:
        return 'You Win\n'

    return 'Computer Wins!!\n'


def is_win(player, opponent):
    # return True if player wins
    # # r > s, s > p, p > r

    if ((player == 'r' and opponent == 's') or
        (player == 'p' and opponent == 'r') or
            (player == 's' and opponent == 'p')):
        return True


rps = play()
print(rps)
'''

##########################################################################
'''
# rock paper scissors


def rps():

    user = input(
        "What do you you choose rock 'r' paper 'p' or scissors 's' ? \n\n").lower()
    if user not in (['r', 'p', 's']):
        print('Invalid Choice!  ')
        return rps()
    computer = random.choice(['r', 'p', 's'])

    print(f'\nPlayer chose: {user}')
    print(f'Computer chose: {computer}\n')

    if user == computer:
        return 'It is a Tie\n'

    elif is_win(user, computer):
        return 'You Win!!\n'

    return 'Player Wins!!'


def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or
        (player == 'p' and opponent == 'r') or
            (player == 's' and opponent == 'p')):
        return True


def proceed():
    # playagain = True
    # while playagain:
    #     playagain = input('Do you want to play again (y / n):   ')
    #     if playagain.lower() not in ['y', 'n']:
    #         continue
    #     else:

    #         break
    # if playagain.lower() == 'y':
    #     print()
    #     print(rps())
    # else:
    #     print('\nThanks for playing Rock Paper Scissors!!\n')
    #     playagain = False
    while True:
        playagain = input('Do you want to play again (y / n):   ')
        if playagain.lower() not in ['y', 'n']:
            continue
        if playagain.lower() == 'y':
            print()
            print(rps())
        else:
            print('\nThanks for playing Rock Paper Scissors!!\n')
            playagain = False


def main():
    play = rps()
    print(play)
    proceed()


main()
'''
##########################################################################
##########################################################################
##########################################################################

'''foods = []
food = input('Enter the food you like (q to quit):  ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')
print()

if not food:
    print('You did not enter any food!!  ')
else:
    print('The foods you like are: ')
    foods = [food.strip() for food in foods]

    for food in foods:
        print(food, end=" ")
    print()
    print()'''

##########################################################################
'''
foods = []
food = input('Enter the food you like (q to quit):  ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')
print()

if not foods:
    print('You did not enter any food you like!!  \n')
else:
    print('The foods you like are: ')
    foods = [food.strip() for food in foods]

    for food in foods:
        print(food, end=" ")
    print()
    print()

'''

##########################################################################
'''
foods = {}
total = 0

while True:
    food = input('Enter the food you like (q to quit): ')
    if food.lower() == 'q':
        break
    while True:
        try:
            price = float(input(f'Enter the price of {food}:  '))
            foods[food] = price
            break
        except ValueError:
            print('Invalid {food} price .Please enter a valid price!!')
            continue
print()
for food, price in foods.items():
    print(f'{food.capitalize():10}: ${price:.2f}')
    # total += foods.get(food)
    total += foods[food]
print(f'Total is: {total:.2f}')
print()'''

##########################################################################


"""menu = {
    'nachos': 200,
    'pretzel': 300,
    'oranges': 500,
    'pizza': 600,
    'milk': 200,
    'burger': 400,
    'chips': 500,
}

total = 0
cart = []

print(f'************** CONCESSION STAND ****************')
for food, price in menu.items():
    print(f'{(food.capitalize()):10}: ${price:.2f}')
print()

while True:
    food = input('Enter the food you want (q to quit): ')
    if food.lower() == 'q':
        break
    if menu.get(food) is not None:
        cart.append(food)
        print(f'{food.capitalize()} added ✅ to Cart 🛒')
    else:
        print('Item not in Menu ❌')

print()
if not cart:
    print('You did not select any item!! ')
    total = 0
else:
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")
print()
print(f'Total Bill: {total:.2f}')
print()"""


##########################################################################

'''menu = {
    'nachos': 200,
    'pretzel': 300,
    'oranges': 500,
    'pizza': 600,
    'milk': 200,
    'burger': 400,
    'chips': 500,
}

total = 0
cart = {}

print(f'************** CONCESSION STAND ****************')
for food, price in menu.items():
    print(f'{(food.capitalize()):10}: ${price:.2f}')
print()

while True:
    food = input('Enter the food you want (q to quit): ')
    if food.lower() == 'q':
        break
    if menu.get(food) is not None:
        cart[food] = menu[food]
        print(f'{food.capitalize()} added ✅ to Cart 🛒')
    else:
        print('Item not in Menu ❌')

print()
if not cart:
    print('You did not select any item!! ')
    total = 0
else:
    for i, (food, price) in enumerate(cart.items(), start=1):
        total += cart[food]
        print(f'{(food.capitalize()):10}: ${price:.2f}')
print()
print(f'Total Bill: {total:.2f}')
print()
'''

##########################################################################

'''
# python slots machine game


def spin_row():
    symbols = ['🍉',  '🍎',  '🍌',  '🔔',  '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('---------------------------------------')
    print('      |       '.join(row))
    print('---------------------------------------')


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


print('-----------------------------------')
print('Welcome to Python Slots Machine Game')
print('Symbols: 🍉  🍎  🍌  🔔  🌟')
print('')


def main():
    balance = 100
    while balance > 0:
        print('-----------------------------------')
        print(f'Current Balance is {balance:.2f}')
        bet = input('Enter bet amount (q to quit):  ')
        if bet.lower() == 'q':
            break
        if not bet.isdigit():
            print(f'Invalid Bet amount !! ❌')
            continue
        bet = int(bet)

        if bet > balance:
            print('Insufficient Funds ❌')
            continue
        if bet == 0:
            print('Bet amount cannot be 0')
            continue
        if bet < 0:
            print('Bet amount cannot be a negative number!! ❌')
        balance -= bet

        row = spin_row()
        display_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Yay!! Congrats You Won!! ${payout:.2f}')
            balance += payout
        else:
            print('Sorry 😔😥 !!! You did not win anything in this round!!!')

        if balance <= 4:
            print('\nYou ran out of funds..Exiting the application!!!')
            break

        should_continue = input('\nContinue playing? (y/n): ')
        if should_continue == 'y':
            print()
            continue
        else:
            break

    print('\nThanks for playing Python Slots Machine Game!! 👋')


if __name__ == "__main__":
    main()
    '''

##########################################################################

# python slots machine game


def spin_row():
    symbols = ['🍉',  '🍎',  '🍌',  '🔔',  '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print('---------------------------------------')
    print('      |       '.join(row))
    print('---------------------------------------')


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


def deposit():
    while True:
        amount = input('Enter amount to deposit (q to quit):  ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu!!')
            return None
        elif not amount.isdigit():
            print('Invalid Deposit amount!! ❌')
            continue
        amount = int(amount)
        if amount < 0:
            print('Deposit amount cannot be 0!! ')

        elif amount < 10:
            print('Minimum Deposit amount is $10')

        elif amount == 0:
            print('Deposit cannot be a a 0!! ')
        else:
            print(f'Successfully Deposited ${amount:.2f} ✅')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw (q to quit):  ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu!!')
            return None
        elif not amount.isdigit():
            print('Invalid withdrawal amount!! ❌')
            continue
        amount = int(amount)
        if amount > balance:
            print(
                'Insuffcient Funds!! Current Wallet Balance is: ${balance:.2f}')

        if amount < 0:
            print('Withdrawal amount cannot be less than 0!! ')

        elif amount < 10:
            print('Minimum Withdrawal amount is $10')

        elif amount == 0:
            print('Withdrawal cannot be a a 0!! ')
        else:
            print(f'Successfully Withdrawan ${amount:.2f} ✅')
            return amount


def show_balance(balance):
    print(f'Your Balance 🤑 is Ksh {balance:.2f}')


def play(balance):
    while balance > 0:
        print('-----------------------------------')
        print(f'Current Balance is {balance:.2f}')
        bet = input('Enter bet amount (q to quit):  ')
        if bet.lower() == 'q':
            break
        if not bet.isdigit():
            print(f'Invalid Bet amount !! ❌')
            continue
        bet = int(bet)

        if bet > balance:
            print('Insufficient Funds ❌')
            continue
        if bet == 0:
            print('Bet amount cannot be 0')
            continue
        if bet < 0:
            print('Bet amount cannot be a negative number!! ❌')
        balance -= bet

        row = spin_row()
        display_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f'Yay!! Congrats You Won!! ${payout:.2f}')
            balance += payout
        else:
            print('Sorry 😔😥 !!! You did not win anything in this round!!!')

        if balance <= 4:
            print('\nYou ran out of funds..')

            deposit_money = input('Do you want deposit more money? (y/n): ')
            if deposit_money.lower() == 'y':
                print()
                result = deposit()

                if result:
                    balance += result

                continue
            elif deposit_money.lower() == 'q' or deposit_money.lower() == 'n':
                break

        should_continue = input('\nContinue playing? (y/n): ')
        if should_continue == 'y':
            print()
            continue
        else:
            break

    print('\nExiting to main Menu')
    time.sleep(3)
    return balance, None


print('-----------------------------------')
print('Welcome to Python Slots Machine Game')
print('Symbols: 🍉  🍎  🍌  🔔  🌟')
print('')


def main():
    balance = 100
    while True:
        print('-----------------------------------')
        print('1. Play Python Slots Game')
        print('2. Show Balance')
        print('3. Deposit Funds')
        print('4. Withdraw Funds')
        print('5. Show Bet History')
        print('6. Exit or Q to quit.')

        choice = input('\nSelect your choice (0-6):  ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Selection!!! Only choose 0-6 !!')
            continue
        choice = int(choice)
        if choice == 0:
            break
        elif choice == 1:
            # balance = play(balance)
            result = play(balance)
            if result is not None:
                balance, _ = result

        elif choice == 2:
            show_balance(balance)

        elif choice == 3:

            result = deposit()
            if result:
                balance += result

        elif choice == 4:

            result = withdraw(balance)
            if result:
                balance -= result

        elif choice == 5:
            pass
        elif choice == 6:
            break
        else:
            print('Invalid Selection!!! Only choose 0-6 !!')
            continue

    print('\nThanks for playing Python Slots Machine Game!! 👋\n')


if __name__ == "__main__":
    main()

##########################################################################
# python bank application

'''
def show_balance():
    pass


def deposit():
    pass

ssss
def withdraw():
    pass


def main():
    pass


if __name__ == "__main__":
    main()
'''
##########################################################################

# OOP Class Based Banking App

'''
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def get_balance():
        pass

    def deposit():
        pass

    def withdraw():
        pass

    def viableTransaction():
        pass

    def transfer():
        pass


class InterestRewards(BankAccount):
    pass


class SavingsInterest(InterestRewards):
    pass
'''
##########################################################################

'''
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def get_balance():
        pass

    def deposit():
        pass

    def withdraw():
        pass

    def viableTransaction():
        pass

    def transfer():
        pass


class InterestRewards(BankAccount):
    pass


class SavingsInterest(InterestRewards):
    pass


def createAccount():
    pass


def displayAccount():
    pass


def findAccount():
    pass


def main():
    pass


if __name__ == "__main__":
    main()'''
