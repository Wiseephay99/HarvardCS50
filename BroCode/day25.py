import random
import math
from enum import Enum
import sys
import time
print()

#######################################################################
#######################################################################

'''
print('-----------------------------------')
foods = []
food = input('Enter food you like q to  quit:   ')
while not food == 'q':
    foods.append(food)
    food = input('Enter another food you like q to  quit:   ')
print('-----------------------------------')
print('The foods you like are: ')
for food in foods:
    print(food, end=' ')
print()
'''

#######################################################################
#######################################################################

'''
print('-----------------------------------')
foods = []
food = input('Enter food you like q to  quit:   ')
while food != 'q':
    foods.append(food)
    food = input('Enter another food you like q to  quit:   ')
print('-----------------------------------')
if not food:
    print('You did not enter any item to your cart')
print('The foods you like are: ')
for food in foods:
    print(food, end=' ')
'''

#######################################################################
#######################################################################
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
#######################################################################
#######################################################################
'''
print('--------------------------------------------------------')

def days_to_units(no_of_days):
    if no_of_days > 0:
        return f'{no_of_days} to hours is {no_of_days * 24}'
    elif no_of_days == 0:
        return f'You entered a 0 so no conversion for you'
    elif no_of_days < 0:
        return f'You eentered a negative number..don\'t ruin the program'


def evalaute_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nExiting Days Conveter...\n')

    if days.isdigit():
        days = int(days)
        print(days_to_units(days))
    else:
        print(f'Invalid # days..Enter a valid number! ')


while True:
    days = input('Enter # days and I will  convert it to hours:  ')
    evalaute_and_excute(days)
   '''
#######################################################################
#######################################################################
'''
print('--------------------------------------------------------')


def days_to_units(no_of_days):
    return f'{no_of_days} to hours is {no_of_days * 24}'


def evalaute_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nExiting Days Conveter...\n')

    if days.isdigit():
        days = int(days)
        if days > 0:
            print(days_to_units(days))
        elif days == 0:
            print(f'You entered a 0 so no conversion for you')
        elif days < 0:
            print(f'You eentered a negative number..don\'t ruin the program')
    else:
        print(f'Invalid # days..Enter a valid number! ')


while True:
    days = input(
        'Enter # days and I will  convert it to hours (q to quit):  ')
    evalaute_and_excute(days)
'''
#######################################################################
#######################################################################

'''
# list

def days_to_units(no_of_days):
    return f'{no_of_days} to hours is {no_of_days * 24}'


def evalaute_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nExiting Days Conveter...\n')

    days = days.split(",")
    days = [day.strip() for day in days]
    for day in set(days):
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(days_to_units(day))
            elif day == 0:
                print(f'You entered a 0 so no conversion for you')
            elif day < 0:
                print(f'You entered a negative number..don\'t ruin the program')
        else:
            print(f'{days} Invalid # day..Enter a valid number! ')


while True:
    print('--------------------------------------------------------')
    days = input('Enter # days a list separated by comma (,) (q to quit): \n')
    evalaute_and_excute(days)'''

#######################################################################
#######################################################################
# dictionary

'''
def days_to_units(no_of_days, units):
    if units == 'hours':
        print(f'{no_of_days} to hours is {no_of_days * 24}')
    elif units == 'minutes':
        print(f'{no_of_days} to minutes is {no_of_days * 24 * 60}')
    elif units == 'seconds':
        print(f'{no_of_days} to seconds is {no_of_days * 24 * 3600}')


def evalaute_and_excute(days):
    if days.lower() == 'q':
        sys.exit('\nExiting Days Conveter...\n')

    days = days.split(":")
    days = [day.strip() for day in days]
    days_units = {'days': days[0], 'units': days[1]}
    user_days = days_units['days']
    user_units = days_units['units']
    if user_days.isdigit():
        if user_days.isdigit():
            user_days = int(user_days)
            if user_days > 0:
                days_to_units(user_days, user_units)
            elif user_days == 0:
                print(f'You entered a 0 so no conversion for you')
            elif user_days < 0:
                print(f'You entered a negative number..don\'t ruin the program')
        else:
            print(f'{user_days} Invalid # day..Enter a valid number! ')


while True:
    print('--------------------------------------------------------')
    days = input(
        'Enter # days and hours separated by colon (:) (q to quit): \n')
    evalaute_and_excute(days)
'''

#######################################################################
#######################################################################
