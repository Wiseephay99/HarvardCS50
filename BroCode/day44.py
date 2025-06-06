from enum import Enum
import sys
import time
import random
print()
'''

def display_cart(cart):
    if not cart:
        print('Your cart is empty!\n')
    else:
        print(f'\n--------- Your Shoping Cart  ---------')
    total_price = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']}")
        total_price += item['price']
    print(f'Total Price is: ${total_price:.2f}')


def main():
    cart = []
    while True:
        print('--------- Shoping Cart Application ---------')
        print('1. Add Item to cart')
        print('2. View Cart')
        print('3. Remove Item from Cart')
        print('4. Exit')

        choice = input('Enter your choice:  ')
        if choice.lower() == 'q':
            break

        if choice == "1":
            item_name = input('Enter item name: ')
            item_price = float(input('Enter item price:  '))
            item = {
                "name": item_name,
                "price": item_price
            }
            cart.append(item)
            print('Item Added ✅ to Cart 🛒')

        elif choice == '2':
            display_cart(cart)

        elif choice == "3":
            if not cart:
                print('Your cart is already empty!!')
            else:
                display_cart(cart)
                item_index = int(
                    input('Enter the item number to remove:  ')) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"Removed 🗑️ item: {removed_item['name']}\n")
                else:
                    print(f'Invalid Item number')

        elif choice == "4":
            print('Exit the Application!! ')
            break

        else:
            print('Invalid Choice. Pleae select a valid option !! ')


if __name__ == "__main__":
    main()
'''

##############################################################################
##############################################################################

'''
def display_cart(cart):
    if not cart:
        print('Your Cart is Empty!!')
    else:
        total = 0
        print('\n------------- YOUR CART -------------')
        for i, item in enumerate(cart, start=1):
            print(
                f'{i}. {(item['name']).capitalize():10}: {item['price']:.2f}')
            total += item['price']

    print(f'Total Bill : {total:.2f}\n')
    print('-------------------------------------')


def add_item(cart):

    item_name = input('\nEnter the name of the item (q to quit):  ')
    while item_name != 'q':
        if item_name == "q":
            print('Exiting to Main Menu!!')
            time.sleep(2)
            return None
        try:
            item_price = float(input(f'Enter the price of {item_name}:  '))
            item = {
                "name": item_name,
                "price": item_price
            }
            cart.append(item)
            print(f"{item['name']} Added ✅ to cart 🛒\n")
            item_name = input('Enter another item (q to quit):  ')
            continue
        except ValueError:
            print('Invalid Price Amount')
            continue
    return cart


def view_cart(cart):
    if not cart:
        print('Your cart is empty!!')
    else:
        print(f'\n------------- YOUR CART -------------')
        for i, item in enumerate(cart, start=1):
            print(f'{i}. {item['name']:10}: ${item['price']:.2f}')
        print()


def remove_cart(cart):
    while True:
        if not cart:
            print('Your cart is already empty')
        else:
            view_cart(cart)
            item_indx = input('Enter the number of the item to remove: ')
            if item_indx.lower() == "q":
                print('Exiting to Mian Menu')
                break

            item_indx = int(item_indx) - 1

            if 0 <= item_indx < len(cart):
                removed_item = cart.pop(item_indx)
                print(f"{removed_item['name']} removed ❌ from cart 🛒 ")
            else:
                print(f'{item_indx} is an invalid number!! ')

    return cart


def main():
    print('Welcome to Online Shopping Cart\n')
    cart = []
    while True:
        print('1. Add Item to Cart')
        print('2. Remove Item from Cart')
        print('3. Display Cart')
        print('4. View Cart')
        print('5. Q to Quit / Exit the Application')

        choice = input('\nSelect your choice?:  ')
        if choice.lower() == 'q':
            break
        if choice == '1':
            cart = add_item(cart)
        elif choice == "2":
            cart = remove_cart(cart)
        elif choice == "3":
            display_cart(cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            break
        else:
            print('Invaid choice!! Only choose 1-5!')
            continue

    print('\nThanks for using Python Online Shopping Cart\n')


if __name__ == "__main__":
    main()
    '''
##############################################################################
##############################################################################


'''# Rock paper scissors

print('ROCK PAPER SCISSORS GAME \n')
while True:
    player = input(
        'Choose....\n1. for Rock\n2. for Paper\n3. for Scissors...\nQ to Quit...\n\n')
    if player.lower() == 'q':
        sys.exit('Bye.Thanks for playing Rock Paper Scissors\n')
    if player not in ['1', '2', '3']:
        print('Invalid Choice!!Please choose 1 2 or 3\n')
        continue
    player = int(player)

    computer = random.choice('123')
    computer = int(computer)

    print(f'\nPlayer choose: {player}')
    print(f'Computer choose: {computer}\n')

    if player == 1 and computer == 2:
        print('Player Wins 🎉🎉🎉')
    if player == 2 and computer == 3:
        print('Player Wins 🎉🎉🎉')
    if player == 3 and computer == 1:
        print('Player Wins 🎉🎉🎉')
    elif player == computer:
        print('It is a Tie 🪢🪢')
    else:
        print('Computer Wins 🧑‍💻 ')

    print()
'''
##############################################################################
##############################################################################
'''
# Rock paper scissors
print('ROCK PAPER SCISSORS GAME \n')


def play():
    player_wins = 0
    computer_wins = 0
    game_count = 0
    game_ties = 0

    def rps():
        nonlocal game_count, game_ties, player_wins, computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player = input(
            'Choose....\n1. for Rock\n2. for Paper\n3. for Scissors...\nQ to Quit...\n\n')
        if player.lower() == 'q':
            sys.exit('\nBye.Thanks for playing Rock Paper Scissors\n')
        if player not in ['1', '2', '3']:
            print('Invalid Choice!!Please choose 1 2 or 3\n')
            rps()
        player = int(player)

        computer = random.choice('123')
        computer = int(computer)

        print(f'\nPlayer choose: {str(RPS(player)).replace("RPS.", " ")}')
        print(f'Computer choose: {str(RPS(computer)).replace("RPS.", " ")}\n')

        def decide_winner(player, computer):
            if player == 1 and computer == 3:
                return 1
            elif player == 2 and computer == 3:
                return 1
            elif player == 3 and computer == 1:
                return 1
            elif player == computer:
                return 2
            else:
                return 0

        result = decide_winner(player, computer)
        game_count += 1
        if result == 1:
            player_wins += 1
            print('Player Wins 🎉 🎉 🎉')
        elif result == 2:
            game_ties += 1
            print('It is a Tie 🪢 🪢 ')
        elif result == 0:
            computer_wins += 1
            print('Computer Wins 🧑‍💻 ')

        print()
        print('Do you want to continue playing?\n')
        play_again = True
        while play_again:
            play_again = input('Y to continue Q to Quit: ')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break
        if play_again.lower() == 'y':
            print()
            rps()
        else:
            print('Computing results ♻️ ♻️ ♻️')
            time.sleep(3)
            print(f'\n----------------------------------------')
            print(f'Game count: {game_count}')
            print(f'Player Wins: {player_wins}')
            print(f'Computer Wins: {computer_wins}')
            print(f'Player and Computer Ties: {game_ties}\n')
            print(f'Thanks for playing ROCK PAPER SCISSORS\n')

    return rps()


play()
'''
##############################################################################
##############################################################################
'''
choices = ['r', 'p', 's']
emojis = {
    "r": "🪨  🪨  🪨",
    "p": "📃  📜  📄",
    "s": "✂️  ✂️  ✂️"
}

while True:
    print('--------------------------------------------')
    choice = input('Choose rock paper or scissors: r/p/s:  ')
    if choice not in choices:
        print('Invalid Choice! Only choose r / p / s')

    computer = random.choice(choices)

    print(f'\nYou choose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')

    if ((choice == 'r' and computer == 's') or
        (choice == 'p' and computer == 'r') or
            (choice == 's' and computer == 'p')):
        print('You Won 🎉 🎉 🎉')
    elif choice == computer:
        print('It is a Tie 🪢 🪢')
    else:
        print('Computer Won 🧑‍💻')
    print()

    should_continue = input('Continue? (y / n):  ')
    if should_continue == 'y':
        continue
    else:
        break

print('\nThanks for playing Rock Paper Scissors\n')
'''

##############################################################################
##############################################################################
'''
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# choices = ['r', 'p', 's']

emojis = {
    ROCK: "🪨  🪨  🪨",
    PAPER: "📃  📜  📄",
    SCISSORS: "✂️  ✂️  ✂️"
}
choices = tuple(emojis.keys())

player_wins = 0
computer_wins = 0
game_count = 0
game_ties = 0


def get_user_input():
    while True:
        print('--------------------------------------------')
        choice = input(
            'Choose rock paper or scissors (q to quit): r / p / s:  ').lower()
        if choice == 'q':
            break
        if choice in choice:
            return choice
        else:
            print('Invalid Choice! Only choose r / p / s')


def display_choices(choice, computer):
    print(f'\nYou choose: {emojis[choice]}')
    print(f'Computer chose: {emojis[computer]}\n')


def decide_winner(choice, computer):
    global player_wins, computer_wins, game_count, game_ties
    game_count += 1
    if ((choice == ROCK and computer == SCISSORS) or
            (choice == PAPER and computer == ROCK) or
            (choice == SCISSORS and computer == PAPER)):
        player_wins += 1
        print('You Won 🎉 🎉 🎉')

    elif choice == computer:
        game_ties += 1
        print('It is a Tie 🪢 🪢')

    else:
        computer_wins += 1
        print('Computer Won 🧑‍💻')
    print()


def results():
    print('-------------------------------------')
    print(f'Game count: {game_count}')
    print(f'Player Wins: {player_wins}')
    print(f'Computer wins: {computer_wins}')
    print(f'Game Ties: {game_ties}')


def main():
    while True:
        choice = get_user_input()
        if choice is None:
            break

        computer = random.choice(choices)

        display_choices(choice, computer)

        decide_winner(choice, computer)

        should_continue = input('Continue? (y / n):  ')
        if should_continue == 'y':
            continue
        else:
            results()
            break

    print('\nThanks for playing Rock Paper Scissors\n')


if __name__ == "__main__":
    main()
'''

##############################################################################
##############################################################################

'''
def play():
    user = input("What\'s your choice? rock paper or scissors: (r/p/s):  ")
    if user.lower() == 'q':
        sys.exit(f'Thanks for playing Rock Paper Scissors!')
    if user not in ['r', 'p', 's']:
        print('Invalid Choice!! Only choose (r p or s) ')
    computer = random.choice(['r', 'p', 's'])

    print(f'\nYou choose: {user}')
    print(f'Computer choose: {computer}\n')

    if user == computer:
        return f'It is a Tie  🪢 🪢\n'

    if is_win(user, computer):
        return f'Player Won 🎉 🎉 🎉\n'

    return f'Computer Won 🧑‍💻  🧑‍💻 \n'


def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or
        (player == 'p' and opponent == 's') or
            (player == 's' and opponent == "r")):
        return True


result = play()
print(result)
'''
##############################################################################
##############################################################################
'''
#   Stop Watch Timer
print('---------------- Stop Watch ----------------')
# coutdown timer in python
time.sleep(3)

my_time = int(input('Enter time in seconds: '))

for x in range(0, my_time):
    print(x)
    time.sleep(2)

print('TIMES UP')

my_time = int(input('Enter time in seconds: '))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(2)

print('TIMES UP')
'''

##############################################################################
##############################################################################

'''
print('Stop Watch')
my_time = int(input('Enter the time in seconds for your stopwatch:  '))

for i in range(0, my_time):
    print(i)
    time.sleep(2)

print('Your Time is Up!!')

'''

'''

your_time = int(input('Enter your time?  '))
for i in range(your_time, 0, -1):
    seconds = i % 60
    minutes = int(i / 60)
    hours = int(i / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(2)

print("Alarm Time is Up!! ")

'''

##############################################################################
##############################################################################

'''
def display_cart(cart):
    if not cart:
        print('Your cart is empty! No Item in your cart!')
    else:
        total = 0
        print('------------- Your Cart -------------')
        for i, item in enumerate(cart, start=1):
            print(
                f"{i}. {(item['name']).capitalize():10}: {item['price']:.2f}")
            total += item['price']
        print()
        print(f'Total is: {total:.2f}\n')


def add_item(cart):
    while True:
        item_name = input('Enter the item you want (q to quit):   ')
        if item_name.lower() == 'q':
            print('Exiting to Main Menu!')
            time.sleep(1)
            break
        try:
            item_price = float(input(f'Enter the price of the {item_name}:  '))
            print(f'{item_name} added ✅ to cart 🛒')
            item = {
                "name": item_name,
                "price": item_price
            }
            cart.append(item)
            continue

        except ValueError:
            print(f'Invalid Price for {item_name} Enter a valid price!! ')
            continue

    return cart


def remove_item(cart):
    while True:
        if not cart:
            print('Your cart is already empty!!')
        else:
            view_cart(cart)
            item_index = input('Enter the number of the item to remove?  ')
            if item_index.lower() == 'q':
                print('Exiting to Main Menu')
                time.sleep(2)
                break
            item_index = int(item_index) - 1
            if 0 <= item_index < len(cart):
                removed_item = cart.pop(item_index)
                print(f"Removed ❌ {removed_item['name']:10} from cart 🛒")
            else:
                print('Invalid Item Number')
                continue
    return cart


def update_cart():
    pass


def view_cart(cart):
    if not cart:
        print('No item in your cart!!')
    else:
        total = 0
        print('------------- Your Cart -------------')
        for i, item in enumerate(cart, start=1):
            print(
                f'{i}. {(item['name']).capitalize():10}: {item['price']:.2f}')
            total += item['price']
        print()


def main():
    cart = []
    print('Welcome to Python Shopping Cart')
    while True:
        print('-----------------------------------')
        print('1. Display Item')
        print('2. Add Item')
        print('3. Remove Item')
        print('4. Update Item')
        print('5. View Item')

        choice = input('\nSelect your choice:  ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid choice!! ')
        choice = int(choice)
        if choice == 1:
            display_cart(cart)
        elif choice == 2:
            cart = add_item(cart)

        elif choice == 3:
            cart = remove_item(cart)

        elif choice == 4:
            cart = update_cart(cart)
        elif choice == 5:
            view_cart(cart)
        else:
            print('Invalid choice!1 Select 1-5')

    print('\nThanks for using  Python Shopping Cart \n')

if __name__ == "__main__":
    main()'''

##############################################################################
##############################################################################

'''
def display_cart(cart):
    if not cart:
        print('Cart 🛒 is Empty! ')
    else:
        total = 0
        print('---------- YOUR CART ------------')
        for i, item in enumerate(cart, start=1):
            print(f'{i}. {item['name']:10}: {item['price']:.2f}')
            total += item['price']
        print()
        print(f'Total Bill: {total:.2f}')


def add_item(cart):
    while True:
        item_name = input('Enter Item Name (Q to Quit):  ')
        if item_name.lower() == 'q':
            time.sleep(1)
            print('Exting to Main Menu')
            time.sleep(2)
            break
        item_price = float(input(f'Enter price of {item_name}:  '))
        item = {
            'name': item_name,
            'price': item_price
        }
        cart.append(item)
        print(f'{item["name"]} Added ✅ to cart 🛒')

    return cart


def remove_item(cart):
    if not cart:
        print(f'Your cart 🛒 is already Empty 🛒')
    else:
        while True:
            view_cart(cart)
            item_index = input('Enter number of item you want to remove:  ')
            if item_index.lower() == 'q':
                break
            item_index = int(item_index) - 1
            if 0 <= item_index < len(cart):
                removed_item = cart.pop(item_index)
                print(f'Removed {removed_item['name']}')
            else:
                print('Invalid Item Number!! ❌')
                continue
        print('Exiting Main Menu')
        time.sleep(2)
        return cart


def update_cart(cart):
    if not cart:
        print(f'Your cart 🛒 is already empty ')
    else:
        while True:
            view_cart(cart)
            item_index = input('Enter number of the item to edit:  ')
            if item_index.lower() == 'q':
                break
            item_index = int(item_index) - 1
            if 0 <= item_index < len(cart):
                new_item = input('New Item name:  ')
                cart[item_index]['name'] = new_item
                print(f"Item updated to: {new_item}")
            else:
                print('Invalid Item number!!')
                continue
        print('Exiting To Main Menu ❌')
        return cart


def view_cart(cart):
    if not cart:
        print('Cart 🛒 is Empty! ')
    else:
        total = 0
        print('---------- YOUR CART ------------')
        for i, item in enumerate(cart, start=1):
            print(f'{i}. {item['name']:10}: {item['price']:.2f}')
            total += item['price']
        print()


def main():
    cart = []
    print('Welcome to Python 🐍 Shopping 🛍️ Cart 🛒')
    while True:
        print('-----------------------------')
        print('1. Display Cart 🛒')
        print('2. Add Item 🏪')
        print('3. Remove Item from Cart! ❌')
        print('4. Update Cart 🛒')
        print('5. View Cart 🧺 ')
        print('6. Q to quit or Exit 👋')

        choice = input('\nSelect your option (1-6):  ')
        if choice.lower() == 'q':
            break
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print('Invalid Option!! ❌Only choose (1-6)')
            continue
        if choice == '1':
            display_cart(cart)
        elif choice == '2':
            cart = add_item(cart)
        elif choice == '3':
            cart = remove_item(cart)
        elif choice == '4':
            cart = update_cart(cart)
        elif choice == '5':
            view_cart(cart)
        elif choice == '6':
            break

    print('\nThanks for Using Python 🐍 Shopping 🛍️ Cart 🛒\n')


if __name__ == "__main__":
    main()
'''

##############################################################################
##############################################################################

'''
questions = (
    ('Which year did Kenya Gain Independence? '),
    ('How many teeth does an adult human being have? '),
    ('How many states does the USA have? '),
    ('Which is the biggest planet in the solar system? '),
    ('What is the name of the new Pope? '),
    ('How many Bones does the human body have? '),
    ('What is the name of the first president of Kenya? '),
)
options = (
    ('A. 1966', 'B. 1963', 'C. 1964', 'D. 1960', 'E. 1952'),
    ('A. 32', 'B. 33', 'C. 34', 'D. 28', 'E. 30'),
    ('A. 51', 'B. 54', 'C. 50', 'D. 49', 'E. 53'),
    ('A. Jupiter', 'B. Venus', 'C. Earth', 'D. Mars', 'E. Pluto'),
    ('A. Pope Paul', 'B. Pope John', 'C. Pope Innocent',
     'D. Pope Francis', 'E. Pope Leo'),
    ('A. 107', 'B. 108', 'C. 109', 'D. 110', 'E. 111'),
    ('A. William Ruto', 'B. Uhuru Kenyatta',
     'C. Jomo Kenyatta', 'D. Raila Odinga', 'E. Mwai Kibaki'),
)
question_num = 0
guesses = []
score = 0
correct_answers = ['B', 'A', 'C', 'A', 'D', 'C', 'C']
total = 0

for question in questions:
    print('-----------------------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    choices = ['A', 'B', 'C', 'D', 'E']
    while True:
        guess = input('Choose your answer: (A B C D or E):  ').upper()
        if guess.lower() == 'q':
            break
        if guess not in choices:
            print('Invalid Guess..Only Guess A B C D E')
            continue
        guesses.append(guess)
        if guess == correct_answers[question_num]:
            score += 1
            print('CORRECT ANSWER ✅ ')
            break
        else:
            print('INCORRECT ANSWER ❌ ')
            break

    question_num += 1

print()
print('----------- Answers ----------- ')
for answer in correct_answers:
    print(answer, end=' ')
print()

print('----------- Guesses ----------- ')
for guess in guesses:
    print(guess, end=' ')
print()

total += score
result = ((total / len(questions)) * 100)
if result > 90:
    print(f'Excellent: {result:.2f}% 💯')
elif 80 < result < 90:
    print(f'Very Good: Your scored: {result:.2f}%')
elif 60 < result < 80:
    print(f'Good: Your scored: {result:.2f}%')
elif 40 < result < 60:
    print(f'Work Harder!: Your scored: {result:.2f}%')
elif result <= 40:
    print(f'Pull Up your socks!!!: Your scored: {result:.2f}%')
print('--------------------------------------------')
'''

##############################################################################
##############################################################################
