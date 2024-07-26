''''
What we will cover:
    Variable Definitions in Python
    Hello, World! Program in Python
    Data Types and Built-in Data Structures in Python
    Python Operators
    Conditionals in Python
    For Loops in Python
    While Loops in Python
    Nested Loops in Python
    Functions in Python
    Recursion in Python
    Exception Handling in Python
    Object-Oriented Programming in Python
    How to Work with Files in Python
    Import Statements in Python
    List and Dictionary Comprehension in Python   
'''
# Varibles
# Format
# <var_name> = <value>
age = 56 # Int
name = 'Nora' # String
color = 'Blue' # String
grades = [67, 100, 87, 56] # List

my_list = [1,2,3,45,67]
greeting = 'Hello World'
print(greeting)
my_name = 'Wise'
print()
print(my_name)
greeting = 'Hello'
print(greeting)

print(greeting + " " + name) # String Concatenation
print()
greet = 'Hi Wise'
print(greet)
print()

# Data Types and Built-in Data Structures in Python
# Integers
print(type(1)) # int
print(type(15)) # int
print(type(0)) # int
print(type(-46)) # int
print()

# float
print(type(4.5)) # float
print(type(5.8)) # float
print(type(2342423424.3)) # float
print(type(4.0)) # float
print(type(0.0)) # float
print(type(-23.5)) # float

# Complex Complex Numbers - They have a real part and an Imaginary Part
print()
print(complex(4, 5))
print(complex(6, 8))
print(complex(3.4, 3.4))
print(complex(0, 0))
print(complex(0, 4))
print(complex(5))

# strings in Python - Sequence of characters
print()
print('Hello World')
print("Hello, World")
# Strings can contain any character that we can type in our keyboard. 
# Spaces are also counted in astring as characters
print()
print('45678')
print('my_email@email.com')
print('#IlovePython')
# Qoutes within Strings
print("I'm 20 years old") #Using a single quote
print('My favourite book is "Snse and sensibility"') #Using a double quote
print()
print()
# String Indexing -- Trying to access characters of a string
message = 'Hello'  # String H E L L O
                   # Index  0 1 2 3 4
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print()
# We can also use negative indices to access these characters:
print(message[-1])
print(message[-2])
print(message[-3])
print(message[-4])
print(message[-5])
print()

#String Slicing  - Acessing a part or subsection of a string or its characters
# syntax: <string_variable> [start:stop:step]
print("=============String Slicing============")
freecodecamp = "freecodecamp"
              # 01234567891011
print(freecodecamp[2:8])
print(freecodecamp[0:3])
print(freecodecamp[0:4])
print(freecodecamp[4:7])
print(freecodecamp[4:8])
print(freecodecamp[8:11])
print(freecodecamp[8:12])
# step
print()
print(freecodecamp[0:9:2])
print(freecodecamp[2:10:13])
print(freecodecamp[1:12:4])
print(freecodecamp[4:8:2])
print(freecodecamp[3:9:2])
print(freecodecamp[1:10:5])
print()
# negativstep
print(freecodecamp[10:2:-1])
print(freecodecamp[11:4:-2])
print(freecodecamp[5:4:-2])
# Ommitting start
print()
print(freecodecamp[:8])
print(freecodecamp[4:])
print(freecodecamp[:8:2])
print(freecodecamp[4::3])
print(freecodecamp[::-2])
print(freecodecamp[::-1]) # Reverse a sring

# f-string. Used in string formatting
print()
print("============= f- string ============")
print()
first_name = 'Nora'
favourite_language = 'Python'
print(f"Hi, I'm {first_name}. I'm learning {favourite_language}")
value = 5
print(f"{value} multiplied by 2 is: {value*2}")
print()
# WE can methods within thin the curly brackets 
freecodecamp = 'FREECODECAMP'
print(freecodecamp.lower())
print(f"{freecodecamp.lower()}")
print()
print("============= String Methods ============")
print()
#General Formula to call a string method is: 
# <string_variable>.<method_name>(<arguements)
freecodecamp = "freeCodeCamp"

print(freecodecamp.capitalize())
print(freecodecamp.count('C'))
print(freecodecamp.find('e'))
print(freecodecamp.index("p"))
print(freecodecamp.isalnum())
print(freecodecamp.isalpha())
print(freecodecamp.isdecimal())
print(freecodecamp.isidentifier())
print(freecodecamp.islower())
print(freecodecamp.isnumeric())
print(freecodecamp.isprintable())
print(freecodecamp.isspace())
print(freecodecamp.istitle())
print(freecodecamp.isupper())
print()
print(freecodecamp.lower())
print(freecodecamp.lower())
print(freecodecamp.lstrip("f"))
print(freecodecamp.rstrip("p"))
print(freecodecamp.replace('e', 'a'))
print(freecodecamp.split('C'))
print(freecodecamp.swapcase())
print(freecodecamp.title())
print(freecodecamp.upper())
print()
