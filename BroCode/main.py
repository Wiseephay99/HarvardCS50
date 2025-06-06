print()
############################################################
'''
# Excercise 2 Shoppping Cart Program

item = input('What item would you liketo buy?: ')
price = float(input('What is the price?: '))
quantity = int(input('How many would you like?: '))
total = price * quantity

print(f'\nYou have bought {quantity} X {item}/s')
print(f'Your total is: ${total}\n')'''

############################################################
'''
# Madlibs Game
# words game where you create a story
# by filling in blanks with random words

adjective1 = input('\nEnter an adjective (descrription): ')
noun1 = input('Enter  noun (person,place,thing): ')
adjective2 = input('Enter an adjective (descrription): ')
verb1 = input('Entera verb ending with "ing": ')
adjective3 = input('Enter an adjective (descrription): ')


print(f'\nToday I went to a {adjective1} zoo.')
print(f'In an exhibit, I saw a {noun1}')
print(f'{noun1} was {adjective2} and {verb1} while')
print(f'I was {adjective3}!')'''

############################################################

'''friends = 5
friends = friends + 1
friends += 1
friends = friends - 1
friends -= 1
friends = friends * 1
friends *= 1
friends = friends / 1
friends /= 1
friends = friends ** 2
friends **= 2
remainder = friends % 2
x = 3.14
y = 4
z= 5

result = round(x)
print(result)
result = abs(y)
print(result)
result = pow(4,3)
print(result)
result = max(x,y,z)
print(result)
result = min(x,y,z)
print(result)


import math
x = 9
print(math.pi)
print(math.e)
result = math.sqrt(x)
print(result)
result = math.ceil(x)
print(result)
result = math.floor(x)
print(result)

'''
############################################################
'''import math
radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f'\nThe circumeference is: {round(circumference,2)}cm')'''

'''import math
radius = float(input('Enter the radius of a circle: '))
area = math.pi * pow(radius, 2)
print(f'\nThe Area of the circle is: {round(area,2)}cm^2')'''

'''import math
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side C = {c}')'''

############################################################

'''age = int(input('Enter your age: '))
if age >= 100:
    print('You are too old too sign up!')
elif age >= 18:
    print('You are now signed up!\n')
elif age < 0:
    print('You haven\'t been born yet')
else:
    print('You must be 18+ to sign up!\n')'''

# *****************************************************************
'''response = input('Would you like food?..(Y/N)')
# \nY for Yes..\nN for No..\n
if response == "Y":
    print('Have some food!')
else:
    print('No food for you!')'''

# *****************************************************************
'''name = input('Enter Your name: ..')
if name == '':
    print('You did not type in your name!')
else:
    print(f'Hello {name.title()}')'''
# *****************************************************************
'''is_student = True
if is_student:
    print('You are still in school!')
else:
    print('You are graduated!')'''

# *****************************************************************
'''for_sale = True
if for_sale:
    print('This item is for sale..')
else:
    print(f'This item is NOT for sale..')'''

# *****************************************************************
'''online = True
    
if online:
    print('The user is online.')
else:
    print(f'The user is offline..')'''

############################################################
############################################################

'''operator = input('Enter an operator (+ - *  /): ')
num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operator} is not valid operator!')'''

################################################################
################################################################

# Python weight converter
'''import sys
weight = float(input('Enter your weight: '))
unit = input('Kilogram or Pounds? (K or L): ')

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    # print(f'{unit}  was not valid!')
    sys.exit(f'{unit}  was not valid!')
    
print(f'Your weight is: {round(weight, 1)} {unit} ')'''

################################################################
################################################################
# Temprature Conversion Program

'''unit = input('Is this temprature in Celsius or Fahrenheit (C/F): ')
temp = float(input('Enter the Temprature: '))

if unit == "C":
    temp = round((9* temp) / 5 + 32, 1)
    print(f'The temperature in Fahrenheit is: {temp}°F')
elif unit == "F":
    temp = round((temp - 32) * 5/ 9, 1)
    print(f'The temperature in Celsius is: {temp}°C')
else:
    print(f'{unit} is an invalid unit measurement]')'''

################################################################
# Logical Operators

'''temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print('The Outdoor event is cancelled!\n')
else:
    print(f'The outdoor event is still schedulaed!\n')'''
# *****************************************************************
'''
temp = 25
# temp = -5

is_sunny = True
if temp >= 28 and is_sunny:
    print('It is HOT outside 🥵')
    print('It is SUNNY ☀️')
elif temp <= 0 and is_sunny:
    print(f'It is COLD outside 🥶😰')
    print('It is SUNNY ☀️')
# elif temp < 28 and temp > 0 and is_sunny:
elif 28 > temp > 0 and is_sunny:
    print(f'It is WARM outside 😃')
    print('It is SUNNY ☀️')
elif temp >= 28 and not is_sunny:
   print('It is HOT outside 🥵')
   print('It is cloudy ⛅')
elif temp <= 0 and not is_sunny:
    print('It is COLD outside!🥶😰')
    print('It is CLOUDY! 🌨️☁️')
elif 28 > temp > 0  and not is_sunny:
    print('It is WARM outside! 🙂😊😃')
    print('iT IS CLOUDY! 🌨️☁️⛅ ')'''

################################################################
# Iternary Operator / Conduitional Expression
# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y
'''
num = 5
print("POSITIVE" if num > 0 else "NEGATIVE")

num = 5
num = 6
age = 13
temprature= 30
user_role ="admin"


result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
status = 'ADULT' if age >= 18 else 'CHILD' 
weather =  "HOT" if temprature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)'''
################################################################
# valid user input excercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# Username must not contain Digits

'''username = input("Enter a username: ")

if len(username) > 12:
    print('Your username can\'t be more than 12 characters \n')
elif not username.find(" ") == -1:
    print(f"our username can't contain spaces")
elif not username.isalpha():
    print(f"Your username can't contain numbers")
else:
    print(f'Welcome {username}')'''
# *****************************************************************

# result = len(name)
# result = name.find(" ")
# result = name.rfind("o")
# result = name.rfind("q")
# name = name.capitalize()
# print(name)
# name = name.upper()
# print(name)
# result = name.isdigit()
# print(result)
# result = name.isalpha()

# name = input('Enter your full name: ')
# phone_number = input('Enter your phone number: ')
# result = phone_number.count('-')
# print(result)

# result = phone_number.replace("-"," ")
# print(result)

# *****************************************************************
# indexing = accessing elements of a sequence using [] (indexing operator)
#               [start : end : step]
'''credit_number = "1234-5678-9012-3456"

print(credit_number)
print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[-3])
print(credit_number[::2])-
print(credit_number[::3])
print(credit_number.replace("-"," "))

print()'''
# *****************************************************************
# Program to get the last three digits of a credit card number
'''credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number = credit_number[::-1]
print(f'Reveresed Credit Card Number is: {credit_number}')'''
# *****************************************************************
# format specifiers = {value:flags} format a value based on what
# flags are inserted
'''price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"Price 1 is ${price1:.2f}")
print(f"Price 1 is ${price1:.3f}\n")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 2 is ${price2:.3f}\n")
print(f"Price 3 is ${price3:.2f}")
print(f"Price 3 is ${price3:.3f}\n")

print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}\n")

print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}\n")
# Left justify

print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}\n")

#centered
print(f"Price 1 is ${price1:^10}")
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}\n")
#Display postive values
print(f"Price 1 is ${price1:+}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}\n")

# or use a space rather

print(f"Price 1 is ${price1: }")
print(f"Price 2 is ${price2: }")
print(f"Price 3 is ${price3: }\n")
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# Comma Separated

print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}\n")
#Mix and match flags
print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.2f}\n")'''

# Above are format specifiers in Python
# *****************************************************************
# *****************************************************************
# while loop = execute some code WHILE some condition remains true
# while loop
'''name = input('Enter your name:      ')
while name == '':
    print("You did not enter a name!!")
    name = input('Enter your name:      ')

print(f'Hello {name}')'''

# *****************************************************************
'''
age = int(input('Enter your age?    '))
while age < 0:
    age = int(input('Enter your age?    '))

print(f'You are {age} years old..')'''
# *****************************************************************

'''food = input('Enter a food you like (q to quit):    ')

while not food == 'q':
    print(f'You like {food}..\n')
    food = input('Enter a food you like (q to quit):    ')

print('Bye!')
'''
# *****************************************************************
'''
num = int(input('Enter a number between 1 and 10: '))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input('Enter a # between 1 - 10:  '))

print(f'Your number is {num}')'''

# *****************************************************************
#   Python Compound Interest Calculator

'''principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the principle amount:    '))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input('Enter the rate amount:    '))
    if rate <= 0:
        print("Rate can't be less than or equal to zero")

while time <= 0:
    time = int(input('Enter the time in years:    '))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} in year/s: ${total:.2f}')
# print(principle)
# print(rate)
# print(time)
#
# '''

# *****************************************************************
#   Example 2
#   if we wan to enter  zero
'''
principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the principle amount:    '))
    if principle <= 0:
        print("Principle can't be less than zero")
    else:
        break
while rate < 0:
    rate = float(input('Enter the rate amount:    '))
    if rate <= 0:
        print("Rate can't be less than zero")
    else:
        break
while time < 0:
    time = float(input('Enter the time amount:    '))
    if time <= 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)

# print(principle)
# print(rate)
# print(time)'''
# *****************************************************************
# for loops = execute a block of code a fixed number of times.
#               You can iterate over a range, string, sequence, etc.
# For loops
'''
for i in range(1, 11):
    print(i)
print('Happy New Year!!')

print()'''
# *****************************************************************
'''
for x in reversed(range(1, 11)):
    print(x)
print('HAPPY NEW YEAR!!..\n')
print()'''
# *****************************************************************
'''
for x in reversed(range(1, 11, 2)):
    print(x)
print('HAPPY NEW YEAR!!..\n')'''
# *****************************************************************

'''for x in reversed(range(1, 11, 3)):
    print(x)
print('HAPPY NEW YEAR!!..\n')

print()'''
# *****************************************************************

# string iterations

'''credit_card = '11234-5678-9012-3456'
for x in credit_card:
    print(x)

print()'''
# *****************************************************************
'''for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

print()'''
# *****************************************************************
'''for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
print()'''

# *****************************************************************
# *****************************************************************
