days_to_hours = 24
days_to_mins = days_to_hours*60
days_to_sec = days_to_mins*60
name_min = 'mins'
name_sec = 'sec'
name_hours = 'hours'

# print()
# print(f'110 days converted to {name_min} is {110*days_to_mins}')
# print(f'500 days converted to {name_min} is {500*days_to_mins}')
# print()

def days_to_units(day, custom_message):
    print(f'{day} days converted to {name_min} is {day*days_to_mins}')
    print(custom_message)
def check_scope():
    # Global or Local Variable
    print(days_to_mins)

    
print()
days_to_units(20, 'All Good!')
days_to_units(40, 'How is This going to happen?')
days_to_units(60, 'Try This')
print()