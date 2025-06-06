print()

name = "Wise"
# def greeting():
#     print(name)
# greeting()

# def greeting():
#     color = 'Red' # Local Scope
#     print(color)

#     print(name)
# greeting()

def greeting(name):
    color = 'Red' # Local Scope
    print(color)

    print(name)
greeting('John')

def another():
    greeting('Dave')

another()
# We can define functions inside another function
# The inner function can only be called from the outer function

name = "Wise"
count = 1
print('--------------------')
def another():
    color = "Blue"
    # count = 2  # will print 2
    # count += 2
    global count
    count += 2   # prints 2
    print(count)
    def greeting(name):
        nonlocal color
        color = 'Red' # Local Scope
        print(color)
        print(name)
    greeting('John')
another()