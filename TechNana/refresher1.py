# 1 day to minutes  = no_of_day * 24 * 60
# 1 day to seconds =  no_of_day * 24 * 60 * 60
unit_type = 'minutes'
unit_type2 = 'seconds'
calculate_to_minutes = 24 * 60
calculate_to_seconds = 24 * 60 * 60

print()
print(f'20 days to minutes is: ' + str(50) + " seconds")
print(f'20 days to minutes is: {20 * 24 * 60}\n')
print(f'20 days converted to minutes is: {20 * calculate_to_minutes} {unit_type}')
print(f'35 days converted to minutes is: {35 * calculate_to_minutes} {unit_type}')
print(f'100 days converted to minutes is: {100 * calculate_to_minutes} {unit_type}')
print()
print(f'20 days converted to seconds is: {20 * calculate_to_seconds} {unit_type2}')
print(f'35 days converted to seconds is: {35 * calculate_to_seconds} {unit_type2}')
print(f'100 days converted to seconds is: {100 * calculate_to_seconds} {unit_type2} \n')
print()
print(f'================= Using Functions ===================')
'''def days_to_units(no_of_days, custom_message):      # Function
    print(f'{no_of_days} days converted to minutes is: {calculate_to_minutes} {unit_type}')
    print(f'{custom_message} \n')
    # print(f'All Good \n')

days_to_units(30, 'All Good')
days_to_units(40, 'Awesome')
days_to_units(50, 'Yes..All Work')
days_to_units(100, 'Very Cool')'''

def days_to_units(no_of_days):
    if no_of_days > 0:
        return f'{no_of_days} days converted to minutes is: {no_of_days * calculate_to_minutes} {unit_type}'
    elif no_of_days == 0:
        return f'You entered a {0}. Enter a positive number'
    else:
        return f'Please Enter a Valid Number only'

def calculate_to_units():
    user_input = input('Enter days to change to Minutes: ')
    if user_input.isdigit():
        user_input = int(user_input)
        calculated_input = days_to_units(user_input)
        print(calculated_input)
    else:
        print(f"Don't ruin my Program. Enter Number Only! ")

    # print(f'{custom_message} \n')
    # print(f'All Good \n')

# print(days_to_units(30) + '\n')
calculate_to_units()


