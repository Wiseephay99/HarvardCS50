calculate_to_units = 24
name_of_units = 'hours'
def day_to_units(num_of_days):
    print(f'{num_of_days} days are {num_of_days * calculate_to_units} {name_of_units}')

print()
user_days_input = int(input('Hey user, enter a number of days and I will convert it to Hours!\n'))