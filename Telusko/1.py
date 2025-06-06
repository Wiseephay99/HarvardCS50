import sys
from math import sqrt, pow
import math as m
import math
import random
name = 'youtube'
print(name)

new_name = name + "rocks"
print(new_name)

print(name[0])
print(name[6])
print(name[-1])
print(name[-2])
print(name[-7])
print(name[0:2])
print(name[1:4])
print(name[1:])
print(name[:4])
print(name[3:10])

# strings are immutable

print('my ' + name[3:])
myname = 'Wise Ephay'
print(len(myname))

#   Lists
print()
nums = [25, 12, 99, 14, 36]
print(nums)
print(nums[0])
print(nums[4])
print(nums[2:])
print(nums[-1])
print(nums[-5])

names = ['wise', 'john', 'kirian']
print(names)
values = [12, 'wise', 9.5]

mil = [nums, names]
print(mil)
nums.append(14)
print(nums)
nums.insert(2, 33)
print(nums)
nums.pop(1)
print(nums)
nums.pop()
print(nums)

nums.remove(14)
print(nums)
del nums[2:]
print(nums)

nums.extend([29, 14, 36])
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
print(sorted(nums))
print()

# Tuple
# are immutable, are faster than a list

print()
tup = (21, 36, 14, 25)
print(tup)
# set ...collection of unique elements....uses hash...does not repeat

s = {22, 24, 14, 21, 5, 22}

print(s)
print(s)
s.update()
print()

#   Dictionary
data = {
    1: 'Wise',
    2: "Kiran",
    3: "Harsh",
}

print(data[3])
print(data[2])
print(data[1])
print()

print(data.get(1))
print(data.get(3))
print(data.get(4, 'Not Found'))

print()
key = ['Kira', 'Navin', 'Harsh']
values = ['Python', 'Java', 'Js']
data2 = dict(zip(key, values))

print(data2)

data2['Monica'] = 'CS'
print(data2)

del data2['Harsh']
print(data2)

print()
prog = {
    'js': 'Atom',
    'cs': 'VS',
    'python': ['Python', 'Sublime'],
    'Java': {'JSE': "Netbeans", 'JEE': 'Eclipse'}
}

print()
print(prog['python'])
print(prog['python'][1])
print(prog['Java'])
print(prog['Java']['JEE'])
print(prog['Java']['JSE'])

print()

#    variables
num = 5
print(id(num))
name = 'narvin'
print(id(name))

st = 'a'
print(st)
print(type(st))
print()
list(range(10, 20))
print(list)
print(list(range(10, 20)))
rev_list = reversed(list(range(10, 20)))
print(list(rev_list))
print()

print()
list(range(2, 10, 2))
print(list)
print(list(reversed(range(2, 10, 2))))

print()
print(type(range(10)))

print()
my_list = list(range(30, 41))
print(my_list)
random.shuffle(my_list)
print(my_list)


d = {
    "navin": 'samsung',
    'rahul': 'Iphone',
    'kiran': 'Oneplus'
}
print(d.keys())
print(d.values())
print(d['kiran'])
print(d.get('kiran'))

# sequence...list tuple set range
print()
#  number system conversion
print(bin(25))

print(0b1101)

print(oct(25))
print(hex(10))
print(0xa)
print(0xf)
print(0b01)

print()
# Python Bitwise ( and or xor, rshift lshift)
print(~-12)
print(~12)
print(12 & 13)
print(bin(12))

print()

print(12 | 13)
print(25 & 30)

print()

print(12 ^ 13)
print(25 ^ 30)
print()
# left shift
print(10 << 2)

# Right shift
print(10 >> 2)

# Import math functions

x = math.sqrt(25)
print(x)

x = math.sqrt(16)
print(x)

print()
print(math.floor(2.9))
print(math.ceil(2.9))
print(math.pow(3, 2))
print(math.pi)
print(math.e)

print(m.sqrt(25))
print(pow(4, 5))

print()

# swap two variables

a = 5
b = 6
print(a, b)
c = a
a = b
b = c
print(a, b)
#
print()
a = 5
b = 6
print(a, b)
a, b = b, a
print(a, b)

print()
# alternative 3
a = 5
b = 6
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)

# x = int(input('Enter 1st number:    '))
# y = int(input('Enter 2nd number:    '))


# print(x + y)

# z = x + y
# print(z)

# character

# ch = input('enter a text:    ')[0]
# print(ch)
# print(ch[0])

# evaluate
result = eval(input('enter an expr:    '))
print(result)

# agrv
if len(sys.argv) > 2:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = x + y
    print(z)
else:
    print("Please provide two numbers as command-line arguments.")
