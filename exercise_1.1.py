name = input("Enter your name: ")
age = int(input("Enter your age: "))
age_100 = 100 - age
year = 2021+age_100
no_of_copies = int(input("Enter No of Copies Needed: "))
print(f"'{name} will turn 100 in the Year {year}!'\n" * no_of_copies)
