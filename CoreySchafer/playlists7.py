
print()
# Python Tutorial: String Formatting - Advanced Operations for 
# Dict, Lists, Numbers and Dates

print()

person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

print()

tag = 'hi'
text = 'This is a headline'

print()

sentence = '<{0}><{1}></{0}>'.format(tag, text)
print(sentence)

l = ['Jane', 23]

new_sentence = 'My name is {0[0]} and I  am {0[1]} ears old.'.format(l)
print(new_sentence)
sentence = 'My name is {0[name]} and I  am {0[age]} ears old.'.format(person)
print(sentence)
print()

class Person():
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
p1 = Person('Jack', '33')

print()
print(f'********************************************')

sentence = 'My name is {0.name}and I am {0.age} years old.'.format(p1)
print(sentence )
        
sentence = 'My name is {name}and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence )

sentence = 'My name is {name}and I am {age} years old.'.format(**person)
print(sentence )
print(f'********************************************')
print()

for i in range(1,11):
    # sentence = 'The value is {}'.format(i)
    sentence = f'The value is {i}'
    print(sentence)

print()
print(f'********************************************')

pi = 3.141159365

sentence = 'Pi is equal to {:}'.format(pi)
print(sentence)
print(f'********************************************')

sentence = '1 MB is equal to {:.3f} bytes'.format(1000**2)
print(sentence)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
print(f'********************************************')

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

print(my_date)
print(f'********************************************')

sentence = '{:%B %D, %y}'.format(my_date)
print(sentence)
print(f'********************************************')

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence = '{0:%B %D, %y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
print(f'********************************************')

setence = '{}'.format(my_date)