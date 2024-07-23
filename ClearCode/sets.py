# Simple container for other variables
print()
message = 'Hello World'
print('Hello World')
print(message)
new_message = 'Bobby\'s World'
updated_message = '''Bobby's world was a 
good cartoon in the 1990's'''
print(new_message)
print(updated_message)
print()
print(len(message))
print(message[0])
print('==========Slicing==========')
print(message[0:5])
print(message[:5])
print(message[6:])
print('===========Methods=========')
print(message.upper())
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('l'))
print(message.find('World'))
print(message.find('Universe'))
cool_message = message.replace('World', 'Universe')
print(cool_message)
# Alternative
# message =  message.replace('World', 'Universe')
# print(message)
print()
greeting = 'Hello'
name = 'Michael'
greet_message = greeting + ', '+ name + '. Welcome!'
greet_message = '{}, {}. Welcome!' .format(greeting, name)
greet_message = F'{greeting}, {name.upper()}. Welcome!' .format(greeting, name)


print(greet_message)
print(dir(name))
print(help(str))
print(help(str.lower))

