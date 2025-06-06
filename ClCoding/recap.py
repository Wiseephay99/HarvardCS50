# Creating a class, instance variables and methods...and calliing the class
import sys
from enum import Enum
import math
import random


class Person:
    def __init__(self, fname, sname, age):
        self.fnname = fname
        self.sname = sname
        self.age = age

    def display_person_details(self):
        print(
            f'\nFirst Name: {self.fnname} \nSecond Name: {self.sname} \nAge: {self.age} years old..\n')

    def update_name(self, fullname):
        self.fnname = fullname

# Inheritance


class Student(Person):
    def student_details(self, student_id, school_name):
        self.student_id = student_id
        self.school_name = school_name

    def display_student_info(self):
        print(
            f'Student Id: {self.student_id} School Name: {self.school_name}\n')


person1 = Person('Wise', 'Ephay', 24)
person1.display_person_details()
person1.update_name('Dave Gray')
person1.display_person_details()

student1 = Student('Brain', 'Gray', '23')
student1.display_person_details()

student1.student_details('001', 'Kagumo Boys')
student1.display_student_info()

# =====================================================================================
# =====================================================================================
# =====================================================================================


class Vehicle:
    make = 'Toyota'
    speed = 120

    def get_details(self):
        return f'\nThe Vehicle is {self.make} and has a spped of {self.speed}Km/hr...\n'


print(f'----------------------------------------------------------------------')
vehicle1 = Vehicle()
print(vehicle1.get_details())

# =====================================================================================
# =====================================================================================
# =====================================================================================

print(f'----------------------------------------------------------------------')

print(f'\n---------- Expense Tracker ----------\n')


def add_expenses(desc, amount):
    add_expenses.append({'description': desc, 'amount': amount})
    print(f'description: {desc} amount: {amount}\n')


user_expenses = input('Add Your expenses sepatared by fullcolon(:) ..\n\n')
user_expenses.split(":")
expenses = [expense.strip() for expense in user_expenses]

user_expenses = add_expenses(user_expenses[0], user_expenses[1])
print(expenses)
print(type(expenses))
sys.exit()

# =====================================================================================
# =====================================================================================
# =====================================================================================


def guess_number():

    total_guesses = 0
    correct_guesses = 0
    incorrect_guesses = 0
    out_of_range_guesses = 0
    invalid_guesses = 0

    print(f'\n------------------------------------------')
    print(f'Choose the 1st and 2nd range of numbers to guess from..\n')
    num1 = input(f'Enter 1st number:    ')
    num2 = input(f'Enter 2nd number:    ')

    try:
        num1 = int(num1)
        num2 = int(num2)
        rand_num = random.randint(num1, num2)
        while True:
            guess_num = input(
                f'\nGuess a random number btwn {num1} & {num2}:..\nQ to Quit..\n\n')
            if guess_num.lower() == 'q':
                print('Thanks for playing Guess Number..')
                print(f'Bye 👋👋👋')
                print(f'Exiting..')
                print(f'-----------------------\n')
            if guess_num.isdigit:
                guess_num = int(guess_num)

                def winner():

                    nonlocal correct_guesses
                    nonlocal incorrect_guesses
                    nonlocal total_guesses
                    nonlocal out_of_range_guesses
                    nonlocal invalid_guesses

                    total_guesses += 1
                    if guess_num < num1 or guess_num > num2:
                        out_of_range_guesses += 1
                        return f'\n{guess_num} is not in the range of {num1} and {num2}..\n'
                    if guess_num == rand_num:
                        correct_guesses += 1
                        print(f'\n------------------------------------------')
                        return f'Correct Guess ...Player Wins..\n'

                    elif guess_num != rand_num:
                        incorrect_guesses += 1
                        if guess_num > rand_num:
                            print(f'\n------------------------------------------')
                            return f'Too High..Try a lower Number..\n'
                        elif guess_num < rand_num:
                            print(f'\n------------------------------------------')
                            return f'\nToo Low...Try a Higher Number..\n'
                result = winner()
                print(result)
                print(f'------------------------------------------')
                print(f'Do you want to play again?  ')
                playagain = True
                playagain = input('Y to continue playing...\nQ to Quit..\n\n')
                while playagain:
                    if playagain in ['Y', 'Q']:
                        continue
                    else:
                        break
                if playagain.lower() == 'q':
                    print(f'\n------------------------------------------')
                    print(f'Total Guesses = {total_guesses}')
                    print(f'Correct Guesses = {correct_guesses}')
                    print(f'Incorrect Guesses = {incorrect_guesses}')
                    print(f'Out of range Guesses = {out_of_range_guesses}')
                    print(f'Invalid Guesses is: {invalid_guesses}..\n')
                    print(f'------------------------------------------')
                    print(f'Thanks for playing guess number..')
                    sys.exit(f'------------------------------------------\n')

            else:
                print(f'Guess a valid number only...\n')
    except ValueError:
        print(f'Only Enter a Number...\n')
        invalid_guesses += 1
    except Exception as e:
        print(f'An error occured: {e}\n')
        invalid_guesses += 1
    except KeyboardInterrupt:
        print(f'You have exited the game..')
        sys.exit(f'------------------------------------------\n')


guess_number()
