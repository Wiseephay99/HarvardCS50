calculate_to_units = 24
name_of_units = 'hours'
def day_to_units(num_of_days):
    return f'{num_of_days} days are {num_of_days * calculate_to_units} {name_of_units}'

print()
# user_days_input = int(input('Hey user, enter a number of days and I will convert it to Hours!\n'))
# user_days_input = int(input('Hey user, enter a number of days and I will convert it to Hours!\n'))
# alternative code: 
user_input = input('Hey user, enter a number of days and I will convert it to Hours!\n')
user_input_number = int(user_input)

#New Line character is represented as:  \n

calculated_value = day_to_units(user_input_number)
print(calculated_value)

# //function with return values


# km_to_meters = 1000
# def calculate_dist_to_meters(km):
#     print(f'{km} km conerted to meters is: {km_to_meters}')

# calculate_dist_to_meters(40)
# calculate_dist_to_meters(50)