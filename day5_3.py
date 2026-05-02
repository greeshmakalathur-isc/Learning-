first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

option1 = (first_name + last_name).lower()
option2 = first_name[0] + last_name + birth_year[-2:]
option3 = last_name + str(len(first_name)) + birth_year

print(f"1. {option1}")
print(f"2. {option2}")
print(f"3. {option3}")

choice = input("Pick 1, 2 or 3: ")
if choice == "1":
    print(f"Your username is {option1}")
elif choice == "2":
    print(f"Your username is {option2}")
elif choice == "3":
    print(f"Your username is {option3}")