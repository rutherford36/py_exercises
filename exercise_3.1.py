a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
i = 0
number = a[i]
length = len(a)
while i <= length:
    if number < 5:
        b.append(number)
        i = i + 1
        number = a[i]
    else:
        print("Done")
        break
print(b)


