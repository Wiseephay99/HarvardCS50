
import time
print()

print()


class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, account_name, initial_amount, account_type):
        self.account_name = account_name
        self.balance = initial_amount
        self.account_type = account_type
        self.transaction_history = []
        self.transaction_history.append(
            f"Initial deposit: ${initial_amount:.2f} at {time.strftime('%H:%M:%S')}")

    def __str__(self):
        return f"Account '{self.account_name}' created  ✅ \nAccount Type: '{self.account_type}' \nBalance 🤑 : ${self.balance:.2f} \n"

    def get_balance(self):
        print(f"{self.account_name}\'s Account Balance 🤑 : ${self.balance:.2f} \n")

    def deposit(self, amount):
        if amount <= 0:
            print("Error ❌: Deposit amount must be positive.")
            amount = 0
        self.balance += amount
        self.transaction_history.append(
            f"Deposited: {' ':10} ${amount:.2f} at {' ':10} {time.strftime('%Y-%m-%d %H:%M:%S')} ")
        print('Deposit Process Completed ✅')
        print(
            f"Deposited ${amount:.2f} to account '{self.account_name}'. New balance: ${self.balance:.2f}")
        self.get_balance()
        print()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Insufficient Funds! ⛔ {self.account_name}\'s Account Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            self.transaction_history.append(
                f"Withdraw: {' ':10} ${amount:.2f} at {' ':10} {time.strftime('%H:%M:%S')}")
            print('Withdraw Process Completed ✅')
            print(
                f"Withdrawn ${amount:.2f} from account '{self.account_name}'. New balance: ${self.balance:.2f}")
            self.get_balance()
            print()
        except BalanceException as error:
            print(f"Withdrawal Process Interrupted  ❌ ")
            print(error)
            print(
                f"Current balance: ${self.balance:.2f}\n")

    def Transfer(self, amount, account):
        try:
            if account == self.account_name:
                raise BalanceException(
                    f"Cannot transfer to the same account '{self.account_name}'")
            if not isinstance(account, BankAccount):
                raise BalanceException(
                    f"Account '{account}' does not exist. Must be a BankAccount instance.")

            print(
                '--------------------- Beginning Transfer.. 🚀 ---------------------- \n')
            print(
                f"Transferring ${amount:.2f} from '{self.account_name}' to {account.account_name} \n")

            if amount <= 0:
                raise BalanceException(
                    f"Transfer amount must be positive. ❌")
            if amount > self.balance:
                raise BalanceException(
                    f"Insufficient funds for transfer. ❌")
            if account.balance + amount < 0:
                raise BalanceException(
                    f"Transfer would result in negative balance for '{account}'. ❌")
            if account == self:
                raise BalanceException(
                    f"Cannot transfer to the same account '{self.account_name}'. ❌")
            if not isinstance(account, BankAccount):
                raise BalanceException(
                    f"Invalid account '{account}'. Must be a BankAccount instance. ❌")

            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer Process Completed ✅')
            self.transaction_history.append(
                f"Transfered: ${amount:.2f} from Acc: '{self.account_name}' to '{account.account_name}' ")
            self.get_balance()
            print(
                f"Transfered ${amount:.2f} from account '{self.account_name}' to {account.account_name} \n")
            account.get_balance()

        except BalanceException as e:
            print(f'Transfer Process Interrupted ❌')
            print(e)

    def get_transaction_history(self):
        print(
            f'--------------------- Acc "{self.account_name}"Transaction History 🚀 ---------------------- ')
        if not self.transaction_history:
            print('No transactions found.')
        else:
            for transaction in self.transaction_history:
                print(transaction)
            print()
            self.get_balance()
            print(
                f'--------------------- End of Acc "{self.account_name}" Transaction History 🚀 ---------------------- \n')


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        super().deposit(amount * 1.05)
        print(f"Deposit Process Completed ✅ with interest")
        self.get_balance()
        print()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, account_name, initial_amount, account_type):
        super().__init__(account_name, initial_amount, account_type)
        self.fee = 5  # Withdrawal fee
        self.interest_rate = 0.05  # 5% interest rate

    def deposit(self, amount):
        super().deposit(amount * (1 + self.interest_rate))

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - (amount + self.fee)
            self.transaction_history.append(
                'Withdrawn with fee: ${amount:.2f} at {time.strftime("%Y-%m-%d %H:%M:%S")}')
            print('Withdraw Process Completed ✅ with fee')
            print(f'Savings Account balance is : {self.fee:.2f}')
            self.get_balance()
        except BalanceException as e:
            print(f'Withdrawal Process Interrupted ❌ ')
            print(e)


# dave = BankAccount('Dave', 1000, 'savings')
# james = BankAccount('James', 5000, account_type='savings')
# # dave.__str__()
# print(dave)
# print(james)
# dave.get_balance()

# print("-------------------------------------------------")
# dave.deposit(200)
# print("-------------------------------------------------")
# dave.withdraw(500)

# dave.Transfer(200, james)

# dave.get_transaction_history()
# james.get_transaction_history()


# wise = InterestRewardsAccount('Wise', 1000, 'Interest Rewards')
# print(wise)
# wise.deposit(500)
# wise.withdraw(300)


# mambo = SavingsAccount('Mambo', 3000, 'savings')
# print(mambo)
# mambo.withdraw(200)


def create_account(account_list):
    while True:
        print('--------------------- Create Account 🚀 ---------------------- ')
        print('Create a New Bank Account')
        print('Choose and account Type to create: ')
        print('1. Normal Account')
        print('2. Savings Account')
        print('3. Interest Rewards Account')
        print('4. Bank Account')
        print('5. Exit or Q to Quit')
        print()

        account_name = input('\nEnter your account name: ')
        if account_name == "":
            print('Account name cannot be empty. Please enter a Valid Name. ')
            continue
        if 3 < len(account_name) > 20:
            print('Account name must be between 3 and 20 characters long.')
            continue
        if any(char.isdigit() for char in account_name):
            print('Account name cannot contain numbers.')
            continue
        if any(char in account_name for char in ['$', '%', '@', '#', '!', '&']):
            print('Account name cannot contain special characters.')
            continue
        if any(char.isspace() for char in account_name):
            print('Account name cannot contain spaces.')
            continue
        if any(char.isupper() for char in account_name):
            print('Account name cannot contain uppercase letters.')
            continue

        initial_amount = float(input('Enter your initial amount: '))
        if initial_amount < 50:
            print('Minimum Deposit is $50.00')
            return
        account_type = input('Select account type (1-4): ')

        if account_type == '1':
            account = BankAccount(account_name, initial_amount, account_type)
        elif account_type == '2':
            account = SavingsAccount(
                account_name, initial_amount, account_type)
        elif account_type == '3':
            account = InterestRewardsAccount(
                account_name, initial_amount, account_type)
        elif account_type == '4':
            account = BankAccount(account_name, initial_amount, account_type)
        else:
            print('Invalid choice. Please select a valid option.')
            return None
        account_list.append(account)
        return account


def display_accounts(account_list):
    if not account_list:
        print('No accounts found.')
        return
    print('--------------------- Account List 🚀 ---------------------- ')
    for account in account_list:
        print(account)


def find_account(account_name, account_list):
    for account in account_list:
        if account.account_name == account_name:
            return account
    return None


def main():
    account_list = []
    print('--------------------- Welcome to BankAccount 🚀 ---------------------- ')
    while True:
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4  Transfer')
        print('5. Transaction History')
        print('6. Display Accounts')
        print('7. Exit or Q to Quit')

        print()
        choice = input('Select you choice (1-7): ')
        if choice.lower() == 'q':
            print('\nExiting...')
            break

        if not choice.isdigit():
            print('Invalid choice. Please Enter a number between 1-6  or Q to Quit')
            continue
        choice = int(choice)

        if choice == 1:
            account = create_account(account_list)
            print(str(account))
            print('Account Created Successfully! ✅ ')
        if choice == 2:
            account_name = input('Enter your account name: ')
            account = find_account(account_name, account_list)
            if not account:
                print('Account not found. Please create an account first.')
                continue
            amount = float(input('Enter the amount to deposit: '))
            account.deposit(amount)
        if choice == 3:
            account_name = input('Enter your account name: ')
            account = find_account(account_name, account_list)
            if not account:
                print('Account not found. Please create an account first.')
                continue
            amount = float(input('Enter the amount to withdraw: '))
            account.withdraw(amount)
        if choice == 4:
            account_name = input('Enter your account name: ')
            account = find_account(account_name, account_list)
            if not account:
                print('Account not found. Please create an account first.')
                continue
            transfer_account_name = input(
                'Enter the account name to transfer to: ')
            transfer_account = find_account(
                transfer_account_name, account_list)
            if not transfer_account:
                print('Transfer account not found. Please create an account first.')
                continue
            amount = float(input('Enter the amount to transfer: '))
            account.Transfer(amount, transfer_account)

        if choice == 5:
            account_name = input('Enter your account name: ')
            account = find_account(account_name, account_list)
            if not account:
                print('Account not found. Please create an account first.')
                continue
            account.get_transaction_history(account_name)

        if choice == 6:
            display_accounts(account_list)
            print('Account List Displayed Successfully! ✅ ')
        if choice == 7:
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please Enter a number between 1-6  or Q to Quit')
            continue

    print('\n👋👋 Thanks for using BankAccount! Bye 👋👋\n')


if __name__ == "__main__":
    main()
