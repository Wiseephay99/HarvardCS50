for i in range(1, 10, 3):
    print(i)
    if (i == 4):
        break
# --------------------------------------------
# --------------------------------------------
print()
# 10 level of writing python functions

# Level 1   Doc Strings
def my_function():
    print('Hello, Wise')
my_function()
print()

#   Level 2     Function with Parameters
# --------------------------------------------

def greet(name):
    print(f'Hello, {name}')

greet('Alice')
print()

# Level 3 Return Values
# --------------------------------------------
def add(a,b):
    return a+b

result = add(3,5)
print(result)
print()

# Level 4   Default Parameters
# --------------------------------------------

def greet(name='Guest'): # This has a default parameter
    print(f'Hello, {name}')
greet()   # Will print Hello Guest...

# Level 5   Docstrings
# --------------------------------------------
def add(a,b):
    '''     This Function adds two numbers      '''
    return a + b 

print()

# Level 6 Variable Scope
# --------------------------------------------

global_var = 10
def some_function():
    local_var = 5
    print(global_var + local_var)
some_function()
print()
# Level 7   Recursion
# --------------------------------------------

#   Recursion
def factorial(n):
    if n == 0:
        return 1
    else: 
        return n * factorial(n-1)
factorial(5)
print(f'{factorial(5)}')
print()

# Level 8 Labda Functions
# --------------------------------------------

double = lambda x: x*2
result = double(3)

print(result)
print()


# Level 9   Function Decorators
# --------------------------------------------

def my_decorators(func):
    def wrapper():
        print('Something is happening before the function is called..')
        func()
        print('Something is happening before the function is called..\n')
    return wrapper

@my_decorators
def say_hello():
    print('Hello')
    
say_hello()
print()

# Level 10  Advanced Functions
# --------------------------------------------

def apply(func, x):
    return func(x)

def sqaure(x):
    return x ** 2

result = apply(sqaure, 5)
print(result)
print()

