# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# define a class
class Car:
    pass


# Create object of the car class
car1 = Car()
car2 = Car()
# Print the object of the car class
print(car1)
print(car2)

# -----------------------------------------------------------------------


class Dog:
    def bark(self):  # This is a method
        print(f'Woof! woof! \n')
#   Making an obejct of the Dog class


dog1 = Dog()
dog1.bark()
# -----------------------------------------------------------------------


class Person:
    # attributes (characteristics of the person)
    name = 'Wise'
    age = 24
    # Methods (behaviour of the person)

    def greet(self):
        print(f'Hello This is: {self.name} and is {self.age} years old. \n')


person1 = Person()
print(person1.name)
person1.greet()
print()

# -----------------------------------------------------------------------


class Human:
    def __init__(self, name, age):  # constructor
        self.name = name  # Instance Variables
        self.age = age  # Instance Variables

    def greet(self):
        print(f'Hello, This is {self.name} and I am {self.age} years old. \n')


# create human object
human1 = Human('Wise', 24)
human1.greet()
print(f'-----------------------------')

# -----------------------------------------------------------------------

# Exploring the __init__ method


class Laptop:
    def __init__(self, brand, model, price):
        # # Constructor
        self.brand = brand
        self.model = model
        self.price = price

    def display_details(self):
        print(
            f'Laptop Brand {self.brand}, Price: {self.price}, Model: {self.model} \n')


laptop1 = Laptop('Dell', 'Inspiron', 500)
laptop1.display_details()
laptop2 = Laptop('HP', 'Pavilion', 600)
laptop2.display_details()
print(f'-----------------------------')


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
