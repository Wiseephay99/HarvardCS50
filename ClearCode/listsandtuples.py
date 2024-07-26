# They are containers
# list = [ 1, 'test', []]
# tuples = cannot be changed.....

# tuple = (1,'test', ('another tuple'))
# tupple cannot be changed...lists can be changed.....

# list
my_list = [1,2,3,4,5,6,'word']
print(my_list)
print(len(my_list))
my_list.reverse()
print(my_list)
my_list.clear()
print(my_list)
print(len(my_list))

my_list.append(10)
print(my_list)
print(len(my_list))

#tuple cannot be changed....
my_tuple = (1,2,3,4,56,'word',[7,8,9])
print()
# my_tuple.append(10) # Cannot be allowed
# print(my_tuple.reverse())

#how to pick elements from a tuple or a list: Indexing
print()
print('===========Indexing==========')
list1 = [1,2,3,4,5,6,'word']
print(list1[0])
print(list1[2])
print((my_tuple[6]))
print((my_tuple[6][0]))
print((my_tuple[-1]))
print((my_tuple[-3]))
print((my_tuple[-4]))

# Excerise
print('=============Excerise==================')
print()
# get the word /string 'hello'  :)'
excercise_list = ['first entry', [123,456,[0,'Hello :)']], 'bye']
solution = excercise_list[1][2][1]
print(solution)
print()


# How to pick multiple elements from a list
print()
print('============Slicing===============')
list2 = [1,2,3,4,5,6,7,8,9]
print(list2)
print(list2[1:1])
print(list2[1:2])
print(list2[1:3])
print(list2[1:2:1])
print(list2[0:8:2])
print(list2[8:0:-1])
print(list2[-1:4:-1])
print(list2[::])
print()
# negative_slicing = list2[start:end:step]
negative_slicing = list2[-1:4:-1]
negative_slicing = list2[::2]
negative_slicing = list2[::3]
negative_slicing = list2[::]
# excercise
# start from 8 and go to 2, pick every second element
print()
excercise_solution = list2[-3:0:-2]
print(excercise_solution)
excercise_solution1 = list2[7:0:-2]
print(excercise_solution1)

print()
# Tuple slicing
tuple1 = (1,2,3,4,5,6,7,8,9)
test_tuple = tuple1[0:5:3]
print(test_tuple)

# Unpacking
a, b = (10,5)
print(a)
print(b)

c, d = [10, 'Hello']

# when creating atuple you don't need brackets
print()
health,energy, weapon = 100,50, 'Sword'
print(weapon)

# Excercise
val1 = 10
val2 = 'test'
# Switch the values of the variables
val1, val2 = val2,val1
print(val1)
print(val2)

# strings ,lists and tuples

test_string = 'this is a test'
test_list = [1,2,3,4]
# turning a string into a list / tuple
print(test_string.split())
print(test_string.split('t'))
print(list(test_string))
print(tuple(test_string))

#turning a list / tuple into a string
print(' '.join(['one','two']))
print(str(test_list))
print(type(str(test_list)))

# Indexing on string
print(test_string[0:5])
 