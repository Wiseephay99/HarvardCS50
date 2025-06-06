print()
nums = [1,2,3,4,5]
#   For Loops and While Loops
for num in nums:
    print(num)
    
print() 

#break and continue statements
for i in nums:
    if i == 3:
        print('Found It!')
        break
    print(i)
    
print()
for e in nums:
    if e == 3:
        print(f'Found It!')
        continue
    print(e)
    
print()
# Loop within a loop!
for num in nums:
    for letter in 'abc':
        print(num, letter)

print()
    
# range()
for i in range(10):
    print(i)
    
print()

for i in range(0, 11):
    print(i)
print()

for i in range(0, 11):
    print(i, end='', sep='')
print()

# while loops
print()
x = 0
while x < 10:
    print(x)
    x = x + 1

print()
print()
x = 0
while True:
    if x == 5:
        break
    print(x)
    x = x + 1
print()
print()


