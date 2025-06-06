import random
import time
from enum import Enum
import sys
'''print()
print('********************************************')
print(f'ROCK 🪨 🪨  PAPER 📃 📜 SCISSORS ✂️ ✂️\n')
# ROCK PAPER SCISSORS

player_wins = 0
computer_wins = 0
ties = 0
game_count = 0


def rps():
    global player_wins, computer_wins, ties, game_count

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    print('***************************')
    player = input(
        'Choose...\n1 for ROCK 🪨 🪨 \n2 for Paper 📃 📜\n3 for Scissors ✂️ ✂️\nQ to quit\n\n')
    if player.lower() == 'q':
        sys.exit('\nBye\n')

    if not player.isdigit():
        print('Invalid Input')
        return rps()

    player = int(player)
    if player < 1 or player > 3:
        print('Invalid Input')
        return rps()

    computer = random.choice('123')
    computer = int(computer)

    # print('***************************')
    # print(f'Player chose: {str(RPS(player)).replace("RPS.", '')}')
    # print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}')
    # print('***************************')

    def display_choices():
        print('***************************')
        print(f'Player chose: {str(RPS(player)).replace("RPS.", '')}')
        print(f'Computer chose: {str(RPS(computer)).replace("RPS.", '')}')
        print('***************************')
    display_choices()

    # Method 1
    # if player == 1 and computer == 2:
    #     print('Player Wins')
    # elif player == 2 and computer == 3:
    #     print('Player Wins')
    # elif player == 3 and computer == 1:s
    #     print('Player Wins')
    # elif player == computer:
    #     print('It is a Tie')
    # else:
    #     print('Computer Wins')

    # Method 2
    def decide_winner():
        if player == 1 and computer == 2:
            return 1
        elif player == 2 and computer == 3:
            return 1
        elif player == 3 and computer == 1:
            return 1
        elif player == computer:
            return 2
        else:
            return 3

    result = decide_winner()
    game_count += 1
    if result == 1:
        player_wins += 1
        print('Player Wins')
    elif result == 2:
        ties += 1
        print('It is a Tie')
    elif result == 3:
        computer_wins += 1
        print('Computer Wins')
    print('***************************')
    print()
    print('Do you want to play again? ')
    play_again = True
    while play_again:
        play_again = input('Y to playagain..N or Q to quit..\n')
        if play_again not in ['q', 'n', 'y']:
            print('Moving to the next question...')
        else:
            print('\n***************************')
            print(f'Game Count: {game_count}')
            print(f'Player Wins: {player_wins}')
            print(f'Computer Wins: {computer_wins}')
            print(f'Game Ties: {ties}')
            print('***************************\n')

            break
    if play_again.lower() == 'y':
        return rps()


rps()
'''
# rock paper scissors
#####################################################################
#####################################################################
#####################################################################
'''

print(f'\n*********************************************')
print(f'ROCK 🪨 🪨  PAPER 📃 📜 SCISSORS ✂️ ✂️\n')

emojis = {
    'r': '🪨',
    'p': '📜',
    's': '✂️'
}
choices = ['r', 'p', 's']
while True:
    print(f'*******************************************')
    choice = input(
        'choose rock, paper or scissors (r/p/s) (q to quit): ').lower()

    if choice not in choices:
        print('Invalid selection choice')
        continue

    computer = random.choice(choices)
    if choice == 'q':
        sys.exit('\n 👋 Bye 👋\n')

    # print(f'\nPlayer chose: {choice}')
    # print(f'Computer chose: {computer}\n')

    print(f'\nPlayer chose: {emojis.get(choice)}')
    print(f'Computer chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        print('🏆🏆 Player Wins 🏆🏆')
    elif choice == computer:
        print('🎭🎭 It is a game Tie 🎭🎭')
    else:
        print(' 🧑‍💻 Computer Wins 🧑‍💻 ')
    print()

    should_continue = input('Continue? (y/n):   ').lower()
    if should_continue == "y":
        print()
        continue
    else:
        break

print('\n👋 Bye 👋 \n')

'''

#####################################################################
#####################################################################
#####################################################################

# print(f'\nPlayer chose: {choice}')
# print(f'Computer chose: {computer}\n')

'''
def get_user_input():
    while True:
        choice = input(
            'choose rock, paper or scissors (r/p/s) (q to quit): ').lower()
        if choice == 'q':
            return None

        if choice not in choices:
            print('Invalid selection choice')
            continue

        return choice


def display_choices(emojis, choice, computer):
    print(f'\nPlayer chose: {emojis.get(choice)}')
    print(f'Computer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    global player_wins, computer_wins, ties, game_count
    game_count += 1
    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        player_wins += 1
        print('🏆🏆 Player Wins 🏆🏆')
    elif choice == computer:
        ties += 1
        print('🎭🎭 It is a game Tie 🎭🎭')
    else:
        computer_wins += 1
        print(' 🧑‍💻 Computer Wins 🧑‍💻 ')
    print()


print(f'\n*********************************************')
print(f'ROCK 🪨 🪨  PAPER 📃 📜 SCISSORS ✂️ ✂️\n')

emojis = {
    'r': '🪨',
    'p': '📜',
    's': '✂️'
}
choices = ['r', 'p', 's']

player_wins = 0
computer_wins = 0
ties = 0
game_count = 0


def rps():
    global player_wins, computer_wins, ties, game_count
    while True:
        print(f'*******************************************')

        choice = get_user_input()
        if choice == None:
            break

        computer = random.choice(choices)

        display_choices(emojis, choice, computer)

        decide_winner(choice, computer)

        should_continue = input('Continue? (y/n):   ').lower()
        if should_continue == "y":
            print()
            continue
        else:
            break

    print(f'\n********************************')
    print(f'              Results             ')
    print(f'********************************')
    print(f'Game count: {game_count}')
    print(f'Player wins: {player_wins}')
    print(f'Computer wins: {computer_wins}')
    print(f'Game ties: {ties}')
    print(f'********************************')

    print('\n👋 Exiting RPS Bye 👋\n')


if __name__ == "__main__":
    rps()
'''
#####################################################################
#####################################################################
#####################################################################

'''print()

# Bank App


def check_balance(balance):
    print(f'\nCurrent Account Balance is: ${balance:.2f}\n')


def deposit():
    while True:
        amount = input('Enter the amount to deposit?    ')
        if amount.lower() == 'q':
            print('\nExiting to Main Menu\n')
            return main()

        if not amount.isdigit():
            print('Invalid Input')
            continue

        amount = int(amount)
        if amount <= 10:
            print('You cannot deposit an amount lower than $10')
            continue

        if amount == 0:
            print('You cannot deposit a 0')
            continue
        else:
            print(f'Successfully deposited ${amount:.2f} to your account')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter the amount to withdraw?    ')
        if amount.lower() == 'q':
            print('\nExiting to Main Menu\n')
            return main()

        if not amount.isdigit():
            print('Invalid Input')
            continue

        amount = int(amount)
        if amount > balance:
            print('Insufficient Funds..')
            continue

        elif amount <= 10:
            print('You cannot withdraw an amount lower than $10')
            continue

        elif amount == 0:
            print('You cannot withadraw a 0')
            continue
        else:
            print(f'Successfully withdrawn  ${amount:.2f} to your account')
            return amount


print('Welcome to Python Bank Application')


def main():
    balance = 0

    while True:
        print(f'*********************')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        print(f'*********************')
        choice = input('\nSelect your option (1-4) ? ')
        if choice == 'q':
            break

        if not choice.isdigit():
            print('Invalid Option')
            continue

        choice = int(choice)

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            # balance += deposit()
            result = deposit()
            if result is not None:
                balance += result
            result = deposit()
            if result == None:
                break
        elif choice == 3:
            # balance -= withdraw(balance)
            result = withdraw(balance)
            if result is not None:
                balance -= result
            result = withdraw(balance)
            if result == None:
                break
        elif choice == 4:
            break
        else:
            print('Invalid Option')
            continue

    print(f'\nThanks for using Python Bank...')
    print(f'Bye... Exiting\n')


if __name__ == '__main__':
    main()
'''

#####################################################################
#####################################################################
#####################################################################
'''
# Python Slot Machine


def spin_row():
    symbols = ['🍉', '🍌', '🍎', '🔔', '🌟']
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results


def display_row(row):
    print()
    print(" | ".join(row))
    print()


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍌':
            return bet * 5
        elif row[0] == '🍎':
            return bet * 7
        elif row[0] == '🍊':
            return bet * 8
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🌟':
            return bet * 20
    return 0


def main():
    print('\nWelcome to Python Slot Machine Game')
    print(f'Symbols:  🍉 🍇 🍌 🍎 🍊 🔔 🌟\n')

    balance = 100
    while balance > 0:
        print(f'Current balance is: {balance:.2f}')
        bet = input('Enter bet amount (q to quit):  ')
        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print('Invalid bet amount')
            continue

        bet = int(bet)

        if bet <= 0:
            print('Bet amount cannot be less than 0')
            continue
        if bet == 0:
            print('Bet amount cannot be a 0')

        balance -= bet

        row = spin_row()
        display_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            balance += payout
            print(f'🎊🎊 Congrats 🎉🎉 you won ${payout:.2f}')
            print(f'Current Balance is: {balance:.2f}')
        else:
            print('😔😔 Sorry, You did not win anything in this round...')

    print('\nThanks for playing Python Slots\n')


if __name__ == "__main__":
    main()
'''


#####################################################################
#####################################################################
#####################################################################
'''
# Conserssion Stand
menu = {
    'porpcorn': 3.50,
    'pretzels': 4.00,
    'soda': 2.50,
    'nachos': 6.00,
    'burger': 2.65,
    'hotdog': 3.60,
    'chips': 1.50,
    'candy': 2.00,
    'icecream': 4.50,
    'water': 1.00,
    'pizza': 5.50,
    'coffee': 2.75,
    'tea': 2.25,
    'milkshake': 3.75,
    'brownies': 2.50,
    'cake': 3.00,
    'cookies': 1.75,
    'donuts': 2.50,
    'cupcakes': 3.50,
    'pancakes': 4.00,
    'waffles': 4.50,
    'sandwich': 5.00,
    'salad': 4.00,
    'soup': 3.50,
}
cart = {}
total = 0

print(f'\n-----------MENU CONSERSSION STAND---------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:<10}: ${price:.2f}')
print()

while True:
    food = input('Enter the food you like: ').lower()
    if food == "q":
        break

    if not food:
        print('You did not select an item!')
        continue

    if menu.get(food) is not None:
        cart[food] = menu[food]

print(f'\n------------------YOUR MENU-----------------------')
for i, (food, price) in enumerate(cart.items(), start=1):
    print(f'{i}. {food:<10}: ${price:.2f}')
print(f'---------------------TOTAL-----------------------')
for price in cart.values():
    total += price

print(f'Your Total Bill is: {total:.2f}')
print(f'----------------------------------------------------')
'''

#####################################################################
#####################################################################
#####################################################################


# print('---------------------------------------')
# foods = []
# food = input('Enter the food you like(q to quit):   ')
# while not food == 'q':

#     foods.append(food)

#     food = input('Enter another food you like(q to quit):   ')

# print()
# if not foods:
#     print('You did not enter any food you like...')

# print(f'The foods you like are: ')
# for food in set(foods):
#     print(food.capitalize(), end=' ')

# print()


#####################################################################
#####################################################################
#####################################################################
'''
print()
print(f'-------------------------------------')
foods = []
food = input('Enter the food you like (q to quit): ')
while not food == 'q':

    foods.append(food)

    food = input('Enter another food you like (q to quit):      ')

print()
if not foods:
    print(f'You did not eter any food you like...')
print(f'The foods you like are: ')
for food in set(foods):
    print(food.capitalize(), end=' ')

print()
'''
#####################################################################
#####################################################################
#####################################################################

print()

questions = (
    '1. How many days are there in a week?',
    '2. How many teeth does an adult Human have?',
    '3. When did Kenya gain independce',
    '4. Who was the first president of Kenya?',
    '5. How many planets are there in the solar system?',
)

answers = (
    ('A. 5', 'B. 7', 'C. 8', 'D. 6'),
    ('A. 34', 'B. 36', 'C. 32', 'D. 38'),
    ('A. 1963', 'B. 1964', 'C. 1964', 'D. 1965'),
    ('A. Kibaki', 'B. Moi', 'C. Kenyatta', 'D. Zakayo'),
    ('A. 10', 'B. 6', 'C. 7', 'D. 9'),
)


question = 0
guess = 0
guesses = []
corrrect_answers = ['B', 'C', 'A', 'C', 'D']

for i, question in enumerate(questions, start=1):
    print('---------------------------------------')
    print(question)

    for line in answers[i - 1]:
        print(line)
    print()

    choices = ['A', 'B', 'C', 'D']
    while True:
        guess = input('Choose your answer (A/B/C/D): ').upper()

        if guess not in choices:
            print('Invalid choice')
            continue

        guesses.append(guess)

        if guess == corrrect_answers[i - 1]:
            print('Correct Answer')
            break
        else:
            print('Incorrect Answer')
            break

    print()  # Add a blank line for better readability before the next question

print('---------------------------------------')
print(f'Guesses: {str(guesses)}')
print('---------------------------------------')
print(f'Correct Answers: {str(corrrect_answers)}')
print('---------------------------------------')
