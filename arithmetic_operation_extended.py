# This program is to take two integers as input and make various arithmetic operations based on choices given
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
print('''Select your choice from below
1 - Addition : 2 - Subtraction : 3 - Multiplication :4 - Exponential : 
5 - Divide : 6 - Floor (//): 7 - Modulo (%)''')
# While loop is set to make sure only integers are taken as input, as well if there are
# non-integers like float, string are typed, then it will give another chance to choose option again
while True:
    try:
        operation = int(input("Select Operation from above: "))
        if operation == 1:
            print("Addition of given operands is : ", num1 + num2)
        elif operation == 2:
            print("Subtraction of given operands is : ", num1 - num2)
        elif operation == 3:
            print("Multiplication of given operands is : ", num1 * num2)
        elif operation == 4:
            print("Exponential of given operands is : ", num1 ** num2)
        elif operation == 5:
            print("Divide of given operands is : ", num1 / num2)
        elif operation == 6:
            print("Floor of given operands is : ", num1 // num2)
        elif operation == 7:
            print("Modulo of given operands is : ", num1 % num2)
        else:
            print("Your choice is invalid !!!")
        break
    except ValueError:
        print("Please input integer only...")
        continue
