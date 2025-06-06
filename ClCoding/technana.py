print()

hours = 24
minutes = hours * 60
seconds = minutes * 60
units = "days"

# Variables, f-strings, and arithemetic operations
print(f'\n--------------------------------------')
print(f'20 days has {20 * 24} hours')
print(f'35 days has {35 * 24} hours')
print(f'50 days has {50 * 24} hours')
print(f'110 days has {110 * 24} hours')
print(f'--------------------------------------')
print(f'20 days has {20 * 24 * 60} minutes')
print(f'35 days has {35 * 24 * 60} minutes')
print(f'50 days has {50 * 24 * 60} minutes')
print(f'110 days has {110 * 24 * 60} minutes')
print(f'--------------------------------------')
print(f'20 days has {20 * 24 * 60 * 60} hours')
print(f'35 days has {35 * 24 * 60 * 60} hours')
print(f'50 days has {50 * 24 * 60 * 60} hours')
print(f'110 days has {110 * 24 * 60 * 60} hours')
print(f'--------------------------------------\n')

print(f'20 {units} to hours is {20 * hours} hours')
print(f'35 {units} to hours is {35 * hours} hours')
print(f'--------------------------------------\n')


'''user_days = input('Enter no of days and covert it to hours and minutes:...      \n')

user_days = int(user_days)
print(f'{user_days} {units} to hours is: {user_days * hours} hours\n')
print(f'{user_days} {units} to minutes is: {user_days * minutes} minutes\n')'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

# Functions and user input

'''
def calculate_to_units(days):
    print(f'{user_days} {days} to Hours is: {user_days * hours} hours\n\
{user_days} {days} to  Minutes is: {user_days * minutes} hours\n\
{user_days} {days} to Seconds is: {user_days * seconds} seconds\n')


user_days = ''
while user_days != "exit":
    if user_days == 'exit':
        print(f'Bye..\n')
        break
    user_days = input(
        'Enter no of days and covert it to hours and minutes:...      \n\n')
    print(f'---------------------------------------------------')
    user_days = int(user_days)
    calculate_to_units(user_days)'''

# =====================================================================================
# =====================================================================================
# =====================================================================================

# change days to units..use a number of days as input

'''
def calculate_to_units(days):
    if days > 0:
        print(f'{days} {units} to minutes is: {days * minutes} minutes.\n')
    elif days == 0:
        print(f'You entered a Zero so no conversion for you....\n')
    elif days < 0:
        print(f'You entered a Negative Number so no conversion for you.../n')
    else:
        print(f'You entered an invalid number so no conversion for you...\n')


while True:
    days = input('Enter no of days and I will convert it to minutes..\n\n')
    if days.isdigit():
        days = int(days)
        calculate_to_units(days)

    if days.lower() == "exit":
        print(f'Bye👋👋👋..\n')
        break'''

# =====================================================================================
# =====================================================================================
#
#
# =====================================================================================
'''
def calculate_to_units(days):
    return f'{days} {units} to minutes is: {days * minutes} minutes.\n'


def validate_and_execute(user_days):
    if user_days.isdigit():
        user_days = int(user_days)
        if user_days > 0:
            print(calculate_to_units(user_days))
        elif user_days == 0:
            print(f'You entered a Zero so no conversion for you....\n')
        elif user_days < 0:
            print(f'You entered a Negative Number..Don\'t ruin my program.../n')
    else:
        print(f'Only Enter a valid number of days..\n')


while True:
    user_days = input(
        'Enter no of days and I will convert it to minutes..\n\n')
    if user_days.lower() == "exit":
        print(f'Bye👋👋👋..\n')
        break
    validate_and_execute(user_days)

'''

# =====================================================================================
# =====================================================================================
#
#
# =====================================================================================

# Lists in Action
'''

def calculate_to_units(days):
    return f'{days} {units} to minutes is: {days * minutes} minutes.\n'


def validate_and_execute(user_days):
    user_days = user_days.split(",")
    user_days = [days.strip() for days in user_days]
    # user_days = [int(days) for days in user_days]
    try:
        for days in user_days:
            if days.isdigit():
                days = int(days)
                if days > 0:
                    print(calculate_to_units(days))
                elif days == 0:
                    print(f'You entered a Zero so no conversion for you....')
                elif days < 0:
                    print(f'You entered a Negative Number..Don\'t ruin my program...')
            else:
                print(f'Only Enter a valid number of days..')
    except ValueError:
        print(f'Only Enter a valid number of days..')


while True:
    user_days = input(
        'Enter no of days separated by comma(,) and I will convert it to minutes..\n\n')
    if user_days.lower() == "exit":
        print(f'Bye👋👋👋..\n')
        break
    validate_and_execute(user_days)

'''
# =====================================================================================
# =====================================================================================
#
#
# =====================================================================================

# Dictioanry in Action


def calculate_to_units(days, conversion_unit):
    if conversion_unit == 'hours':
        return f'{days} days to hours is: {days * 24} hours.\n'
    elif conversion_unit == 'minutes':
        return f'{days} days to minutes is: {days * 24 * 60} minutes.\n'
    elif conversion_unit == 'seconds':
        return f'{days} days to seconds is: {days * 24 * 3600} seconds.\n'
    else:
        return f'Invalid conversion unit..'


def validate_and_execute(user_days):
    user_days = user_days.split(":")
    user_days = [days.strip() for days in user_days]
    user_days_dict = {"days": user_days[0], 'unit': user_days[1]}

    try:
        user_days_input = int(user_days_dict['days'])
        if user_days_input > 0:
            print(calculate_to_units(user_days_input, user_days_dict['unit']))
        elif user_days_input == 0:
            print(f'You entered a Zero so no conversion for you....')
        elif user_days_input < 0:
            print(f'You entered a Negative Number..Don\'t ruin my program...')

    except ValueError:
        print(f'Only Enter a valid number of days..')


while True:
    user_days = input(
        'Enter no of days  and units separated by colon(:) and I will convert it to minutes..\n\n')
    if user_days.lower() == "exit":
        print(f'Bye👋👋👋..\n')
        break
    validate_and_execute(user_days)
