import os

while True:
    os.system('cls')    #clearscreen
    print("calculator")
    print('1. ➕')
    print('2. ➖')
    print('3. ✖')
    print('4. Exit')
    ch = input('Select a number: ')
    if ch == '1':
        a = int(input("Enter Value 1: "))
        b = int(input("Enter Value 2: "))
        print(f'{a}+{b}={a + b}')
    elif ch == '2':
        a = int(input("Enter Value 1: "))
        b = int(input("Enter Value 2: "))
        print(f'{a}-{b}={a - b}')
    elif ch == '3':
        a = int(input("Enter Value 1: "))
        b = int(input("Enter Value 2: "))
        print(f'{a}*{b}={a * b}')
    elif ch == '4':
        print("Bye")
        break
    else:
        print("Invalid Input")
