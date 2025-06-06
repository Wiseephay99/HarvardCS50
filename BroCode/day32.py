import time
import random
import math
print()


class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.acc_name = acc_name
        print(
            f"Account '{self.acc_name}' created ✅ . Balance 💰 : ${self.balance:.2f}")

    def get_balance(self):
        print(f"Account 🏦 '{self.acc_name}' Balance 💵: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Balance 💵: ${self.balance:.2f}')
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nInsufficient balance for the transaction.\nAccount '{self.acc_name}' has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('Withdrawal Complete ✅')
            print(
                f"Successfully Deposited 💳 ${amount:.2f} to  '{self.acc_name}' ")
            self.get_balance()
        except BalanceException as error:
            print(f'Withdraw Interrupted. \n{error}')

    def transfer(self, amount, account):
        try:
            print('***********\n\nBeginning Transfer.. 🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed ✅\n\n*****************')
        except BalanceException as error:
            print(f'\nTransfer Interrupted. ❌')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit complete')
        self.get_balance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw Completed')
            self.get_balance()
        except BalanceException as error:
            print(f'\n\nWithdraw Interrupted: {error}')


dave = BankAccount(30000, 'Dave')
sarah = BankAccount(40000, 'Sarah')

print()
dave.get_balance()
sarah.get_balance()

print()
dave.deposit(200)
sarah.deposit(3000)

print()
dave.withdraw(10000)
sarah.withdraw(300)

print()
dave.transfer(10000, sarah)
print()

Jane = InterestRewardsAcct(1000, 'Jim')
Jane.get_balance()
Jane.deposit(100)
Jane.transfer(100, dave)
print()
Blaze = SavingsAcct(1000, 'Blaze')
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(1000, sarah)
