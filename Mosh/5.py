print()

# ======================================================
# Strings

course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('y'))
print(course.find('Y'))
print()

print(course.replace('x', '4'))

print()
print('Python' in course)
print()

print(10/3)
print(10 % 3)
print(10//3)
print()

# Arithmentic Operator

x = 10
x = x+3
x += 3  # Aurgumented Operator

print()
y = 10 + 3 * 2
print(y)
print()

# Comparison Operators

x = 3 > 2  # Boolean Expression
print(x)
x = 3 < 2

x = 3 != 2

#   Logical Operators
print()
price = 25
print(price > 10) and (price < 30)

print()
price = 5
print(price > 10) or (price < 30)

print()
print(not price > 10)

print()

# If statements

temparature = 25
if temparature > 30:
    print(f"It's a HOT day")
    print("Drink plenty of Water...")
elif temparature > 20:
    print("It's a nice day")
elif temparature > 10:
    print("It's a bit COLD")
else:
    print("It's COLD")

print('Done')

#   weight converter program
weight = input('Weight:    ')
unit = input('(K)g or (L)bs:    ')
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print(f'Weight in Lbs: {round(converted, 2)} Lbs\n')
else:
    converted = float(weight) * 0.45
    print(f'Weight in Kgs: {round(converted, 2)} Kgs\n')

print()
