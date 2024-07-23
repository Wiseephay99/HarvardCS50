calculate_to_units = 24
name_of_units = 'hours'
def day_to_units(num_of_days):
    # conditional statements.. >=,  <=
    # print(num_of_days > 0) This is a  Boolean conditional
    if num_of_days > 0:
        return f'{num_of_days} days are {num_of_days * calculate_to_units} {name_of_units} \n'
    elif num_of_days == 0:
        return 'You entered a 0, please enter a valid number! \n'
    else:
        return 'You entered a negative value, so no conversion for you! \n'
    
def validate_and_excute():
    if user_input.isdigit():
        # isdigit filters string keyed in as input.
        user_input_number = float(user_input)
        calculated_value = day_to_units(user_input_number)
        print(calculated_value)
    else:
        print(f'Your inout is not a number. Dont ruin my program! \n ')

print()
user_input = input('Hey user, enter a number of days and I will convert it to Hours!\n')
validate_and_excute()


# More user Input validations