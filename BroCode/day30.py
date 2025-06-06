import math
print()
# classes , inheritance, polymorphism ,encaplaion,


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves Along...')

    def get_info(self):
        print(f'I am a {self.make} {self.model}')

# Inheritance


class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    # method overiding

    def moves(self):
        print('Rumbles along...')


class Airplane(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    # method overiding

    def moves(self):
        print('Flys along...')


class Lamborghini(Vehicle):
    pass


cessna = Vehicle('cessna', 'cessna001')
jeep = Vehicle('Jeep', 'jeepydash')
print('*******************************************')
print(cessna.make)
print(cessna.model)
print()

print(jeep.make)
print(jeep.model)

print()
cessna.moves()
jeep.moves()
print()
skyhawk = Airplane('Skyhawk', 'A380k')
skyhawk.moves()
skyhawk.get_info()
print()
mark_truck = Truck('MarkTruck', 'HeavyLoader')
mark_truck.moves()
mark_truck.get_info()
print()
lamboghini = Lamborghini('lamborghini', 'l0590')
lamboghini.moves()
lamboghini.get_info()

print()
print('*******************************************')
print()
# Project on classes, polymorphism Inheritance and encapsulation


class BalanceException(error):
    pass


class Bank:
    def __init__(self, acc_name, acc_balance):
        self.acc_balance = acc_balance
        self.acc_name = acc_name

    def display_account(self):
        print(
            f"Acc 💳 '{self.acc_name}' created ✅ : Balance💰: ${self.acc_balance:.2f}")

    def deposit(self, amount):
        self.amount = amount
        self.acc_balance += amount
        print(
            f'Successfully ✅ Deposited: {amount:.2f} \nAcc Balance 💰: ${self.acc_balance:.2f}')

    def vaiable_transaction(self, amount):
        if amount > self.acc_balance:
            return
        else:
            raise Exception


dave = Bank('Dave', 1000)
dave.display_account()

sarah = Bank('Sarah', 2000)
sarah.display_account()
print()

wise = Bank('Wise', 1000)
wise.display_account()
wise.deposit(100)

print()
