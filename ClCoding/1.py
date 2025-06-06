# Review of python fundamentals
# Python Variables

name = 'Wise'
print(f'\n---------------Variables-----------------')
print(name)
print(f'\n---------------Functions-----------------')

#  Declare a function


def greet():
    print(f'Hello {name}\n')


greet()

print(f'\n---------------Function with Arguments-----------------')

# Function with arguements


def greet(name):
    print(f'\nHello {name}\n')


greet('Adam')

print(f'\n---------------Data Structures-----------------')
print(f'---------------------Lists-----------------')
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(f'\n---------------------Dictionaries-----------------\n')
student = {
    "name": "Alice",
    'Age': 22,

}

print(student['Age'])
print(student['name'])
print(f'\n---------------------Tuples-----------------\n')
# Immutable data types
fruits = ('apple', 'banana', 'cherry')
print(fruits)
print(fruits[0])

coordinates = (10, 20)
print(coordinates[0])
print(f'\n---------------------Sets-----------------\n')
