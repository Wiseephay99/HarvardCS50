
print()
'''
operator = input('Enter an operator (+ - * /):  ')
num1 = float(input('Enter 1st number:     '))
num2 = float(input('Enter 2nd number:     '))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f'{operator} is not valid')
print(result)'''

# *********************************************************
# python weight conveter program
'''
weight = input('Enter your weight: ')
unit = input('Kilograms or Pounds? (K or L):    ')

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "L":
    weight = weight * 2.205
    unit = "Kgs."
else:
    print(f'{unit} was not valid')

print(f'Your weight is: {round(weight, 1)} {unit}')'''

# *********************************************************
# Python weight conversion program
'''
unit = input('Is the temprature in Celcius or Fahrenheit (C/F):     ')
temp = float(input('Enter the temprature:   '))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temprature in Fahrenheit is: {temp}F')
elif unit == "F":
    temp = round((temp - 32) / 5 / 9, 1)
    print(f'The temprature in Celcius is: {temp}C')
else:
    print(f'{unit} is an invalid unit of measurement')'''

# *********************************************************
#   Logical Operator
'''
temp = 40
sunny = True

if temp > 0 and temp < 30:
    print('The temprature is bad')
else:
    print('The temprature is good')

if sunny:
    print('It is sunny outside')
else:
    print('It is cloudy outside')

num = 5
a = 6
b = 7
age = 25
temperature = 30
user_role = 'guest'

print('Positive' if num > 0 else "Negative")

result = 'EVEN' if num % 2 == 0 else "ODD"
print(result)


max_num = a if a > b else b
min_num = a if a < b else b
status = 'ADULT' if age >= 18 else 'CHILD'
temprature = 'HOT' if temperature > 20 else "COLD"
access_level = 'Full Access' if user_role == 'admin' else 'Limited Access'

print(max_num)
print(min_num)
print(status)

print(access_level)
'''
# *********************************************************
# validate user input excercise
# 1. username is no more than 12  characters
# 2. username must not contain spaces
# 3. username must not contain digits
'''
username = input('Enter a username: ')

if len(username) > 12:
    print(f'Username can\'t be more than 12 characters')
elif username.find(" ") == -1:
    print('Your username can\'t contain spaces')
elif username.isalpha():
    print('Your username can\'t  contain numbers')
else:
    print(f'Welcome {username}')
'''
# *********************************************************
# Email slicing Program
'''
email = input('Enter your email:    ')

index = email.index("@")
username = email[:index]
dormain = email[index + 1:]

username = email[:email.index("@")]
dormain = email[email.index("@") + 1:]
print(f'Your username is {username} and dormain is {dormain}')
'''
# *********************************************************
# format specifiers
'''
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f'Price 1 is {price1:.1f}')
print(f'Price 2 is {price2:.1f}')
print(f'Price 3 is {price3:.1f}\n')

print(f'Price 1 is {price1:.2f}')
print(f'Price 2 is {price2:.2f}')
print(f'Price 3 is {price3:.2f}\n')

print(f'Price 1 is {price1:.3f}')
print(f'Price 2 is {price2:.3f}')
print(f'Price 3 is {price3:.3f}\n')

print(f'Price 1 is {price1:10}')
print(f'Price 2 is {price2:10}')
print(f'Price 3 is {price3:10}\n')

print(f'Price 1 is {price1:010}')
print(f'Price 2 is {price2:010}')
print(f'Price 3 is {price3:010}\n')

print(f'Price 1 is {price1:<10}')
print(f'Price 2 is {price2:<10}')
print(f'Price 3 is {price3:<10}\n')

print(f'Price 1 is {price1:>10}')
print(f'Price 2 is {price2:>10}')
print(f'Price 3 is {price3:>10}\n')

print(f'Price 1 is {price1:^10}')
print(f'Price 2 is {price2:^10}')
print(f'Price 3 is {price3:^10}\n')

print(f'Price 1 is {price1:+}')
print(f'Price 2 is {price2:+}')
print(f'Price 3 is {price3:+}\n')

print(f'Price 1 is {price1: }')
print(f'Price 2 is {price2: }')
print(f'Price 3 is {price3: }\n')

# 1000 separator
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f'Price 1 is {price1:,}')
print(f'Price 2 is {price2:,}')
print(f'Price 3 is {price3:,}\n')

print(f'Price 1 is {price1:,.2f}')
print(f'Price 2 is {price2:,.2f}')
print(f'Price 3 is {price3:,.2f}\n')

print(f'Price 1 is {price1:+,.2f}')
print(f'Price 2 is {price2:+,.2f}')
print(f'Price 3 is {price3:+,.2f}\n')
'''
# *********************************************************
# name = input('Enter your name:      ')

# if name == "":
#     print(f'You did not enter your name')
# else:
#     print(f'Hello {name}')

name = input('Enter your name:      ')
while name == "":
    print(f'You did not enter your name')
    name = input('Enter your name:      ')
print(f'Hello {name}')

# *********************************************************

age = int(input('Enter your age:    '))
while age < 0:
    print('Age can\'t be negative')
    age = int(input('Enter your age:    '))

print(f'You are {age} years old')

# *********************************************************

food = input('Enter a food you like (q to quit):    ')

while not food == 'q':
    print(f'You like {food}')
    food = input('Enter another food you like')

print('\nBye\n')

# *********************************************************

num = int(input('Enter anumber between 1 to 10: '))

while num < 1 or num > 10:
    print(f'Number {num} is not valid')
    num = int(input('Enter anumber between 1 to 10: '))

print(f'Your number is {num}\n')

# *********************************************************
# Python Compund Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the principle amount:    '))
    if principle <= 0:
        print('Princple can\'t be less than or equal to zero')
while rate <= 0:
    rate = float(input('Enter the Interest rate amount:    '))
    if rate <= 0:
        print('Interest Rate can\'t be less than or equal to zero')
while time <= 0:
    time = float(input('Enter the time in years:    '))
    if time <= 0:
        print('Time can\'t be less than or equal to zero')

print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year\'s: ${total:.2f}\n')

# *********************************************************
# Python Compund Interest Calculator 2

principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the principle amount:    '))
    if principle < 0:
        print('Princple can\'t be less than zero')
    else:
        break
while True:
    rate = float(input('Enter the Interest rate amount:    '))
    if rate < 0:
        print('Interest Rate can\'t be less than zero')
    else:
        break

while True:
    time = float(input('Enter the time in years:    '))
    if time < 0:
        print('Time can\'t be less than zero')
    else:
        break
print(principle)
print(rate)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year\'s: ${total:.2f}\n')

# *********************************************************
