#A program that calculates the highest score from a list of scores.

student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_value = 0
for m in student_scores:
    if m >highest_value:
        highest_value = m
print(f"The highest score in the class is : {highest_value}")