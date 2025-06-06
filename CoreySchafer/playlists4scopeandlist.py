print()
''' 
LEGB
Local, Enclosing, Global, Built-in
'''

x ='global x'
# global scope

print(f'This is a global scope: {x}')
def test():
    y = 'local y' # local variable to the test function
    print(x)
    print(f'This is a local scope: {y}')
    
test()
print(x)

print()

def test1():
    # This is a global variable:
    # global l 
    global l 
    l = 'local l'
    print(l)
    
test1()
print(l)
print()

def test2(z):
    x = 'local x'
    print(z)
    
test2('local z')
# print(z)

print()

# import builtins   ... to view functions within the builtin scope
import builtins
print(dir(builtins))

# print(dir(__builtins__))

#   bultin minmum function

m = min([5, 1, 4, 2, 3])
print(m)

print(f'=========================================')

def my_min():  # if you set it to min it will not print the mn but throw an error...Typerror ()
    pass

n = min([5,7,8,14,67])

print(n)

# Enclosing Scope
def outer():
    r = 'outer r'
     
    def inner():
        # nonlocal r # will print x twice
        r = 'inner r'
        print(r)
        
    inner()
    print(r)

outer()
print(x)
# Slicing Lists and Strings
print()
print(f'=========================================')
print(f'Slicing Lists and Strings')
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        # -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# new_list = list[start:end:step]
print(my_list[5])
print(my_list[-1])
print(my_list[-10])
print(my_list[0:6])
print(my_list[3:8])
print(my_list[-7:-2])
print(my_list[1:-2])
print(my_list[1:])
print(my_list[5:])
print(my_list[:])
print()
print(my_list[2:-1:2])
print(my_list[2:-1:1])
print(my_list[-1:2:-1])
print(my_list[-2:1:-2])
print(my_list[::-1])
print()
sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url 
print(sample_url[::-1])

# Get the top level domain 
print(sample_url[-4:])

# Print the url without the http://
print(sample_url[7:])

# Print the url without the http:// or the top level domain
print(sample_url[7:-4])
# List Comprehensions in python