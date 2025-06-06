print()
#   break, continue and pass

#   break statement
# while loops
'''
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break #Loops breaks when i is 5
    i += 1
    # for loop
    
print()

for letter in "python":
    if letter  == "h":
        break 
    print(letter)
    
print()
'''
#   continue statement

'''i = 0
while i < 10:
    print(i)
    if i == 2:
        continue #Loops continue when i is 5
    i += 1
    # for loop

for i in range(1, 6):
    if i == 3:
        continue
    print(i)'''

#   pass statement
'''
for i in range(5):
    pass

x = 10
if x > 5:
    pass
else:
    print(f'{x} is less than or equal to 5.')'''

# ***********************************************************
# ***********************************************************
'''
Practice Question
1. Write a program that simulates a login system where the user gets three attempts to enter the correct password. Use break to exit the loop if the user
enters the correct password before the third attempt
2. Write a program that uses nested for loops to print pairs of numbers (i, j) where i ranges from 1 to 3 and j ranges from 1 
to 3. Use break to exit the inner loop when j == 2.
3. Write a Python program that uses a while loop to print numbers from 1 to 5, but skips the number 3 using the continue statement.

'''
#   question 1

'''
attempts = 3
while attempts > 0:
    value = input('Enter your password:     ')
    if value == "new":
        print('You are logged in!!..')
        break
    attempts -= 1

print('Out of trials')
'''

#   question 2

'''print()
for i in range(1, 3):
    for j in range(1, 3):
        if j == 2:
            break
        print(j, end=" ")
    print(i, end=' ')'''

# question 3

# i = 0
# while i <= 5:
#       i += 1
#       if i == 3:
#           continue
#       print(i)


'''i = 0
while i < 5:
    i += 1
    if i == 3:
        continue

    print(i)

print()
'''
