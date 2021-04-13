x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = input('''
    Enter the Operator :
    + - Addition ; - - Subtraction ; * - Multiplication ;/ - Division ; ''')
if z == '+':
    print(f'Addition of Numbers is: {x + y}')
elif z == '-':
    print(f'Subtraction of Numbers is: {x - y}')
elif z == '*':
    print(f'Multiplication of Numbers is: {x * y}')
elif z == '/':
    print(f'Division of Numbers is: {x / y}')
else:
    print("Not a valid Choice")
