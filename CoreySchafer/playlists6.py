print()
# sorting lists, tuples and objects 

li = [9,1,8,2,7,8,3,6,4,5]

s_li = sorted(li)

sort_li = li.sort()  # sorts the list but return a none value
print(f'********************************************')

print(f'Sorted Variable:\t {sort_li}')

# sort method return a none but sorted returns a value
print()
print(f'********************************************')

print(f'Sorted Variable:\t {s_li}')
print(f'Original Variable:\t {li}')
print(f'********************************************')
li.sort()
print(li)

print(f'********************************************')
print()

s_li = sorted(li, reverse=True)
print(s_li)
print(f'Original Variable:\t {li}')
print(f'********************************************')
print()

# print(f'Original Variable:\t {li}')
print(f'********************************************')

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(f'Tuple:\t {s_tup}')

print()
print(f'********************************************')

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print(f'Dict:\t {s_di}') # sorts only the keys...
print(f'********************************************')
print()
print(f'********************************************')
num_li = [-6,-5,-4,1,2,3]
print(num_li)
s_num_li = sorted(num_li)
print(s_num_li)
s_num_li = sorted(num_li, key=abs)
print(s_num_li)
# sortin based on absolute numbers
print(f'********************************************')

print()
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __repr__(self):
        return f'{self.name}, {self.age}, {self.salary}'


# from operator import attrgetter

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]
def e_sort(emp):
    # return emp.name
    # return emp.age
    return emp.salary

s_employees = sorted(employees, key=e_sort, reverse=True)

s_employees = sorted(employees, key=lambda e: e.name)  #Alternative of using the def e sort 
# function we just use a lambda function

# s_employees = sorted(employees, key=attrgetter('age'))


print(s_employees)
print()
print(f'********************************************')
print(f'********************************************')

li = [9,1,8,2,7,8,3,6,4,5]