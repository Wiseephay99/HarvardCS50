
print()
# Recap of codrey schaufer tutorials

# writing code in the editor
 # strings...woring with textual data
message = 'Hello World'
my_message = 'Hello World'
print('Hello World')
new_message = 'bobby\'s World'
new_message = "bobby\'s World"
print(new_message)
print(message)
print(new_message)
updated_message = """ Boby was a good cartoon 
in the eighties"""
print(updated_message)
print(len(updated_message))
print()
print(message)
# string slicing and string indexing
print(message[0])
print(message[9])
print(message[0:5])
print(message[:5])
print(message[6:])

print()
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('Universe'))
print(message.find('World'))
split_list = message.split()
print(f'The split list is : {split_list}')
print(type(split_list))
strip_list = message.strip()
print(f'The stripped list is: {strip_list}')
print(type(strip_list))
print()
newer_message = message.replace('World', 'Universe')
message = message.replace('World', 'Universe')
print(newer_message)
print(message)

print()

greeting = 'Hello'
name = 'Wise'
info = greeting + ', '  + name
new_info = greeting + ', '  + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
new_message = f'{greeting}, {name.upper()}. Welcome!' # f strings
print(info)
print(new_info)
print(message)
print(new_message)

# Learning methods
# print(dir(name))
# print(help(str))
# print(help(str.lower))
print(f'****************************************')
# 3 Integers and floats
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)
print()
print(2%2)
print(4%2)
print(5%2)
print()
print(3 * 2 + 1)
print(3 * (2 + 1))
num = 1
num = num + 1
print(num)
num += 1
num *= 10
print(num)

print()
print(abs(-3))
print(round(3.756, 1))
print()
print(f'Comparison Operators')
num1 = 3
num2 = 2
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

print()
num1 = '100'
num2 = '200'
print(num1 + num2)
# casting
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

print(f'****************************************')
# 4. lists Tuples and Sets
print(f'Lists Tuples and Sets')

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1]) # Access the last item in the list
print(courses[0:2]) # start item to second item but not including the second item
print(courses[:2])
print(courses[2:])
print()
# list methods
courses.append('Art') # Add iem at the end of the list
print(courses)
courses.insert(0, 'Art') # adds item or list at a specific index
print(courses)
courses2 = ['Art', 'Education']
# courses.insert(0, courses2)
courses.extend(courses2) # add items t the list
print(courses)
courses.remove('Math')
print(courses)
popped = courses.pop()
print(popped)
print(courses)
courses.sort()
print(courses)
courses.reverse()
print(courses)
print()
sorted_courses = sorted(courses)
nums = [1,2,3,5,7,8,9,35]
nums.sort(reverse=True)
print(nums)
# nums.sort()
# print(nums)
print()
nums.reverse()
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
print()
print(courses.index('CompSci'))
print('Art' in courses)
print(f'\n============== For Loop ===============')
print(f'Lopping through items in a list\n')
for item in courses:
    print(item)
print()
for course in courses:
    print(course)
print(f'\n=======Using Enumerate Function==== \n')
for course in enumerate(courses):
    print(course)
print(f'\n=======Using Enumerate Function==== \n')
for index, course in enumerate(courses, start=1):
    print(course)

# Turning list to strings
print(courses)
courses_str = ', '.join(courses)
courses_str2 = '-'.join(courses)
print(courses_str)
print(courses_str2)
# reverse of turning a string to a list
new_list = courses_str.split(', ')
new_list2 = courses_str.split()
print(new_list)
print(new_list2)

# Tuples
# tuples are immutable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1
#
# print(list_1)
# print(list_2)
#
# # list_1[0] = 'Art'
# Tuples are immutable...cannot be modified
print(f'\n============== Tuples ===============')
print()
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art'   # TypeError: 'tuple' object does not support item assignment
print(tuple_1)
print(tuple_2)

# Sets

print(f'\n============== Sets ===============\n')
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print(art_courses)
# to remove duplicate values
# to test if values are part of a set....called membership test
print('Math' in cs_courses)
# Intersection Method
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses)) # What is in art courses and not in cs courses
print(cs_courses.union(art_courses))
print(f'\n============== Empty List, Sets  and Tuples ===============\n')
# creating an empty list,set and tuple
#Empty Lists
empty_list = []
empty_list1 = list()
# Empty Tuples
empty_tuples = ()
empty_tuples1 = tuple()
#Empty Sets
# empty_set = {} This is not right! It creates a dictionary! Dict
empty_set = set()
print(f'\n============== Dictionaries ===============\n')
# Allows us to work with key value pairs...Harsh Maps
student = {
    'name': 'John',
    'age': 25,
    'courses': ['Math', 'CompSci'],
    1: 'John'
}
print(student)
print(type(student))
print(student['name'])
print(student['courses'])
print(student[1])
# print(student['phone']) # Returns a key error ...uses get function below;
print(student.get('Phone')) # Returns None...We can also improve it to return custom message like not found
print(student.get('Phone', 'Not Found')) # Returns None
# adding a new entry to our dictionary
student['phone'] = '555-5555'
print(student)
student['name'] = 'Jane'
print(student)
student.update({'name': 'Peter', 'age': 26, 'phone': '666-666'}) # Updating all at once
print(student)
del student['age']
print(student)
phone = student.pop('phone')
print(phone)
print(student)
print()
print(student.keys())
print(student.values())
print(student.items())
print(f'\n============== For Loop in Dictionary ===============')
print(f'Lopping through a Dictionary \n')
for key in student:
    print(key)
print()
for key, value in student.items():
    print(key, value)

print(f'\n============== If..Else...Elseif... ===============\n')
#Comparisons Operators
# Equal:                        ==
# Not Equal:                    !=
#Greater Than:                  >
#Lesser Than:                   <
# Greater than or Equal to:     >=
# Less than or Equal to:        <=
# Object Identity:              is
if True:
    print('Conditional was True')

language = 'Java' # Python
if language == 'Python':
    print('Langauge is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')
# Check for multiple languages
# from another language...python has no switch statements
user = 'Admin'
logged_in = False # True
if user == 'Admin' and logged_in: # or
    print('Admin Page')
else:
    print('Bad Credentials!')
# Not conditional operator
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]
print()
print(a == b)
print(a is b)
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = None # 10, # True, # [], # '', # {}, # ()
if condition:
    print('Evaluate to True')
else:
    print('Evaluated to False')

print(f'\n============== Loops and Iterations ===============\n')
print(f'For Loops and While Loops\n')
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    print(num)
# break and continue keywords
print()
for nums in numbers:
    if nums == 3:
        print('Found it!')
        break
    print(nums)
print()
for nums in numbers:
    if nums == 3:
        print('Found it!')
        continue
    print(nums)

print()
print(f' Loop within a loop! \n')
new_number = [1,2,3,4,5]
for n in new_number:
    for letter in 'abc':
        print(n, letter)
print()


# When we want to go over a loop a certain number of times: we use the range function
for i in range(10):
    print(i)
print()
for e in range(1, 11):
    print(e)
print(f'\nWhile Loop\n')
x = 0
while x < 10:
    print(x)
    x = x+1
print()
y = 0
while y < 10:
    if y == 5:
        break
    print(y)
    y = y + 1






print()























