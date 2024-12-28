'''Strings

Strings in python are surrounded by either single quotation marks, or double 
quotation marks.
'hello' is the same as "hello".
You can display a string literal with the print() function:'''

print()
print("Hello")
print('Hello')
print()
# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the 
# quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
print()
'''Assign String to a Variable
Assigning a string to a variable is done with the variable name followed 
by an equal sign and the string:'''
a = "Hello"
print(a) 
print()
print(f'================== Multiline Strings ==================')
print()
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
print()

# Accessing Items in a String

a = "Hello, World!"
print(a[1])
print()

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop
for x in "banana":
    print(x)

# String Length
# To get the length of a string, use the len() function.
print()
a = "Hello, World!"
print(len(a))
print()
print(f'================ Check String Example 1 ===============')

# Check String
# To check if a certain phrase or character is present in a string, 
# we can use the keyword in.

txt = "The best things in life are free!"
# Use it in an if statement:
if 'free' in txt:
    print(f'Yes, "free" is present')
else:
    print(f'No "free is not present"')
# print("free" in txt)
# Use it in an if statement:
print()
print(f'================ Example 2============')
text = 'The best things in life are free'
print(text)
# print('expensive' not in text)
# Use it in an if statement:
if 'expensive' not in text:
    print('No, "expensive" is NOT present')
if 'free' in text:
    print(f'Yes, "free" is present')
print()
    
# ===================================Sting Slicing============================
print(f'=======================String Slicing=======================')
'''Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, 
to return a part of the string.'''
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
'''Slice From the Start
By leaving out the start index, the range will start at the first character:'''
b = "Hello, World!"
print(b[:5])
'''Slice To the End
By leaving out the end index, the range will go to the end:'''
b = "Hello, World!"
print(b[2:])
'''Negative Indexing
Use negative indexes to start the slice from the end of the string:'''
b = "Hello, World!"
print(b[-5:-2])

# ===========================Python - Modify Strings============================
print(f'=======================Modify Strings=======================')
# Python has a set of built-in methods that you can use on strings.
a = "Hello, World!" 
print(a.upper())  # Upper Case: The upper() method returns the string in upper case:
print(a.lower())  # Lower Case: The lower() method returns the string in lower case:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"  Remove Whitespace. Whitespace is the space before 
# and/or after the actual text, and very often you want to remove this space.

# Replace String: The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String. The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 
print()
# =========================== String Concatenation ============================
print(f'======================= String Concatenation =======================')
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
print()
a = "Hello"
b = "World"
c = a + " " + b
print(c)
print()

# =========================== Python - Format - Strings ============================
print(f'======================= Python - Format - Strings =======================')
'''String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt)
But we can combine strings and numbers by using f-strings or the format() method!'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print()
'''Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.
'''
price = 59
txt = f"The price is {price} dollars"
print(txt)
'''A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:'''
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
print()
# A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)

# =========================== Python - Escape Characters ============================
print(f'======================= Python - Escape Characters =======================')
'''Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside
a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north." '''

txt = "We are the so-called \"Vikings\" from the north." 
print(txt)
print()

# Escape Characters
    # Code 	Result 	
    # \' 	Single Quote 	
    # \\ 	Backslash 	
    # \n 	New Line 	
    # \r 	Carriage Return 	
    # \t 	Tab 	
    # \b 	Backspace 	
    # \f 	Form Feed 	
    # \ooo 	Octal value 	
     # \xhh 	Hex value
# =========================== Python - String Methods ============================
print(f'======================= Python - String Methods =======================')
new_text = 'my name is wise and I love programming'
print(new_text.capitalize())    
print(new_text.casefold())    
print(new_text.upper())
print(new_text.lower())
print(new_text.count('e'))
print(new_text.encode())
print(new_text.endswith('w'))
print(new_text.expandtabs())
print(new_text.find('t'))
print(new_text.format())
print(new_text.format_map('i'))
print(new_text.index('g'))
print(new_text.isalnum())
print(new_text.isalpha())
print(new_text.isascii())
print(new_text.isdecimal())
print(new_text.isdigit())
print(new_text.islower())
print(new_text.isnumeric())
print(new_text.isprintable())
print(new_text.isspace())
print(new_text.istitle())
print(new_text.isupper())
print(new_text.join('t'))
# print(new_text.ljust('2'))
print(new_text.lower())
print(new_text.lstrip())
# print(new_text.maketrans())
# print(new_text.partition())
print(new_text.replace('w','j'))
# /print(new_text.rindex())
print(new_text.title())
print(new_text.split())
print(new_text.upper())
# print(new_text.translate())





    