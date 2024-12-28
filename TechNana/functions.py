calculate_hours = 24
unit_name = 'hours'
# Function to convert days to units
def days_to_units(num_of_days, custom_message):
    print(f'{num_of_days} days are {20 * calculate_hours} {unit_name}')
    print(custom_message)
    
# Function to check on Scope...Global or local scope
def scope_check(num_days):
    # This is a local scope therefore cannot be accessed Locally
    print(calculate_hours)
    # This is a local scope therefore cannot be accessed Locally
    # print(num_of_days) 
    # This is a scope created and thus can be accessed globally
    print(num_days) 
    # You can created a varible inside a function
    my_var = 'TechWithNana'
    print(my_var)
    
    
days_to_units(20, 'Awesome!')
days_to_units(35, 'Looks Good')
days_to_units(50, 'This is the way, ')
days_to_units(110, 'Okay Fine')
print()
scope_check(20)