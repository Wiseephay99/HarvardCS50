# lambda num: num * num
# lambda function are referred to as anonymous variables;


# squared = lambda num: num * num
# print(squared(5))

multiply = lambda num: num * num
print(multiply(5))
addTwo = lambda num: num + 2
print(addTwo(12))
print()
sum = lambda a, b: a+b
print(sum(10, 8))
print(sum(5, 6))

print()

################################################
# using lambda with filter
# filter() function in Python takes in a function and a list as arguments.
# This offers an elegant way to filter out all the elements of a sequence "sequence", for which the function returns True.
# Here is a small program that returns the odd numbers from an input list:
# Program to filter out only the even items from a list
print()
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)    
addTwenty = funcBuilder(20) 

print(addTen(7))
print(addTwenty(7))

################################################
# High Order Functions
# lambda num : num * num

print()
numbers =  [3,7,12,18,20,21]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

print()

# Filter
# lambda num: num % 2 != 0
odd_nums = filter(lambda num: num % 2 != 0, numbers)   
print(list(odd_nums)) 

print()
################################################
# Reduce
from functools import reduce
# lambda acc, curr: acc + curr
number = [1,2,3,4,5, 1]
result = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(result)
print()

# lambda acc, curr: acc + len(curr)

names = ['Dave Gray', 'Tommy', 'John', 'Jane']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)

