'''print()

menu = {
    'burger': 5.00,
    'fries': 2.50,
    'soda': 1.75,
    'pizza': 8.00,
    'hotdog': 3.60,
    'popcorn': 2.00,
    'nachos': 4.00,
    'pretzel': 3.50,
    'ice cream': 4.50,
    'chips': 1.50,
}

cart = {}
total = 0

print('*******************************')
print('Welcome to Concesssion Stand!')
print('*******************************')

for i, (item, price) in enumerate(menu.items(), start=1):
    print(f"{i}. {item.capitalize():<10} : ${price:.2f}")


print('*******************************')

while True:
    item = input('Enter the food you want to buy (q to quit):  ')

    if item.lower() == 'q':
        print('Thanks for using the Consession Stand!')
        return 0

    if not item:
        print('You did not select an item!')

    if menu.get(item) is not None:
        cart[item] = menu[item]

print()

print(f'***************** Your Cart *****************')
for i, (item, price) in enumerate(cart.items(), start=1):
    print(f'{item}: ${price:.2f}')
print()
print(f'***************** Total *****************')
for price in cart.values():
    total += price
print(f'Your Total Cost is: {total:.2f}')
print('*******************************')
'''
# *************************************************************
# *************************************************************

'''print('---------------------------------------')
foods = []
food = input('Enter the food you like(q to quit):   ')
while not food == 'q':

    foods.append(food)

    food = input('Enter another food you like(q to quit):   ')

print()
if not foods:
    print('You did not enter any food you like...')

print(f'The foods you like are: ')
for food in set(foods):
    print(food.capitalize(), end=' ')

print()'''

# *************************************************************
# *************************************************************

'''print("------------------------------------------")
foods = []

food = input('Enter food you like(q to quit):   ')
while food != 'q':
    foods.append(food)

    food = input('Enter another food you like:  ')

print()

if not foods:
    print('You did not enter any food you like')
print('The foods you like are:')
for food in set(foods):
    print(food, end=" ")
print()'''
# *************************************************************
# *************************************************************

# python bank app
import time
def check_balance(balance):
    print(f'Your current account balance is: ${balance:.2f}')


def deposit(balance):
    while True:
        amount = input('Enter amount to deposit (q to quit): $ ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            return main()
        if not amount.isdigit():
            print(f'{amount} is not a valid deposit amount')
            continue
        amount = float(amount)
        if amount <= 10:
            print('You cannot deposit an amount less than $10')
            print(f'Current account balance is: {balance:.2f}')
        elif amount == 0:
            print('Deposit cannot be a zero')
        elif amount == 100000:
            print('Deposit cannot be more than $100000')
        else:
            print(f'Successfully deposited: ${amount:.2f}')
            return amount


def withdraw(balance):
    while True:
        amount = input('Enter amount to withdraw (q to quit): $ ')
        if amount.lower() == 'q':
            print('Exiting to Main Menu')
            return main()

        if not amount.isdigit():
            print(f'{amount} is not a withdrawal valid amount')
            continue
        amount = float(amount)
        if amount > balance:
            print('Insufficient Funds...Please Try a lower amount')
            print(f'Current account balance is: {balance:.2f}')
        elif amount == 0:
            print('You cannot withdraw a 0')
        elif amount <= 10:
            print('Withdrawal amount cannot be less $10')
        else:
            print(f'Successfully withdrawn: ${amount:.2f}')
            return amount


print('\nWelcome to Python Easy Bank App')


def main():
    balance = 0
    while True:
        print('---------------------------------------')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        print('---------------------------------------')

        choice = input('Select your choice(1-4)(q to quit):   ')

        if choice.lower() == 'q':
            break

        choice = int(choice)

        if choice == 1:
            check_balance(balance)
        if choice == 2:
            balance += deposit(balance)
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            break
    print('Thanks for using Easy Bank App')
    print(f'Current Balance is: {balance:.2f}')
    time.sleep(2)
    print('Exiting...')
    print('\n👋 Bye 👋\n')


if __name__ == "__main__":
    main()
