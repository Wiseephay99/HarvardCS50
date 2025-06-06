import sys
import math
import time
import random
print()

'''questions = (
    "How many days are there in a week?",
    "How many planets are there in the solar system?",
    'How many states does the USA have?',
    'Which year did Kenya gain independence?',
    'How many couties are there in Kenya?'
)
answers = (
    ("A. 5", "B. 6", "C. 7", "D. 8", "E. 10"),
    ("A. 5", "B. 8", "C. 9", "D. 6", "E. 7"),
    ("A. 50", "B. 51", "C. 45", "D. 52", "E. 55"),
    ("A. 1963", "B. 1964", "C. 1965", "D. 1966", "E. 1962"),
    ("A. 45", "B. 46", "C. 47", "D. 48", "E. 50")
)

correct_answers = ['C', 'C', 'A', 'A', 'C']
question_num = 0
guess = 0
guesses = []
score = 0

for i, (question) in enumerate((questions), start=1):
    print('---------------------------------------')
    print(f'{i}. {question}')

    for answer in answers[i-1]:
        print(answer)
    print()

    choices = ['A', 'B', 'C', 'D', 'E']
    while True:
        guess = input('Enter your answer: A B C D E:  ').upper()
        if guess not in choices:
            print('Invalid choice..')
            continue

        guesses.append(guess)

        if guess == correct_answers[i-1]:
            score += 1
            print('CORRRECT ANSWER')
            break
        else:
            print('INCORRECT ANSWER')
            break
    question_num += 1
    print()
print()
print('--------------------RESULTS-------------------')
print('Guesses:', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print('Answers:', end=" ")
for correct_answer in correct_answers:
    print(correct_answer, end=" ")
print()

score = (score / len(questions) * 100)
print(f'You Scored {score:.2f}%')
print('---------------------------------------\n')
'''
#######################################################################
#######################################################################

'''print(f'Printing a NumPad Lock')

print()

# print((1, 2, 3),
# (4, 5, 6),
# (7, 8, 9),
# ('*', 0, '#')
#       )
num_lock = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

for row in num_lock:
    for e in row:
        print(e, end=" ")
    print()
'''
#######################################################################
#######################################################################

'''
foods = []

food = input('Enter food you like (q to quit):  ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')
    if food in foods:
        print(f'{food} already in list')
        continue

print()
for food in set(foods):
    print(food, end=" ")
'''

#######################################################################
#######################################################################

'''foods = []

food = input('Enter food you like (q to quit):  ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):  ')


print()
if not foods:
    print('No fruits in your list')
for food in set(foods):
    print(food, end=" ")

'''

#######################################################################
#######################################################################

'''
foods_prices = {}
while True:
    print('-----------------------------------------------')
    food = input('Enter the food you like (q to quit):  ')
    if food == 'q':
        break
    while True:
        price = input(f'Enter price of {food}:  ')
        if not price.isdigit():
            print(f'{price} is not a valid amount')
            continue
        else:
            foods_prices[food] = float(price)
            break
print()
for i, (food, price) in enumerate((foods_prices.items()), start=1):
    print(f'{i}. {food:10}: {price:.2f}')
print()
for price in foods_prices.values():
    total += price
print(f'Total Cost is: ${total:.2f}')
print('-----------------------------------------------')
'''

#######################################################################
#######################################################################
'''
menu = {
    'apple': 2.30,
    'tea': 4.50,
    'nachos': 3.60,
    'pretzel': 4.60,
    'chips': 1.45,
    'popcorn': 2.70,
    'candy': 3.40
}
cart = {}
total = 0
print('------------------MENU----------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:10}: {price:.2f}')
print('----------------------------------------')

while True:
    food = input('Enter the food item from the menu (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food item...')
    if menu.get(food) is not None:
        cart[food] = menu[food]

print()
print('------------------YOUR CART----------------')
for i, (food, price) in enumerate(cart.items(), start=1):
    print(f'{i}. {food:10}: {price:.2f}')
print()
print('------------------TOTAL----------------')
for price in cart.values():
    total += price
print(f'Total Cost is: ${total:.2f}')
print('----------------------------------------')
'''


#######################################################################
#######################################################################

# Python Slots Game

def check_balance(balance):
    print(f'\nCurrent Account Balance: 💵 ${balance:.2f}\n')


def spin_row():
    symbols = ['🍉', '🍎', '🍌', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def dispaly_row(row):
    print('-----------------------------------')
    print('        |       '.join(row))
    print('-----------------------------------')


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


def play_game(balance):
    while balance > 0:
        print('-----------------------------------')
        print(f'Current Account Balance: 💵 ${balance:.2f}')
        bet = input('Enter bet amount (q to quit): ')
        if bet.lower() == 'q':
            print('Exiting to Main Menu')
            main(balance)
        if not bet.isdigit():
            print('Invalid bet amount.')
            continue

        bet = int(bet)
        if bet > balance:
            print('Insufficient Funds..')
            continue
        if bet == 0:
            print('Bet amount cannot be 0')
            continue
        if bet <= 5:
            print('Minimum bet amount is $5')
            continue
        balance -= bet
        row = spin_row()
        dispaly_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f'🎉🎊 Congrats 🎉🎊 You won ${payout:.2f}')
            balance += payout
            print(f'Current Account Balance: 💵 ${balance:.2f}\n')
        else:
            print('😓 😔 😞 You did not win anything in this round...\n')

        if balance <= 5:
            print('You ran out of betting funds..')
            print('Top Up to continue playing...')
            print('Exiting to Main Menu')
            time.sleep(2)
            main(balance)
            return


def deposit():
    while True:
        amount = input('Enter the amount to deposit (q to quit):  ')
        if amount.lower() == 'q':
            time.sleep(2)
            print('Exiting to Main Menu')
            main(balance)
            return
        if not amount.isdigit():
            print(f'{amount} is an invalid amount...')
            continue
        amount = int(amount)
        if amount == 0:
            print('You cannot deposit 0')
            continue
        elif amount <= 10:
            print('Minimum deposit amount is $10')
            continue
        elif amount <= 0:
            print('Deposit cannot be a Negative Number..')
        else:
            print(f'Successfully Deposited ${amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter the amount to withdraw (q to quit):  ')
        if amount.lower() == 'q':
            time.sleep(2)
            print('Exiting to Main Menu')
            main(balance)
            return
        if not amount.isdigit():
            print(f'{amount} is an invalid amount...')
            continue
        amount = int(amount)
        if amount > balance:
            print('Insufficient Funds')
            continue
        if amount == 0:
            print('You cannot withdraw 0')
            continue
        elif amount <= 10:
            print('Minimum withdrawal amount is $10')
            continue
        elif amount <= 0:
            print('amount cannot be a Negative Number..')
        else:
            print(f'Successfully withdrawn ${amount:.2f}')
            return amount


def exit_game():
    print('\n-----------------------------------')
    print('Exiting Game... Thanks for playing Python Slots Machine')
    time.sleep(2)
    sys.exit('Bye 👋 🙋‍♂️ 🙋‍♀️ \n')


print('Welcome to Python Slots Spin Game')
print('Symbols: 🍉 🍎 🍌 🔔 🌟')
balance = 100


def main(balance):
    while True:
        print('-----------------------------------')
        print('1. Show Balance 💶 💵')
        print('2. Play Game ▶️  🎭 ')
        print('3. Deposit Funds 💳 💸')
        print('4. Withdraw Funds 🪙  💰 💳')
        print('5. Exit ❌ or Q to quit Game')
        print('-----------------------------------')

        choice = input('Select you choice 1-5 🔢 (q to quit):  ')
        if choice.lower() == 'q':
            exit_game()
        if not choice.isdigit():
            print('Invalid Choice')
            continue
        choice = int(choice)
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            play_game(balance)
        elif choice == 3:
            balance += deposit()
        elif choice == 4:
            balance -= withdraw(balance)
        elif choice == 5:
            exit_game()
        else:
            print('Invalid choice..')
            continue


if __name__ == "__main__":
    main(balance)
