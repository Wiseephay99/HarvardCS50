
print()
'''name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    # Conditional IF/ELSE/IF-ELSE statement
    print(num_of_days > 0)
    conditional_check = num_of_days > 0
    print(type(conditional_check))
    if num_of_days > 0:
        return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'
    elif num_of_days == 0:
        return f'You entered a {num_of_days}. Enter Positive Numbers only!'
    else:
        return f'You entered a Negative Value, so no conversion for you!'

user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
user_input_number = int(user_input) # Casting
calculated_value = days_to_units(int(user_input_number))
print(calculated_value)'''
# Above when a user enters a text or float the program crashes

# More user input Validation
# ======================================================================
# ======================================================================


'''print(f' ============== More User Input Validation ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    # Conditional IF/ELSE/IF-ELSE statement
    if num_of_days > 0:
        return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'
    elif num_of_days == 0:
        return f'You entered a {num_of_days}. Enter Positive Numbers only!'
    # else:
    #     return f'You entered a Negative Value, so no conversion for you!'

user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
if user_input.isdigit():
    user_input_number = int(user_input) # Casting
    calculated_value = days_to_units(int(user_input_number))
    print(calculated_value)
else:
    print(f"Your input is not a number, Don't ruin my program")'''


# ======================================================================
# ======================================================================
'''
# Cleaning up our code

print(f' ============== More User Input Validation ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    # Conditional IF/ELSE/IF-ELSE statement
    if num_of_days > 0:
        return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'
    elif num_of_days == 0:
        return f'You entered a {num_of_days}. Enter Positive Numbers only!'
    # else:
    #     return f'You entered a Negative Value, so no conversion for you!'

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)  # Casting
        calculated_value = days_to_units(int(user_input_number))
        print(calculated_value)
    else:
        print(f"Your input is not a number, Don't ruin my program")

user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
validate_and_execute()'''


# adding it to two functions....Nested if statements
# Adding validation in from two places to one place
# ======================================================================
# ======================================================================

# Cleaning up our code
'''
print(f' ============== More User Input Validation ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:# Casting
            calculated_value = days_to_units(int(user_input_number))
            print(calculated_value)
        elif user_input_number == 0:
            print(f'You entered a {user_input_number}. Enter Positive Numbers only!')
    else:
        print(f"Your input is not a number, Don't ruin my program")

user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
validate_and_execute()'''


# ======================================================================
# ======================================================================

''''print(f' ============== Error Handling with Try Except ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'


def validate_and_execute():
    try:
            user_input_number = int(user_input)
            if user_input_number > 0:  # Casting
                calculated_value = days_to_units(int(user_input_number))
                print(calculated_value)
            elif user_input_number == 0:
                print(f'You entered a {user_input_number}. Enter Positive Numbers only!')
            else:
                print(f'You entered a negative number, please enter a valid positive number')
    except ValueError:
            print(f"Your input is not a Valid number, Don't ruin my program")



user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
validate_and_execute()'''

'''# ======================================================================
# ======================================================================
print()
print(f' =================== While Loops ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'


def validate_and_execute():
        try:
                user_input_number = int(user_input)
                if user_input_number > 0:  # Casting
                    calculated_value = days_to_units(int(user_input_number))
                    print(calculated_value)
                elif user_input_number == 0:
                    print(f'You entered a {user_input_number}. Enter Positive Numbers only!')
                else:
                    print(f'You entered a negative number, please enter a valid positive number')
        except ValueError:
                print(f"Your input is not a Valid number, Don't ruin my program")


while True:
    user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
    validate_and_execute()
'''


'''# ======================================================================
# ======================================================================
print()
print(f' =================== While Loops ================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'


def validate_and_execute():
        try:
                user_input_number = int(user_input)
                if user_input_number > 0:  # Casting
                    calculated_value = days_to_units(int(user_input_number))
                    print(calculated_value)
                elif user_input_number == 0:
                    print(f'You entered a {user_input_number}. Enter Positive Numbers only!')
                else:
                    print(f'You entered a negative number, please enter a valid positive number')
        except ValueError:
                print(f"Your input is not a Valid number, Don't ruin my program")

user_input = ''
while user_input != "exit":
    user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
    validate_and_execute()'''

'''# ======================================================================
# ======================================================================
print()
print(f' =================== While Loops & For Loops & Lists ==================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'


def validate_and_execute():
        try:
                user_input_number = int(user_input)
                if user_input_number > 0:  # Casting
                    calculated_value = days_to_units(int(user_input_number))
                    print(calculated_value)
                elif user_input_number == 0:
                    print(f'You entered a {user_input_number}. Enter Positive Numbers only!')
                else:
                    print(f'You entered a negative number, please enter a valid positive number')
        except ValueError:
                print(f"Your input is not a Valid number, Don't ruin my program")

user_input = ''
while user_input != "exit":
    user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
    validate_and_execute()'''

''''# ======================================================================
# ======================================================================
print()
print(f' =================== While Loops & For Loops & Lists ==================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'

def validate_and_execute():
        try:
                user_input_number = int(num_of_days_element)
                # we want to do conversion only for positive integers
                if user_input_number > 0:  # Casting
                    calculated_value = days_to_units(user_input_number)
                    print(calculated_value)
                elif user_input_number == 0:
                    print(f'You entered a {user_input_number}. Enter Positive Numbers only!\n')
                else:
                    print(f'You entered a negative number, please enter a valid positive number\n')
        except ValueError:
                print(f"Your input is not a Valid number, Don't ruin my program\n")

# "string example" , 10, 19.99, True , False, [10, 15, 40, 100]

user_input = ''
while user_input != "exit":
    user_input = input('Hey User, Enter a number of days as comma separated list and I will convert it to hours! \n')
    for num_of_days_element in user_input.split(","):
        validate_and_execute()
        
        
        
#        ============== END OF WHILE AND FOR LOOP ============== '''

# Sets does not allow multiple values
# We can use Dictionaries in our program to Allow user to input:
    # 1. number of days e.g 50
    # 2.  unit to convert to....eg hours or minutes.....


# Set

# ======================================================================
# ======================================================================
print()
print(f' =================== While Loops & For Loops & Lists ==================')
name_of_unit = 'hours'
calculation_to_units = 24
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'

def validate_and_execute():
        try:
                user_input_number = int(num_of_days_element)
                # we want to do conversion only for positive integers
                if user_input_number > 0:  # Casting
                    calculated_value = days_to_units(user_input_number)
                    print(calculated_value)
                elif user_input_number == 0:
                    print(f'You entered a {user_input_number}. Enter Positive Numbers only!\n')
                else:
                    print(f'You entered a negative number, please enter a valid positive number\n')
        except ValueError:
                print(f"Your input is not a Valid number, Don't ruin my program\n")

# "string example" , 10, 19.99, True , False, [10, 15, 40, 100]

user_input = ''
while user_input != "exit":
    user_input = input('Hey User, Enter a number of days as comma separated list and I will convert it to hours! \n')
    list_of_days = user_input.split(", ")

    # for num_of_days_element in user_input.split(", "):
    for num_of_days_element in set(list_of_days):
        validate_and_execute()

# Sets does not allow multiple values
# We can use Dictionaries in our program to Allow user to input:
    # 1. number of days e.g 50
    # 2.  unit to convert to....eg hours or minutes.....








