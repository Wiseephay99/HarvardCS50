print()

# Variables

age = 20
print('Hello World')
print(age)
age = 30
print(age)

# Data Types

price = 19.95
first_name = 'Wise'
second_name = 'Hamdani'

is_online = 'False'

# ======================================================

# Input Function
user_name = input('What is your name?   ')
print(f'Hello {user_name}...\n')

# ======================================================

birth_year = input(f'Enter your birth year:     ')
try:
    age = 2020 - int(birth_year)
    print(age)
except ValueError:
    print(f'Invalid Input')

# ======================================================

int(), float(), bool(),
# Excerise
try:
    print()
    num1 = float(input('First num:    '))
    num2 = float(input('Second num:    '))

    result = num1 + num2
    print(f'Sum: {round(result, 2)}')
    print()
except ValueError:
    print(f'Invalid Input!.....\n')
