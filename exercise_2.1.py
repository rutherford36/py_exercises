# Program to find odd or even
number = int(input("Enter a Number:"))
result = (number % 2)
multiple_four = (number % 4)
if result == 0 and multiple_four == 0:
    print("Given Number is Multiple of 4")
elif result == 0:
    print("Given Number is Even")
else:
    print("Given Number is Odd")
