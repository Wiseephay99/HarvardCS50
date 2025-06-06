print()

'''try:
    risky_code()
except ZeroDivisionError:
    print('You can\'t divide by zero')'''
# ********************************************************

try:
    result = 10/0
except ZeroDivisionError:
    print('You can\'t divide by zero')

print()

# ********************************************************

# Handling multiple exceptions
try:
    num = int(input('Enter a number; '))
    result = 10 / num
except ValueError:
    print('That is not a valid number\n')
except ZeroDivisionError:
    print('You can\'t divide by zero')

# ********************************************************

# Catching and exceptions

try:
    result = 10/0
except:
    print('An error occurrred')

#   Using else with try and except

# ********************************************************

try:
    num = int(input('Enter a number: '))
    result = 10 / num
except ZeroDivisionError:
    print('You can\'t divide by zero')
except ValueError:
    print('That is not a valid number..\n')
else:
    print('The result is: result')

# using finally
# finally is always excuted whether an exception occurs or  not

# ********************************************************

file = None  # Initialized the file variable to none

try:
    file = open('Output.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print('The file was nor found!..')
finally:
    if file:  # Only close the file if it was successfully opened
        file.close()
        print('The file has been closed.\n')

# ********************************************************

# raise an exception
# for example:
'''def check_age(age):
    if age < 18:
        raise ValueError('You must be at least18 years old.')
    return True

check_age(5)
'''
# ********************************************************


def check_age(age):
    if age < 18:
        raise ValueError('You must be at least 18 years old.')
    return True


try:
    check_age(5)
except ValueError as e:
    print(e)

# ********************************************************

# Accessing Exception Infromation
try:
    number = int(input('Enter a number:     '))
    result = 10 / number
except Exception as e:
    print(f'An error occurred..{e} \n')

# ********************************************************

'''
Practice Questions
1. Write a Python program that asks the user to input two numbers and divides the first number by the second. 
Use try-except to handle a division by zeroerror and print a user-friendly message.
2. Write a program that takes a number from the user and divides 100 by that number. 
Handle the following exceptions:
ValueError (if the Input is not a valid number).
ZeroDivisionError (if the user enters 0).
3. Create a Python function that raises an exception, and inside the except block, raise a new exception while maintaining the original exception context
(using raise new _exception from original_ exception).

'''
