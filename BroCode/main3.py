
import example
from math import pi
import math as m
import math
import string
import random
import time
from wordlist import words
# ============================================================
# ============================================================

'''print()
name = input('Enter your name:  ')
phone_number = input('Enter your phone #:   ')
result = len(name)
print(result)
result = name.find("o")
print(result)
result = name.rfind('q')
print(result)
result = name.capitalize()
print(result)
result = name.upper()
print(result)
result = name.lower()
print(result)
result = name.isdigit()
print(result)
result = name.isalpha()
print(result)
result = name.isdigit()
print(result)
result = phone_number.count('-')
print(result)
result = phone_number.count('-')
print(result)
result = phone_number.replace('-', ' ')
print(result)

print(help(str))
'''
# ============================================================
# ============================================================

# # validate  user input
'''
username = input('Enter a username:  ')

if len(username) > 12:
    print('Your username cant be more than 12 characters')
elif not username.find(" ") == -1:
    print('Username cant contain  spaces')
elif not username.isalpha():
    print('Your username can contain numbers')
else:
    print(f'Hello {username}')
'''
# ============================================================
# ============================================================
# Indexing
'''
credit_card = '1234-5678-9012-34656'

print(credit_card[0])
print(credit_card[1])
print(credit_card[2])
print(credit_card[4])
print(credit_card[4])

print()
print(credit_card[0:4])
print(credit_card[:4])
print(credit_card[5:9])
print(credit_card[5:])
print(credit_card[-1])
print(credit_card[-2])
print(credit_card[-3])
print(credit_card[-5])

print()
print(credit_card[::2])
print(credit_card[::3])

print()
last_digits = credit_card[-4:]
print(f'XXXX-XXXX-XXXX-{last_digits}')

credit_card = credit_card[::-1]
print(credit_card)
'''
# ============================================================
# ============================================================
# Email slicer
'''
email = input('Enter your email:    ')

index = email.index('@')
username = email[:index]
dormain = email[index:]
print(f'Your username is {username} and dormain is {dormain}')

# alternative
username = email[:email.index('@')]
dormain = email[email.index('@') + 1:]
'''
# ============================================================
# ============================================================
# format specifiers

'''price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f'Price1 is {price1:.2f}')
print(f'Price2 is {price2:.2f}')
print(f'Price3 is {price3:.2f}\n')
print(f'Price1 is {price1:.1f}')
print(f'Price2 is {price2:.1f}')
print(f'Price3 is {price3:.1f}\n')
print(f'Price1 is {price1:.3f}')
print(f'Price2 is {price2:.3f}')
print(f'Price3 is {price3:.3f}\n')
print(f'Price1 is {price1:10}')
print(f'Price2 is {price2:10}')
print(f'Price3 is {price3:10}\n')
print(f'Price1 is {price1:010}')
print(f'Price2 is {price2:010}')
print(f'Price3 is {price3:010}\n')
print(f'Price1 is {price1:<10}')
print(f'Price2 is {price2:<10}')
print(f'Price3 is {price3:<10}\n')
print(f'Price1 is {price1:>10}')
print(f'Price2 is {price2:>10}')
print(f'Price3 is {price3:>10}\n')
print(f'Price1 is {price1:^10}')
print(f'Price2 is {price2:^10}')
print(f'Price3 is {price3:^10}\n')
print(f'Price1 is {price1:+}')
print(f'Price2 is {price2:+}')
print(f'Price3 is {price3:+}\n')
print(f'Price1 is {price1: }')
print(f'Price2 is {price2: }')
print(f'Price3 is {price3: }\n')

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f'Price1 is {price1:,}')
print(f'Price2 is {price2:,}')
print(f'Price3 is {price3:,}\n')

#   Mix and match flags

print(f'Price1 is {price1:+,.2f}')
print(f'Price2 is {price2:+,.2f}')
print(f'Price3 is {price3:+,.2f}\n')
'''
# ============================================================
# ============================================================

'''# while loops

name = input('Enter your name: ')

while name == '':
    print('You did not enter your name')
    name = input('Enter your name:  ')
print(f'Hello {name}')

'''
# ============================================================
# ============================================================

'''age = int(input('Enter your age:    '))
while age < 0:
    print('Age cant be negative')
    age = int(input('Enter your age:    '))

print(f'Your are {age} age years old ')


food = input('Enter a food you like (q to quit): ')

while not food == 'q':
    print(f'You like {food}')
    food = input('Enter another food you like (q to quit):  ')

print('Bye')
'''
# ============================================================
# ============================================================

'''number = int(input('Enter a number between 1- 10:   '))

while number < 1 or number > 10:
    print(f'Your number {number} is not valid')
    number = int(input('Enter a number between 1- 10:   '))

print(f'Your number is {number}')
'''

# ============================================================
# ============================================================

'''principle = 0
rate = 0
time = 0

print()

while principle <= 0:
    principle = float(input('Enter the principle amount:  '))
    if principle <= 0:
        print(f'Principle cant be less than or equal to zero.')
while rate <= 0:
    rate = int(input('Enter the interest rate amount:  '))
    if rate <= 0:
        print(f'Interest rate cant be less than or equal to zero.')
while time <= 0:
    time = int(input('Enter the time in years:  '))
    if time <= 0:
        print(f'Time cant be less than or equal to zero.')

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year\'s : $ {total:.2f}')

'''
# ============================================================
# ============================================================
'''
principle = 0
rate = 0
time = 0

print()

while True:
    principle = float(input('Enter the principle amount:  '))
    if principle < 0:
        print(f'Principle cant be less than zero.')
    else:
        break
while True:
    rate = int(input('Enter the interest rate amount:  '))
    if rate < 0:
        print(f'Interest rate cant be less than zero.')
    else:
        break
while True:
    time = int(input('Enter the time in years:  '))
    if time < 0:
        print(f'Time cant be less than zero.')
    else:
        break

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year\'s : $ {total:.2f}')

'''
# ============================================================
# ============================================================
'''
# for loops

for i in range(11):
    print(i, end=" ")
print()
for i in range(1, 11):
    print(i, end=" ")

print()
for i in reversed(range(1, 11)):
    print(i, end=" ")
print('Happy New Year')
print()
for i in reversed(range(1, 11, 2)):
    print(i)
print('Happy New Year')

print()

credit_card = '1234-5678-9012-4567'
for n in credit_card:
    print(n, end=" ")
print()

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
'''


# ============================================================
# ============================================================
# nested loop ...inner loop, outer loop

'''
print()
for x in range(3):
    for y in range(1, 11):
        print(y, end=" ")

    print()

print()

# rectangle
rows = int(input('Enter # of rows:  '))
columns = int(input('Enter # of columns:    '))
symbol = input('Enter a symbol to use:  ')

for r in range(rows):
    for c in range(columns):
        print(symbol, end=" ")
    print()
print()

'''
# ============================================================
# ============================================================
'''
# coutdown timer in python
import time
time.sleep(3)

my_time =  int(input('Enter time in seconds: '))

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


# ============================================================
# ============================================================

# lists
# collection
'''
fruits = ['orange', 'banana', 'apple', 'coconut']
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])
print()
for fruit in fruits:
    print(fruit)

# print()
# print()

# print(dir(fruits))
# print()
# print(help(fruits))

print()
print()
print(len(fruits))
print('apple' in fruits)
print('pineapple' in fruits)


print()

fruits[0] = 'pineapple'
print(fruits)
fruits.append('pineapple')
fruits.remove('apple')
fruits.insert(0, 'Pinepple')
fruits.sort()
fruits.reverse()
# print(fruits.index('apple'))
print(fruits.count('pineapple'))
fruits.clear()
print(fruits)'''


# ============================================================
'''
# set # unordered and immutable , add and remove ok. No duplicates

fruits = {'orange', 'banana', 'apple', 'coconut'}

print(fruits)

# Tuple ordered and unchangeable, Duplicates Ok. Faster
fruits = ('orange', 'banana', 'apple', 'coconut')
print(fruits)
'''
# ============================================================

# shopping cart program

'''
foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit):  ').lower()
    if food == 'q':
        break
    else:
        price = float(input('Enyer the price of {food}:  $'))
        foods.append(food)
        prices.append(price)

print()
print('-------------- Your Cart -------------')

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print(f'\nYour total is: $ {total}')
print('-------------------------------------')
'''
# ============================================================
# 2d lists
'''
fruits = ['apple', 'orange', 'banana', 'cocomut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

# 2d list
groceries = [fruits, vegetables, meats]

print(fruits)

print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[0][3])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[2][1])

# alternative

groceries = [
    ['apple', 'orange', 'banana', 'cocomut'],
    ['celery', 'carrots', 'potatoes'],
    ['chicken', 'fish', 'turkey']
]
print()
print()

for collection in groceries:
    for food in collection:
        print(food, end='  ')
    print()

print()'''

# ============================================================
# 2d phonepad

'''num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#"),
)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

print()
'''

# ============================================================
# Python Quiz Game

'''questions = ('How many elements are in the periodic table?:     ',
             'Which animal lays the largest eggs?:  ',
             'What is the most abundant gas in the Earth\'s atmosphere?:    ',
             'How manu bones are in the human body?:    ',
             'Which planet in the solar system is the  hottest?:    '
             )
options = (
    ('A. 116', 'B. 117', 'C. 118', 'D. 119'),
    ('A. Whale', 'B. Crocodile', 'C. Elephant', 'D. Ostrich'),
    ('A. Nitrogen', 'B. Oxygen', 'C. Carbon-Dixide', 'D. Hydrogen'),
    ('A. 206', 'B. 207', 'C. 208', 'D. 209'),
    ('A. Mercury', 'B. Venus', 'C. Earth', 'D. Mars'),
)
answers = ('C', 'D', 'A', 'A', 'B')
guesses = []
score = 0
question_num = 0

for i, question in enumerate((questions), start=1):
    print('---------------------------------------------------')
    print(f'{i}.{question}')
    for option in options[question_num]:
        print(option)
    guess = input('Enter (A, B, C, D);  ').upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print('Correct')
    else:
        print(f'Incorrect')
        print(f'{answers[question_num]} is the correct answer')

    question_num += 1

print('---------------------------------------------------')
print('                         RESULTS                   ')
print('---------------------------------------------------')

print('Answers: ', end='')
for answer in answers:
    print(answer, end=" ")
print()

print('Guesses: ', end="")
for guess in guesses:
    print(guess, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score}%')
print('---------------------------------------------------')

'''
# ============================================================
# dictionary

'''capitals = {
    'usa': 'washington dc',
    'india': 'new delhi',
    'china': 'beijing',
    'russia': 'Moscow'
}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get('Japan'))

if capitals.get('Russia'):
    print('That capital Exists')
else:
    print('That capital does not exist')

capitals.update({'germany': 'berlin'})
capitals.update({'usa': 'detroit'})
capitals.pop('china')
# print(capitals.popitem())
# capitals.clear()
print(capitals)


keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)
print()

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)
print()

items = capitals.items()
for key, value in capitals.items():
    print(f'{key}: {value}')
'''

# ============================================================
# cncersion stand  program
'''
menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0.0

print(f'------------------ MENU ------------------')
for key, value in menu.items():
    print(f'{key:10}: ${value:.2f}')

print(f'-----------------------------------------')

while True:
    food = input('Select an item (q to quit): ')
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print()

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f'Total is: ${total:.2f}')
print(f'-----------------------------------------')
'''

# ============================================================

# print(help(random))
# random numbers
'''
import random
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f'Enter a # between ({low}-{high}):   '))
    guesses += 1

    if guess < number:
        print(f'{guess} is too low')
    elif guess > number:
        print(f'{guess} is too high')
    else:
        print(f'{guess} is correct')
        break
print(f'This round took you {guesses} guesses')'''

# ============================================================
'''
import random

lowest_num = 1
highest_num = 1

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print(f'Python Number Guessing Game')
print(f'Select a number between {lowest_num} and {highest_num}')

while is_running:
    guess = input('Enter your guess:    ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print('That number is out of range')
            print(f'Select a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Too low! Try again!')
        elif guess > answer:
            print('Too High! Try again!')
        else:
            print(f'Correct! The answer was {answer}')
            print(f'Number of guesses: {guesses}')
            is_running = False
    else:
        print('Invalid Guess')
        print(f'Select a number between {lowest_num} and {highest_num}')
'''

# ============================================================
'''
options = ('rock', 'paper', 'scissors')


print()

running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ')

    print(f'\nPlayer: {player}')
    print(f'Computer: {computer}\n')

    if player == computer:
        print('It is a tie')
    elif player == 'rock' and computer == 'scissors':
        print('You Win')
    elif player == 'paper' and computer == 'rock':
        print('You Win')
    elif player == 'scissors' and computer == 'paper':
        print('You Win')
    else:
        print('You Loose')

    print()

    play_again = input('Play again? (y/n): ').lower()
    if not play_again == 'y':
        running = False

    # if not input('Play again? (y/n): ').lower() == 'y':
    #     running = False

print('Thanks for playing')

'''
# ============================================================
# dice roller program
'''
'''

# print((" \u25CF \u250C  \u2500 \u2510 \u2502 \u2514 \u2518   "))

# ● ┌  ─ ┐ │ └ ┘

' ┌─────────┐ '
' │         │ '
' │         │ '
' │         │ '
' │         │ '
' └─────────┘ '
'''

dice_art = {
    1: (' ┌─────────┐ ',
        ' │         │ ',
        ' │    ●    │ ',
        ' │         │ ',
        ' └─────────┘ '),

    2: (' ┌─────────┐ ',
        ' │ ●       │ ',
        ' │         │ ',
        ' │       ● │ ',
        ' └─────────┘ '),

    3: (' ┌─────────┐ ',
        ' │ ●       │ ',
        ' │    ●    │ ',
        ' │       ● │ ',
        ' └─────────┘ '),

    4: (' ┌─────────┐ ',
        ' │ ●     ● │ ',
        ' │         │ ',
        ' │ ●     ● │ ',
        ' └─────────┘ '),

    5: (' ┌─────────┐ ',
        ' │ ●     ● │ ',
        ' │    ●    │ ',
        ' │ ●     ● │ ',
        ' └─────────┘ '),

    6: (' ┌─────────┐ ',
        ' │ ●     ● │ ',
        ' │ ●     ● │ ',
        ' │ ●     ● │ ',
        ' └─────────┘ '),

}

dice = []

total = 0

num_of_dice = int(input('How many dice?:    '))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end='')
    print()


for die in dice:
    total += die
print(f'total: {total}')
'''

# ============================================================
# encryption and decryption program
'''

chars = " " + string.punctuation + string.digits + string.ascii_letters

print(chars)

chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f'Chars: {chars}')
print(f"Key: {key}")


# Encrypt

plain_text = input('Enter a message to encrypt:   ')
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'Original Message:  {plain_text}')
print(f'Encrypted message:  {cipher_text}')

# Decrypt

cipher_text = input('Enter a message to encrypt:   ')
plain_text = ""

for letter in cipher_text:
    index = chars.index(letter)
    plain_text += key[index]

print(f'Encrypted message:  {cipher_text}')
print(f'Original Message:  {plain_text}')

'''
# ============================================================

# functions
'''
print('Happy Birthday to you')
print('How old are you now? ')
print('Happy Birthday to you')


def happy_birthday(name, age):
    print()
    print(f'Happy Birthday to {name}')
    print(f"You are {age} years old")
    print('Happy Birthday to you')
    print()


happy_birthday("Bro", 20)
happy_birthday('Steve', 30)
happy_birthday('Joe', 40)


def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')
    print()


display_invoice("Wise", 42.50, '01/01')
display_invoice("Joeschmo", 100.50, '04/01')

# return


def add(x, y):
    z = x + y
    return z


def sub(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(2, 3))
print(multiply(2, 3))
print(sub(2, 3))
print(divide(2, 3))

print()


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f'{first} {last}\n'


full_name = create_name('Spongebob', 'squarepants')
print(full_name)

# default arguements


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1 + tax)


print(net_price(500))
print(net_price(500, 0.05))

# default arguements

print()


# def count(end, start):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print('Done')


# count(30, 15)

# print()


# keword arguements

def hello(greeting, title, f_name, l_name):
    print((f"{greeting} {title} {f_name} {l_name}"))


hello('Hello', 'Mr.', 'spongebob', 'squarepants')
hello('Hello', 'Mr.', 'John', 'James')

for x in range(1, 11):
    print(x, end=" ") # end is keyword arguement.....

print()

print('1', '2', '3', '4', '5', sep="-") # sep is a keyword arguement

print()
print()


def get_phone(country, area, first, last):
    return f'{country}  {area} - {first} - {last}'


phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
print()

'''

# ============================================================
'''
# *args **kwags
# args


def add_numbers(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add_numbers(1, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")


display_name('Dr.', 'Spongebob', 'Harlod', 'Sqauurepants', 'III')


def print_address(**kwags):
    print(type(kwags))  # dictionary
    for key, value in kwags.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.",
              apt="100",
              city='Detroit',
              state='MI',
              zip='54321'
              )'''

# ============================================================
'''
# keyword arguments follow positional arguements
print()
print()

print(f'=======================================================')
print(f'Shipping Label')
print(f'=======================================================')


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')} ")


shipping_label("Dr", 'Spongebob', 'Sqauurepants', 'III',
               street="123 Fake St.",
               pobox="#100",
               city='Detroit',
               state='MI',
               zip='54321'
               )
'''
# ============================================================
'''
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print()


for number in reversed(numbers):
    print(number, end="-")

print()
# tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# set
fruits = {'apple', 'orange', 'banana', 'coconut'}

for fruit in fruits:
    print(fruit, end=" ")
# dictionary

my_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

for key in my_dict.keys():
    print(key)
print()
for value in my_dict.values():
    print(value)
print()
for key, value in my_dict.items():
    print(f"{key}: {value}")
print()
'''


# ============================================================
# membership operators
'''
word = 'apple'

letter = input('Guess a letter in the secret word:  ')

if letter in word:
    print(f'There is a letter {letter}')
else:
    print(f'{letter} was not found.')

# alternative code

if letter not in word:
    print(f'{letter} was not found.')
else:
    print(f'There is a letter {letter}')


# set
students = {'spongebob', 'patrick', 'sandy'}

student = input('Search the name of a student:  ')
if student not in students:
    print(f'{student} was not found.')
else:
    print(f'There is a student {student}')


# dictionaries
grades = {"Sandy": "A",
          "Squirward": "B",
          "Spongebob": "C",
          "Patrick": "D"
          }
student = input('Search the name of a student:  ')

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f'{student} was not found')

email= 'Brocode@gmail.com'

if "@" in email and "." in email:
    print('Valid Email')
else:
    print('Invalid Email')
    
'''

# ============================================================
'''
# List comprehensions

# expression for value in iterable if condition
print()

doubles = []
for x in range(1, 11):
    doubles.append(x*2)

print(doubles)

print()

doubles = [x*2 for x in range(1, 11)]
print(doubles)
print()

triples = [y * 3 for y in range(1, 11)]
print(triples)

squares = [pow(n, 2) for n in range(1, 11)]
print(squares)

fruits = ['apples', 'oranges', 'guavas', 'pineapples', 'mangoes']

fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers)
negative_numbers = [n for n in numbers if n < 0]
print(negative_numbers)

odd_nums = [n for n in numbers if n % 2 == 1]
print(odd_nums)


grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)

# compact and easier to read
'''
# ============================================================
# match case statements

'''
def day_of_week(day):
    if day == 1:
        return 'It is Monday'
    elif day == 2:
        return 'It is Tuesday'
    elif day == 3:
        return 'It is Wednesday'
    elif day == 4:
        return 'It is Thursday'
    elif day == 5:
        return 'It is Friday'
    elif day == 7:
        return 'It is Saturday'
    else:
        return 'Not a valid day'


print(day_of_week(7))

print()


def day_of_week(day):
    match day:
        case 1:
            return 'It is Monday'
        case 2:
            return 'It is Tuesday'
        case 3:
            return 'It is Wednesday'
        case 4:
            return 'It is Thursday'
        case 5:
            return 'It is Friday'
        case 7:
            return 'It is Saturday'
        case _:
            return 'Not a valid day'


print(day_of_week(7))

print()


def is_weekend(day):
    match day:
        case "Saturday" | 'Sunday':
            return True
        case "Monday" | 'Tuesday' | 'Wednseday' | 'Thursday' | 'Friday':
            return False
        case _:
            return False


print(is_weekend('Friday'))

'''
# ============================================================
# modules  from import example(example.py)
'''
result = example.pi
print(result)

result = example.square(3)
print(result)

result = example.cube(3)
print(result)

result = example.circumference(3)
print(result)

result = example.area(3)
print(result)'''

# ============================================================

# variable scope
# legb local , enclosed, global, built-in


# ============================================================

'''def main():
    pass


if __name__ == "__main__":
    main()
'''
# ============================================================
'''# python credit card validator program

# python scredit_card_number

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step 1
card_number = input('Enter a credit card #:  ')
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# step 2

for x in card_number[::2]:
    sum_odd_digits += int(x)

# step 3
for x in card_number[1::2]:
    x = int(x)**2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x
# step 4
total = sum_odd_digits + sum_even_digits

# step5
if total % 10 == 0:
    print('Valid')
else:
    print('Invalid')


print(card_number)

'''
# ============================================================
#   Pthon Banking Program

'''
def show_balance(balance):
    print('--------------------------')
    print(f'Your balance is ${balance:.2f}')


def deposit():
    amount = float(input('Enter amount to be deposited: $'))

    if amount < 0:
        print('--------------------------')
        print('That is not a valid amount')
        print('--------------------------')
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input('Enter amount to be withdrawn: $'))

    if amount > balance:
        print('--------------------------')
        print('Insufficient funds!')
        print('--------------------------')
        return 0
    elif amount < 0:
        print('--------------------------')
        print('Amount must be greater than 0')
        print('--------------------------')
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True
    while is_running:
        print()
        print('--------------------------')
        print('Banking Program')
        print('1. Show Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        print('--------------------------')

        choice = input('\nEnter your choice(1-4): ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('\nThat is not a valid choice!')

    print('\nThank You! Have a nice day!!\n')


if __name__ == "__main__":
    main()
'''
# ============================================================
'''
#   Python Slot Machine Program


def spin_row():
    symbols = ['🍇', '🍉', '🥭', '🔔', '⭐']

    results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results

    # return [random.choice(symbols) for _ in range(3)]

    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print('***************')
    print(" | ".join(row))
    print('***************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍇':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🥭':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100
    print()
    print('************************')
    print('Welcome to Python Slots ')
    print('Symbols:   🍇🍉🥭🔔⭐')
    print('************************')

    while balance > 0:
        print(f'Current balance: ${balance:.2f}')

        bet = input('Place your bet amount:  ')

        if not bet.isdigit():
            print('Please enter a valid number')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient Funds')
            continue

        if bet <= 0:
            print('Bet must be greater than 0')
            continue

        balance -= bet

        row = spin_row()

        # print(row)         print(row)

        print('Spining...\n')

        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f'You won ${payout:.2f}')
        else:
            print('Sorry you Lost this round!....')

        balance += payout
        play_again = input('Do you want to spin again? (Y/N): ')

        if play_again != 'Y':
            break

    print(f'Game Over!... Your final balance is ${balance:.2f}\n')


if __name__ == "__main__":
    main()
'''
# ============================================================
# Hangman in python


words = ('apple', 'orange', 'banana', 'cocont', 'pineapple')

# dictionary of key
hangman_art = {
    0: ("       ",
        "       ",
        "       "),
    1: ("   O   "
        "       ",
        "       ",),
    2: ("   O    ",
        "   |    ",
        "       ",),
    3: ("   O    ",
        "  /|    ",
        "       ",),
    4: ("   O    ",
        "  /|\\   ",
        "       ",),
    5: ("   O    ",
        "  /|\\   ",
        "  /     ",),
    6: ("   O    ",
        "  /|\\   ",
        "  / \\    ",),
}

# for line in hangman_art[5]:
#     print(line)


def display_man(wrong_guesses):
    print("\n*********************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*********************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    # print(answer)
    hint = ["_"] * len(answer)
    # print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input('Enter a letter:   ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid Input')
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guesses ')
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You Win')
            is_running = False
        elif wrong_guesses > len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print('You Loose')
            is_running = False


if __name__ == "__main__":
    main()
