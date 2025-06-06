import sys
import time
import random
print()

'''# ere is an example of a program that uses classes to manage a library system


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return f"You borrowed '{self.title}'. "
        return f"'{self.title}' is currently unavailable!."

    def return_book(self):
        self.copies += 1
        return f"You returned '{self.title}'. "

    def __str__(self):
        return f"'{self.title}' by {self.author} - Copies available: [self.copies]"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = []

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        return f"Added {copies} copies of {title}."

    def borrow_book(self, title):
        if title in self.books:
            self.borrowed_books.append(self.books[title])
            return self.books[title].borrow()
        return f"'{title} is not available int the library.' "

    def return_book(self, title):
        if title in self.books:
            return self.books[title].return_book()
        return "\n".join(str(book) for book in self.books.values())

    def view_books(self):
        if not self.books:
            return f'No books available in the Library.'
        return "\n".join(str(book) for book in self.books.values())

    def view_borrowed_books(self):
        if not self.borrowed:
            return 'No Books Borrowed.'
        return "\n".join(f"'{book.title}' by {book.author}" for book in self.borrowed)


def main():
    library = Library()
    while True:
        print('📚 Library Menu 🗽')
        print('1. Add Book 📚')
        print('2. Borrow Book 📙')
        print('3. Return Book  📗')
        print('4. View Books 📘')
        print('5. Borrowed Books 📔📚')
        print('0. Exit 📕')

        choice = input('\nSelect your choice: ')
        if choice.lower() == 'q':
            break
        if choice == "1":
            title = input('Enter book title:  ')
            author = input('Enter book author:  ')
            copies = int(input('Enter number of copies:  '))
            print(library.add_book(title, author, copies))

        elif choice == '2':
            title = input('Enter book title to borrow:  ')
            print(library.borrow_book(title))

        elif choice == '3':
            title = input('Enter book title to borrow:  ')
            print(library.return_book(title))

        elif choice == "4":
            print('Books in the Library')
            print(library.view_books())

        elif choice == "5":
            print(library.borrowed_books)

        elif choice == "0":
            print('Borrowed Books:')
            print(library.view_borrowed_books())
            break
        else:
            print('Ivalid choice. Please Try Again!! ')
            continue

    print('\nThanks for using Python Library.\n')


if __name__ == "__main__":
    main()'''
###########################################################################################
###########################################################################################
# Here's an example of a program that uses classes to manage a library system.

'''
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1

            return f"You borrowed '{self.title}'. "
        return f"'{self.title}' is currently unavailable. "

    def return_book(self):
        self.copies += 1
        return f"You returned '{self.title}'. "

    def __str__(self):
        return f"'{self.title}' by {self.author} - Copies available: {self.copies}"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = []

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        return f"Added ✅ {copies} copies of '{title}'"

    def borrow_book(self, title):
        if title in self.books:
            self.borrowed_books.append(self.books[title])
            return self.books[title].borrow()
        return f"'{title}' is not available in the library."

    def return_book(self, title):
        if title in self.books:
            return self.books[title].return_book()
        return f"'{title}' does not belong to this library "

    def view_books(self):
        if not self.books:
            return 'No books available in the Library'
        print('-------- BOOKS AVAILABLE --------')
        return "\n".join(str(book) for book in self.books.values())

    #   def borrowed_books(self):
    #         # borrowed = [book.title for book in self.books.values()
    #         #             if book.copies < 1]
    #         if not self.borrowed_books:
    #             return "No books are currently borrowed."
    #         for book in self.borrowed_books:
    #             return book
    #         # return "Borrowed books:\n" + "\n".join(borrowed)
    #

    def view_borrowed_books(self):
        if not self.borrowed_books:
            return 'No Books Borrowed.'
        print('-------- BOOKS BORROWED --------')
        return "\n".join(f"'{book.title}' by {book.author}" for book in self.borrowed_books)


def main():
    library = Library()
    print('Welcome To Python Library ')
    while True:
        print('Library Menu')
        print('1. Add Book')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. View Books in Library')
        print('5. View Brrowd Books')
        print('6. Exit or Q to Quit')

        choice = input('\nSelect your choice:  ')
        if choice.lower() == 'q':
            break
        if choice == "1":
            title = input('Enter your title: ')
            author = input('Enter book author:  ')
            copies = int(input('Enter number of copies:  '))
            print(library.add_book(title, author, copies))

        elif choice == "2":
            title = input('Enter bok title to borrow:  ')
            print(library.borrow_book(title))

        elif choice == '3':
            title = input('Enter book title to return:  ')
            print(library.return_book(title))

        elif choice == "4":
            print('Books in Library')
            print(library.view_books())

        elif choice == "5":
            print(library.view_borrowed_books())

        elif choice == "6":
            print('Exiting Program. Goodbye!')
            break

        else:
            print('Invalid choice. Please try again!\n')
            continue

    print('Thanks for using Python Library\n')


if __name__ == "__main__":
    main()
'''

###########################################################################################
###########################################################################################
'''
# Here is an example of a program that uses classes to manage a student grading system.

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print('--------------------------------------')
            return f'Grade {grade} added for {self.name}.'
        return f"Invalid Gade. Please enter a value between 0 and 100."

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        print('--------------------------------------')
        return f"Student Id: {self.student_id}, Name: {self.name}, Average Grade: {self.calculate_average():.2f}"


class GradingSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            return 'Student ID already exists.'
        self.students[student_id] = Student(student_id, name)
        return f'Student {name} added ✅ with ID {student_id}.'

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            return self.students[student_id].add_grade(grade)
        return 'Student not Found'

    def view_students(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])
        return "Student not Found"

    def view_all_students(self):
        if not self.students:
            return 'No students registered in this class!'

        print('--------------------------------------')
        return "\n".join(str(student) for student in self.students.values())


def main():
    grading_system = GradingSystem()
    print('Welcome to Python School Grading System')
    while True:
        print('-------------- Grading System Menu -------------- ')
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student")
        print("4. View All Students")
        print("0. Exit")

        choice = input('Enter your choice:  ')
        if choice.lower() == "q":
            break
        if choice == "1":
            student_id = input("Enter student ID:  ")
            name = input('Enter student name:  ')
            print(grading_system.add_student(student_id, name))

        elif choice == "2":
            student_id = input("Enter student ID:  ")
            grade = float(input('Enter grade: '))
            print(grading_system.add_grade(student_id, grade))

        elif choice == "3":
            student_id = input("Enter student ID:  ")
            print(grading_system.view_students(student_id))
        elif choice == "4":
            print('-------------- All Students--------------')
            print(grading_system.view_all_students())
        elif choice == "0":
            print('Exiting program. Goodbye')
            break

        else:
            print('Invalid choice. Please try again.')
            continue
    print('\nThanks for using Python Grading System.\n')


if __name__ == "__main__":
    main()

'''
###########################################################################################
###########################################################################################

'''
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.status = False  # Initialize status as False (not borrowed)

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            self.status = True
            return f"You borrowed the book: '{self.title}' \n"
        return f"'{self.title}' is currently not available in the library\n"

    def return_book(self):
        self.copies += 1
        self.status = False
        return f"You returned the book: '{self.title}' \n"

    def __str__(self):
        return f"{self.title} by {self.author} Copies available: {self.copies}"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        return f"Added ✅ {copies} copies of the book '{title}' by {author}"

    def borrow_book(self, title):
        if title in self.books:
            self.borrowed_books[title] = self.books[title]
            return self.books[title].borrow()
        return f'{title} is not available in the library.'

    def return_book(self, title):
        if title in self.books:
            return self.books[title].return_book()
        return f"'{title}' is not available in the library\n"

    def view_books(self):
        if not self.books:
            return f"No books in Library Currently\n"
        return "\n".join(str(book) for book in self.books.values())

    def view_borrowed_books(self):
        if not self.borrowed_books:
            return "No books borrowed Currently"
        return "\n".join(f"'{book.title}': status: {'Borrowed' if book.status else 'Available'}" for book in self.borrowed_books.values())


def main():
    library = Library()
    print('Welcome to Python Online Library')
    while True:
        print('------- Python Library Menu -------')
        print('1. Add Book')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. View Books in the Library')
        print('5. View Borrowed Books')
        print('0. Q to Quit or Exit')

        choice = input('\nSelect your choice:  ')
        if choice.lower() == "q":
            break

        if choice == "1":
            title = input('Enter book Title:  ')
            author = input('Enter book author:  ')
            copies = int(input('Enter number of copies:  '))
            print(library.add_book(title, author, copies))

        elif choice == "2":
            title = input('Enter book title to borrow:  ')
            print(library.borrow_book(title))

        elif choice == "3":
            title = input('Enter book title to return:  ')
            print(library.return_book(title))

        elif choice == "4":
            print(library.view_books())

        elif choice == "5":
            print(library.view_borrowed_books())

        elif choice == "0":
            break

        else:
            print('Invalid Choice!! Olease Try Again Later!!')
            continue

    print('\nThanks for using Python Online Library\n')


if __name__ == "__main__":
    main()
'''
###########################################################################################
###########################################################################################
'''

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        status = False

    def borrow(self):
        if self.copies > 0:
            self.copies += 1
            status = True
            return f"You borrowed {self.title}\n"
        return f"Book {self.title} currently not available"

    def return_book(self):
        self.copies += 1
        status = False
        return f"You returned {self.title}\n"

    def __str__(self):
        return f"{self.title} by {self.author}. Copies available: {self.copies}"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
        return f"Added ✅ {copies} copies of {title} by {author}\n"

    def borrow_book(self, title):
        if title in self.books:
            return self.books[title].borrow()
        return f"book '{title}' currently not availbale \n "

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book()
        return f"Book '{title}' doe not belong in this library. \n"

    def view_books(self):
        if not self.books:
            return f'No books in the Library'
        return "\n".join(str(book) for book in self.books.values())

    def view_borrowed_books(self):
        if not self.borrowed_books:
            return f'No books borrowed currently\n'
        return '\n'.join(f"Book: '{book.title}', status: {'Borrowed' if book.status else 'Available'}" for book in self.borrowed_books())

return "\n".join(f"Book: '{book.title}', Status: {'Borrowed' if getattr(book, 'status', False) else 'Available'}" for book in self.borrowed_books.values())
return "\n".join(f"Book: '{book.title}', Borrowed Copies: {count}" for book, count in self.borrowed_books.items())

def main():
    library = Library()
    while True:
        print('Library Menu')
        print('1. Add Book')
        print('2. Borrow Book')
        print("3. Return Book")
        print('4. View Book')
        print("5. View Borrowed Books")
        print('0. Exit or Q to Quit')

        choice = input('\nSelect your choice 0-5 : ')
        if choice.lower() == "q":
            break
        if choice == "1":
            title = input('Enter book title:  ')
            author = input('Enter author of the book: ')
            copies = int(input('Enter number of book copies:  '))
            print(library.add_book(title, author, copies))

        elif choice == "2":
            title = input('Enter book title:  ')
            print(library.borrow_book(title))
        elif choice == "3":
            title = input('Enter book title:  ')
            print(library.return_book(title))
        elif choice == "4":
            print(library.view_books())
        elif choice == "5":
            print(library.view_borrowed_books())
        elif choice == "0":
            break
        else:
            print('Invalid choice!! Please Try Again Later!! ')
            continue

    print('\nThanks for using Python Library\n')


if __name__ == "__main__":
    main()

'''
###########################################################################################
###########################################################################################

'''
questions = (
    ('How many planets are there in the solar system? '),
    ('When did Kenya gain Independce? '),
    ('How many teeth does an adult human have? '),
    ('Who was the first President of Kenya? '),
    ('How many bones does an adult human being have? '),
    ('Which is the largest planet in the solar system? ')
)
options = (
    ('A. 10', 'B. 9', 'C. 8', 'D. 7', 'E. 11'),
    ('A. 1960', 'B. 1963', 'C. 1964', 'D. 1966', 'E. 1962'),
    ('A. 32', 'B. 30', 'C. 28', 'D. 36', 'E. 34'),
    ('A. Kibaki', 'B. Moi', 'C. Kenyatta', 'D. Raila', 'E. Ruto'),
    ('A. 109', 'B. 110', 'C. 112', 'D. 108', 'E. 104'),
    ('A. Neptune', 'B. Pluto', 'C. Jupiter', 'D. Mars', 'E. Venus'),
)
question_num = 0
guesses = []
correct_answers = ['B', 'B', 'A', 'C', 'A', 'C']
score = 0
total = 0
for question in questions:
    print('---------------------------------------------')
    print(question)

    for option in options[question_num]:
        print(option)

    choices = ['A', 'B', 'C', 'D', 'E']
    while True:
        choice = input('Choose your answer (A B C D E): ').upper()
        if choice not in choices:
            print('Invalid choice Only choose A B C D or E!')
            continue
        guesses.append(choice)
        if choice == correct_answers[question_num]:
            print('Correct Answer ✅✅\n')
            score += 1
            break
        else:
            print('Wrong Answer ❌❌ \n')
            break
    question_num += 1

print('Answers: ', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print('Correct Answers: ', end=" ")
for answer in correct_answers:
    print(answer, end=' ')
print()

total += score
print('Results')
result = (total / len(questions) * 100)
print(f'You Scored: {result:.2f}%\n')
'''

###########################################################################################
###########################################################################################

'''
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"Grade {grade} added for {self.name}."
        return "Invalid grade. Please enter a value between 0 and 100."

    def calculate_avaerage(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Average Grade: {self.calculate_avaerage():.2f}"


class GradingSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name):
        if student_id in self.students:
            return "Student ID already exists."
        self.students[student_id] = Student(student_id, name)
        return f"Student {name} added with ID {student_id}."

    def add_grade(self, student_id, grade):
        if student_id in self.students:
            return self.students[student_id].add_grade(grade)
        return 'Student not found'

    def view_student(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])
        return "Student not found."

    def view_all_students(self):
        if not self.students:
            return "No students available."
        return "\n".join(str(student) for student in self.students.values())


def main():
    grading_system = GradingSystem()
    while True:
        print('\nGrading System Menu:')
        print('1. Add Student')
        print('2. Add Grade')
        print('3. View Student')
        print('4. View All Students')
        print('0. Exit')

        choice = input('Enter your choice: ')
        if choice.lower() == "q":
            break
        if choice == "1":
            student_id = input('Enter student ID: ')
            name = input('Enter student name:  ')
            print(grading_system.add_student(student_id, name))

        elif choice == "2":
            student_id = input('Enter student ID:  ')
            grade = float(input('Enter Grade:  '))
            print(grading_system.add_grade(student_id, grade))

        elif choice == "3":
            student_id = input('Enter student ID:  ')
            print(grading_system.view_student())

        elif choice == "3":
            student_id = input('Enter student ID:  ')
            print(grading_system.view_all_students())

        elif choice == "4":
            print('Exiting Program. Goodbye!')
            break

        else:
            print('Invalid choice Please try again')


if __name__ == "__main__":
    main()'''

###########################################################################################
###########################################################################################

# Here is an example of a program that uses classes to manage an inventory system.

'''
class Item:
    def __init__(self, item_id, name, quantity, price):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
            return f'Added {amount} unit of {self.name} to invetory.'
        return f'Invalid Stock amount.Please enter a positive number'

    def remove_stock(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            return f"Removed {amount} units of {self.name} from inventory"
        return 'Invalid stock amount or insufficient stock.'

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price:.2f}"


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            return 'item ID already exists.'
        self.items[item_id] = Item(item_id, name, quantity, price)
        return f'Item {name} added with ID {item_id} and Quantity {quantity}'

    def update_stock(self, item_id, amount, add=True):
        if item_id in self.items:
            if add:
                return self.items[item_id].add_stock(amount)
            else:
                return self.items[item_id].remove_stock(amount)
        return 'Item not found in inventory.'

    def remove_stock(self, item_id, amount, add=False):
        if item_id in self.items:
            if add:
                return self.items[item_id].add_stock(amount)
            else:
                return self.items[item_id].remove_stock(amount)
        return 'Item not found in inventory.'

    def view_item(self, item_id):
        if item_id in self.items:
            return str(self.items[item_id])
        return 'Item not found in inventory.'

    def view_all_items(self):
        if not self.items:
            return 'no items in Invenntory.'
        return "\n".join(str(item) for item in self.items.values())


def main():
    inventory = Inventory()
    print("Inventory Management System")
    while True:
        print("\nInventory Menu")
        print('1. Add Item')
        print('2. Add Stock')
        print('3. Remove Stock')
        print('4. View Item')
        print('5. View All Items')
        print('0. Exit')

        choice = input('\nSelect your choice: ')
        if choice.lower() == "q":
            break

        if choice == "1":
            item_id = input('Enter item ID:  ')
            name = input('Enter item name:  ')
            quantity = int(input('Enter item Quantity: '))
            price = float(input('Enter item price:   '))
            print(inventory.add_item(item_id, name, quantity, price))

        elif choice == "2":
            item_id = input('Enter item ID:  ')
            amount = int(input('Enter amount to add:  '))
            print(inventory.update_stock(item_id, amount, add=True))

        elif choice == "3":
            item_id = input('Enter item ID:  ')
            amount = int(input('Enter amount to remove:  '))
            print(inventory.remove_stock(item_id, amount, add=False))

        elif choice == "4":
            item_id = input('Enter item ID:  ')
            print(inventory.view_item(item_id))

        elif choice == "5":
            print(inventory.view_all_items())

        elif choice == "0":
            break

        else:
            print('Invalid choice!! Please tyr again!!')

    print('\nThanks for using Inventory Management System.')
    print('Exiting program .Goodbye!\n')


if __name__ == "__main__":
    main()
'''

###########################################################################################
###########################################################################################

# Here's an example of a program that uses classses to manage a to-do list application.

'''
class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True
        return f"Task '{self.description}' marked as completed."

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, description):
        if task_id in self.tasks:
            return 'Task ID already exists.\n'
        self.tasks[task_id] = Task(task_id, description)
        return f"Task '{description}' added with ID {task_id}\n"

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            return self.tasks[task_id].mark_completed()
        return "Task not found.\n"

    def view_task(self, task_id):
        if task_id in self.tasks:
            return str(self.tasks[task_id])
        return "Task Not Found\n"

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return f"Task ID {task_id} deleted.\n"
        return "Task not Found\n"

    def view_all_tasks(self):
        if not self.tasks:
            return "No tasks available.\n"
        return "\n".join(str(book) for book in self.tasks.values())


def main():
    todo_list = ToDoList()
    print('Welcome to Python To-Do List Application')
    while True:
        print('To-Do List Menu:')
        print('1. Add Task')
        print('2. Mark Task as completed')
        print("3. Delete Task")
        print('4. View All Tasks')
        print('5. View Task')
        print('0. Exit')
        choice = input('Enter your choice:  ')

        if choice.lower() == "q":
            break
        if choice == "1":
            task_id = input('Enter task ID:  ')
            description = input('Enter task description:  ')
            print(todo_list.add_task(task_id, description))

        elif choice == "2":
            task_id = input('Enter task ID:  ')
            print(todo_list.mark_task_completed(task_id))

        elif choice == "3":
            task_id = input('Enter task ID:  ')
            print(todo_list.delete_task(task_id))

        elif choice == "4":
            print('All Tasks:')
            print(todo_list.view_all_tasks())

        elif choice == "5":
            task_id = input('Enter task ID:  ')
            print(todo_list.view_task(task_id))

        elif choice == "0":
            break
        else:
            print('Invalid choice!! Please try again!!')
            continue

    print('\nThanks for using Python To-Do List Application \n')


if __name__ == "__main__":
    main()

'''

###########################################################################################
###########################################################################################


class Book:
    def __init__(self,  title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        status = False

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return f'You Borrowed the book {self.title}\n'
        return f'No copies currently available in the library'

    def return_book(self):
        self.copies += 1
        return f"You returned the book {self.title}\n"

    def __str__(self):
        return f"Book: {self.title} by {self.title}: Copies Available: {self.copies}\n"


class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = []

    def add_book(self, title, author, copies):
        if title in self.books:
            self.books[title].copies += copies
            return F'You added {copies} of the book {title}\n'
        else:
            self.books[title] = Book(title, author, copies)
        return f'Added {copies} copies of {title}.\n'

    def borrow_book(self, title):
        if title in self.books:
            self.borrowed_books.append(self.books[title])
            return self.books[title].borrow()
        return f"'{title} is not available in the library.\n"

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_books()
        return f"'{title}' does not belong to this library.\n"

    def view_book(self, title):
        if title in self.books:
            return str(self.books[title])
        return f"'{title}' not found in the library.\n"

    def view_books(self):
        if not self.books:
            return 'No books currently available in the library\n'
        print('-------- BOOKS AVAILABLE --------')
        return f'\n'.join(str(book) for book in self.books.values())

    def view_borrowed_books(self):
        if not self.borrowed_books:
            return 'No books borrowed currently for now in the library\n'
        print('-------- BOOKS BORROWED --------')
        return f'\n'.join(f"{book.title} by {book.author} " for book in self.borrowed_books)
        # return f"'{self.title}' by {self.author} - Copies available: {self.copies}\n"

    # def view_borrowed_books(self):
    #     if not self.borrowed_books:
    #         return 'No books borrowed currently for now in the library\n'
    #     print('-------- BOOKS BORROWED --------')
    #     return "\n".join(f"'{book.title}' by {book.author}" for book in self.borrowed_books)


def main():
    library = Library()
    print('Welcome to Python Library')
    while True:
        print('Library Menu ')
        print('1. Add Book')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Search Book')
        print('5. View Books in the Library')
        print('6. View Borrowed Books')

        choice = input('\nSelect your choice? ')
        if choice.lower() == "q":
            break
        if not choice.isdigit():
            print('Invalid choice Please enter 1-5')
            continue

        if choice == "1":
            title = input('Enter book title?  ')
            author = input('Enter name of author:  ')
            copies = int(input('Enter number of copies:  '))
            print(library.add_book(title, author, copies))

        elif choice == "2":
            title = input('Enter book title?  ')
            print(library.borrow_book(title))

        elif choice == "3":
            title = input('Enter book title?  ')
            print(library.return_book(title))

        elif choice == "4":
            title = input('Enter book title?  ')
            print(library.view_book(title))

        elif choice == "5":
            print(library.view_books())

        elif choice == "6":
            print(library.view_borrowed_books())

        else:
            print('Invalid Choice!! Please Try Again!! \n')
            continue
    print('\nThanks for using Python Library\n')
