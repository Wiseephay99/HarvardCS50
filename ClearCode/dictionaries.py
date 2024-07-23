# STORES  DATA IN KEY VALUE PAIR
print()
test_dict = {"A": 123, 
             "B":[1,2,3], 
             1: True}
print(test_dict)
# methods
# clear()
# copy()
# fromkey()
# get()
# items()
# keys()
# pop()
# popitems()
# setdefault()
# update()
# values()
print(test_dict.values())
print(type(test_dict.values()))
print(test_dict.keys())
print(test_dict.items())
print(len(test_dict))
# Converting a Dict
print()
print('==========Converting a Dictionary===========')
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))
print()
print('============Indexing with Dictionaries===========')
print(test_dict['A'])
print(test_dict.get('A'))  # Does crash when it doesn't find a key
print(test_dict.get('X')) # Doesn't  crash when it cannot find a key 
print()
print('==========Excerise===========')
#Excerise
# Do reasarch and use the update method to addd another key value pair
test_dict.update({"Another Key": (1,2,3)})
test_dict.update(C = 'test', D = '123')
test_dict['E'] = 100
print(test_dict)



