
# math.science,urdu,english from user
math =input("Enter your math score: ")
science = input("Enter your science score: ")
urdu = input("Enter your urdu score: ")
english = input("Enter your english score: ")
total_score = int(math) + int(science) + int(urdu) + int(english)
print(f"Your total score is: {total_score}")
total_score = 400
obtained_score = int(math) + int(science) + int(urdu) + int(english)
percentage = (obtained_score / total_score) * 100
print(f"Your percentage is: {percentage}%")

