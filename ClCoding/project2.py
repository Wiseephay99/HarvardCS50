print()


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(
            f'\nTitle: {self.title}, Author: {self.author}, Price: {self.price} \n')

    def update_price(self, new_price):
        self.price = new_price
        print(
            f'The price of the book {self.title} has been updated to ${self.price} \n')


book1 = Book('Python for beginners', 'Wise', 20)
book1.display_details()
book1.update_price(30)
book1.display_details()
print()

#   python coding challenge
for i in range(1, 10, 3):
    print(i)
    if i == 4:
        break

print()


def reverse_a_number(number):
    reversed_number()


print()
