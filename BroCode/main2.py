# *****************************************************************
import time
print()
# Countdown timer

'''time.sleep(3)
print("TIME'S UP!!..\n")'''

# *****************************************************************
'''my_time = int(input('Enter the Time you would like to sleep in seconds :    '))
for x in range(0, my_time):
    print(x)
    time.sleep(1)

print(f'TIME\'S UP!!..\n')'''

# *****************************************************************
'''my_time = int(input('Enter the Time you would like to sleep in seconds :    '))
for x in range(my_time, 0, -1):  # Instead of using reversed function
    print(x)
    time.sleep(1)

print(f'TIME\'S UP!!..\n')'''
# *****************************************************************
# Now a digital clock

'''my_time = int(input('Enter the Time you would like to sleep in seconds :    '))
for x in range(my_time, 0, -1):  # Instead of using reversed function
    seconds = x % 60
    minutes = int(x / 60)
    hours = int(x/ 3600)
    print(f"{hours:02}:{minutes:.02}:{seconds:02}")
    # print(f'00:00:{minutes}')
    time.sleep(1)

print(f'TIME\'S UP!!..\n')'''
# *****************************************************************
# *****************************************************************
# nested 1oop = A loop within another loop (outer, inner)
#   outer 100p:
#       inner 1oop:

# *****************************************************************
'''for x in range(3):
    for y in range(1, 10):
        print(y, end=' ')
    print()

print()'''
# *****************************************************************
#   Project
'''
rows = int(input('Enter the number of rows:   '))
columns = int(input('Enter the number of columns:   '))
symbol = input('Enter a symbol to use:  ')

for x in range(rows):
    for y in range(columns):
        print(symbol, end=' ')
    print()
'''
# *****************************************************************
'''

collection = single "variable" used to store multiple values
List = [] ordered and changeable. Duplicates OK
Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
Tuple = () ordered and unchangeable. Duplicates OK. FASTER



fruits = ['apple', 'orange', 'banana', 'coconut']
print(fruits)
print(fruits[0])
print(fruits[3])
print(fruits[2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print()

print(dir(fruits))
print(help(fruits))

print(len(fruits))

print('apple' in fruits)
print('pineapple' in fruits)
fruits[0] = 'pineapple'

print(fruits)
fruits.append('guava')
print(fruits)
fruits.remove('orange')
print(fruits)
fruits.insert(0, 'pineapple')
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index('banana'))
fruits.clear()
print(fruits)
fruits.count("banana")
print(fruits)

'''

# *****************************************************************
# set
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

'''fruits = {'apple', 'orange', 'banana', 'coconut'}
print(fruits)

fruits.add('pineapple')
fruits.remove('apple')
fruits.pop('coconut')
fruits.clear()'''
# *****************************************************************
# set
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
'''
fruits = ('apple', 'orange', 'banana', 'coconut')
print(fruits)

fruits.count("apple")
fruits.index('apple')
print(fruits)
for fruit in fruits():
    print(fruits)'''

# *****************************************************************
#   Shopping Cart Program

'''foods = []
prices = []
total = 0
while True:
    food = input('\nEnter  a food to buy (q to quit):      ')
    if food.lower() == "q":
        break
    else:
        price = float(input(f'Enter the price of a {food}: $'))
        foods.append(food)
        prices.append(price)

print("\n------- YOUR CART ------\n")
for food in foods:
    print(food, end=' ')

for price in prices:
    total = total + price

print()
print(f'Your Total is: ${total}\n')'''

# *****************************************************************
'''# 2D Lists

#   2d lists is a list made up of lists
fruits = ['appels', 'orange', 'banana', 'coconut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

# 2d list
groceries = [fruits, vegetables, meats]
print()
print(groceries)
print(groceries[0])
print(groceries[2])
print(groceries[0][2])
print(groceries[1][2])
print(groceries[2][2])
print()
# alteranative lists
groceries = [
    ['appels', 'orange', 'banana', 'coconut'],
    ['celery', 'carrots', 'potatoes'],
    ['chicken', 'fish', 'turkey']
]'''
# *****************************************************************
'''
print()
for collection in groceries:
    print(collection)'''
# *****************************************************************
'''
print()
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
print()'''
# *****************************************************************
'''
#   Creating a 2d Keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

print()

# for row in num_pad:
#     print(row)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

print()
'''
# *****************************************************************
#   Python Quiz Game

'''questions = (
    "How many elements are in the Periodic table?:  ",
    "Which animal lays the largest eggs?    ",
    "What is the most abundant gas in the earth's atmosphere?:  ",
    "How many boes are in the Human Body:   ",
    "Which animal in the solar system is the hottest?:"
)

options = (
    ("A. 116", "B. 117", "C. 118", "D. 119"),
    ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
    ("A. Nitrgoen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
)
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print('--------------------------------------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input('Enter (A,  B,  C, D):  ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('correct')
    else:
        print('Incorrect!')
        print(f'{answers[question_num]} is correct answer.\n')
    question_num += 1

print('--------------------------------------------------------')
print(f'                        RESULTS                        ')
print('--------------------------------------------------------')

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")

print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f'Your Score is: {score}%.\n')
'''
# *****************************************************************

# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("Japan"))
if capitals.get("Japan"):  # Russia
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop('China')
capitals.popitem()
capitals.clear()
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
    print(F"{key}: {value}")

# *****************************************************************
# *****************************************************************

# Concession stand program
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

print("---------- MENU ----------")
for key, value in menu.items():
    print(f'{key:10}: {value:.2f}')
print(f'---------------------------')
while True:
    food = input("Select an item (q to quit): "). lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print()
print(f'---------------------------')
print(f'Total is: ${total:.2f}')
print(f'---------------------------\n')
