# List Comprehensions in Python
nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
print()
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
print()

# Alternative code is: 

my_list = [n for n in nums]
print(my_list)
print()

# I want 'n*n' for each "n" in nums

my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)
print()

my_list = [n*n for n in nums]
print(my_list)

# Using Maps + Lambda

my_list = list(map(lambda n: n*n, nums))
print(my_list)

print()

# I want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list) 
# Altrernative code for the above
my_list = [n for n in nums if n%2 == 0]
print(my_list)
# Alternative Filter  function  
# Using a filter + lambda
my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)
print()
# I want a (letter, num) pair for each in 'abcd' and EACH NUMBERIN '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)
# Altrernative code for the above

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)
print()


# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

print(list(zip(names, heroes))) # will form a list of tuples
print()

# I want a dict {'name': 'hero'} for each name, hero in zip(names,heroes)
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print (my_dict)
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

print()

# if not equal to Peter
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

print()
print()

# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)
# alternative set comprehensions
my_set = {n for n in nums}
print(my_set)

print()

# Generator Expressions
# I want to yeild 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n
      
my_gen = gen_func(nums)

print()

#   Alternative source code

my_gen = list((n*n for n in nums))
print(my_gen)
print()
for i in my_gen:
    print(i)

print()


