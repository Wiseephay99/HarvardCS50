import random

# Project 1
# Pythn dice_rolling game
'''
Loop
    If user enteres y
        Generate two random numbers
        print them 
    If user enteres n
        Print thank you message
        Terminate
    Else:
        print invalid choice
        
'''

playing = True
while playing:
    choice = input('Roll the dice? (y/n):   ')
    if choice.lower() == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1},{die2})')
    elif choice == "n":
        print('Thanks for playing...\n')
        break
    else:
        print(f'Invalid Choice....\n')
