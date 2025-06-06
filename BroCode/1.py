import random
import time
import math
print()


'''

# Python program
print('I like Pizza..\n')
# Variables... strings integers, booleans

# These are strings
first_name = 'Wise'
print(first_name, " \n")
print(f'Hello {first_name}\n')
food = 'chips'
print(f'You like {food}\n')
email = 'Wise123@fale.com'
print(f'Your email is: {email}\n')

# Integers
age = 25
print(f'You are {age} years old.\n')
quantity = 3
print(f'You are buying {quantity} items\n')
num_of_students = 30
print(f'Your class has {num_of_students} students\n')

# Float
price = 10.99
gpa = 3.2
dist = 5.5

print(f'The price is: ${price}\n')
print(f'Your gpa is: {gpa}\n')
print(f'You ran {dist}km\n')

# Boolean True or False

is_student = True
for_sale = True
is_online = True
is_admin = True

if is_student:
    print(f'Are you a student? {is_student}\n')
else:
    print(f'You are NOT a student..\n')

if for_sale:
    print('That item is for sale..\n')
else:
    print('That item is NOT for sale...\n')

if is_online:
    print('You are ONLINE...\n')
else:
    print('You are NOT ONLUINE...\n')

# Type casting
casting = 24
gpa = 3.2
is_student = True

gpa = int(gpa)
print(gpa, ' \n')

age = float(age)
print(age, ' \n')

age = str(age)
print(age, '\n')
print(type(age), " \n")

name = ''
name = bool(name)
print(name, ' \n')
print(type(name), ' \n')

# Input()

name = input('What is your name?   ')
print(f'Hello {name}..\n')
age = int(input('How old are you?   '))
# age = int(age)
age = age + 1

print(f'HAPPY BIRTHDAY!!!{name}')
print(f'You are {age} years old..\n')

length = float(input('Enter the length:   '))
width = float(input('Enter the width:   '))
area = length * width
print(f'Area of Rectangle is: {area} cm^2..\n')

# Shopping cart Program
item = input('What item would you like to buy:  ')
price = float(input('What is the Price:     '))
quantity = int(input('How many would you like to buy?'))
total = price * quantity

print(f'-----------------------------------------')
print(f'You have bought: {quantity} x {item}')
print(f'Your Total is: Ksh{total}')
print(f'-----------------------------------------')

# Madlibs Game

# Words where you create a story by filling in blanks by random words
adj1 = input('Enter an adjective..description:      ')
noun1 = input('Enter a noun (person, place or thing):       ')
adj2 = input('Enter an adjective..description:  ')
verb1 = input('Enter a verb endng with \'ing\':     ')
adj3 = input('Enter an adjective..description:      ')


print(f'\nToday I went to {adj1} zoo.')
print(f'In an exhibit, I saw a {noun1}.')
print(f'{noun1} was {adj1} and {verb1}.')
print(f'I was {adj3}!...\n')

'''
'''
# Arithemetic Operators
friends = 10
# friends = friends + 1
friends += 1
# friends = friends -2
friends -= 2
# friends = friends * 3
friends *= 3
# friends = friends / 2
friends /= 2
# friends = friends ** 2
friends **= 2
# remainder = friends % 3


print(friends, " \n")

x = 3.14
y = 4
z = 5
max = max(x, y, z)
print(f'The maximum is: {max} \n')


print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
x = 9.9
result = math.floor(x)

print(result, ' \n')

print()
'''

'''# area, circumference of a right angle triangle

radius = input('Enter the radius of a circle:   ')
circumference = 2 * math.pi * radius
print(f'The circumeference is: {round(circumference, 2)}cm^2')

radius = float(input('Enter the radius of a circle:   '))
area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)}cm^2')

a = float(input('Enter side A:    '))
b = float(input('Enter side B:    '))

c = math.sqrt(pow(a*2) + pow(b, 2))

print(f'Side C = {c}cm \n')

# =-----------------------------------------------------------
# =-----------------------------------------------------------

# if statements
age = int(input('Enter your age:    '))
if age >= 100:
    print('You are TOO OLD to be signed up!...\n')
elif age >= 18:
    print(f'You are now signed up...\n')
elif age < 0:
    print(f'You haven\'t been born yet..\n')
else:
    print(f'You MUST be 18+ to sign up..\n')

# =-----------------------------------------------------------

response = input('Would you like food(y/n):     ').lower()
if response == 'y':
    print('Have some food..\n')
else:
    print('No food for you...\n')

# =-----------------------------------------------------------

name = input('Enter your name:      ')
if name == '':
    print('You did not type in your name...\n')
else:
    print(f'Hello, {name}..\n')

# =-----------------------------------------------------------

for_sale = True
if for_sale:
    print('This item is for sale...\n')
else:
    print('This item is not available...\n')

# =-----------------------------------------------------------

online = True
if online:
    print('User is Online...\n')
else:
    print('User is Offline...\n')


# =-----------------------------------------------------------
operator = input('Enter an operator (+ - * /):  ')
num1 = int(input('Enter first number:    '))
num2 = int(input('Enter second number:    '))

if operator == "+":
    result = num1 + num2
    print(result, ' \n')
elif operator == "-":
    result = num1 - num2
    print(result, ' \n')
elif operator == "*":
    result = num1 * num2
    print(result, ' \n')
elif operator == "/":
    result = num1 / num2
    print(f'{round(result, 2)} \n')
else:
    print(f'{operator} is not a valid operator...\n')

# =-----------------------------------------------------------
# =-----------------------------------------------------------

# Python Weight converter

weight = float(input('Enter your weight:    '))
unit = input('Kilograms or Pounds? (K or L):    ')

if unit == 'K':
    weight = weight * 2.205
    unit = 'Kgs'
    print(f'Your new Weight is:{round(weight, 3)} {unit} \n ')
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Lbs'
    print(f'Your new Weight is:{round(weight, 3)} {unit} \n ')
else:
    print(f'{unit} is not valid..\n')



# =-----------------------------------------------------------

temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print('It is HOT outside🥵')
    print('It is SUNNY☀️')
elif temp <= 0 and is_sunny:
    print('It is COLD outside🥶')
    print('It is SUNNY☀️')
elif 28 > temp > 0 and is_sunny:
    print('It is WARM outside🌞')
    print('It is SUNNYs☀️')
elif temp >= 28 and not is_sunny:
    print('It is HOT outside🥵')
    print('It is Cloudy⛅')
elif temp <= 0 and not is_sunny:
    print('It is COLD Outside🥶❄️')
    print('It is CLOUDY🌥️🌥️')
elif 28 > temp > 0 and not is_sunny:
    print('It is WARM outside🌞')
    print('It is CLOUDY⛅')

print()

# =-----------------------------------------------------------
# =-----------------------------------------------------------
# Conditional expression /tenary operator

# return x if conditon is true
num = 5
print('POSITIVE' if num > 0 else "NEGATIVE")

a = 6
b = 7
age = 13
temperature = 20
user_role = 'admin'

result = 'EVEN' if num % 2 == 0 else 'ODD'
max_num = a if a > b else b
min_num = a if a < b else b

status = 'adult' if age >= 18 else "child"
weather = 'hot' if temperature > 20 else "COLD"
acess_level = 'Full Access' if user_role == 'admin' else 'Limited Access'
print(acess_level)


# =-----------------------------------------------------------
# =-----------------------------------------------------------

name = input('Enter your full name:     ')
result = len(name)
result = name.find(' ')
result = name.find('o')
result = name.find('e')
result = name.rfind('q')

name = name.capitalize()
name = name.lower()
print(name, ' \n')
name = name.upper()
print(name, ' \n')

result = name.isdigit()
result = name.isalpha()


print(name)
print(result)

phone_number = input('Enter your phone number:      ')
total = phone_number.count('-')
phone_number = phone_number.replace("-", ' ')

print(total, ' \n')
print(phone_number)

print()

# =-----------------------------------------------------------
# =-----------------------------------------------------------
# Validate user input exercise
# 1. Username is no more tham 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

user_name = input('Enter a username:    ')

if len(user_name) > 12:
    print('Your username can not be more than 12 characters..\n')
elif not user_name.find(' ') == -1:
    print(f'Your username cannot contain spaces...\n')
elif not user_name.isalpha():
    print(f'Your username cannot contain numbers...\n')
else:
    print(f'Welcome {user_name}')

'''

'''# =-----------------------------------------------------------
# =-----------------------------------------------------------

# String iNdexing:

print()
print(f'=======================================')
credit_card_number = '1234-5678-9012-3456'
print(credit_card_number[1])
print(credit_card_number[0])
print(credit_card_number[4])
print(credit_card_number[0:4])

print()

print(credit_card_number[:4])
print(credit_card_number[5:])
print(credit_card_number[5:9])

print()

print(credit_card_number[5:])
print(credit_card_number[-1])
print(credit_card_number[::2])
print(credit_card_number[::3])

# Program to get the last 4 digits of a credit card number....
# =-----------------------------------------------------------
# =-----------------------------------------------------------

credit_card_number = '1234-5678-9012-3456'
last_digits = credit_card_number[-4:]
print(f'XXXX-XXXX-XXXX-{last_digits}')

# Reverse the chacracters ina string
# =-----------------------------------------------------------
# =-----------------------------------------------------------

credit_card_number = credit_card_number[::-1]
print(f'Credit Crad number backwards: {credit_card_number}')

# Format specifiers
# =-----------------------------------------------------------
# =-----------------------------------------------------------
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f'The price1 is: ${price1:2f}')
print(f'The price2 is: ${price2:2f}')
print(f'The price3 is: ${price3:2f}\n')

print(f'The price1 is: ${price1:3f}')
print(f'The price2 is: ${price2:3f}')
print(f'The price3 is: ${price3:3f}\n')

print(f'The price1 is: ${price1:10}')
print(f'The price2 is: ${price2:10}')
print(f'The price3 is: ${price3:10}\n')

print(f'The price1 is: ${price1:010}')
print(f'The price2 is: ${price2:010}')
print(f'The price3 is: ${price3:010}\n')

print(f'The price1 is: ${price1:>10}')
print(f'The price2 is: ${price2:>10}')
print(f'The price3 is: ${price3:>10}\n')

print(f'The price1 is: ${price1:<10}')
print(f'The price2 is: ${price2:<10}')
print(f'The price3 is: ${price3:<10}\n')

print(f'The price1 is: ${price1:^10}')
print(f'The price2 is: ${price2:^10}')
print(f'The price3 is: ${price3:^10}\n')

price1 = 3000.14159
price2 = -9870.6500
price3 = 1234.3400

print(f'The price1 is: ${price1:,}')
print(f'The price2 is: ${price2:,}')
print(f'The price3 is: ${price3:,}\n')

print(f'The price1 is: ${price1: }')
print(f'The price2 is: ${price2: }')
print(f'The price3 is: ${price3: }\n')

print(f'The price1 is: ${price1:+,.2f}')
print(f'The price2 is: ${price2:+,.2f}')
print(f'The price3 is: ${price3:+,.2f}\n')

'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
# While Loop
'''
name = input('Enter your name:      ')
while name == '':
    if name == "":
        print(f'You did not enter your name')
        name = input('Enter your name:      ')
print(f'Hello {name}')
'''

# =-----------------------------------------------------------
'''
age = int(input('enter your age:    '))

while age < 0:
    print(f'Age can not be NEGATIVE!!....\n')
    age = int(input('enter your age:    '))
print(f'You are {age} years old..\n')
'''

# =-----------------------------------------------------------
'''
food = input('Enter the food you like(q to quit):   ')

while not food == 'q':
    print(f'You like {food}..\n')
    food = input('Enter the food you like(q to quit):   ')
print('Bye...\n')
'''
# =-----------------------------------------------------------

'''
num = input('Enter a num btween 1 and 10:   ')
num = int(num)
while num < 1 or num > 10:
    print(f'{num} is not valid..\n')
    num = input('Enter a num btween 1 and 10:   ')

print(f'Your number is {num}...\n')

'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------

# # Python Compund Interest Calculator
# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input('Enter the principle amount:    '))
#     if principle <= 0:
#         print(f"Principle cannot be less than or equal to zero...\n")
# while rate <= 0:
#     rate = float(input('Enter the Interest rate:    '))
#     if rate <= 0:
#         print(f"Rate cannot be less than or equal to zero...\n")
# while time <= 0:
#     time = float(input('Enter the Time in years:    '))
#     if time <= 0:
#         print(f"Time cannot be less than or equal to zero...\n")

# print()
# print(principle)
# print(rate)
# print(time)
# print()

# total = principle * pow((1 + rate/100), time)
# print(f'Balance after {time} year\'s: ${total:.2f}\n')

# Python Compund Interest Calculator
# principle = 0
# rate = 0
# time = 0
# =-----------------------------------------------------------
# =-----------------------------------------------------------

'''principle = 0
rate = 0
time = 0
while True:
    principle = float(input('Enter the principle amount:    '))
    if principle < 0:
        print(f"Principle cannot be less than  zero...\n")
    else:
        break
while True:
    rate = float(input('Enter the Interest rate:    '))
    if rate < 0:
        print(f"Rate cannot be less than zero...\n")
    else:
        break
while True:
    time = float(input('Enter the Time in years:    '))
    if time < 0:
        print(f"Time cannot be less than zero...\n")
    else:
        break

print()
print(principle)
print(rate)
print(time)
print()

total = principle * pow((1 + rate/100), time)
print(f'Balance after {time} year\'s: ${total:.2f}\n')

'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
# For loop
'''
for x in range(1, 10):
    print(x)

print('Happy New Year!!')

# =-----------------------------------------------------------


for x in reversed(range(1, 11, 2)):
    print(x)
print('All Done!!')

print()

credit_card = '1234-5678-9012-3456'
for n in credit_card:
    print(n)

print()
for x in range(10, 21):
    if x == 15:
        continue
    else:
        print(x)

print()
for x in range(10, 21):
    if x == 15:
        break
    else:
        print(x)
'''
# =-----------------------------------------------------------
# Countdown timer in Python
print()
# time.sleep(3)
# print('Tine\'s Up!!')

# my_time = input('Enter time in seconds:     ')

# print()
# my_time = int(my_time)

# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
# print(f'Times Up!...\n')

# =-----------------------------------------------------------
# =-----------------------------------------------------------

'''# display a digital clock
my_time = int(input('Enter time in seconds:     '))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)
print(f'TIMES UP!')'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
#      Nested Loops
'''
for x in range(1, 10):
    print(x, end=' ')

print()
print()
'''
# =-----------------------------------------------------------

'''for x in range(3):
    for x in range(1, 10):
        print(x, end='')
    print()

print()
print()'''

# =-----------------------------------------------------------
# print a ractanngle of a user input
'''
rows = int(input('Enter nuumber of rows:    '))
cols = int(input('Enter number of columns:  '))
symbol = input('Enter a symbol to use:    ')
print()
for x in range(rows):
    for y in range(cols):
        print(symbol, end='')
    print()
print()
print()
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------
# colletion List [], Tuple (), Set {}, Dict
#   List = [] ordered and changeable
#   Set = {} unordered and immutable, but add and remove ok...No dulicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
'''
fruit = ['apple']
print(fruit)

fruits = ['apple', 'coconut', 'banana', 'orange']
print(fruits)
print(fruits[3])
print(fruits[2])
print(fruits[0:3])
print(fruits[::])
print(fruits[::2])
print(fruits[::-1])

print()
for fruit in fruits:
    print(fruit)

print()

# print(help(fruits))
# print(dir(fruits))
print(len(fruits))

print('pineapple' in fruits)
print()

fruits[2] = 'mangoes'
print(fruits)
print()
# List methods

fruits.append('pineapple')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.insert(0, 'pineapple')
print(fruits)

print()
fruits.sort()
print(f'Sorted fruits: \n{fruits}')

print()
fruits.reverse()
print(f'Reversed fruits: \n{fruits}')

print(fruits.index('pineapple'))
print(fruits.count('banana'))

for fruit in fruits():
    print(fruits)
print()

print(fruits.add('guava'))
print(fruits.remove('guava'))
fruits.pop()
popped_fruit = popped(fruits)
'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''#   set
fruits = {'apple', 'coconut', 'banana', 'orange'}

#   tuple

fruits = ('apple', 'coconut', 'banana', 'orange')'''


# =-----------------------------------------------------------
# =-----------------------------------------------------------
# Shoppping Cart Program
'''
foods = []
prices = []
total = 0

while True:
    food = input('Enter a food to buy (q to quit):  ')
    if food.lower() == 'q':
        break
    else:
        price = input(f'Enter the price of a ${food}:    ')
        price = float(price)
        foods.append(food)
        prices.append(price)

print(f'\n-------------YOUR CART-------------------\n')
for food in foods:
    print(food, end=' ')
for price in prices:
    total += price

print('\n------------------------------------')
print(f'Your Total is: ${total:.2f}')
print('------------------------------------')
'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
# 2D lists
'''
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

groceries = [fruits, vegetables, meats]

groceries = [
    ['apple', 'banana', 'cherry', 'date', 'elderberry'],
    ['celery', 'carrots', 'potatoes'],
    ['chicken', 'fish', 'turkey']]

print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])

print()

print(groceries[1][0])
print(groceries[1][2])
print(groceries[1][2])

print()
print(groceries[2][1])
print(groceries[2][2])
print(groceries[2][0])


print()

# Looping
print(f'\nLooping\n')

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()

print(f'\nLooping Set\n')

groceries = (
    ('apple', 'banana', 'cherry', 'date', 'elderberry'),
    ('celery', 'carrots', 'potatoes'),
    ('chicken', 'fish', 'turkey'))

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()

print(f'\n Tuple made of sets')

groceries = (
    {'apple', 'banana', 'cherry', 'date', 'elderberry'},
    {'celery', 'carrots', 'potatoes'},
    {'chicken', 'fish', 'turkey'})

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''# Creating a Numpad

# 2D Tuple
num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9,),
    ('*', 0, "#")
)

for row in num_pad:
    for num in row:
        print(num, end=' ')
    print()

print()'''

# =-----------------------------------------------------------
# =-----------------------------------------------------------
'''
# Python Quiz Game

questions = ('How many elements are in the periodic table?:',
             'Which animal lays the largest eggs?',
             'What is the most abundant gas in earth\'s atmosphere?',
             'How many bones are in the human body?',
             'Which planet in the Solar system is the largest?',)

options = (('A. 116', 'B. 117', 'C. 118', 'D. 119'),
           ('A. Whale', 'B. Crocodile', 'C. Elephant', 'D. Ostrich'),
           ('A. Nitrogen', 'B. Oxygen', 'C. Carbon-dioxide', 'D. Hydrogen'),
           ('A. 206', 'B. 207', 'C. 208', 'D. 209'),
           ('A. Mercury', 'B. Venus', 'C. Earth', 'D. Mars'))

answers = ('C', 'D', 'A', 'A', 'B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('------------------------------------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A,B,C,D):     ').upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print('\nCORRECT')
    else:
        print(f'\nINCORRECT')
        print(f'{answers[question_num]} is the CORRECT answer...\n')

    question_num += 1

print(f'------------------------------------')
print(f'            RESULTS                 ')
print(f'------------------------------------\n')

print('Answers: ', end="")
for answer in answers:
    print(answer, end=' ')

print()

print('Guesses: ', end='')
for guess in guesses:
    print(guess, end=' ')
print()

score = score / len(questions) * 100
print(f'Your score is: {score}%')
print(f'------------------------------------')

'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------

# dictionaries
'''
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow',
            }

# print(dir(capitals))

# print(help(capitals))

print(capitals.get('India'))
# check if key is in our dictionary
if capitals.get('Russia'):
    print(f'The capital exsists..\n')
else:
    print('That capital does not exist!..\n')

capitals.update({'Germany': 'Berlin'})
print(capitals)

capitals.update({'USA': 'Detroit'})
capitals.pop('China')
capitals.popitem()
# capitals.clear()

print(capitals)

keys = capitals.keys()
print(keys)
print()

for key in capitals.keys():
    print(key)

print()

values = capitals.values()
for value in capitals.values():
    print(value)

print()

items = capitals.items()
for key, value in capitals.items():
    print(f'{key}: {value}')
print()
'''

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
# for loops working well
'''
foods = []
prices = []
total = 0
while True:
    try:

        food = input('Enter food name:  ').lower()
        if food == 'q':
            break
        elif food.isalpha():
            foods.append(food)
            price = float(input(f'Enter the price of {food}: $ '))
            prices.append(price)
    except ValueError:
        print(f'{food} is not a food..')
        continue

print(f'------------ Your Food Items ------------')
for food in foods:
    print(food)
print()
for price in prices:
    print(price)
print()
print(f'------------------ Total --------------------')
for price in prices:
    total += price
print(f'Total Bill is: ${total:.2f}')
print(f'---------------------------------------------')
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------
# for loops working well
'''
food_price = {}
total = 0
while True:
    try:

        food = input('Enter food name(q to quit):  ').lower()
        if food == 'q':
            break
        elif food.isalpha():
            price = float(input(f'Enter the price of {food}: $ '))
            food_price[food] = price
    except ValueError:
        print(f'{food} is not a food..')
        continue

print(f'------------ Your Food Items ------------')
# for food in food_price.keys():
#     print(food, end=' ')
# print()
# for price in food_price.values():
#     print(price, end=' ')
# print()
for i, (food, price) in enumerate(food_price.items(), start=1):
    print(f'{i}. {food:10} {price:.2f}')
print(f'------------------ Total --------------------')
for price in food_price.values():
    total += price
print(f'Total Bill: ${total:,.2f}')
print(f'---------------------------------------------')
'''
# =-----------------------------------------------------------
# =-----------------------------------------------------------

menu = {
    'nachos': 14,
    'pretzel': 30,
    'pizza': 20,
    'chips': 14,
    'maize': 18,
    'soda': 35
}
cart = {}
print(f'------------CONCERSION STAND----------------')
for i, (key, value) in enumerate(menu.items(), start=1):
    print(f'{i}. {key:10}: {value:.2f}')

print()

while True:
    item = input('Choose your item (q to quit) ')

    if item == 'q':
        break

    if None in menu:
        if item in menu:
            if item in cart:
                cart[item] += 1
            else:
                cart[item] = 1
        else:
            print(f"'{item}' is not on the menu. Please choose a valid item.")

print(f'---------------YOUR MENU----------------')

for key, value in cart.items():
    print(f'{key}: {value}')
print()
