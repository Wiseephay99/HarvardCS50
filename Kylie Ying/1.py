import sys
import random
import time
# Beginner Projects

# Madlibs Insert a word to what you have already

# word = input("\nEnter a word:    ")

# channel_name = word
# madlib = f'Subscribe to {channel_name}...\n'
# print(madlib)


'''========================================================================'''
'''========================================================================'''

'''print()
adj = input('Adjective: ')
verb1 = input('Verb:  ')
verb2 = input('Verb:  ')
famous_person = input('Famous person:  ')
madlib = f"Computer programming is so {adj}!. It makes me so excited all \
    the time beacause I love to {verb1}. Stay Hydrated and {verb2} like you are\
    {famous_person}"

print(madlib)'''


'''========================================================================'''
'''========================================================================'''

# Fake Login

'''username = 'Kylie'
password = 'secretpassword'

print()

username_input = input('Username:   ')
password_input = input('Password:   ')

if username_input == username and password_input == password:
    print('Access Granted')
    print('Please wait....')
    time.sleep(5)
    print('Ok.....Loading....')
    time.sleep(1)
    print(f'....')
    time.sleep(1)
    print('....')
    print(f'Alright you have security clearance.Pulling up the secret mainframe...\n')

elif username_input == username and password_input != password:
    print('Incorrect Password')
elif username_input != username and password_input == password:
    print('Incorrect Username')'''


'''========================================================================'''
'''========================================================================'''
'''# Loops, loops, loops
print()
# While loop
i = 1
while i < 5:
    print(i)
    i += 1
print(f'The end...\n')

# For loop
name = 'wiseephay'

for letter in name:
    print(letter, end=' ')
print()
print()

name = ['subscribe', 'to', 'kylie', 'ying']
for x in name:
    print(x)

print()
print()

adjs = ['shiny', 'purple', 'clear']
nouns = ['coin', 'speaker', 'iphone']

for adj in adjs:
    for noun in nouns:
        print(adj, noun)

print()
print()

#   break and continue
i = 1
while i < 5:
    print(i)

    if i == 3:
        break
    i += 1

print()
print()
i = 1
while i < 5:
    print(i)
    i += 1

    if i == 3:
        continue
'''


'''========================================================================'''
'''========================================================================'''

# Guessing the computer's number....


'''def guess(x):
    computer = random.randint(1, x)
    guess = 0
    while guess != computer:
        # Get the users guess
        guess = input(f'\nGuess a number between 1 and {x}:    ')
        guess = int(guess)
        if guess > computer:
            print('Sorry Guess again....Too High...')
        elif guess < computer:
            print('Sorry Guess again....Too Low...')
    print(
        f'Yay, congrats you have guessed the number {computer} correctly!!\n')


guess(100)


def computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        feedback = input(
            f'\nIs the number {comp_guess} too low(L), too high(H), or correct(C):   ').lower()

        if low != high:
            comp_guess = random.randint(low, high)
        else:
            feedback = low

        if feedback in ['q', 'exit']:
            sys.exit(f'Bye!👋👋\n')

        if feedback == 'h':
            high = comp_guess - 1
        elif feedback == 'l':
            low = comp_guess - 1

        comp_guess = random.randint(1, x)

    print(
        f'Yay, the computer guess your secret number, {computer},  correctly!!\n')


computer(1000)

'''


'''========================================================================'''
'''========================================================================'''
#   classes


# class Beach:
#     # location = 'Cap Cod' # class variable
#     # part = ['water', 'sand']  # class variable
#     # Intilialising a function...

#     def __init__(self, location, water_color, temperature):
#         self.location = location  # instance variable
#         self.water_color = water_color
#         self.temperature = temperature
#         self.heat_rating = 'HOT' if temperature > 80 else 'COOL'
#         self.parts = ['water', 'sand']

#     def add_parts(self, part):  # method class function in class
#         self.parts.append(part)


# print()
# # Initializing an object....
# cap_cod_beach = Beach('Cape Cod', 'dark blue', 70)
# cancun_beach = Beach("Cancun", 'crystal blue', 90)

# print(cap_cod_beach.heat_rating)
# print(cancun_beach.heat_rating)
# print()
# print(cap_cod_beach.location, cancun_beach.location)
# print(cancun_beach.heat_rating, cap_cod_beach.heat_rating)
# print()
# print(cap_cod_beach.parts)
# cap_cod_beach.add_parts('rock')
# print(cap_cod_beach.parts)


'''========================================================================'''
'''========================================================================'''

'''# script using classes


class Beach:

    def __init__(self, location, water_color, temperature):
        self.location = location  # instance variable
        self.water_color = water_color
        self.temperature = temperature
        self.heat_rating = 'HOT' if temperature > 80 else 'COOL'
        self.parts = ['water', 'sand']

    def add_parts(self, part):  # method class function in class
        self.parts.append(part)


def main():
    cap_cod_beach = Beach('Cape Cod', 'dark blue', 70)
    cancun_beach = Beach("Cancun", 'crystal blue', 90)
    cap_cod_beach.add_parts('rock')
    la_beach = Beach('LA', 'turquise', 85)
    italy_beach = Beach('Italy', 'blue', 82)
    italy_beach.add_parts('rock')

    hot_not_rocky = []

    for beach in [cap_cod_beach, cancun_beach, la_beach, italy_beach]:
        if beach.heat_rating == 'HOT' and 'rock' not in beach.parts:
            hot_not_rocky.append(beach)

    return hot_not_rocky


if __name__ == "__main__":
    beaches = main()
    print([beach.location for beach in beaches])
'''


'''========================================================================'''
'''========================================================================'''
#   Inheritance


class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    def bark(self):
        return 'Bark!!'


class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def shedding_amount(self):
        return 0


class GoldenRetriver(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fretch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7

    def bark(self):
        return 'Arf arf!!!'


class GoldenPoodle(Poodle, GoldenRetriver):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return 'AROO AROOO!!!!'


print()

samoyed1 = Samoyed('Sammy', 1, 10)
print(samoyed1.name, samoyed1.age, samoyed1.friendliness)
print(samoyed1.likes_walks())
# print(samoyed1.fetch_ability())

print()
retreiver1 = GoldenRetriver('retriver', 2, 9)
print(retreiver1.name, retreiver1.age, retreiver1.friendliness)
print(retreiver1.likes_walks())


# Multiple Inheritance
goldie = GoldenPoodle('Goldie', 1, 10)
print(goldie.name, goldie.age, goldie.friendliness)
print(goldie.likes_walks())


print(goldie.fretch_ability())  # Muliple Inheritance

print(goldie.shedding_amount())  # Muliple Inheritance

# Polymorphism

generic_dogo = Dog('Gene', 3, 10)
print(generic_dogo.bark())
print(goldie.bark())
print(samoyed1.bark())
print(retreiver1.bark())
