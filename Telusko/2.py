import array as arr
from array import *
import array
import random
print()
# if elif else
x = 8
r = x % 2

if r == 0:
    print('Even')
    if x > 5:
        print(f'{x} is greater than 5')
    else:
        print(f'{x} is less than 5')
else:
    print('Odd')

print('Bye\n')

# **********************************
x = 5
if (x == 1):
    print("One")
elif x == 2:
    print('Two')
elif x == 3:
    print('Three')
elif x == 4:
    print('Four')
else:
    print('Number is greater than 4')
# **********************************

# Loops
# while loops

print('Telusko')
print('Telusko')

print()
# **********************************

i = 10
while i > 0:
    print(f'{i}. Telusko')
    i -= 1

print()

# **********************************

i = 1
while i < 10:
    print(f'{i}. Telusko')
    i += 1

print()

# **********************************
print()

k = 1
while k <= 5:
    print('Wise', end=" ")
    j = 1
    while j <= 4:
        print('Rocks', end=" ")
        j += 1

    k += 1
    print()

print()

# for loops
# **********************************

x = ['wise', 68, 4.4]
for i in x:
    print(i)
print()

ch = 'wise ephay'
for l in ch:
    print(l, end=' ')

print()

for x in range(20, 10, -1):
    print(x, end=" ")
print()
print()
for x in range(1, 21):
    if x % 5 != 0:
        print(x, end=" ")

# **********************************
print()
print()
# break continue and pass

'''available_candies = 10
x = int(input('How many candies do you want?    '))
i = 1
while i <= x:
    if i > available_candies:
        print('Out of stock')
        break

    print('candy')
    i += 1
print('Bye')

'''
print()
print()
# **********************************
# skip values divisible by 3
for i in range(101):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i, end=" ")
print()
# **********************************
print()
# skip values divisible by 3
for i in range(101):
    if (i % 2 != 0):
        pass
    else:
        print(i, end=" ")
print()

# **********************************
print()
for i in range(5):

    if i == 3:
        continue
    if i == 4:
        print('Bye')

    print('Hello', i)
print()

# **********************************


def func():
    pass
    print('do something')


func()

print()

# **********************************
# **********************************

# print("########")
# print("########")
# print("########")
# print("########")

print()
'''
for j in range(4):
    print("#", end="")

print()
for j in range(4):
    print("#", end="")

print()
for j in range(4):
    print("#", end="")

print()
for j in range(4):
    print("#", end="")

print()
'''
# **********************************

for i in range(4):
    for j in range(4):
        print("# ", end="")

    print()
print()

# **********************************

for i in range(4):
    for j in range(i + 1):
        print("# ", end="")

    print()

print()
# **********************************

for i in range(4):
    for j in range(4 - i):
        print("# ", end="")

    print()

# **********************************

nums = [12, 14, 18, 22, 26, 10]
print()
print()

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('Not Found')

print()
print()
# **********************************
num = 10
for i in range(2, num):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print('Prime')


values = arr.array('i', [5, 9, 8, 4, 2])
print(values)
print(values.buffer_info())
print(values.reverse())
print(values[1])

print()
for i in range(len(values)):
    print(values[i])

print()

# **********************************
# array
'''vals = arr.array('u', ['a', 'b',])

newArr = array.array(values.typecode, (a*a for a in values))
print(newArr)
# for e in vals:
#     print(e)

# print()
print()

i = 0
while i < len(newArr):
    print(newArr[i])
    i + 1

print()'''

#   add the elements


arr = array('i', [])
n = int(input('Enter th length of the array:    '))
for x in range(n):
    x = int(input('Enter the next valus:    '))
    arr.append(x)
print(arr)

val = int(input('Enter the value for search:  '))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

'''
1) Create an array with 5 values & delete the value at index no. 2 without using in-built function. 
2) write a code to reverse an array without using in-built function.
'''
