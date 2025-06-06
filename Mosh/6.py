# While loops
# ===============================
i = 1
while i <= 5:
    print(i)
    i = i + 1

# ===============================

print()
i = 0
while i < 5:
    print(i)
    i = i + 1
print()
# ===============================

r = 1
while r < 11:
    print(r * '*')
    r = r+1
    #   prints a star

# ===============================


# ===============================
# Lists

names = ['john', 'Bob', 'Mosh', 'Sam', 'Mary']

print(names)
print(names[0])
print(names[-2])

print()
names[0] = 'Jon'
print(names)
print(names[0])

# ===============================
# Lists

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)
numbers.insert(0, 6)
numbers.remove(3)
print(1 in numbers)
numbers.clear()

print()
print(len(numbers))
print(numbers)

#   For loops

print()

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print()
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# ===============================
# Range Functions
print()

numbers = range(5, 11, 2)  # Start end and step values
for y in numbers:
    print(y)
print()

print()
for y in range(5, 11, 2):
    print(y)
print()

print()
# Tuples are immutable...cannot be changed once created
numbers = (1, 2, 3, 4, 5)

numbers.count()
numbers.index()
