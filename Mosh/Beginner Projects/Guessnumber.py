import random

# Project 2
# Word guessing gaess
# # Guess the number between 1 and 100:
# please enter a valid number

'''
rand_comp_num = random.randint(1, 100)
playing = True
while playing:
    print()
    user_num = input('Guess a number between 1 and 100...\n')
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num == rand_comp_num:
            print(
                f'Correct Guess... \nSecret Computer number is {rand_comp_num}..\n')
            break
        elif user_num > rand_comp_num:
            print(f'Too high')
        elif user_num < rand_comp_num:
            print(f'Too Low!')
    else:
        print('Invalid Number...\n')

'''

# Solution
# Generate a random number
# Loop
#      Ask the user to make a guess
#      if not a valid number
#           print an error
#      if number < guess


number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input('\nGuess the number beween 1 and 100..\n'))
        if guess < number_to_guess:
            print('Too Low')
        elif guess > number_to_guess:
            print('Too High')
        else:
            print('Congradulations you guessed the nummber')
            break

    except ValueError:
        print('Enter a valid number')
