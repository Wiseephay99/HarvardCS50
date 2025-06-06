print()

#   Input Statements
# variable = input('prompts for the user: ')


'''name = input('Enter your name: ')
print('Hello, ' + name + "!\n")
#   convert input to other types
age = input('How old are you? ')
age = int(age)
print('You are ', age , 'years old\n')
print(name, 'you will be ' + str(age + 1) + ' years old next years\n')

#   Float input 

height =  float(input('Enter your height in meteres: '))
print('Your height is ' + str(height) + " meters.\n")

#   Using multiple input statements

name = input('Enter your name:  ')
age = int(input('Enter your age:    '))
height = float(input('Enter  your height in meteres:    '))
city = input('Enter your city   ')

print(f'\n{name} is {age} years old and {height} meters tall and lives in {city}\n')'''

'''
Practice Questions
1. Basic Input: Write a program that asks the user for their favorite color and prints a message using the input.
2. Sum of Two Numbers: Write a program that asks the user for two numbers, adds them together, and prints the result.
3. Age in 10 Years Write a program that asks for the user's current age and prints how old they will be in 10 years.
'''
favourite_color = input('Enter you favourite color:    ')
print(f'\nYour Favourite color is: {favourite_color}')
print(f'\nEnter two numbers I will add them together..\n')
num1 = int(input('Enter 1st Number:     '))
num2 = int(input('Enter 2nd Number:     '))
print(f'\nThe sum of ' , num1 , 'and ', num2, ' is: ', str(num1 + num2), '.\n')
user_age= int(input('What is your current age?   '))
print('\nYour age in 10 years will be; ', str(user_age + 10), ' years old.\n')
print('In 10 years time you will be..', str(user_age + 10), 'years old.\n')