# Conditional and Booleans 
if True:
    print('Conditional was True')
    
# if True:
#     print('Conditional was True')
# 
'''language = 'python'
if language == 'python':
    print('Language is Python')
else:
    print('No match')'''

# if, elif,else statements

'''
language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript ')
else:
    print('No match')
    
'''
# and 
# or
# not
# use of true 
'''
user = 'admin'
logged_in = True
if user =='admin' and logged_in:
     print('Admin Page')
else:
    print('Bad Creds')
'''
    
# use of  false
'''
user = 'admin'
logged_in = True
if user =='admin' or logged_in:
     print('Admin Page')
else:
    print('Bad Creds')

'''
if True:
    print('My name is Wise')
    
print()

if False:
    print('I  am Wise')
    
print()
langauge = 'French'
if langauge == 'french':
    print('lAanguage is French')
elif langauge == 'Spanish':
    print('Language is Spanish')
elif langauge == 'Kiswahili':
    print('Language is Kiswahili')
else:
    print('No Match')
    
#and
#or
#not
user = 'admin'
logged_in = True
# logged_in = False
if user == 'admin' and logged_in:
# if user == 'admin' or logged_in:
    print('Admin Page')    
else:
    print('Bad Creds')
    
'''
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
    
    
'''
print()
# Object Identity
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

print()
print('==============False Conditions====================')
# False Values
# False
# None
# Zero of any numeric type
# Any empty sequence .For example , '' , (), []
# Any empty mapping . For example , {}

condition = False
# condition = None # Evaluate to False
# condition = 0 # Evaluate to False
# condition = 10 # Evaluate to True
# condition = [] # Evaluate to False
# condition = {} # Evaluate to False
# condition = '' # Evaluate to False
# condition = 'Test' # Evaluate to True
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
    