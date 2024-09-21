# 140 Basic Python Pograms
print()
##########################################################################
# 1. python prgram to print hello world

'''print('Hello World')'''

##########################################################################

'''#2. python program to do arithemetic operations addition and division
num1= float(input('Enter a number :'))
num2= float(input('Enter a second :'))
sum_result = num1 + num2
difference_result = num1 - num2
multiplication_result = num1 * num2
print(f'The sum of {num1} and {num2} is : {sum_result}')
print(f'The subraction of {num1} and {num2} is : {difference_result}')
print(f'The multiplication of {num1} and {num2} is : {multiplication_result}')
print()
# Division
print(f'=========Division=============')
num3= float(input('Enter a number :'))
num4= float(input('Enter another :'))
if num4 == 0:
    print(f'Error: Division by zero is not allowed')
else:
    division_result = num3 / num4
    print(f'The Division of {num3/num4} = {division_result} ')
print()'''

##########################################################################

'''# 3. Python program to calculate the Area of a Triangle
base = float(input('Enter the base of the Triangle: '))
height = float(input('Enter the height of the Triangle: '))
area_of_triangle = 0.5 * base * height
print(f'The area of the Traingle is: {area_of_triangle} cm')'''

##########################################################################
'''# Python program to swap two variables
a = input('Enter the first value of the variable: ')
b = input('Enter the first value of the variable: ')
print(f'The original variables are: {a} and {b}')
# swapping the two variables
c = a
a = b
b = c
print(f'The swapped values are: {a} and {b}')
print()'''
##########################################################################
'''# Python program to generate a random number
import random
print(f'Random Number: {random.randint(1,100)}')
print()'''
##########################################################################
'''# Python program to convert kilometers to miles
kilometers = float(input('Enter the Kilometers you want to convert to meter: '))
# 1mile = 1000 km
# print(f'{kilometers} km Converted to miles is {kilometers / 1000} miles.')
# print()
# correction
# Coversion Factor: 1km = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f'{kilometers} kilometers is equal to {miles} miles')
print'''
##########################################################################
'''#Python program to convert degrees celcius to fahrnheit
celcius = float(input('Enter the celcius temp to convert to Fahrenheit: '))
# farhrenheit = (0°C × 9/5) + 32
farhrenheit =  (celcius * (9/5)) + 32
print(f'{celcius}°C converted to Fahrenheit is: {farhrenheit} F')
print()'''
##########################################################################
'''#python program to display a calendar
import calendar
year = int(input('Enter Year: '))
month = int(input('Enter Month: '))
print()
cal = calendar.month(year, month)
print(cal)
print()'''
##########################################################################
'''# Python pprogram to swap two variables without a third variable or temp var
a = int(input('Enter a first digit: '))
b = int(input('Enter a second digit: '))
print(f'Original Values are: {a} and {b}')
a, b = b, a
print(f'Swapped values are : {a} and {b}')
print()'''
##########################################################################
'''# Python program to check if a Number is Positive, Negative or Zero
number = float(input('Enter any number: '))
if number > 0:
    print(f'{number} is a positive number')
elif number == 0:
    print(f'{number} is Zero')
else:
    print(f'{number} is negative')
print()'''
'''
num = input('Enter a number: ')
if num.isdigit():
    num = float(num)
    if num == 0:
        print(f'{num} is zero')
    elif num > 0:
        print(f'{num} is positive')
    elif num < 0:
        print(f'{num} s negative.')
else:
    print(f'Enter Number not Text!')'''
##########################################################################
# Program to check if a number is Odd or Even
'''
number = float(input('Enter a Number: '))
if number % 2 == 0:
    print(f'{number} is even.')
else:
    print(f'{number} is odd')
print()
trials = 5
while trials > 0:
    number = input('Enter a Number: ')
    if number.isdigit():    
        number = int(number)
        if number % 2 == 0:
            trials = trials - 1
            print(f'{number} is even.')
            print(f'You have {trials} trials remaining!')
        else:
            trails = trials - 1
            print(f'{number} is odd')
            print(f'You have {trials} trials remaining!')
            print()
    else:
        print(f'Only Enter a Number!')
        break
if trials == 0:
    print(f'You have no trails left.. Exiting! Goodbye!') 
'''

'''
    num = input('Enter any number to check if its odd or even:')
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            pass
        else:
            exit
        
        
    else:
        print(f'Only enter a number!')
        exit

'''

##########################################################################
'''import random
print(random.randint(1, 100))'''
##########################################################################
'''
# program to check if a number is odd or even
trials = 5
while trials > 0:
    user_num = input(f'Enter a number to check if its Oddor Even: ')
    if user_num.isdigit():
        user_num = int(user_num)
        if user_num % 2 == 0:
            trials = trials - 1
            print(f'{user_num} is an Even number')
            print(f'You have {trials} trials remaining')
        else:
            trials = trials - 1
            print(f'{user_num} is an Odd number.')
            print(f'You have {trials} trials remaining')

    else:
        print('Only Enter a Number!')
        break
if user_num == 0:
    print(f'You ran out of Options! GoodBye! Exiting!')
'''

##########################################################################
# Python program to check if a year is leap year
year = input('Enter a Year to check if it\'s a Leap Year? ')
if year.isdigit():
    year = int(year)
    if (year % 4 == 0) and (year % 100 == 0):
        print(f'{year} is a leap'.format(year))
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f'{year} ia a leap year'.format(year))
    else:
        print(f'{year} is not a leap year!')
    pass
else:
    print(f'Only Enter a Number'.format(year))


##########################################################################




##########################################################################



##########################################################################



##########################################################################


##########################################################################
