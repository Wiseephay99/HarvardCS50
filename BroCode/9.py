import time
print()


# *********************************************************
# for loops
'''
for x in range(1, 11):
    print(x)
print()

for x in reversed(range(1, 11)):
    print(x)
print('Happy new Year!!!')
for x in reversed(range(1, 11)):
    print(x)
print('Happy new Year!!!')

print()
for x in reversed(range(1, 11, 3)):
    print(x)
print()

credit_card = '1234-5678-9012-3456'
for x in credit_card:
    print(x)

print()
print()'''

# *********************************************************

'''for x in range(1, 10):
    if x == 6:
        continue
    else:
        print(x)
print()
'''
# *********************************************************
#   Nested Loop
'''for x in range(3):
    for y in range(1, 10):
        print(y, end='')
    print()'''

# *********************************************************
#   Nested Loop
'''rows = int(input('Enter the # of rows:  '))
columns = int(input('Enter the number of columns:   '))
symbol = input(f"Enter the symbol to use:       ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end='')
    print()

print()
'''
# *********************************************************
# countdown timer program in python

# time.sleep(3)

# print('TIME\'S UP!')

my_time = int(input('Enter the time in seconds:     '))

'''for x in reversed(range(0, my_time)):
    print(x)
    time.sleep(1)

print(f'TIME\'S UP')
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

print(f'TIME\'S UP') '''

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print(f'TIME\'S UP')
