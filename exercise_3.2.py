a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
i = 0
number = a[i]
user_num=int(input("Enter the Number: "))
length = len(a)
while i <= length:
    if number < user_num:
        b.append(number)
        i = i + 1
        number = a[i]
    else:
        print("Done")
        break
print(b)


