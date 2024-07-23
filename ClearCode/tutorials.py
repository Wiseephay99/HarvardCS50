# Complete Giude to Python


# # Methods
print()
test = 'A word'
print(test)
print()
username = 'JOhn SmIthXX'.title().strip('x')
print(username)
# .title() translates to capitalize each word.
# .strip() removes unwanted character
print()
# prints all methods associated to string or character
#  prints all methods associated to string or character

print(username.isalpha())  # checks if characters are in the the alphabet

exercise_string = 'I like puppies'
print(exercise_string.replace('puppies', 'cubs'))
print(exercise_string.replace('puppies', 'cubs'))
# methods
# print()
# .replace
# .isalpha
# .title
# .strip
# abs() Returns whole number

print()
# Return
test_variable = len(' A test'.upper().replace('A', 'X'))
print(test_variable)
print(print(test_variable)) # prints none

# comments
'''
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
another_variable = 12312334535454
'''
# error 
# syntax error 
# identation error 
# breking a line
# print('first line'); print('second line')

# Data Types:  
# 1. string - words 
# 2. integers - numbers, 
# 3. float- floating point numbers, 
# 4. boorlean - true/False
# 5. list
# 6. tuples // cannot be changed
# 7. set  has uniques set of value
# 8. dictionaries

#Datatypes
print()
# converting an int to float
print(float(2))
print(int(5.1))
print(1.1*3)
# Strings
# single or double quotation marks
# fstrings
print()
test_var = 'Test 1'
test_var2 = 'Test 2'
test_var3 = '  "He said "This was great" '
print(test_var)
print(test_var2)
print(test_var3)
print()
test_var4 = '\"\'' #Escape character
print(test_var4)

#Escape Character 
test_var5 = 'Line 1: some text \nLine 2: Some more text'
test_var6 = 'Line 1: some text \rLine 2: Some more text'
print(test_var5)
print()
print(test_var6)
# \n jumps to new line Line break
# \r
test_var7 = '''A comment
test on a new line
anoter text on another line'''
print()
# math and string
print(test_var7)
test_var8 = 'hello' + " " + "world"
print(test_var8)
# how to get values into strings
print()
name = "Bob"
age = 30
greeting_string = 'Hello {}, you are {} years old'.format(name, age)
greeting_string2 = 'Hello {one}, you are {two} years old'.format(one = name, two = age)
# alternative text 
greeting_string1 = 'Hello {name}, you are {age} years old'
print()

print(greeting_string)
print(greeting_string1)
print(greeting_string2)
print()
greeting_string_better = f'Hello {name}, you are {age+10} years old'
print()
print(greeting_string_better)
print()

#Exercise
X = 'Wise'
Y = 'Programming'
z = f"Hello, my name is {X} and \nmy hobby is 'Y' "
excerise2 = f'''Hello, my name is {X}
and my hobby is {Y}'''
print(z)
print(excerise2)
print()
# List and Tuples
# list.append(value)
my_list = [1,2,3,4,5,6,7,'word']
print(my_list)
my_list.append(10)
print(my_list)
# my_list.clear() #removes all items from the list
# my_list.index()
# my_list.sort()
# mylist.reverse()
# print(len(my_list))
print()
#Tuple   == Cannot be changed
my_tuple = (1,2,3,4,5,6,7,'word',[7,8,9])
print(my_tuple)

# How to pick elements from a List   123456
print()                               #    0123456
print(my_list[0])
print(my_list[2])
print(my_list[2])
print(f"This is the Tuple: {my_tuple[8]} ")
print(f"This is the Tuple indexing : {my_tuple[8][0]} ")
print(f"This is the Tuple indexing : {my_tuple[8][-1]} ")
print(f"This is the Tuple indexing : {my_tuple[8][-2]} ")
print(f"This is the Tuple indexing : {my_tuple[8][-3]} ")

print()
# Excerise 
# Get the word / string 'hello ::)'
excercise_list = ['first entry', [123,456,[0,'Hello: )']], 'bye'] 
solution_var = excercise_list[1]
print(solution_var)
solution_var = excercise_list[1][2]
print(solution_var)
solution_var = excercise_list[1][2][1]
print(solution_var)
# lists and tuples part two:
# lists :picking two elements nor one:
# slicing
print()
print('============Slicing by Index==========')
test_lists = [1,2,3,4,5,6,7,8,9,10]
print(test_lists[1:1])
print(test_lists[1:2])
print(test_lists[1:3])
# slicing by direction by step
# [1,2,3,4,5,6][1:2:3]
print('============Slicing by Index Step==========')
print(test_lists[0:8:2])
print(test_lists[0:8:-1])
print(test_lists[-1:4:-1])
# [1,2,3,4,5,6][start:end:step]
negative_slicing = test_lists[-1:4:1]
# default_slicing = test_lists[start:end:second]
default_slicing = test_lists[::2]
default_slicing = test_lists[::3]
default_slicing = test_lists[::]
print(default_slicing)

# excerise:

# start from 8 and go to  2, pick every second element
print()
print('============Excericse Solution==========')
numbers = [1,2,3,4,5,6,7,8,9,10]
solution1 = numbers[-3:-9:2]
solution2 = numbers[7:0:-2]
solution = numbers[::-1]
print(solution)
print(solution2) # Gives the correct answers
print('============Tuple Slicing==========')

# Also this works for tuple....
test_tuple = (1,2,3,4,5,6,7,8,9,10)
print(test_tuple[0:5:3])
#Unpacking  a,b = (10,5) a,b = [10,5]
print('============Unpacking a Tuple and a List==========')
a,b = (10,5)
print(a)
print(b)
c,d = [2, 'Hello']
print(c)
print(d)
health, energy, weapon = 100, 50, 'Sword'
print(weapon)
print('============Excericse Solution==========')
value_1= 10
value_2 = 'Test'
# Switch the values of the two variables
value_1, value_2 = value_1, value_1
print(value_2)
print(value_1)
# string list ans tuples are just containers
print('============Converting a String to a List and Tuple==========')
test_string = 'this is a test'
test_list = [1,2,3,4,5,6,]
# turning a string into a list/tuple
print('===== turning a string into a list/tuple=======')
print(test_string.split())
print(test_string.split('t'))
print(list(test_string))
print(tuple(test_string))
# turning a list /tuple into a string
print()
print(" ".join(['one','two','three','four']))
print(str(test_list))
print(" ".join(str(test_list)))

# indexing on strings
print('========indexing on strings=======')
print(str(test_string[0:5]))

#Exercise
print('===========Excerices================')
print(str(test_list))
excerices = str(test_list).strip('[').strip(']').replace(',','').replace(' ','')
print(excerices)






