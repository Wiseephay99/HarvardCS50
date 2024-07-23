# days_to_hours = 24
# days_to_mins = days_to_hours*60
# days_to_sec = days_to_mins*60
# name_min = 'mins'
# name_sec = 'sec'
# name_hours = 'hours'

# # print()
# # print(f'110 days converted to {name_min} is {110*days_to_mins}')
# # print(f'500 days converted to {name_min} is {500*days_to_mins}')
# # print()

# def days_to_units(day, custom_message):
#     print(f'{day} days converted to {name_min} is {day*days_to_mins}')
#     print(custom_message)
# def check_scope():
#     # Global or Local Variable
#     print(days_to_mins)

    
# print()
# days_to_units(20, 'All Good!')
# days_to_units(40, 'How is This going to happen?')
# days_to_units(60, 'Try This')
# print()

# input_day = input('Enter the No. of days you want to convert to minutes? ')
# if input_day.isdigit():
#     pass
# else:
#     print(f"You did not enter a Number! Don't ruin my program!!")
   
   
    
# days_to_hours = 24
# days_to_mins = days_to_hours*60
# days_to_sec = days_to_mins*60
# name_min = 'mins'
# name_sec = 'sec'
# name_hours = 'hours'
# # 10 days =  days_to_min*10
# def days_to_units(day):
#         return f'{day} days converted to {name_min} is: {day*days_to_mins}'
    
# def check_and_validate():
#     try:
#         # if user_input.isdigit():
#         user_input_num = float(user_input)
#         if user_input_num > 0:
#             calculate_value = days_to_units(user_input_num)
#             print(calculate_value)
#         elif user_input_num == 0:
#             print(f'You have entered  zero so no conversion for You!')
#         else:
#             print(f'You have entered a negative number...Converting positive numbers only!' )
#     except:
#         print(f"You did not enter a number...Please Enter a Valid Number!") 
# print()
# user_input = ""
# while user_input != 'exit':
#     user_input = input('Enter the No. of Days you want to convert to hours?:   ')
#     check_and_validate()

days_to_seconds = 24*60*60
# function declaration
def calculate_days_to_mins(days):
    return f'{days} converted to minutes is {days*days_to_seconds}\n'

# function declaration
def check_and_calculate():
    # ry catch block
    try:
        # if user_num.isdigit():
        #Nested if elif else statement
            user_data = float(user_num)
            if user_data > 0:
                new_value = calculate_days_to_mins(user_data)
                print(new_value)
            elif user_data == 0:
                print(f'You entered a Zero(0), So no convertion for You! \n')
            else:
                print(f'You entered a Negative Number , Enter a positive Number! \n')
        # else:
        #     print(f'Enter a Valid Number. \n')
    except:
        print(f'Only enter a Valid Number. \n')
        
print()
user_num = ""
# While Loop
while user_num != "exit":
    user_num = input('Enter days to convert  to seconds: ')
    # Function Call
    check_and_calculate()
    
