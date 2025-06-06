print()
person = 'Tommy'
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

message = '\n%s has %s coins left.' % (person, coins)
print(message)

message = '\n{} has {} coins left.'.format(person, coins)
print(message)

message = '\n{1} has {0} coins left.'.format(coins, person)
print(message)

player = {'person': 'Dave','coins': 3}

message = '\n{person} has {coins} coins left.'.format(**player)
print(message)

#   f-strings.  This is the way
print(f'\n{person} has {coins} coins left.')

print(message)

print(f'\n{person.lower()} has {2 * 5} coins left.')

print(message)

print(f'\n{player['person']} has {2 * 5} coins left.')

print(message)

###############################################
# you can passformatting option
num = 10
print(f'\n 2.25 times {num} is {num*2.25:.2f}\n')
print('**********************')
for num in range(1, 11):
    print(f'2.25 times {num} is {num*2.25:.2f}')

print('**********************')
print('\n**********************')
for num in range(1, 11):
    print(f'{num} divided by 4.52 times is {num / 4.52:.2%}')

print('**********************')
print('\n')

