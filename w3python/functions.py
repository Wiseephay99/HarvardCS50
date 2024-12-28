'''Python Functions
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
Creating a Function
In Python a function is defined using the def keyword:'''


     
''' Calling a Function
To call a function, use the function name followed by parenthesis:
'''
print()
def my_func():
     print('Hello from a function')
my_func()     
print(f'======Arguements======')
'''Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is
called, we pass along a first name, which is used inside the function to print 
the full name: '''
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
# Arguments are often shortened to args in Python documentations.
print()
'''
Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
Example

This function expects 2 arguments, and gets 2 arguments:

'''

def my_function2(first_name, lname):
    print(first_name + " " + lname)
    
my_function2('Wise', 'Oketch')
my_function2('Orlando', 'Kim')
my_function2('Emil', 'Refsnes')

'''
Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
Example

If the number of arguments is unknown, add a * before the parameter name:

'''
print()
print(f'===========Arbitrary Arguments, *args======')

def my_function3(*kids):
    print('The youngest child is ' + kids[2])
    
my_function3('Emil','Tobias','Linus')


# Arbitrary Arguments are often shortened to *args in Python documentations.
print()
print(f'===========Arbitrary Keyword Arguments, **kwargs======')
'''
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two 
asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access
the items accordingly:
Example

If the number of keyword arguments is unknown, add a double ** before the parameter name:

'''
def my_function4(**kid):
  print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

print()
print()
'''
Default Parameter Value

The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:

'''
print(f'========= Default Parameter Value============')
def my_function5(country = "Norway"):
    print(f'I am from {country}')
    
my_function5("Sweden")
my_function5("India")
my_function5()
my_function5("Brazil")
my_function5("Kenya")

print()
print()
print(f'=========Passing a List as an Arguement============')

'''Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, 
dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches 
the function:'''

def new_function(food):
    for x in food:
        print(x)
fruits = ["Apple", 'banana', 'cherry']
new_function(fruits)
print()
print(f'======Return Values========')
'''
Return Values
To let a function return a value, use the return statement:
'''
def returning_function(x):
    return 5*x

print(returning_function(3))
print(returning_function(5))
print(returning_function(9))
print()
print(f'==========The Pass Statement==========')

'''
The pass Statement

function definitions cannot be empty, but if you for some reason have a function 
definition with no content, put in the pass statement to avoid getting an error.

'''
def empty_function():
    pass
# having an empty function definition like this, would raise an error without the pass statement

'''
Positional-Only Arguments

You can specify that a function can have ONLY positional arguments, 
or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / 
after the arguments:
'''
def my_function6(x, /):
    print(x)
my_function6(6)