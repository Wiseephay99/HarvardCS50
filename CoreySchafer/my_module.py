print()
print('Imported my_module...')

test = 'Test String'

# This program uses a file from  intro.py

def find_index(to_search, target):
    ''' Find the Index of a value in a sequence '''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1