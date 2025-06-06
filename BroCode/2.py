import example
from math import e
from math import pi
import math as m
import math
import time
import random
# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''
# Bro Code
# Concession Stand to keep track of menu items..like inna movie

menu = {
    'pizza': 3.00,
    'nachos': 4.30,
    'popcorn': 6.00,
    'fries': 2.30,
    'chips': 1.00,
    'pretzel': 3.00,
    'soda': 3.50,
    'lemonade': 4.25
}


cart = []
total = 0
print('=========== MENU ===========')
for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')
print('=================================')

while True:
    food = input('Select an item(q to quit):    ').lower()
    if food == 'q':
        break

    elif menu.get(food) is not None:
        cart.append(food)

# print(cart)
print('\n=========== CART ITEMS  ===========')
for food in cart:
    total += menu.get(food)
    print(f'{food}', end=' ')

print()
print('=================================')
print(f'Total is: ${total:.2f}')
print('=================================\n')
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''
low = 1
high = 100
options = ('rock', 'paper', 'scissors')
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

number = random.randint(low, high)
number = random.random()

option = random.choice(options)

random.shuffle(cards)'''

# -----------------------------------------------
# number guesssing game
'''lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

print(answer)
guesses = 0
is_running = True

print(f'----------------------------------------------')
print(f'Python Number Guessing Game\n')
print(f'Select a number between {lowest_num} and {highest_num}')

while is_running:
    guess = input('Enter your Guess?:   ')
    if guess.isdigit():
        guess = int(guess)

        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f'{guess} is out of range')
            print(
                f'Please select a number btween {lowest_num} & {highest_num}\n')
        elif guess < answer:
            print('Too Low! Try again....!!')
        elif guess > answer:
            print(f'Too high!! Try again...!!')
        else:
            print(f'CORRECT!The answer was: {answer}')
            print(f'Number of Guesses: {guesses}')

    else:
        print(
            f'Inavlid Guess! Please select a number btween {lowest_num} & {highest_num}\n')
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''options = ('rock', 'paper', 'scissors')
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("\nEnter choice(rock, paper, scissors):    ")

    print(f'Player chose: {player}')
    print(f'Computer chose: {computer}..\n')

    if player == computer:
        print('it is a Tie...\n')
    elif player == 'rock' and computer == 'scissors':
        print(f'You win! Computer Looses..\n')
    elif player == 'paper' and computer == 'rock':
        print(f'You win! Computer Looses..\n')
    elif player == 'scissors' and computer == 'paper':
        print(f'You win! Computer Looses..\n')
    else:
        print(f'Computer Wins!...\n')

    # playagain = input('Play again? (y/n):    ').lower()
    # if not playagain.lower() == 'y':
    #     running = False
    if not input('Play again? (y/n):    ').lower() == 'y':
        running = False


print(f'Thanks for playing...\n')'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------

'''# =-----------------------------------------------------------
# =-----------------------------------------------------------
# Rolling dice Game

# print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518')

# ● ┌ ─ ┐ │ └ ┘

# "┌───────────────┐"
# "│               │"
# "│               │"
# "│               │"
# "│               │"
# "└───────────────┘"

dice_art = {
    1: ("┌───────────────┐",
        "│               │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│               │",
        "└───────────────┘"),
    2: ("┌───────────────┐",
        "│   ●           │",
        "│               │",
        "│               │",
        "│               │",
        "│            ●  │",
        "└───────────────┘"),
    3: ("┌───────────────┐",
        "│  ●            │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│             ● │",
        "└───────────────┘"),
    4: ("┌───────────────┐",
        "│  ●         ●  │",
        "│               │",
        "│               │",
        "│               │",
        "│  ●         ●  │",
        "└───────────────┘"),
    5: ("┌───────────────┐",
        "│  ●         ●  │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│   ●        ●  │",
        "└───────────────┘"),
    6: ("┌───────────────┐",
        "│ ●         ●   │",
        "│               │",
        "│ ●         ●   │",
        "│               │",
        "│ ●         ●   │",
        "└───────────────┘"),
}

dice = []

total = 0

num_of_dice = int(input('\nHow many dice?     '))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

# PRINTING DICE VERTICALLY

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# PRINTING DICE HORIZONATTALY

for line in range(7):
    for die in dice:
        print(dice_art.get(die)[line], end='')
    print()

for die in dice:
    total += die
print(f'Total is: {total}')
'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------

# Functions

# print('Happy Birthday!!')
# print('Happy Birthday to you!!')
# print('Happy Birthday!!')

# print('Happy Birthday!!')
# print('Happy Birthday to you!!')
# print('Happy Birthday!!')

# print('Happy Birthday!!')
# print('Happy Birthday to you!!')
# print('Happy Birthday!!')


# def happy_birthday():
#     print('Happy Birthday!!')
#     print('Happy Birthday to you!!')
#     print('Happy Birthday!!')


# print()
# happy_birthday()
# happy_birthday()
# happy_birthday()
# print()
'''
def happy_birthday(name, age):
    print(f'Happy Birthday {name}!!')
    print(f'You are {age} years old...')
    print(f'Happy Birthday to you...{name}!!')
    print()


happy_birthday('Wise', 20)
happy_birthday('Bro Code', 30)
happy_birthday('Joe', 40)

print()


def display_invpice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}\n')


display_invpice('JoeSchmo', 100.01, '21/01/2025')
display_invpice('BVroCode', 40.50, '21/01')

print()

# return functions


def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

print()
'''
# ----------------------------------------------

'''
def create_name(f_name, l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()
    return f'{f_name} {l_name}..\n'


fullname = create_name('wise', 'oketch')
fullname = create_name('spongebob', 'squarepants')
print(fullname)

print()

# ----------------------------------------------


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print()

print(net_price(500, 0.1))
print()
print(net_price(500, 0.1, 0))
print()'''

# ----------------------------------------------

# Count of Timer


'''def count(start, end):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('DONE')


count(0, 10)'''

'''def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('DONE')


count(20, 15)'''

# ----------------------------------------------

# Keyword Arguements

'''
def hello(greeting, title, first, last):
    print(f'{greeting} {title} {first} {last}\n')


hello('Hello', 'Mr', 'spongebob', 'squarepants')
hello('Hello', title='Mr', last='spongebob', first='squarepants')
print()

# End and separate are keyword arguements

for x in range(1, 11):
    print(x, sep='*', end='')

print()
print()'''

# ----------------------------------------------
# Keyword Arguements

'''
def get_phone_number(country, area, first, last):
    return f'{country}--{area}--{first}--{last}\n'


phone_num = get_phone_number(country=1, area=123, last=7890, first=456)
print(phone_num)
'''

# ----------------------------------------------

# Arbitrary Arguments...**args(arguements), ***kwargs(keyword arguemnts)
# positional ,default, keyword, arbitrary

'''
def add(*args):
    total = 0
    print(type(args))  # Tuple
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8))
print()


def add(*nums):  # can change parameter name
    total = 0
    print(type(nums))  # Tuple
    for num in nums:
        total += num
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8))

print()


def display_name(*args):
    for arg in args:
        print(arg, end=' ')
    print()


display_name('Dr', 'Spongebob', 'SquarePants', 'Harlod', 'Squarepants', 'III')
print()


# ----------------------------------------------

# ** kwargs   ....mulitple keyword arguements
print()

print()


def print_address(**kwargs):
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    print()


print_address(street="123 Fake Streer",
              apartment='100',
              city="Detroit",
              state="iMitchigan",
              zip="54321")

# ----------------------------------------------
# Shipping Label Function


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()

    # for value in kwargs.values():
    #     print(value, end=' ')
    # print()
    if 'apt' in kwargs:
        print(f'{kwargs.get('street')} {kwargs.get('apt')}')
    elif 'pobox' in kwargs:
        print(f'{kwargs.get('street')}')
        print(f'{kwargs.get('pobox')}')
    else:
        print(f'{kwargs.get('street')}')
    print(f'{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}')


shipping_label("Dr", 'SpongeBob', 'III',
               street="123 Fake Streer",
               #    apartment='#100',
               pobox='PO BOX #1001',
               city="Detroit",
               state="Mitchigan",
               zip="54321")
print()
'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''# Iterables
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number, end=' ')
print()
print()

numbers = set(numbers)
print(numbers)

fruits = {'apple', 'orange', 'banana', 'coconut'}

print(fruits)
print()

# set object not reversible
# for fruit in reversed(fruits):
#     print(fruits)

print()
print()

# strings
name = 'Wise Code'
for l in name:
    print(l, end=" ")

print()
print()

my_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

for key in my_dict:
    print(key)

print()
print()

for value in my_dict.values():
    print(value)
print()
print()

for key, value in my_dict.items():
    print(f'{key}: {value}')
print()
print()
'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''
# Membership Operator

word = "APPLE"

letter = input('Guess a letter in the secret word:  ')
if letter.upper() in word:
    print(f'There is a {letter}..\n')
else:
    print(f'{letter} was not found!!!')
# Alternative Code
# -------------------------------------------------------------
word = "APPLE"

letter = input('Guess a letter in the secret word:  ')
if letter.upper() not in word:
    print(f'{letter} was not found!!!')
else:
    print(f'There is a {letter}..\n')
# -------------------------------------------------------------
students = ['spongebob', 'Patrick', 'Sandy']

student = input('Enter the name of the student?     ')
if student in students:
    print(f'{student} ias a student..\n')
else:
    print(f'{student} was not found..\n')

students = ['spongebob', 'Patrick', 'Sandy']

# -------------------------------------------------------------

student = input('Enter the name of the student?     ')
if student not in students:
    print(f'{student} was not found..\n')
else:
    print(f'{student} ias a student..\n')
# -------------------------------------------------------------

grades = {'Sandy': 'A',
          'Squidward': "B",
          'Spongebob': "C",
          'Patrick': 'D'
          }
student = input('Enter the name of a student:   ')
if student in grades:
    print(f'{student}\'s grade is: {grades[student]}....\n')
else:
    print(f'{student} was not found...\n')

# -------------------------------------------------------------

email = 'wiseephay87@gamil.com'

if "@" in email and "." in email:
    print(f'{email} is a valid email...\n')
else:
    print('Invalid Email...\n')
'''


# =-----------------------------------------------------------
# =-----------------------------------------------------------
# List Comprehensions
'''
double = []

for x in range(1, 11):
    double.append(x*2)
print(double)
print()

doubles = [x*2 for x in range(1, 11)]

print(double)
print()

triples = [y*3 for y in range(1, 11)]
print(triples)
print()

squares = [z*z for z in range(1, 11)]
print(squares)
print()

fruits = ['apple', 'orange', 'banana', 'coconut']

fruits = [fruit.upper() for fruit in fruits]
print(fruits)
print()


fruizy = [fruit.upper() for fruit in ['apple', 'orange', 'banana', 'coconut']]
print(fruizy)
print()

new_fruits = ['apple', 'orange', 'banana', 'coconut']
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)

print()

numbers = [1, -2, 3, 4, -5, 6, 8, 10, 13, 15, 16, 19]

positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
print()

negative_nums = [num for num in numbers if num < 0]
print(negative_nums)
print()

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
print()

odd_nums = [num for num in numbers if num % 2 == 1]
print(odd_nums)
print()

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
print()
'''


# =-----------------------------------------------------------
# =-----------------------------------------------------------
# Match Case Statements

# def day_of_week(day):
#     if day == 1:
#         return True
#     elif day == 2:
#         return 'It is Monday'
#     elif day == 3:
#         return 'It is Tuesday'
#     elif day == 4:
#         return 'It is Wednesday'
#     elif day == 5:
#         return 'It is Thursday'
#     elif day == 6:
#         return 'It is Friday'
#     elif day == 7:
#         return 'It is Saturday'
#     else:
#         return 'Not a valid day'


# print(day_of_week('Pizza'))
'''def day_of_week(day):
    match day:
        case 1:
            return 'It is Sunday'
        case 2:
            return 'It is Monday'
        case 3:
            return 'It is Tuesday'
        case 4:
            return 'It is Wednesday'
        case 5:
            return 'It is Thursday'
        case 6:
            return 'It is Friday'
        case 7:
            return 'It is Saturday'
        case _:
            return 'Not a valid day'


print(day_of_week(1))

'''

print()


'''def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case 'tuesday':
            return False
        case 'wednesday':
            return False
        case "thursday":
            return False
        case 'friday':
            return False
        case 'saturday':
            return True
        case _:
            return False


print(is_weekend('monday'))

print()'''

'''print()


# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''
'''

def is_weekend(day):
    match day:
        case "sunday" | 'saturday':
            return True
        case "monday" | 'tuesday' | 'wednesday' | "thursday" | 'friday':
            return False
        case _:
            return False


print(is_weekend('minday'))

print()


# modules
print(help("modules"))


print(math.pi)

print(m.pi)


# a, b, c, d, e = 1, 2, 3, 4, 5

# print(e ** a)
# print(e ** b)
# print(e ** c)
# print(e ** d)

print()

# Create a

result = example.pi

result = example.square(3)
print(result)

result = example.cube(3)
print(result)


result = example.circumference(3)
print(result)

result = example.area(7)
print(result)


print(result)

print()

'''
