print()
#   Tuples

#   Collection of items that are ordered and immuttable ....cannot be changed
#   set does not allow duplicates while tuples allow duplicates

#   creating a tuple
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple)

your_tuple = 'apple', 'banana', 'cherry'
print(your_tuple)

# empty tuple

empty_tuple = ()
print(empty_tuple)

# You can have as much elements in a tuple as you want..

single_tuple = ('apple')
print(single_tuple)

#   Accessing items in a tuple
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

#   slicing tuples
print(my_tuple[0:1])
print(my_tuple[1:])
print(my_tuple[1:3])

# tuple immutability
my_tuple = ('apple', 'banana', 'cherry')

# trying to change banana
# my_tuple[1] = 'orange'

# tuple methods
print(my_tuple.count(3))
print(my_tuple.count('apple'))

print()
my_tuple = (1, 2, 3, 2, 2, 4)
print(my_tuple.index(2))
print(my_tuple.index(1))

# working with tuples

# Tuple concatenation
print()
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# Repeating tuples
my_tuple = ('apple', 'banana')
repeated_tuple = my_tuple * 2
print(repeated_tuple)

print()

# converting between lists and tuples
# while tuples are immutable, you can convert them to a list, moduify the list, and convert it back to a tuple.
my_tuple = ('apple', 'banana', 'cherry')

my_list = list(my_tuple)
print(my_list)

my_list = 'orange'
print(my_list)


#   Nesting Tuples
# Tuple inside another tuple

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])


#   Checking for membership
my_tuple = ('apple', 'banana', 'cherry')
print('apple' in my_tuple)
print('berry' in my_tuple)

print()
# Iterating over a tuple

for fruit in my_tuple:
    print(fruit)

print()
print()

'''
Practice questions

1. Write a Python program that attempts to change the second element of a tuple and handles the TypeError that arises when doing so.
2. Write a Python program to concatenate two tuples, tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6), then print the resulting tuple.
3. Write a Python program that creates a nested tuple nested_tuple = ((1,2), (3, 4). (5, 6)), then prints the second element of the first nested tuple.
'''
# solution 2

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)

print()

nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple[1])
print(nested_tuple[1][1])

print()

# checking membership

my_tuple = ('apple', 'banana', 'cherry')
print("berry" in my_tuple)
print("berry" not in my_tuple)

#   iterating over a tuple
for i in my_tuple:
    print(i)

print

'''
Practice questions
1. Write a Python program that attempts to change the second element of a tuple and handies the TypeError that arises when doing so.
2. Write a Python program to concatenate two tuples, tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6), then print the resulting tuple.
3. Write a Python program that creates a nested tuple nested_tuple = ((1, 2), (3, 4). (5, 6)), then prints the second element of the first nested tuple.
'''
print()

user_tuple = ('wise', 'ann', 'jane')
try:
    user_tuple[0] = 'ephay'
    print(user_tuple)
except:
    print("You can't alter a tuple")

print()
