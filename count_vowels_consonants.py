str1 = input("Please Enter Your Own String : ")
vowels = 0
digits = 0
consonants = 0
spaces = 0
symbols = 0
str1 = str1.lower()
for i in range(0, len(str1)):
    if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or str1[i] == 'u':
        vowels = vowels + 1
    elif 'a' <= str1[i] <= 'z':
        consonants = consonants + 1
    elif '0' <= str1[i] <= '9':
        digits = digits + 1
    elif str1[i] == ' ':
        spaces = spaces + 1
    else:
        symbols = symbols + 1

print("No of Vowels: ", vowels)
print("No of Consonants: ", consonants)
print("No of Digits: ", digits)
print("No of White spaces: ", spaces)
print("No of Symbols : ", symbols)
