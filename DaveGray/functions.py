
print()
print()

def hello():
    print('Hello, Wise One!')

hello()

def hello_person():
    print('Hello, Wise Ephay!')

hello_person()

def sum(num1, num2):
    print(num1 + num2)
    
sum(2, 3)
sum(1, 7)
sum(100, 3)
print()

def sum(num1, num2):
    return num1 + num2

total = sum(2, 3)
print(total)

print()

def sum(num1, num2=3):
    if type(num1) is not  int or type(num2) is not int:
        # return 'Sorry, I can only add integers!'
        # return 
        return 0
    return num1 + num2

total = sum(2, 3)
result = sum(10)
print(total)
print(result)

print()

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items()
multiple_items("Dave","John", "Jane", "Doe")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(first= "Wise", last="Samuel", age= 30)