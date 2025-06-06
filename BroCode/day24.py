
import math
import random
from enum import Enum
import time
import sys

##############################################################
##############################################################

'''
print()
print('---------------------------------------------------')
foods = []
food = input('Enter food you like? (q to quit)  ')
while not food == 'q':
    foods.append(food)

    food = input('Enter another food you like? (q to quit)  ')

    if food in foods:
        print(f'{food} is already in your cart')

print('\n---------------------------------------------------')
print('The foods you like are:')
for food in set(foods):
    print(food, end=" ")

print()
print('---------------------------------------------------')
'''

##############################################################
##############################################################

'''menu = {
    "nachos": 3.50,
    "pretzel": 2.00,
    "chips": 1.50,
    "tea": 2.00,
    "coffee": 2.60,
    "candy": 1.70,
    "popcorn": 3.00,
    "magaritos": 4.00,
}
print('\n--------------------YOUR MENU--------------------')
for i, (food, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {food:10}: ${price:.2f}')
print()
print('--------------------------------------------------')

cart = {}
total = 0

while True:
    food = input('Enter the food you want? (q to quit): ')
    if food.lower() == 'q':
        break

    if not food:
        print('You did not select an item!')
        continue

    if menu.get(food) is not None:
        cart[food] = menu[food]
        continue

print()
print('\n--------------------YOUR CART--------------------\n')
if not cart:
    print('You have no items in your cart...')
else:
    for i, (food, price) in enumerate(cart.items(), start=1):
        print(f'{i}. {food:10}: $ {price:.2f}')
print('\n--------------------TOTAL COST--------------------\n')
for price in cart.values():
    total += price
print(f'Your Total Cost is: ${total:.2f}')
print('\n----------------------------------------------------\n')

'''

##############################################################
##############################################################

'''
print(f'\n-----------------------------------------------')
foods = {}
total = 0

while True:

    food = input('Enter food you like (q to quit):  ')

    if food.lower() == 'q':
        break

    while True:
        price = input(f'Enter the price of {food}:  ')
        if not price.isdigit():
            print('Invalid price..')
            continue
        elif price.isdigit():
            foods[food] = float(price)
        break

print(f'--------------------YOUR ITEMS-------------------------')
for i, (food, price) in enumerate(foods.items(), start=1):
    print(f'{i}. {food:10}: {price:.2f}')
print(f'-----------------------------------------------')
for price in foods.values():
    total += price
print(f'Total cost of items is: {total:.2f}')
print(f'-----------------------------------------------')

'''
##############################################################
##############################################################

'''print('-----------------------------------------------------')


def days_to_units(days):
    if days > 0:
        return f'{days} days to hours is {days * 24} hours'
    elif days == 0:
        return 'You entered a 0 so no conversion for you...'
    elif days < 0:
        return f'You entered a negative number!! don\'t ruin the program'


while True:
    no_of_days = input(
        'Enter # days and I will convert to units (q to quit): ')

    if no_of_days.lower() == 'q':
        break
    elif no_of_days.isdigit():
        no_of_days = int(no_of_days)
        print(days_to_units(no_of_days))
    else:
        print(f'{no_of_days} is invalid ..enter a valid number')
        continue


print('\nExiting Days to units converter...\n')
'''
##############################################################
##############################################################

'''print('-----------------------------------------------------')


def days_to_units(days):
    if days > 0:
        return f'\n{days} days to hours is {days * 24} hours\n'
    elif days == 0:
        return '\nYou entered a 0 so no conversion for you...\n'
    elif days < 0:
        return f'\nYou entered a negative number!! don\'t ruin the program\n'


def execute_and_validate(no_of_days):
    if no_of_days.lower() == 'q':
        sys.exit('\nExiting Days to units converter...\n')

    elif no_of_days.isdigit():
        no_of_days = int(no_of_days)
        print(days_to_units(no_of_days))
    else:
        print(f'\n{no_of_days} is invalid ..enter a valid number\n')


while True:
    no_of_days = input(
        'Enter # days and I will convert to units (q to quit): ')
    execute_and_validate(no_of_days)'''

##############################################################
##############################################################

'''
print('-----------------------------------------------------')
def days_to_units(days):
    return f'\n{days} days to hours is {days * 24} hours\n'


def execute_and_validate(no_of_days):
    if no_of_days.lower() == 'q':
        sys.exit('\nExiting Days to units converter...\n')

    elif no_of_days.isdigit():
        no_of_days = int(no_of_days)
        if no_of_days > 0:
            print(days_to_units(no_of_days))
        elif no_of_days == 0:
            print(f'\nYou entered a 0 so no conversion for you...\n')
        elif no_of_days < 0:
            print(f'\nYou entered a negative number!! don\'t ruin the program\n')
    else:
        print(f'\n{no_of_days} is invalid ..enter a valid number\n')


while True:
    no_of_days = input(
        'Enter # days and I will convert to units (q to quit): ')
    execute_and_validate(no_of_days)'''

##############################################################
##############################################################
# for loop
'''
print('-----------------------------------------------------')
def days_to_units(days):
    return f'{days} days to hours is {days * 24} hours'


def execute_and_validate(no_of_days):
    if no_of_days.lower() == 'q':
        sys.exit('\nExiting Days to units converter...\n')

    no_of_days = no_of_days.split(",")
    no_of_days = [day.strip() for day in no_of_days]
    for day in no_of_days:
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(days_to_units(day))
            elif day == 0:
                print(f'You entered a 0 so no conversion for you...')
            elif day < 0:
                print(f'You entered a negative number!! don\'t ruin the program')
        else:
            print(f'{day} is invalid ..enter a valid number')


while True:
    no_of_days = input(
        'Enter # days separated by comma (",") and I will convert to units (q to quit):\n\n')
    execute_and_validate(no_of_days)'''


##############################################################
##############################################################
# for loop

print('-----------------------------------------------------')


def days_to_units(days, units):
    if units == 'hours':
        return f'{days} days to hours is {days * 24} hours'
    elif units == 'seconds':
        return f'{days} days to minutes is {days * 24 * 60} minutes'
    elif units == 'minutes':
        return f'{days} days to seconds is {days * 24 * 3600} seconds'
    else:
        return f'{units} is an invalid unit'


def execute_and_validate(no_of_days):
    if no_of_days.lower() == 'q':
        sys.exit('\nExiting Days to units converter...\n')

    no_of_days = no_of_days.split(":")
    no_of_days = [day.strip() for day in no_of_days]
    no_of_days_dict = {'days': no_of_days[0], 'units': no_of_days[1]}
    days_dict = no_of_days_dict['days']
    units_dict = no_of_days_dict['units']

    if days_dict.isdigit():
        day = int(days_dict)
        if day > 0:
            print(days_to_units(day, units_dict))
        elif day == 0:
            print(f'You entered a 0 so no conversion for you...')
        elif day < 0:
            print(f'You entered a negative number!! don\'t ruin the program')
    else:
        print(f'{days_dict} is invalid ..enter a valid number')


while True:
    no_of_days = input(
        '\nEnter # days separated by colon(":") and unit and I will \nconvert to units (q to quit):\n\n')
    execute_and_validate(no_of_days)
