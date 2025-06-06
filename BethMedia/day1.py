#Print Function

print()

print('Hello Beth Media')
#   Multiple values
print('The result is: ', 45)

# Custom Separators
print()

print('apple','banana', 'cherry', sep="; ")
print('apple','banana', 'cherry', sep=" - ")
print('apple','banana', 'cherry', sep=" # ")

print()
# Custom End Character

print('Hello ', end="")
print('Beth Media')

print()
# Escape Characters

print('First Line\nSecondLine\n')
print('First Line\tSecondLine\t')
print()

# Printing Variables
name = 'John'
age = "25"
print('Name:', name, "Age:", age)

print()

#   String format in print()

name = "Wise"
print('Hello ' + name + "!\n")

#   f-string

name ='John'
age = "30"
print(f'Hello, {name}. You are {age} years old.\n')

#   format() method
name ='John'
age = "30"
print('Hello, {}. You are {} years old.\n'.format(name, age))

#   printing data structures
fruits = ['apples', 'banana', 'cherry']
print(fruits)
# Printing a dictionary data structures

print()
person = {'name': "Alice", "age": "25"}
print(person)
print()

#   common errors
#   use brackets always