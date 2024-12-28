print()
# Int
print(type(1))
print(type(15))
print(type(0))
print(type(-46))
print()
# Float
print(type(4.5))
print(type(5.8))
print(type(2342423424.3))
print(type(4.0))
print(type(0.0))
print(type(-23.5))
print()
# Complex : Has a real part and Imaginary part
print(complex(4, 5))
print(complex(6, 8))
print(complex(3.4, 3.5))
print(complex(0, 0))
print(complex(5))
print(complex(0, 4))
# Strings in Python
print()
print('Hello World')
print('Hello World!')
print("Hello World!")
print('45678')
print("my_email@email.com")
print("#IlovePython")
print()
#  Quotes Within Strings
print("I'm 20 years old")
print('My favourite book is "Sense and sensibility"')
# String Indexing
print()
my_string = "Hello"
print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
#  We can also use negative indices to access these characters:
print()
print(my_string[-1])
print(my_string[-2])
print(my_string[-3])
print(my_string[-4])
print(my_string[-5])
print()
#  String Slicing

print()
freecodecamp = "freecodecamp"
print(freecodecamp[2:8])
print(freecodecamp[0:3])
print(freecodecamp[0:4])
print(freecodecamp[4:7])
print(freecodecamp[4:8])
print(freecodecamp[8:11])
print(freecodecamp[8:12])
print(freecodecamp[8:13])
print()
print(freecodecamp[0:9:2])
print(freecodecamp[2:10:3])
print(freecodecamp[1:12:4])
print(freecodecamp[4:8:2])
print(freecodecamp[3:9:2])
print(freecodecamp[1:10:5])
print()
print(freecodecamp[10:2:-1])
print(freecodecamp[11:4:-2])
print(freecodecamp[5:2:-4])
print()
# Default start and step
print()
print(freecodecamp[:8])
print(freecodecamp[4:])
print(freecodecamp[:8:2])
print(freecodecamp[4::3])
print(freecodecamp[::-2])
print(freecodecamp[::-1])

# f strings
print()
first_name = 'Nora'
favourite_langauge = 'Python'
print(f"Hi, I'm {first_name}.I'm learning {favourite_langauge}.")
value = 5
print(f'{value} multiplied by 2 is: {value*2}')
freecodecamp = "FREECODECAMP"
print(f'{freecodecamp.lower()}')
print()
print(f'==================String Methods======================')
freecodecamp = "freeCodeCamp"
print(freecodecamp.capitalize())
print(freecodecamp.count('C'))
print(freecodecamp.find('e'))
print(freecodecamp.index('p'))
print(freecodecamp.isalnum())
print(freecodecamp.isdecimal())
print(freecodecamp.isdigit())
print(freecodecamp.isidentifier())
print(freecodecamp.islower())
print(freecodecamp.isprintable())
print(freecodecamp.isspace())
print(freecodecamp.istitle())
print(freecodecamp.isupper())
print(freecodecamp.lower())
print(freecodecamp.lstrip())
print(freecodecamp.rstrip())
print(freecodecamp.replace('e', 'a'))
print(freecodecamp.split('C'))
print(freecodecamp.swapcase())
print(freecodecamp.title())
print(freecodecamp.upper())

print()
print(f'==================Booleans in Python======================')

print()
print(type(True))
print(type(False))
print()
print()
print(f'==================Lists in Python======================')
print(f'\n')
list = [1, 2, 3, 4, 5, 6, 7]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 =  [3.4, 2.4, 2.6, 3.5] 
list4 = [1, 'Emily', 3.4]
my_list = [1, 2, 3, 4, 5, 6]
letters = ['a', 'b', 'c', 'd', 'e']
print(list)
print(list2)
print(list3)
print(list4)
print(my_list)
print()
print(f'==================Nested Lists======================')
print(f'\n')
list5 = [[1,2,3], [4,5,6]]
print(list5)
list6 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(list6)
list7 = [1, [2,3,4], [5,6,7], [3.4]]
print(list7)
# We can access items in a list using their corresponding index
print()
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0])
print(my_list[1])
print(f'\n')
#  Sample Board Where:
# 0 = Empty tile
# 1 = Coin
# 2 = Enemy
# 3 = Goal
board = [
    [0,0,1],
    [0,2,0],
    [1,0,3]
]

print(board)
print(f'\n')
# Length of a List
my_list2 = [1,2,3,4,5]
print(len(my_list2))
#  Update a Value in a List
letters = ['a','b','c','d','e','f']
#  Add a Value to a List
new_list = [1,2,3,4,5]
new_list.append(5)
print(new_list)
#  Remove a Value from a List
new_list.remove(3)
print(new_list)

letters[0] = "e"
print(letters[0])
# List Indexing
print(f'=============List Indexing=====================')
alphabet = ['a','b','c','d','e','f']
print(alphabet[0])
print(alphabet[1])
print(alphabet[2])
print(alphabet[3])
print(alphabet[4])
print(alphabet[5])
print()
# List Slicing
print(f'=============List Slicing=====================')
test_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(test_list[2:6:2])
print(test_list[2:8])
print(test_list[1:10])
print(test_list[4:8:2])
print(test_list[::1])
print(test_list[::-2])
print(test_list[8:1:-1])
print()
print(f'=============List Methods=====================')
print()
crazy_list = [1,2,3,4]
print(crazy_list)

crazy_list.append(5)
print(crazy_list)

crazy_list.extend([6,7,8,9])
print(crazy_list)

crazy_list.insert(2,15)
print(crazy_list)

crazy_list.remove(2)
print(crazy_list)

crazy_list.pop()
print(crazy_list)

crazy_list.index(6)
print(crazy_list)

crazy_list.sort()
print(crazy_list)

crazy_list.reverse()
print(crazy_list)

crazy_list.clear()
print(crazy_list)
#  https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
print()

print()
print(f'======================================================')
print()
print(f'===================Booleans in Python==================')
print(type(True))
print(type(False))
