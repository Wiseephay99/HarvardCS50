# Learning Functions
# Functions are instructions packaged together to perform a certain /specific  task
print(f'====================== Learning Functions ==================')
def hello_func():
    # pass
    print('Hello Function!')

hello_func()
# functions allow us to reuse code without repeating ourselves through code reuse
# Keeping your code DRY don't repeat yourself  below is called DRY
# Don't Repeat Yourself
print()
hello_func()
hello_func()
hello_func()
hello_func()
# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')
# print('Hello Function!')

# Take a function that creates a machine and produces a result!
def hello_func():
    return 'Hello Function!'

print()
print(hello_func())
print(hello_func().upper())
print(len('Test'))
# How to pass arguements to our function.
def hello_func2():
    pass

print()
def hello_func2():
    return 'Hello Wise 😊'

hello_func2()
# Dry
print(hello_func2())
print(hello_func2())
print(hello_func2())
print(hello_func2())
print(len('Test'))
print(hello_func2().upper())
# How to pass arguments to our functions
# default value parameters ...name = 'You'

def hello_func3(greeting, name = 'You'):
    return f'{greeting} {name} Function'

print(hello_func3('Hi', 'Corey'))
# Positional arguments have to come before keyword arguements
def hello_func4(greet, name):
   return f'Message: {greet}, {name}? How are you doing? \n'
print(hello_func4('Hey', 'Wise'))

print()

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
# student_info('Math', 'Art', name = 'John', age = 22)
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
# student_info(courses, info)
student_info(*courses, **info)

print()
print(f'===========================Recap ================================')
# Number of days per month. First value plcaeholder for indexing purposes.
month_days = [0, 31, 28 , 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """ Return True for leap years, False for non-leap years. """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """ Return number of days in that month in that year """
    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2020))
print(is_leap(2017))
print(days_in_month(2017,2))
