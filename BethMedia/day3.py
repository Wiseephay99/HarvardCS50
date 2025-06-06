print()

#   While Loops
#   while condition:
    #code to be excuted
#    simple while loop
#************************************************************
'''
counter = 1
while counter <= 5:
    print('Counter is:', counter)
    # counter += 1
    counter += 2
print()'''
#************************************************************
'''counter = 0
while counter < 5:
    print('Counter is:', counter)
    # print(counter)
    counter += 1
print()'''
#************************************************************
  
'''print()
trial = 5
while trial > 0:
    print(f'The trial is: ', trial)
    trial = trial - 1
print()'''
#************************************************************

'''print()
x = 0
while x < 10:
    print(x)
    x = x + 1
print()
'''
#************************************************************
'''
print()
x = 0
while True:
    if x == 5:
        break
    print(x)
    x = x + 1
print()'''
#************************************************************

#    user input with while loop
###########################################################################
###########################################################################
'''response = ""
while response != "yes":
    response = input("Do you want to exit? Type 'Yes' to exit: ")
print('Goodbye!')

###########################################################################
###########################################################################

# Infinite Lopp with break
while True:
    command = input("Enter a command (type 'exit' to quit):     ")
    if command == "exit":
        print('Exiting the program...')
        break
    print('You entered:', command) '''

###########################################################################
###########################################################################

'''playagain = True
while playagain == True:
    response = input('Do you want to playagain?..\nyes to continu..\nq to quit...\n\n')
    if response.lower() == 'yes':
        print(f'Welcome to arcade game..')
        #  do something here
        break
    elif response.lower() == "q":
        print(f'Bye!')
        playagain = False
    else:
        print(f'Invalid Choice!')
        continue
else:
    print(f'Bye@!!!')'''
    
#   Avoid Infinite loop
'''number = 5
while number > 0:
    print(number)
    number -= 1'''
    
#   Using a continue statement
'''
counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue # Skips when the counter is 3
    print('Counter is:', counter)'''

'''
Practice Questions
Write a program that prints a countdown from 10 to 1, then prints "Liftoff!" after the countdown is complete.
Write a program that generates a secret number between 1 and 10. The user has to guess the number, 
and the program should keep asking until they guess it correctly.
Write a program that keeps asking the user to enter positive numbers. The program should stop 
when the user enters a negative number and then print the sum of all the positive numbers entered.


'''
#************************************************************
'''
print(f'Program 1')
print()
counter = 10
while counter > 0:
    print('Counter: ', counter)
    counter -= 1
print('Liftoff!!\n\n')'''

#************************************************************

'''print(f'Program 2')
import random
secret_number = random.randint(1,10)
while True:
    user_guess_number = int(input('Guess a random number bewtween 1 and 10?     '))
    if user_guess_number != secret_number:
        continue
    else:
        print(f'Correct Guess!!')
        break
print(f'Bye!\n')'''

#************************************************************
'''total_sum = 0
while True:
    num = int(input("Enter a positive number (negative number to stop): "))
    if num < 0:
        break
    total_sum += num
print(f"Total sum of all positive numbers: {total_sum}")'''
#************************************************************
total_even_numbers = 0
while True:
    even_num = input('Enter an even number (Q to Quit..)..  ')
    if even_num.lower() == 'q':
        print('Exiting!..\n')
        break
    else:
        even_num = int(even_num)
        if even_num % 2 == 0:
            total_even_numbers = total_even_numbers + even_num
            continue
        elif even_num % 2 != 0:
            print(f'{even_num} is not an even number..\n')
        
print(f'\nThe total sum of all even numbers is {total_even_numbers}\n')
#************************************************************


        

