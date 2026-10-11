# name and age from user 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f" {name}! You are {age} years old.")
if age < 0:
    print(f"Please enter a valid age.")
elif age >= 18:
    print(f"Congratulations {name}! You are eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote yet.")