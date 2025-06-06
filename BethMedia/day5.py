print()

'''
Day 5 of Programming..
Objective.,, Write a program that selects a number bween 1 and 100
and the user must guess the number
Steps..
Import the random module
Generate a random number using random randint()
Use a while loop to allow the user multiple attempts to Guess the number..
Provide a feedback like 'Too High' or 'Too Low..' after each attempt..

'''
#*******************************************************************
import random
print(f'       Simple Number Guessing Game!!🔢        ')
random_num = random.randint(1, 100)
while True:
    guess_num = int(input('Guess a random number between 1 and 100:     '))
    if guess_num == random_num:
        print(f'Correct Guess')
        break
    elif guess_num != random_num:
        if guess_num > random_num:
            print(f'Top High..Guess a lower number..\n')
        elif guess_num < random_num:
            print(f'Top Low..Guess a Higher number..\n')
print(f'Bye!!')

#--------------------------------- Alternative Code -------------------
import random
number = random.randint(1, 100)
attempts= 0
while True:
    guess = int(input('Guess the Number (1-100)..       '))
    attempts += 1
    if guess < number:
        print('Too Low')
    elif guess > number:
        print('Too High!!')
    else:
        print(f'Congrats! You guessed it in {attempts} attempts.\n')
        break
#*******************************************************************