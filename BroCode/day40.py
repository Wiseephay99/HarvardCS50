import time
import sys
from enum import Enum
import random
print()

'''
#   Shopping Cart Program

def display_cart(cart):
    if not cart:
        print('You have no items in your cart')
    else:
        print(f'\n************** SHOPPING CART **************\n')
    total = 0
    for item in cart:
        print(f"{item['name']}: ${item['price']:.2f}")
        total += item['price']
    print(f'\nTotal Bill: {total:.2f}')
    print(f'******************************************\n')


def add_item(cart):
    print('\nAdd Items you want')
    item_name = input('Enter item name (q to quit): ')
    while not item_name == 'q':
        if item_name == 'q':
            break
        item_price = float(input(f"Enter {item_name}'s price: "))
        item = {
            'name': item_name,
            'price': item_price, }
        cart.append(item)
        print(f"{item['name']} added ✅ to cart")
        item_name = input('Enter another item name (q to quit): ')
        continue
    return cart, item


def main():
    cart = []
    print('Welcome to Python Shopping  🛍️')
    while True:
        print('1. Add Item/s to cart 🛒')
        print('2. Remove Item/s from cart 🛒')
        print('3. Display Cart 🏪')
        print('0. Exit')
        choice = input('\nSelect your choice (0-3):  ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice!')
            continue
        choice = int(choice)
        if choice == 1:
            cart = add_item(cart)
        elif choice == 2:
            if not cart:
                print('Your Cart is already empty!!')
            else:
                display_cart(cart)
                item_index = int(
                    input('Enter the item number to remove: ')) - 1
                if 0 <= item_index < len(cart):
                    removed_item = cart.pop(item_index)
                    print(f"{removed_item['name']} removed from cart")
                else:
                    print('Invalid Item Number!')
        elif choice == 3:
            display_cart(cart)
        elif choice == 0:
            break
        else:
            print('Invalid Choice! Please select a valid option')

    print('\nThanks for using Python Shopping!!')
    print('Exiting the Application  \n')


if __name__ == "__main__":
    main()
'''

###########################################################################################
###########################################################################################
###########################################################################################
'''

def display_cart(cart):
    total = 0
    if not cart:
        print('No items in your to cart!')
    print('*****************🛒 CART 🛒*****************')
    for i, item in enumerate(cart, start=1):
        print(f'{item['name']:10}: ${item['price']:.2f}')
        total += item['price']
    print()
    print(f'Total Bill: {total:.2f}')
    print('*********************************************')


def view_cart(cart):
    if not cart:
        print('No items in cart')

    else:
        print(f'\n****************** YOUR CART ******************')
        for i, item in enumerate(cart, start=1):
            print(f'{i}. {item['name']:10}: {item['price']:.2f}')
        print('\n*********************************************')


def add_item(cart):
    print(f'\n🛍️  Add Items to Shopping Cart  🛍️')
    while True:
        item_name = input('\nEnter name of item (q to quit):  ')
        if item_name == 'q':
            break
        try:
            item_price = float(input(f'Enter price of {item_name}:  '))
        except ValueError as e:
            print('Invalid Price value!!! ❌')
            continue
        item = {
            'name': item_name,
            'price': item_price
        }
        cart.append(item)
        print(f"{item['name']} added ✅ to cart 🛒 ")

    return cart


def remove_item(cart):
    if not cart:
        print('Your Cart is already empty!!')
    else:
        view_cart(cart)
        iten_num = int(
            input('Enter item number to remove (q to quit):  ')) - 1

        if 0 <= iten_num <= len(cart):
            removed_item = cart.pop(iten_num)
            print(f"{removed_item['name']} removed ❌ from cart 🛒")
            return cart
        else:
            print('Invalid Item Number')


def main():
    cart = []
    print(f'Welcome to Python Shopping Store 🛒')
    while True:
        print('1. Add Item(s) to cart 🛍️')
        print('2. Remove Item(s) to cart 🧺')
        print('3. Display Cart 🛒')
        print('4. View Cart 🛒')
        print('0. Exit ❌')

        choice = input('\nSelect your choice (0-4):   ')
        if choice.lower() == 'q':
            break
        if not choice.isdigit():
            print('Invalid Choice!!')
            continue
        choice = int(choice)
        if choice == 1:
            cart = add_item(cart)
        elif choice == 2:
            remove_item(cart)
        elif choice == 3:
            display_cart(cart)
        elif choice == 4:
            view_cart(cart)
        elif choice == 0:
            break
        else:
            print('Invalid choice!!❌ Please select 1 , 2, 3, 4 or 0')

    print('\nExiting Application')
    print('Thanks for using Python Shopping Store 🛒\n')


if __name__ == "__main__":
    main()
'''

###########################################################################################
###########################################################################################
###########################################################################################

'''
questions = (
    'Which year did Kenya gain Independece ?',
    'How many planets are there in there in the solar system? ',
    'How many teeth does and adult human being have? ',
    'How many Bones are there in the Human Body? ',
    'USA has how many states? '
)
options = (
    ('A. 1968', 'B. 1963', 'C. 1964', 'D. 1965'),
    ('A. 9', 'B. 10', 'C. 11', 'D. 8'),
    ('A. 28', 'B. 32', 'C. 34', 'D. 30'),
    ('A. 110', 'B. 108', 'C. 109', 'D. 107'),
    ('A. 51', 'B. 52', 'C. 48', 'D. 50'),
)
question_num = 0
guesses = []
guess = 0
correct_answers = ['B', 'A', 'B', 'A', 'D']
score = 0
total = 0

for i, question in enumerate(questions, start=1):
    print(f'{i}. {question}')

    for option in options[question_num]:
        print(option)

    choices = ['A', 'B', 'C', 'D']
    guess = input('\nSelect your choice: (A B C or D):  ').upper()
    if guess not in choices:
        print('Invalid choice!!')
        continue
    if guess == correct_answers[question_num]:
        print('Correct Guess ✅\n')
        score += 1
    else:
        print('Incorrect Guess ❌\n')

    guesses.append(guess)
    question_num += 1

print()
print('Answers: ', end=" ")
for answer in correct_answers:
    print(answer, end=' ')
print()

print('Guesses: ', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print('\n************ RESULTS ************')

total += score
result = score / len(questions) * 100
print(f'You Scored: {result}%')
print('**********************************\n')

'''

###########################################################################################
###########################################################################################
###########################################################################################

'''
questions = (
    'Which year did Kenya gain Independece ?',
    'How many planets are there in there in the solar system? ',
    'How many teeth does and adult human being have? ',
    'How many Bones are there in the Human Body? ',
    'USA has how many states? '
)
options = (
    ('A. 1968', 'B. 1963', 'C. 1964', 'D. 1965'),
    ('A. 9', 'B. 10', 'C. 11', 'D. 8'),
    ('A. 28', 'B. 32', 'C. 34', 'D. 30'),
    ('A. 110', 'B. 108', 'C. 109', 'D. 107'),
    ('A. 51', 'B. 52', 'C. 48', 'D. 50'),
)
question_num = 0
guesses = []
guess = 0
correct_answers = ['B', 'A', 'B', 'A', 'D']
score = 0
total = 0

for i, question in enumerate(questions, start=1):
    print(f'{i}. {question}')

    for option in options[question_num]:
        print(option)

    choices = ['A', 'B', 'C', 'D']
    while True:
        guess = input('\nSelect your choice: (A B C or D):  ').upper()
        if guess not in choices:
            print('Invalid choice!!')
            continue
        if guess == correct_answers[question_num]:
            print('Correct Guess ✅\n')
            score += 1
            break
        else:
            print('Incorrect Guess ❌\n')
            break

    guesses.append(guess)
    question_num += 1

print()
print('Answers: ', end=" ")
for answer in correct_answers:
    print(answer, end=' ')
print()

print('Guesses: ', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print('\n************ RESULTS ************')

total += score
result = score / len(questions) * 100
print(f'You Scored: {result}%')
print('**********************************\n')
'''

###########################################################################################
###########################################################################################
###########################################################################################


'''questions = (
    "How many days are there in a week?",
    "How many planets are there in the solar system?",
    'How many states does the USA have?',
    'Which year did Kenya gain independence?',
    'How many couties are there in Kenya?'
)
answers = (
    ("A. 5", "B. 6", "C. 7", "D. 8", "E. 10"),
    ("A. 5", "B. 8", "C. 9", "D. 6", "E. 7"),
    ("A. 50", "B. 51", "C. 45", "D. 52", "E. 55"),
    ("A. 1963", "B. 1964", "C. 1965", "D. 1966", "E. 1962"),
    ("A. 45", "B. 46", "C. 47", "D. 48", "E. 50")
)

correct_answers = ['C', 'C', 'A', 'A', 'C']
question_num = 0
guess = 0
guesses = []
score = 0

for i, (question) in enumerate((questions), start=1):
    print('---------------------------------------')
    print(f'{i}. {question}')

    for answer in answers[i-1]:
        print(answer)
    print()

    choices = ['A', 'B', 'C', 'D', 'E']
    while True:
        guess = input('Enter your answer: A B C D E:  ').upper()
        if guess not in choices:
            print('Invalid choice..')
            continue

        guesses.append(guess)

        if guess == correct_answers[i-1]:
            score += 1
            print('CORRRECT ANSWER')
            break
        else:
            print('INCORRECT ANSWER')
            break
    question_num += 1
    print()
print()
print('--------------------RESULTS-------------------')
print('Guesses:', end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print('Answers:', end=" ")
for correct_answer in correct_answers:
    print(correct_answer, end=" ")
print()

score = (score / len(questions) * 100)
print(f'You Scored {score:.2f}%')
print('---------------------------------------\n')
'''


###########################################################################################
###########################################################################################
###########################################################################################
'''
print()

questions = (
    '1. How many days are there in a week?',
    '2. How many teeth does an adult Human have?',
    '3. When did Kenya gain independce',
    '4. Who was the first president of Kenya?',
    '5. How many planets are there in the solar system?',
)

answers = (
    ('A. 5', 'B. 7', 'C. 8', 'D. 6'),
    ('A. 34', 'B. 36', 'C. 32', 'D. 38'),
    ('A. 1963', 'B. 1964', 'C. 1964', 'D. 1965'),
    ('A. Kibaki', 'B. Moi', 'C. Kenyatta', 'D. Zakayo'),
    ('A. 10', 'B. 6', 'C. 7', 'D. 9'),
)


question = 0
guess = 0
guesses = []
corrrect_answers = ['B', 'C', 'A', 'C', 'D']

for i, question in enumerate(questions, start=1):
    print('---------------------------------------')
    print(question)

    for line in answers[i - 1]:
        print(line)
    print()

    choices = ['A', 'B', 'C', 'D']
    while True:
        guess = input('Choose your answer (A/B/C/D): ').upper()

        if guess not in choices:
            print('Invalid choice')
            continue

        guesses.append(guess)

        if guess == corrrect_answers[i - 1]:
            print('Correct Answer')
            break
        else:
            print('Incorrect Answer')
            break

    print()  # Add a blank line for better readability before the next question

print('---------------------------------------')
print(f'Guesses: {str(guesses)}')
print('---------------------------------------')
print(f'Correct Answers: {str(corrrect_answers)}')
print('---------------------------------------')

'''

###########################################################################################
###########################################################################################
###########################################################################################

questions = (
    'How many states are there in the USA ? ',
    'How many planets are there in the solar system ? ',
    'Which year did Kenya gain independence ? ',
    'Which is the largest planet in the solar system ? ',
    'How many teeth does an adult human being have ? ',
)
options = (
    ('A. 51', 'B. 50', 'C. 48', 'D. 52', 'E. 49'),
    ('A. 10', 'B. 11', 'C. 9', 'D. 8', 'E. 12'),
    ('A. 1952', 'B. 1964', 'C. 1968', 'D. 1963', 'E. 1965'),
    ('A. Mercury', 'B. Venus', 'C. Jupiter', 'D. Neptune', 'E. Pluto'),
    ('A. 32', 'B. 30', 'C. 31', 'D. 34', 'E. 28')
)

questions_num = 0
correct_answers = ['B', 'C', 'D', 'C', 'A']
guess = 0
guesses = []
score = 0


for i, question in enumerate(questions, start=1):
    print('-------------------------------------------------')
    print(f'{i}. {question}')

    for option in options[questions_num]:
        print(option)
    print()
    choices = ['A', 'B', 'C', 'D', 'E']
    guess = input('Choose your answer? (A B C D E):  ').upper()
    if guess not in choices:
        print('Invalid Answer!')

    guesses.append(guess)

    if guess == correct_answers[questions_num]:
        print('Correct Answer ✅ ')
        score += 1
    else:
        print('Incorrect Answer ❌ ')

    questions_num += 1

print()
print('**********************************\n')

print('Answers: ', end=" ")
for answer in correct_answers:
    print(answer, end=" ")
print()
print('Guesses: ', end=" ")
for guess in guesses:
    print(guess, end=" ")

print()
print('\n*********** RESULTS ***********')
result = (score / len(questions) * 100)
if result == 100:
    print('🎉🎉🎉Congrats you scored 💯 %')
else:
    print(f'Your Score is: {result:.2f}%')
print('**********************************\n')
