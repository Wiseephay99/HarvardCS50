print()
print("Hello Mosh! 😸")
print("---------------------")
print("*" * 10)

print()

x = 1
y = 2

# Jython = Java
# IronPython  = c# (csharp)
# Pypy = "subset of python"

'''what is an  expressooion  = a piece of code that produces a result
    what is a syntax error = an error in the structure of the code that prevents it from being parsed and executed
what does a linter do = check for errors in our code '''

students_count = 1000
print(students_count)
print()

rating = 4.99
is_published = False
course_name = "python Programming"

'''
    1. variables...are meaningful and descriptive
    2. lowercase letters for varibles
    3. Underscore to seprate multiple words
    4. space around an eual sign
'''

# Strings
course = "Python Programming"
message = """
Hi John,

This is Mosh from codewithmosh.com 

Blah 
"""

# Function is a reuseable piece of code that does a piece of work and can be reused

print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print(f'========================')
# Escape Sequences
print()
course  = 'Ptyhon \'Programming\' '
print(course)

print(f'========================')

# This is a comment
# Escape sequences
#\"
#\'
#\
#\n

print()

first = 'Mosh'
last = 'Hamadani'

full = first + " " + last
print(full)
print()
# Format strings

first = 'wise'
last = 'Ephay'
full = f"{first}  {last}"
print(full)
print()

print(f'========================')

course = 'Python Programming'
# string methods
# Evertyhong in function is a object
capital_courses = course.upper()
print()
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())

print()
print(course.rstrip())
print(course.lstrip())
print(course.find('Pro'))
print(course.replace('P', 'j'))
print("pro" in course) # An Expression that either return true or False
print("swift" not in course)


'''Numbers'''
# Integers, Floats, Complex, 
x = 1
x = 1.1
x = 1 + 2j # a + b

print(10+3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Argumeneted assignment operator
x = 10
x = x + 3
x += 3

# Usefull functions to work with numbers
print(round(2.9))
print(abs(-2.9))

import math

print(math.ceil(2.2))


# x = input('X:   ')
# x = int(x)
# y = x + 1
# print(y)
# print(type(x))
# print(f'x: {x}, y: {y}\n')


'''Conversion types
int(x)
float(x)
bool(x)
str(x)'''


# Truthy and Falsly Values

bool
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('Wise'))

fruit = 'Apple'
print()
print(fruit[1:-1])
print(fruit[1])

print()

print(bool('False'))

