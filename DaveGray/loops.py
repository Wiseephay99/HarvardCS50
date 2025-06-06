value = 1
# while value <= 10:
#     print(value)
#     # value = value + 1
#     value += 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     # value = value + 1
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     # value = value + 1
#     print(value)
# else:
#     print(f'Value is now equal to ' + str(value))
    
print()
names = ['Dave', 'Sara', 'John']

for x in names:
    print(x)

print()  
for x in 'mississippi':
    print(x)
print()

for x in names:
    if x == 'Sara':
        break
    print(x)
print()

for x in names:
    if x == 'Sara':
        continue
    print(x)
print() 

for x in range(4):
    print(x)

print()

for x in range(2, 5):
    print(x)

print()

for num in range(0, 100, 5):
    print()
else:
    print('Glad That\'s over!')
    
print()

names = ['Dave', 'Sara', 'John']
actions = ['codes', 'eats', 'sleeps']

for name in names:
    for action in actions:
        print(f'{name} {action}.')

print()
        
for action in actions:
    for name in names:
        print(f'{name} {action}.')

print()

