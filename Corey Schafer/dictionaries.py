student = {'name': 'John', 'age': '25','courses': ['math','CompSci']}
print()
print(student)
print(student['name'])
print(student['courses'])
'''
    print(student['phone']) # key error
'''
print(student.get('name'))
'''print(student.get('phone')) # None
print(student.get('phone', 'Not Found')) # Not Found'''
print()
print('============Add,Del,Update Methods==========')
print()
'''student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)
'''
student.update({'name': 'Jane','age':'26','phone': '555-5555'})
print(student)

print()
print('============List Methods==========')
print()
# del student['age']
print(student)
age = student.pop('age')
print(age)
print(len(student))
print(student.items())
print(student.keys())
print(student.values())
print()
print(student.get('name'))
print()
print('============Looping through a List=============')
for key in student:
    print(key)
print()

for key, value in student.items():
    print(key, value)
print()

print()
print('===============LIST RECAP==========')
shopping_cart = {'bread': 65,'id': 'sugar','name': 'sheila', 'age': 27, 'utensils': ['cups','spoons','forks','plates']} 
print(shopping_cart)
# methods
print()
for item in shopping_cart:
    print(item)
print()
for key in shopping_cart:
    print(key)
print()
for key, value in shopping_cart.items():
    print(key, value)
print()
print(shopping_cart.items())
print(shopping_cart.values())
print(shopping_cart.keys()) 
print()
# del shopping_cart['utensils']
# print(shopping_cart)
print()
poppped_shooping_cart = shopping_cart.pop('age')
print(poppped_shooping_cart)
print()
update_shopping_cart = shopping_cart.update({'address': 'Kipiripiri'})
print(shopping_cart)
print()