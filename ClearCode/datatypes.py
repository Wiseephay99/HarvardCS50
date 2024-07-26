# DataTypes
'''

String = words = text
integers
floating numbers = float
boorlean =  true/false
List - [1,2, 'Test']
Tuple
Set 
Dictionary
'''
print()
print(type(1))
print(type(1.1))
print(1 + 1.1)
print(10/5) # Gives a float
print()
print(2+0.0)# Converting to float
print(float(2))
print(int(5.1))#Converst to string and one losses a 
print(1.1 * 3) # 3.3
print('===========Strings===========')

'''
    .upper()
    .isnumeric()
    .strip()
'''
#Quote for strings
test_var = 'Test 1'
test_var2 = 'Test 2'
print(test_var)
print(test_var2)

#quote inside of strings
test_var3 = " He said 'This was great' "
test_var4 =  '\" \''  # simple escape character
print(test_var3)
print(test_var4)
print()
# Escape Character
test_var5 = 'Line 1: some text \nLine 2: some more text'
print(test_var5)
# Multiple Line
test_var6 = '''A comment
  *   
  ***  
 ***** 
*******
   *   
   *   
   *   
   *   
   '''
print(test_var6)
print()
print('=========Math and Strings========')
test_var7 = 'Hello' + " " + 'World'
print(test_var7)
test_var8 = 'copy' * 10
print(test_var8)
print()
#How to get values to strings
name = 'Tom'
age = 40
greeting_string = 'Hello {}, you are {} years old'.format(name,age)
greeting_string1 = 'Hello {one}, you are {two} years old'.format(one = name,two = age)
greeting_string2 = f'Hello {name}, you are {age} years old'
greeting_string3 = f'Hello {name}, you are {age +3} years old'

print(greeting_string)
print(greeting_string1)
print(greeting_string2)

# Exercise
# create an f-string that says; Hello, my name is x and my hobby is y
# x and y should be separate variables
# the second half  of the sentence should also be on a separate line
x= 'Wise'
y= 'programming'
greet = f"Hello my name is {x} and \nMy hobby is {y}"
print(greet)
print()
