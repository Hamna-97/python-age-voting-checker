
# obtained marks, total marks from user
obtained_marks = int(input("Enter your obtained marks: "))
total_marks = int(input("Enter your total marks: "))
if total_marks <= 0:
    print("Invalid.Total marks must be greater than zero.")
elif total_marks < obtained_marks:
    print("Invalid input. Obtained marks cannot be greater than total marks.")
elif obtained_marks < 0:
    print("Obtained marks cannot be negative.")
else:
    percentage = (obtained_marks / total_marks) * 100
    print(f"Your percentage is: {percentage:.2f}%")
    if percentage >= 90:
     grade = 'A+'
    elif percentage >= 80:
     grade = 'A'
    elif percentage >= 70:
     grade = 'B'
    elif percentage >= 60:
     grade = 'C'
    elif percentage >= 50:
     grade = 'D'
    else:
     grade = 'Fail'
    print(f"Your Grade is: {grade}")
