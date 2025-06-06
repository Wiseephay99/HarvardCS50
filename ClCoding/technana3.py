print()

import math 
import random
import sys 
import math 


'''def calculate_days_to_units(days):
    return f'{days} Days converted to Units is: {days * 24} hours...'

def evaluate_and_execute(days):
    try:
        if days.lower() in ['q', 'exit']:
            sys.exit(f'Bye..Thanks for Using Days Converter...\n')
            
        days = int(days)
        if days > 0:
            print(calculate_days_to_units(days))
        elif days == 0:
            print(f'You entered a 0 so no conversion for you.....')
        elif days < 0:
            print(f'You entered a NEGATIVE NUMBER ...don\'t ruin my program...')
    except ValueError:
        print(f'Invalid Input..')
        
while True:
    print(f'---------------------------------------------------------')
    days = input('Enter no of days and we will convert it to Hours..\n\n')
    print(f'---------------------------------------------------------')
    evaluate_and_execute(days)'''

#=================================================================================================
#=================================================================================================
#=================================================================================================

'''
def calculate_days_to_units(days):
    return f'{days} Days converted to Units is: {days * 24} hours...'

def evaluate_and_execute(days):
    
        if days.lower() in ['q', 'exit']:
            sys.exit(f'Bye..Thanks for Using Days Converter...\n')
            
        
        days = days.split(",")
        days = [day.strip() for day in days]
        for day in days:
            try:
                day = int(day)
                if day > 0:
                    print(calculate_days_to_units(day))
                elif day == 0:
                    print(f'You entered a 0 so no conversion for you.....')
                elif day < 0:
                    print(f'You entered a NEGATIVE NUMBER ...don\'t ruin my program...')
            except ValueError:
                print(f'Invalid Input..')
        
while True:
    print(f'---------------------------------------------------------')
    days = input('Enter no of days as list separated by comma and we will convert it to Hours..\n\n')
    print(f'---------------------------------------------------------')
    evaluate_and_execute(days)  '''

#=================================================================================================
#=================================================================================================
#=================================================================================================


def calculate_days_to_units(days, units):
    if units.lower() == 'hours':
        return f'{days} Days converted to Hours is: {days * 24} hours...'
    elif units.lower() == 'minutes':
        return f'{days} Days converted to minutes is: {days * 24 * 60} minutes...'
    elif units.lower() == 'seconds':
        return f'{days} Days converted to seconds is: {days * 24 * 3600} seconds...'
    else:
        return f'Invalid Units'

def evaluate_and_execute(days):
    
        if days.lower() in ['q', 'exit']:
            sys.exit(f'Bye..Thanks for Using Days Converter...\n')
        try:   
            days = days.split(":")
            days = [day.strip() for day in days]
            days_dict = {'days': days[0], 'units': days[1]}
            user_days = int(days_dict['days'])
            user_days_units = days_dict['units']
            if user_days > 0:
                print(calculate_days_to_units(user_days, user_days_units))
            elif user_days == 0:
                print(f'You entered a 0 so no conversion for you.....')
            elif user_days < 0:
                print(f'You entered a NEGATIVE NUMBER ...don\'t ruin my program...')
        except IndexError:
            print(f'You need to enter no of days and units separated by colon..')

while True:
    print(f'---------------------------------------------------------')
    days = input('Enter no of days and units sepatarated by colon and \nI\'ll covert it to your units..\n\n')
    print(f'---------------------------------------------------------')
    evaluate_and_execute(days)  
    