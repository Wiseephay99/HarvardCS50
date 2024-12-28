print()
print("Hello, Wise!") 
if 5 > 2:
    print('Five is greater than two')
    print('Five is greater than two')
# Variables
x = 5
y = "Hello, World!"
#  #This is a comment.
# Variables are containers for storing data values.
x = 5
y = "John"
print(x)
print(y)
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# Castimg: If you want to specify the data type of a variable, 
# this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print()
x = 5
y = "John"
print(type(x))
print(type(y))
# String variables can be declared either by using single or double quotes:
print()
x = "John"
# is the same as
x = 'John'
# Case sensitive
a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a 

print()
print(f'=================== Variable Names ============')
myvar = 'John'
print(myvar)
my_var = 'John'
print(my_var)
_my_var = 'John'
print(_my_var)
myVar = 'John'
print(myVar)
MYVAR = 'John'
print(MYVAR)
myvar2 = 'John'
print(myvar2)
myVariableName = "John" 
print(myVariableName)  #Camel Case
MyVariableName = 'John'
print(MyVariableName)   #Pascal Case
my_variable_name = "John"
print(my_variable_name)  #snake case
print()
# Many Values to Multiple Variables , 
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print()
# One Value to Multiple Variables. And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
print()
# Unpack a Collection. If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print()
print(f'=================================================')
print()
# Output Variables. The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)
print(f'======================= Global Variable ==========================')
'''Python - Global Variables
Variables that are created outside of a function (as in all of the examples                                                   
in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.'''
x = 'awesome'
def my_func():
    print("python is " + x)
my_func()
'''If you create a variable with the same name inside a function, this variable will be
local, and can only be used inside the function. The global variable with the same
name will remain as it was, global and with the original value.'''
y = 'great'
print(f'======================= Local Variable ==========================')
def myfunc2():
    y = 'new'
    print('python is ' + y)
myfunc2()

'''The global Keyword
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.'''
def my_func3():
    global h 
    h = 'fantastic'
my_func3()
print('Python is ' + h)
# Also, use the global keyword if you want to change a global variable inside a function.
p = "crazy"

def myfunc4():
  global p
  p = "fantastic"

myfunc4()

print("Python is " + p) 
print(f'======================= Excerise ==========================')

# Assignment
f = 'awesome'
def myfunc():
  f = 'fantastic'
  print(f'Python is {f} ')
myfunc()
print('Python is ' + f)
print('Hello', 'World')