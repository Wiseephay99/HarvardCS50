import math
import sys  # sys.exit()
import random
print()

'''def days_to_units(days):
    return f'{days} days is: {days * 24} hours\n'

def evaluate_and_execute(user_days):
    try:
        user_days = user_days.split(',')
        user_days = [days.strip() for days in user_days]
        
        for days in set(user_days):
            days = int(days)
            if days > 0:
                print(days_to_units(days))
            elif days == 0:
                print(f'You entered a 0, so no converision for you..\n')
            elif days < 0:
                print(f'You entered a NEGATIVE NUMBER. Don\'t ruin the program..\n')
            else:
                print(f'Invalid Input..\n')

    except ValueError:
        print(f'Invalid Input..\n')

user_days = ''
while True:
    user_days = input('Enter days separated by comma(,) and I\'ll convert it to hours...\nQ to Quit..\n\n')
    print(f'\n----------------------------------------------------')
    if user_days.lower() == 'q':
        print(f'Bye👋👋👋..\n')
        sys.exit()
    else:
        evaluate_and_execute(user_days)'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

'''
def days_to_units(days,conversion_units):
    if conversion_units.lower() == 'hours':
        return f'{days} days is: {days * 24} hours..\n'
    elif conversion_units.lower() == 'minutes':
        return f'{days} days is: {days * 24 * 60} minutes..\n'
    elif conversion_units.lower() == 'seconds':
        return f'{days} days is: {days * 24 * 3600} seconds..\n'
    else:
        return f'Invalid conversion unit..\n'
    
def validate_and_execute(user_days):
    try:
        user_days = user_days.split(':')
        user_days = [days.strip() for days in user_days]
        user_days_dict = {'days': user_days[0], 'units': user_days[1]}
        user_days_input = int(user_days_dict['days'])

        if user_days_input > 0:
            print(days_to_units(user_days_input, user_days_dict['units']))
        elif user_days_input == 0:
            print(f'You entered a 0 so no conversion for you!...\n')
        elif user_days_input < 0:
            print(f'You entered a NEGATIVE NUMBER...don\'t ruin the program!...\n')
    except ValueError:      
        print(f'Invalid Input..\n')

while True:
    print(f'----------------------------------------------------')
    user_days = input('Enter days and units separated by colon(:) and ..\nwe can convert it to your preffered units...\n\n')
    print(f'\n----------------------------------------------------')
    if user_days.lower() == 'q':
        print(f'Bye👋👋👋..\n')
        break
    else:
        validate_and_execute(user_days)

'''
# =====================================================================================
# =====================================================================================
# =====================================================================================

'''
def calculate_days_to_units(days):
    return f'{days} days to Hours is: {days * 24} hours'

def evaluate_and_execute(days):
    
    if days.lower() == 'exit':
        sys.exit('\nBye...\n')
    if days.isdigit():
        days = int(days)
        if days > 0:
            print(calculate_days_to_units(days))
        elif days < 0:
            print('You have entered a NEGATIVE NUMBER so no conversion for you..\n')
        elif days == 0:
            print('You have entered a ZERO. so no conversion for you...\n')
    else:
        print('Enter a VALID NUMBER...\n')
        
days = ''
while days != 'exit':
    print(f'-------------------------------------------------------------')
    days = input('Enter number of days and I\'ll conert it to hours..\n\n')
    evaluate_and_execute(days)
 '''   
# =====================================================================================
# =====================================================================================
# =====================================================================================
'''
# Lists in practise...
def calculate_days_to_units(days):
    return f'{days} days to Hours is: {days * 24} hours'

def evaluate_and_execute(days):
    
    if days.lower() == 'exit':
        sys.exit('\nBye...\n')
    days = days.split(',')
    days = [day.strip() for day in days]
    for day in days:
        if day.isdigit():
            day = int(day)
            if day > 0:
                print(calculate_days_to_units(day))
            elif day < 0:
                print('You have entered a NEGATIVE NUMBER so no conversion for you..\n')
            elif day == 0:
                print('You have entered a ZERO. so no conversion for you...\n')
        else:
            print('Enter a VALID NUMBER...\n')
        
days = ''
while days != 'exit':
    print(f'-------------------------------------------------------------')
    days = input('Enter number of days separated by comma(,)as a list and I\'ll convert it to hours..\n\n')
    evaluate_and_execute(days)
'''
# Using a Dictionary

# =====================================================================================
# =====================================================================================
# =====================================================================================
'''

def calculate_days_to_units(days, unit):
    return f'{days} days to Hours is: {days * 24} {unit}'

def evaluate_and_execute(days):
    
    if days.lower() == 'exit':
        sys.exit('\nBye...\n')
    days = days.split(':')
    days = [day.strip() for day in days]
    days_dict = {'days':days[0],'unit':days[1]}
    user_days  = int(days_dict['days'])
    user_days_units = days_dict['unit']
    
    if user_days > 0:
        print(calculate_days_to_units(user_days, user_days_units))
    elif user_days < 0:
        print('You have entered a NEGATIVE NUMBER so no conversion for you..\n')
    elif user_days == 0:
        print('You have entered a ZERO. so no conversion for you...\n')
    else:
        print('Enter a VALID NUMBER...\n')
        
days = ''
while days != 'exit':
    print(f'-------------------------------------------------------------')
    days = input('Enter number of days  and units separated by (:) and I\'ll convert it for you...\n\n')
    evaluate_and_execute(days)

'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

'''def day_to_units(days):
    return f'\n{days} converted to hours is: {days * 24} hours..'

def calculate_and_evaluate(days):
    try:        
        if days.lower() == 'exit':
            sys.exit(f'\nBye 👋👋👋...\n')
        days = int(days)
        if days > 0:
            print(day_to_units(days))
        elif days == 0:
            print(f'You entered a Zero..so no conversion for you....')
        elif days < 0:
            print(f'You entered a NEGATIVE NUMBER so no coversion for you....')
    except ValueError:
        print(f'Invalid Input...')
        
days = ''
while days != 'exit':  
    days = input('Enter no of days and I\'ll convert it to hours?...\n\n')
    calculate_and_evaluate(days)
'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

# List in Practise

'''def day_to_units(days):
    return f'{days} converted to hours is: {days * 24} hours..'

def calculate_and_evaluate(days):
    if days.lower() == 'exit':
        sys.exit(f'\nBye 👋👋👋...\n')
    days = days.split(',')
    days = [day.strip() for day in days]
    for day in set(days):
        try: 
            day = int(day)
            if day > 0:
                print(day_to_units(day))
            elif day == 0:
                print(f'You entered a Zero..so no conversion for you....')
            elif day < 0:
                print(f'You entered a NEGATIVE NUMBER so no coversion for you....')
        except ValueError:
            print(f'Invalid Input')
        
days = ''
while days != 'exit':  
    print(f'----------------------------------------------------------------------------------')
    days = input('Enter no of days as a list separated by a comma and I\'ll convert it to hours?...\n\n')
    print()
    calculate_and_evaluate(days)'''
    

# =====================================================================================
# =====================================================================================
# =====================================================================================    

# Use of Dictionaries...
'''
def day_to_units(days, units):
    if units.lower() == 'hours':
        return f'{days} days converted to hours is: {days * 24} hours..'
    elif units.lower() == 'minutes':
        return f'{days} days converted to minutes is: {days * 24} minutes..'
    elif units.lower() == 'seconds':
        return f'{days} days converted to seconds is: {days * 24} seconds..'
    else:
        return f'Invalid Units'

def calculate_and_evaluate(days):
    if days.lower() == 'exit':
        sys.exit(f'\nBye 👋👋👋...\n')
        
    days = days.split(':')
    days = [day.strip() for day in days]
    days_dict = {'days':days[0], 'units':days[1]}
    
    days_to_convert = int(days_dict['days'])
    
    if days_to_convert > 0:
        print(day_to_units(days_to_convert, days_dict['units']))
    elif days_to_convert == 0:
        print(f'You entered a Zero..so no conversion for you....')
    elif days_to_convert < 0:
        print(f'You entered a NEGATIVE NUMBER so no coversion for you....')

        
days = ''
while days != 'exit':  
    print(f'----------------------------------------------------------------------------------')
    days = input('Enter no of days and units to change to separated by colon\nand I\'ll convert it to either hours,minutes or seconds...\n\n')
    print()
    calculate_and_evaluate(days)

''' 
    
    
# =====================================================================================
# =====================================================================================
# =====================================================================================

'''ROCK PAPER SCISSORS GAME

print('-------------------------------------------')
print(f' Welcome to ROCK PAPER SCISSORS GAME')
print('-------------------------------------------')

import random
import math
from enum import Enum
import sys

player = input('Choose...\n1 for ROCK🪨🪨..\n2 for PAPER📄📃..\n3 FOR SCISSIORS✂️✂️...\n\n')
python = random.choice('123')
python = int(python)
player = int(player)

print(f'\nPlayer chose: {player}')
print(f'Python chose: {python}\n')

if player ==  '1' and python == '2':
    print(f'Player Wins')
elif player ==  '2' and python == '3':
    print(f'Player Wins')
elif player ==  '3' and python == '1':
    print(f'Player Wins')
elif player ==  python:
    print(f'Its a Tie..')
else:
    print(f'Python Wins')

print()

'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

'''ROCK PAPER SCISSORS GAME'''

import random
import math
from enum import Enum
import sys

print('-------------------------------------------')
print(f' Welcome to ROCK PAPER SCISSORS GAME')
print('-------------------------------------------')

def rps():
    class RPS(Enum):
        ROCK = 1 
        PAPER = 2
        SCISSSORS = 3

    # print(RPS(2))
    # print(RPS.PAPER)
    # print(RPS.PAPER.name)
    # print(RPS.PAPER.value)
    # print(RPS['PAPER'])
    # print(RPS['PAPER'].value)
    # print(RPS(2).name)
    # print(RPS(2).value)

    player = input('Choose...\n1 for ROCK🪨🪨..\n2 for PAPER📄📃..\n3 FOR SCISSIORS✂️✂️...\n\n')

    if player.lower() == 'exit':
        sys.exit('Thanks for playing ROCK PAPER SCISSORS...\n')
        
    python = random.choice('123')
    python = int(python)
    player = int(player)

    # print(f'\nPlayer chose: {player}')
    # print(f'Python chose: {python}\n')
    print(f'\nPlayer chose: {player}')
    print(f'Python chose: {python}\n')

    def decide_winner():
        if player ==  '1' and python == '2':
            return f'Player Wins'
        elif player ==  '2' and python == '3':
            return f'Player Wins'
        elif player ==  '3' and python == '1':
            return f'Player Wins'
        elif player ==  python:
            return f'Its a Tie..'
        else:
            return f'Python Wins'

    result = decide_winner()
    print(result)
    print()

    print(f'-----------------------------------')
    print(f'Do you want to play again?...\n')
    playagain = True
    while playagain:
        playagain = input(f'Y to continue playing again..\nQ  or exit to Quit..\n\n')
        if playagain.lower() not in ['y', 'q', 'exit']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        print()
        return rps()
    elif playagain.lower() == 'exit' or 'q':
        print(f'---------------------------------------------')
        print(f'Thanks for playing ROCK PAPER SCISSORS.......')
        print(f'---------------------------------------------\n')
        playagain = False
    

rps()