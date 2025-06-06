import sys
from enum import Enum
import math
import random
import time
print()

print('-------------------------------------------------')

# 1. Create a class called "Animal" with a method called "speak" that prints "The animal makes a sound".
# Create a subclass called "Dog" that overrides the "speak" method to print "The dog barks".
# Create an instance of the "Dog" class and call its "speak" method.


class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("The dog barks")


dog = Dog()
dog.speak()  # Output: The dog barks
print()
# 2. Create a class called "Shape" with a method called "area" that raises a NotImplementedError.
# Create subclasses "Circle" and "Rectangle" that implement the "area" method to calculate the area of the respective shapes.
# Create instances of both classes and print their areas.


print('-------------------------------------------------')
print()


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(4, 6)
# Output: Circle area: 78.53981633974483
print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 24
print()

print('-------------------------------------------------')
print()


# 3. Create a class called "Person" with attributes "name" and "age".
# Create a subclass called "Student" that adds an attribute "student_id".
# Create instances of both classes and print their attributes.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"


person = Person("Alice", 30)
student = Student("Bob", 20, "S12345")
print(person)  # Output: Name: Alice, Age: 30
print(student)  # Output: Name: Bob, Age: 20, Student ID: S12345
print()

print('-------------------------------------------------')
print()


# 4. Create a class called "Vehicle" with a method called "start" that prints "The vehicle is starting".
# Create subclasses "Car" and "Bike" that override the "start" method to print "The car is starting" and "The bike is starting", respectively.


class Vehicle:
    def start(self):
        print("The vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("The car is starting")


class Bike(Vehicle):
    def start(self):
        print("The bike is starting")


car = Car()
car.start()  # Output: The car is starting
bike = Bike()
bike.start()  # Output: The bike is starting
print()

print('-------------------------------------------------')
print()

# 5. Create a class called "Book" with attributes "title" and "author".
# Create a subclass called "EBook" that adds an attribute "file_size".
# Create instances of both classes and print their attributes.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB"


book = Book("The Great Gatsby", "F. Scott Fitzgerald")
ebook = EBook("1984", "George Orwell", 1.5)
print(book)  # Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald
print(ebook)  # Output: Title: 1984, Author: George Orwell, File Size: 1.5 MB
print()

print('-------------------------------------------------')
print()

# 6. Create a class called "Calculator" with methods for addition, subtraction, multiplication, and division.
# Create an instance of the class and perform some calculations.


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b


calculator = Calculator()
print(calculator.add(5, 3))  # Output: 8
print(calculator.subtract(5, 3))  # Output: 2
print(calculator.multiply(5, 3))  # Output: 15
print(calculator.divide(5, 3))  # Output: 1.6666666666666667
print(calculator.divide(5, 0))  # Output: ValueError: Cannot divide by zero
print()

print('-------------------------------------------------')
print()

# 7. Create a class called "Animal" with a method called "speak" that prints "The animal makes a sound".
# Create a subclass called "Cat" that overrides the "speak" method to print "The cat meows".
# Create an instance of the "Cat" class and call its "speak" method.


class Animal():
    def speak(self):
        print('The animal mankes a sound')


class Cat(Animal):
    def speak(self):
        print('The cat Meows')


animal = Animal()
animal.speak()  # Output: The animal makes a sound
cat = Cat()
cat.speak()  # Output: The cat meows
print()


print('-------------------------------------------------')
print()

# 8. Create a class called "Person" with attributes "name" and "age".
# Create a subclass called "Employee" that adds an attribute "employee_id".
# Create instances of both classes and print their attributes.


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name {self.name}, Age: {self.age}'


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}'


person = Person('Alice', 30)
employee = Employee('Bob', 25, 'E12345')

print(person)
print(employee)  # Output: Name: Bob, Age: 25, Employee ID: E12345
print()
print('-------------------------------------------------')

print()


print()

print()
