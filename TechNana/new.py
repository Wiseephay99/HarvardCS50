
print()
unit_name = 'hours'
days_to_hours = 24
def convert_days_to_hours(days):
        return f'{days} converted to {unit_name} is: {days * days_to_hours} {unit_name}\n'

def validation_and_execution():
    try:

        user_choice_number = int(user_choice)
        if user_choice_number > 0:
                print(convert_days_to_hours(user_choice_number))
        elif user_choice_number == 0:
                return f'You entered a {user_choice_number}, Please enter a valid number\n'
        else:
            print('You entered a negative number, no conversion for you!\n')
    except ValueError:
        print("Your input is not a number. Don't ruin the program!\n")

user_choice = " "

# while True:  This option runs indefinitely
while user_choice != 'exit':
    user_choice = input("Enter days to convert to Hours: ")
    validation_and_execution()


