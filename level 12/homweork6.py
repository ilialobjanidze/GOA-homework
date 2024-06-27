
score = int(input("შეიყვანეთ ქულა (0-100): "))


if score >= 90 and score <= 100:
    grade = "Grade A"
elif score >= 80 and score <= 89:
    grade = "Grade B"
elif score >= 70 and score <= 79:
    grade = "Grade C"
elif score >= 60 and score <= 69:
    grade = "Grade D"
elif score >= 0 and score <= 59:
    grade = "Grade F"
else:
    grade = "Invalid score entered"

# დაბეჭდვა შედეგის მიხედვით
print(f"Your Score is : {score}, Your grade is: {grade}")
