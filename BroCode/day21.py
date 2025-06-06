'''print()

# Concersion Stand

menu = {
    'porpcorn': 3.50,
    'pretzels': 4.00,
    'soda': 2.50,
    'nachos': 6.00,
    'burger': 2.65,
    'hotdog': 3.60,
    'chips': 1.50,
    'candy': 2.00,
    'icecream': 4.50,
    'water': 1.00,
    'pizza': 5.50,
    'coffee': 2.75,
    'tea': 2.25,
    'milkshake': 3.75,
    'brownies': 2.50,
    'cake': 3.00,
    'cookies': 1.75,
    'donuts': 2.50,
    'cupcakes': 3.50,
    'pancakes': 4.00,
    'waffles': 4.50,
    'sandwich': 5.00,
    'salad': 4.00,
    'soup': 3.50,
}
cart = {}
total = 0
print('-----------------------------------')
print('Welcome to the Concersion Stand 🛒')
print('-----------------------------------')

for i, (item, price) in enumerate(menu.items(), start=1):
    print(f'{i}. {item.capitalize():<10} : ${price:.2f}')
print()
print('-----------------------------------')

print(f'Select the item you want to buy from the above menu(q to quit):')
print('-----------------------------------\n')

while True:
    item = input('Enter the item name:  ')
    if item.lower() == 'q':
        print('Thanks for visiting the concersion stand!')
        break

    print('-----------------------------------')


'''


'''foods = []
food = input('Enter the food you want:  ')
while True:
    if not food:
        print("Please enter a valid food item or 'q' to quit.")
    elif food.lower() == 'q':
        break
    else:
        foods.append(food)
    food = input('Enter another food you want:  ')

print()
print('The food you want are:')
if not foods:
    print('You did not want any food!')
for food in foods:
    print(f'{food}', end=" ")
print()
'''
