#Converting student scores into grades into a new dictionary called student_grades.
student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermoine" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades ={}

for thing in student_scores:
    if student_scores[thing] >90:
        student_grades[thing] = "Outstanding"
    elif student_scores[thing] >80:
        student_grades[thing] = "Exceeds Expectations"
    elif student_scores[thing] >70:
        student_grades[thing] = "Acceptable"
    else:
        student_grades[thing] = "Fail"

print(student_grades)
