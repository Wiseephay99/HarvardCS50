print()
# Booleans
# Boolean values: True or False
# ********************************************************
# ********************************************************

is_True = True
is_false = False
print(is_True)
print(is_false)

# ********************************************************
print(5 > 4)
print(5 == 3)
print(5 != 3)

# Logical Operators
print((5 > 3 and 21 > 20))
print((5 > 3 or 21 > 20))
print(not (5 > 3))

#  and operator

# ********************************************************

# boolean in conditional statements
age = 20
if age >= 18:
    print('You are an adult')
else:
    print('You are a minor')

# ********************************************************

# boolean in loops
counter = 5
while counter > 0:
    print('Counter: ', counter)
    counter -= 1

#   combining boolean expressions
age = 25
is_employed = True
if age >= 16 and is_employed:
    print(f'You area elligible for a loan')
else:
    print(f'You are NOT elligible for a Loan!')

# ********************************************************

print()
print()

'''
Practice Question
1. Write a program that checks if a number is both greater than 10 and even. If it is, print "Valid number", otherwise, print "Invalid number."
2. Ask the user to enter two numbers and check if both numbers are greater than 100 using an and condition. Then, check if either of the two numbers is greater than 100 using an or condition.
3. Write a Python function that takes a year as input and returns True if it is a leap year, and False otherwise. A leap year is divisible by 4 but not divisible by
100, unless it is also divisible by 400.

'''
# Practice Question 1

num = int(input("Enter Number:      "))
if num >= 10 and num % 2 == 0:
    print('Valid Number!')
else:
    print('Invalid Number!')

print()

# ********************************************************
# ********************************************************

# Practice Question 2
user_num1 = int(input('Enter 1st number:    '))
user_num2 = int(input('Enter 2nd number:    '))
result = user_num1 + user_num2

if result > 100:
    print('Yes, Number is greater than 100\n')
else:
    print('Number is less than 100!\n')

print()

# ********************************************************
# ********************************************************

# Practice Question 3

year = int(input('Enter a year and I\'ll determine if it is LEAP year...\n\n'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('It is LEAP year..\n')
        else:
            print('NOT a LEAP year!\n')
    else:
        print('It is LEAP year..\n')
else:
    print(f'NOT a LEAP Year!\n')

# ********************************************************
# ********************************************************
