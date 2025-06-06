from enum import Enum
import random
import sys
import time
print()

print('############################################################################################')
print('############################################################################################')

print()

'''foods = []
food = input('Enter food you like (q to quit): ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit): ')

print()
if not foods:
    print('You did not enter any food you like!')

foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=" ")
'''
print()

####################################################################################################
####################################################################################################

'''
foods = []
food = input('Enter food you like (q to quit): ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit): ')

print()
if not foods:
    print('You did not enter any food you like!')

foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=" ")

print()
'''
####################################################################################################
####################################################################################################

'''foods = []
while True:
    food = input('Enter the foods you like (q to quit):  ')
    if food.lower() == 'q':
        break
    foods.append(food)

if not foods:
    print('You did not enter any food you like!\n')
foods = [food.strip() for food in foods]
for food in set(foods):
    print(food, end=" ")
print()
print()
'''

####################################################################################################
####################################################################################################

'''
food_price = {}
total = 0

while True:
    food = input('Enter the food you like (q to quit):  ')
    if food.lower() == 'q':
        break

    price = input(f'Enter the price of {food}: ')
    food_price[food] = float(price)

for food, price in food_price.items():
    total += food_price.get(food)
    total += foods_price.get(food)
    print(f'{food:10}: ${price:.2f}')

print()
print()
print(f'Your Total is: ${total:.2f}')
print()

'''

####################################################################################################
####################################################################################################
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

# display Menu
print(f'--------------🛍️  YOUR MENU 🛍️--------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f"{i}. {(food.capitalize()):10} ${price:.2f} ")
print()
print()

while True:
    food = input('Enter your food choice ( q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did not enter any food item')
        continue
    if menu.get(food.lower()) is None:
        print(f'{food} not available  📃 ')
        continue
    if menu.get(food.lower()) is not None:
        print(f'{food} added to cart ✅')
        cart.append(food)
print()

print(f'--------------🛒  YOUR CART  🛒--------------')

if not cart:
    print('Your Cart is Empty..Please choose the food items you want!')

for food in cart:
    if not cart:
        total = 0
    total += menu.get(food)
    print(food, end=" ")
print()
print(f'Your total is: ${total:.2f}')
print(f'------------------------------------------')

print()
'''
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

'''
foods = []
food = input('Enter food you like (q to quit):      ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):      ')
print()
foods = [food.strip() for food in foods]
for food in set(foods):
    print(food)

print()
print()
'''

####################################################################################################

'''
foods = []
food = input('Enter food you like (q to quit):  ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like (q to quit):      ')
print()
foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=" ")
print()
print()

'''

####################################################################################################

'''

foods = []
while True:
    food = input('Enter food you like (q to quit):  ')
    if food.lower() == 'q':
        break
    if not food:
        print('You did ot enter any food')
        continue
    foods.append(food)

print()
print('The foods you want are:  ')
foods = [food.strip() for food in foods]
for food in foods:
    print(food, end=' ')
print()
print()

'''
####################################################################################################

'''foods_price = {}
total = 0
while True:
    food = input('Enter food you like (q to quit):   ')
    if food.lower() == 'q':
        break
    price = input(f'Enter price of {food}:  ')
    foods_price[food] = float(price)

print()
print('The foods you like are: \n')
if not foods_price:
    print('You did not add any food you want!')
for food, price in foods_price.items():
    total += foods_price.get(food)
    print(f'{food:10}: ${price:.2f}')
print(f'\nTotal Bill: {total:.2f}')
print()
print()
'''
####################################################################################################
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


#   Display Menu
print('---------------- 🛍️  MENU 🛍️ ----------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {(food.capitalize()):10}: ${price:.2f}')
print()
print()

while True:
    food = input('Enter food you like:  ')
    if food.lower() == 'q':
        break

    if not food:
        print('You did not enter any  food')

    if menu.get(food) is not None:
        cart.append(food)
        print(f'{food} added to cart ✅ ')
        continue
    else:
        print(f'{food} not in menu ❌')
        continue
print()
print('----------------🛒 CART 🛒----------------')
if not cart:
    print('No item added to your cart')
total = 0
for food in cart:
    total += menu.get(food)
    print(food)
print()
print(f'Your Total is $ {total:.2f}')
'''
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

'''
# day to units converter
choices = ['😀', '😁', '😊', '😎', '🤩', '🤓']


def days_hours(days):
    emoji = random.choice(choices)
    if days > 0:
        print(f'{days} Days to hours ⏳ is {days * 24} Hours {emoji}')
    elif days == 0:
        print('You entered a  0️⃣ . so no conversion for You!! 😟')
    elif days < 0:
        print("You entered a NEGATIVE NUMBER 🚫 !! don\'t ruin the program 🚫")


def validate_and_excute(days):
    if days.isdigit():
        days = int(days)
        days_hours(days)
    else:
        print('Enter valid # 🔢 of days ❌ ')


while True:
    days = input('Enter # 🔢 of days and I\'ll convert it to Hours ⌛:   ')
    if days.lower() == 'q':
        break
    validate_and_excute(days)

print('\n 👋👋 Thanks for Using Days Convter!!!\n')
'''

####################################################################################################

# Using a List
# day to units converter

'''choices = ['😀', '😁', '😊', '😎', '🤩', '🤓']


def days_hours(days):
    emoji = random.choice(choices)
    return f'{days} Days to hours ⏳ is {days * 24} Hours {emoji}'


def validate_and_excute(days):
    days = days.split(',')
    days = [day.strip() for day in days]
    for day in days:
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(days_hours(day))
            if day == 0:
                print(f'You entered a  0️⃣ . so no conversion for You!! 😟')
            elif day < 0:
                print(f"You entered a NEGATIVE NUMBER 🚫 !! don\'t ruin the program 🚫")
        else:
            print('Enter valid # 🔢 of days ❌ ')


while True:
    print('\n-----------------------------------------------------------------')
    print('Enter 🔢 days as a List sepated by a comma (,) \nand I\'ll convet them to Hours ⌛ eg 10, 20, 30, 50 \n')
    days = input('Your Days:     ')
    if days.lower() == 'q':
        break
    validate_and_excute(days)

print('\n 👋👋 Thanks for Using Days Convter!!!\n')'''


####################################################################################################

'''# Using a Dicionary
# day to units converter

choices = ['😀', '😁', '😊', '😎', '🤩', '🤓']


def days_hours(days, units):
    emoji = random.choice(choices)
    if units.lower() == 'hours':
        return f'{days} Days to hours ⏳ is {days * 24} Hours {emoji}'
    elif units.lower() == 'minutes':
        return f'{days} Days to minutes ⏳ is {days * 24} Minutes {emoji}'
    elif units.lower() in ['seconds', 'sec', 'second', 'secs']:
        return f'{days} Days to seconds ⏳ is {days * 24} Seconds {emoji}'
    else:
        return f'Invalid Unit'


def validate_and_excute(days):
    days = days.split(':')
    days = [day.strip() for day in days]
    days_units = {
        'days': days[0],
        'units': days[1]
    }
    user_days = days_units['days']
    user_units = days_units['units']

    if user_days.isdigit():
        user_days = int(user_days)
        if user_days > 0:
            print(days_hours(user_days, user_units))
        elif user_days == 0:
            print(f'You entered a  0️⃣ . so no conversion for You!! 😟')
        elif user_days < 0:
            print(f"You entered a NEGATIVE NUMBER 🚫 !! don\'t ruin the program 🚫")
    else:
        print('Enter valid # 🔢 of days ❌ ')


while True:
    print('\n-----------------------------------------------------------------')
    print('Enter 🔢 Days and Units Seperated by colon (:) \nand I\'ll convet them to Hours ⌛ eg 10:Hours, 20:Minutes, 30:seconds\n')
    days = input('Your Days:     ')
    if days.lower() == 'q':
        break
    validate_and_excute(days)

print('\n 👋👋 Thanks for Using Days Convter!!!\n')'''


####################################################################################################
'''
# python rock paper scissors
print('ROCK 🪨 🪨  PAPER 📃 📃  SCISSORS ✂️  ✂️ ')
print()

player_wins = 0
python_wins = 0
game_ties = 0
gamecount = 0


def rps():
    global player_wins, python_wins, game_ties, gamecount

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    player = input(
        'Choose...\n1. for Rock\n2. for Paper\n3. for Sciccors..\n\n')
    if player.lower() == 'q':
        print('\nThanks for playing Rock 🪨 Paper 📃 Scissors ✂️')
        sys.exit(f'👋👋 Bye 👋👋\n')

    if player not in ['1', '2', '3']:
        print('Please Enter 1, 2, 3 only... \n')
        return rps()

    player = int(player)
    python = random.choice('123')
    python = int(python)

    print(f'\nPlayer Chose: {str(RPS(player)).replace('RPS.', '')}')
    print(f'Computer Chose: {str(RPS(python)).replace('RPS.', '')} \n')

    def decide_winner(player, python):
        if player == 1 and python == 2:
            return player
        elif player == 2 and python == 3:
            return player
        elif player == 3 and python == 1:
            return player
        elif player == python:
            return 0
        else:
            return python

    result = decide_winner(player, python)
    gamecount += 1
    if result == player:
        player_wins += 1
        print('You Won 🎉🎉')
    elif result == 0:
        game_ties += 1
        print('🎭 🎭 It is a Tie  🪢 🪢 ')
    elif result == python:
        python_wins += 1
        print('Computer Wins 🧑‍💻')

    print('\nDo you want to Play Again? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue Q to Quit:  ')
        if play_again.lower() not in ['q', 'y']:
            continue
        else:
            break
    if play_again.lower() == 'y':
        print()
        return rps()
    else:
        print(f'\n------------------------------------------------')
        print(f'Total Game Count: {gamecount} time(s)')
        print(f'Player Wins: {player_wins} time(s)')
        print(f'Python Wins: {python_wins} time(s)')
        print(f'Player and Python ties: {game_ties} time(s)')
        print(f'\nThanks for playing Rock 🪨  Paper 📃 Scissors ✂️')
        sys.exit(f'👋   👋    Bye     👋  👋  \n')


rps()

'''

####################################################################################################

'''
# non local, return function 
# python rock paper scissors
print('ROCK 🪨 🪨  PAPER 📃 📃  SCISSORS ✂️  ✂️ ')
print()


def play():

    player_wins = 0
    python_wins = 0
    game_ties = 0
    gamecount = 0

    def rps():
        nonlocal player_wins, python_wins, game_ties, gamecount

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player = input(
            'Choose...\n1. for Rock\n2. for Paper\n3. for Sciccors..\n\n')
        if player.lower() == 'q':
            print('\nThanks for playing Rock 🪨 Paper 📃 Scissors ✂️')
            sys.exit(f'👋👋 Bye 👋👋\n')

        if player not in ['1', '2', '3']:
            print('Please Enter 1, 2, 3 only... \n')
            return rps()

        player = int(player)
        python = random.choice('123')
        python = int(python)

        print(f'\nPlayer Chose: {str(RPS(player)).replace('RPS.', '')}')
        print(f'Computer Chose: {str(RPS(python)).replace('RPS.', '')} \n')

        def decide_winner(player, python):
            if player == 1 and python == 2:
                return player
            elif player == 2 and python == 3:
                return player
            elif player == 3 and python == 1:
                return player
            elif player == python:
                return 0
            else:
                return python

        result = decide_winner(player, python)
        gamecount += 1
        if result == player:
            player_wins += 1
            print('You Won 🎉🎉')
        elif result == 0:
            game_ties += 1
            print('🎭 🎭 It is a Tie  🪢 🪢 ')
        elif result == python:
            python_wins += 1
            print('Computer Wins 🧑‍💻')

        print('\nDo you want to Play Again? ')
        play_again = True
        while play_again:
            play_again = input('Y to continue Q to Quit:  ')
            if play_again.lower() not in ['q', 'y']:
                continue
            else:
                break
        if play_again.lower() == 'y':
            print()
            return rps()
        else:
            print(f'\n------------------------------------------------')
            print(f'Total Game Count: {gamecount} time(s)')
            print(f'Player Wins: {player_wins} time(s)')
            print(f'Python Wins: {python_wins} time(s)')
            print(f'Player and Python ties: {game_ties} time(s)')
            print(f'\nThanks for playing Rock 🪨  Paper 📃 Scissors ✂️')
            sys.exit(f'👋   👋    Bye     👋  👋  \n')

    return rps()


result = play()
print(result)
'''

####################################################################################################
'''
#   Use of while loop

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


while True:
    player = input(
        'Choose...\n1. for Rock\n2. for Paper\n3. for Sciccors..\n\n')
    if player.lower() == 'q':
        print('\nThanks for playing Rock 🪨 Paper 📃 Scissors ✂️')
        sys.exit(f'👋👋 Bye 👋👋\n')

    # if player not in ['1', '2', '3']:
    #     print('Please Enter 1, 2, 3 only... \n')
    #     continue
    if not player.isdigit():
        print('Invalid Input....\n')
        continue
    player = int(player)
    if 1 < player > 3:
        print('Invalid choice...Only Enter 1 , 2 or 3')
        continue

    python = random.choice('123')
    python = int(python)

    print(f'\nPlayer Chose: {str(RPS(player)).replace('RPS.', '')}')
    print(f'Computer Chose: {str(RPS(python)).replace('RPS.', '')} \n')

    def decide_winner(player, python):
        if player == 1 and python == 2:
            return player
        elif player == 2 and python == 3:
            return player
        elif player == 3 and python == 1:
            return player
        elif player == python:
            return 0
        else:
            return python

    result = decide_winner(player, python)
    if result == player:
        print('You Won 🎉🎉')
    elif result == 0:
        print('🎭 🎭 It is a Tie  🪢 🪢 ')
    elif result == python:
        print('Computer Wins 🧑‍💻')

    print('\nDo you want to Play Again? ')
    play_again = True
    while play_again:
        play_again = input('Y to continue Q to Quit:  ')
        if play_again.lower() not in ['q', 'y']:
            continue
        else:
            break
    if play_again.lower() == 'y':
        print()
        continue
    else:
        print(f'\n------------------------------------------------')
        print(f'\nThanks for playing Rock 🪨  Paper 📃 Scissors ✂️')
        sys.exit(f'👋   👋    Bye     👋  👋  \n')

'''

####################################################################################################
####################################################################################################

'''
# Version 2     #   Programming with Mosh
choices = ['r', 'p', 's']
while True:
    choice = input('Choose rock paper or scissors (r/p/s):  ').lower()
    if choice.lower() == 'q':
        break

    if choice not in choices:
        print('\nInvalid choice! Only Choose r/p/s\n')
        continue

    computer = random.choice(choices)

    print(f'\nYou choose: {choice}')
    print(f'Commputer chose: {computer}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        print(f'You Win 🎉🎉')
    elif choice == computer:
        print('It is a Tie  🪢  🪢  ')
    else:
        print(f'Computer Wins   🧑‍💻  👨‍💻  ')
    print()

    should_continue = input('Continue? (y/n):  ').lower()
    if should_continue == 'y':
        continue
    else:
        break

print('\nThanks for using ROCK PAPER SCISSORS')
print(f'Exiting....Bye...\n')

'''

####################################################################################################

'''
emojis = {
    'r': '🪨  🪨',
    'p': '📃  📜',
    's': '✂️  ✂️'
}
choices = ['r', 'p', 's']

print('ROCK 🪨 🪨  PAPER 📃 📃  SCISSORS ✂️  ✂️ ')


while True:
    choice = input('Choose rock paper or scissors (r/p/s):  ').lower()
    if choice.lower() == 'q':
        break

    if choice not in choices:
        print('\nInvalid choice! Only Choose r/p/s\n')
        continue

    computer = random.choice(choices)

    print(f'\nYou choose: {emojis.get(choice)}')
    print(f'Commputer chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        print(f'You Win 🎉🎉')
    elif choice == computer:
        print('It is a Tie  🪢  🪢  ')
    else:
        print(f'Computer Wins   🧑‍💻  👨‍💻  ')
    print()

    should_continue = input('Continue? (y/n):  ').lower()
    if should_continue == 'y':
        continue
    else:
        break

print('\nThanks for using ROCK 🪨 PAPER 📜 SCISSORS ✂️')
print(f'Exiting....Bye 👋👋...\n')

'''


####################################################################################################

'''
# Version 2 Updated code

def get_user_input():
    while True:
        choice = input('Choose rock paper or scissors (r/p/s):  ').lower()
        if choice.lower() == 'q':
            return None

        if choice not in choices:
            print('\nInvalid choice! Only Choose r/p/s\n')
            continue
        return choice


def display_choices(choice, computer, emojis):
    print(f'\nYou choose: {emojis.get(choice)}')
    print(f'Commputer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    global player_wins, computer_wins, game_ties, gamecount
    gamecount += 1
    if ((choice == 'r' and computer == 'p') or
        (choice == 'r' and computer == 'p') or
            (choice == 'r' and computer == 'p')):
        player_wins += 1
        print(f'You Win 🎉🎉')
    elif choice == computer:
        game_ties += 1
        print('It is a Tie  🪢  🪢  ')
    else:
        computer_wins += 1
        print(f'Computer Wins   🧑‍💻  👨‍💻  ')
    print()


emojis = {
    'r': '🪨  🪨',
    'p': '📃  📜',
    's': '✂️  ✂️'
}
choices = ['r', 'p', 's']
player_wins = 0
computer_wins = 0
gamecount = 0
game_ties = 0

print('ROCK 🪨 🪨  PAPER 📃 📃  SCISSORS ✂️  ✂️ ')


def main():
    global player_wins, computer_wins, game_ties, gamecount

    while True:

        choice = get_user_input()
        if choice == None:
            break

        computer = random.choice(choices)
        display_choices(choice, computer, emojis)
        decide_winner(choice, computer)

        should_continue = input('Continue? (y/n):  ').lower()
        if should_continue == 'y':
            continue
        else:
            break

    print('\n-----------------------------------------------')
    print(f'Total Game Count: {gamecount}')
    print(f'Your Wins: {player_wins}')
    print(f'Computer Wins: {computer_wins}')
    print(f'Game Ties: {game_ties}')
    print('\nThanks for using ROCK 🪨 PAPER 📜 SCISSORS ✂️')
    print(f'Exiting....Bye 👋👋...\n')


if __name__ == "__main__":
    main()
'''

####################################################################################################
####################################################################################################
