# Fundamnentals of programming

print()
age = 22
if age >=18:
    print(f'Elligible...')
else:
    print(f'NOT Elligible..')
print('Done')
print()

# ========================================
print(f'==============================')

age = 23
if age >= 18:
    message = f'Elligle..\n'
else:
    message = f'Not Elligible...\n'
print(message)
print()

# ========================================
# Tenary Operators
print(f'==============================')
age = 24
message = "Elligle.." if age >= 18 else 'NOT Elligible..'
print(message)

# ========================================
# aPP FOR PROCESSING LOANS

high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print(f'You Qualify for a loan...')
else:
    print(f'You don\'t qualify for a loan...')

# NOT OPERATOR
if not student:
    print('Elligible')
else:
    print(f'Not Eliible')

# ==================================================
  
if (high_income and good_credit) and not student:
    print('Elligible..\n')
else:
    print(f'Not Ellible....\n')
    
# It is a short circuit 
#   chaning comparison operators
# age should be btween 18 and 65

age = 22
if age >= 18 and age < 65:
    print('Elligible...')

# alternative way to write it is...
age = 22
if 18 <= age < 65:
    print('Elligible...')

# ==================================================

if 10 == "10":
    print('a')
elif 'bag' > 'apple' and 'bag' > "cat":
    print('b')
else:
    print('c')
    
# ==================================================
# for loops
message = 'Attempt'
'''
for number in range(3):
    print(message, number)'''
    
'''for number in range(3):
    print(message, number + 1)'''
    
'''for number in range(3):
    print(message, (number * ('.')))'''

print()

for number in range (5):
    print(f'Trial Attempt: {number + 1}{(number + 1) * ('.')}')

print()

for msg in range(4):
    print(msg)
    if message == True:
        break 
else:
    print('attempted 5 times but...')

print()

# ==================================================
# nested for loops

for x in range(5):
    for y in range(3):
        print(f'{x}, {y}')
        
print()

# ==================================================
# while loops

# program to display even numbers beween 1 and 10
print()
total_even_num = 0
for num in range(1, 10):
    if num % 2 == 0:
        total_even_num += 1
        print(num)
else:
    print(f'We have {total_even_num} even numbers') 

print()

# ==================================================
# Functions
def greet():
    print('Hi there')
    print('Welcome Aboard')
    
greet()
   
print()
# ==================================================

def greet2(first_name, last_name):
    print(f'Hi, {first_name} {last_name}')
    print('Welcome Aboard')
    
greet2('Mosh', 'Hamdani')

# ==================================================

# # There are two types of functions
# 1. Functions that persform a task
# 2. Functions that have a return value 

def greet3(name):
    print(f'Hi {name}')

greet3('Wise')

round(1.9)

def get_greeting(name):
    return f'Hi {name}..\n'

message = get_greeting('Wise')
print(get_greeting('Wise'))
print()
print(message)

file = open("content.txt", 'w')
file.write(message)

# ==================================================
# Keyword Arguements

def increment(number, by=1):
    return number + by
print(increment(3, 6))
print()


# ==================================================
# *args 

def multiply(*numbers):
    return numbers

print(multiply(2,4,5,67,7))

# ==================================================

def multiply2(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
        
print(multiply2(2,4,5,67,7))

print()