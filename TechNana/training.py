# One can loop around aournd a sequence...ie a string , a list , or tuple
# Looping through a string
name = 'wiseephay'
for character in name:
    # print(character)
    # print(f"{character} end='' ")
    print(character, end="")


print()
# Looping through a list
names = ['wise', 'sam', 'john', 'ester', 'peter', 'kim', 'joy', 'antony']
for each_name in names:
    print(each_name, end=" ")
    
print()
print()
print()
    
print('===================Currency Converter=================')
pin = 1234
user_name = input('Enter your name: ')
print(f'Welcome {user_name} to currency conveter')
while True:
    user_pin = int(input('Enter your Pin: '))
    if user_pin == pin:
        print('Welcome to Online Currency Converter')
        print('1. Convert Ksh to USD | JYEN | POUNDS  ')
        print('2. Convert USD to KSH | JYEN | POUNDS  ')
        print('3. Convert EURO to YUAN | JYEN | POUNDS  ')
        print('4. Convert JYEN to POUNDS | JYEN |   ')
        print('5. Exit')
        user_choice = input('Enter Your Choice')
        if user_choice == '1':
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            pass
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            print('Thank you for using Currency Converter')
            break
    else:
        print('Incorrect Pin!Please Try Again')
        break
# 1 usd to ksh = 130
# ksh to euro  = 140
# ksh to pound sterling = 165.86
# ksh to omani rial = 333.85
