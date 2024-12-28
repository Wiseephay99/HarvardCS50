# Leaning Python with Tech with Nana

print()
print('20 days are ' + str(50) +  'minutes')
print(f'20 days are {50} minutes')
print(f'20 days are {20 * 24 * 60} minutes')  # Formatting string
# Variables
print(f'20 days are {35 * 24 * 60} minutes')  
print(f'50 days are {50 * 24 * 60} minutes')  
print(f'110 days are {110 * 24 * 60} minutes')  
print(f'20 days are {20 * 24 * 60} minutes')  
# Calculating to seconds
print(f'20 days are {20 * 24 * 60 * 60} seconds')  

days_to_seonds = 24 * 60 * 60
days_to_minutes = 24 * 60 * 60
calculation_to_seconds = 24 * 60 * 60
# Take care of reserved words
print(f'20 days are {20 * calculation_to_seconds} seconds')  
print(f'35 days are {35 * calculation_to_seconds} seconds')  
print(f'50 days are {50 * calculation_to_seconds} seconds')  
print(f'110 days are {110 * calculation_to_seconds} seconds')  

calculation_to_units = 24 * 60 * 60
name_of_unit = 'seconds'
print(f'20 days are {20 * calculation_to_units} {name_of_unit}')  
print(f'35 days are {35 * calculation_to_units} {name_of_unit}')  
name_of_unit = 'hours'
calculation_to_units = 24
print(f'20 days are {20 * calculation_to_units} {name_of_unit}')  
print(f'35 days are {35 * calculation_to_units} {name_of_unit}')  

# use descriptive variable names

# Functions To avoid duplication
# functions are block of code that do repetitve tasks

print()
print(f'***** ====== Functions  ======= ******\n')


name_of_unit = 'hours'
calculation_to_units = 24

def days_to_units():
    print(f'20 days are {20 * calculation_to_units} {name_of_unit}')  
    print(f'All Good\n')
    
days_to_units() # Calling the function

print(f'***** ====== Functions with Parameters  ======= ******\n')

# Function paratameters
def days_to_units(num_of_days, custom_message):
    print(f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}')
    print(custom_message)
# days_to_units()  # Raises an error
days_to_units(20, 'Tech Wise')
days_to_units(35, "Awesome")
days_to_units(50, "Looks Good")
days_to_units(110, "Finally")
print()

print()
print(f'***** ======  Scope of Variables ======= ******\n')
# Scope
# Local Scope and Global Scope of variables

def scope_check(num_of_days):
    my_var = 'Variable Inside a Function'
    print(name_of_unit)
    print(num_of_days)    
    print(my_var)
scope_check(20)

# ====================================================================== 
# ====================================================================== 
print()
print(f'***** ======  User Input======= ******\n')
name_of_unit = 'hours'
calculation_to_units = 24
# Built in functions are provided bt the python itself
def days_to_units(num_of_days):
    print(f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}')  
    
my_var = days_to_units(20)
user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
# Use of a new line character to go to next line....makes it more user friendly

print(user_input)
'''print(f'==================================**********============================')

# Function with return value
name_of_unit = 'hours'
calculation_to_units = 24
# Built in functions are provided bt the python itself
def days_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}'  
    
my_var = days_to_units(20)
print(my_var)
# user_input = input('Hey User, Enter a number of days and I will convert it to hours! \n')
# Use of a new line character to go to next line....makes it more user friendly

print(user_input)'''

# Function with return value














