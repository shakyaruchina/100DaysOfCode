#A program that calculates the average student height from a list of heights.

#split function changes the user input into list
student_heights = input("Input a list of student heights. ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
for height in student_heights:
    total_heights += height
#print(total_heights)

number_inputs = 0
for m in student_heights:
    number_inputs+=1
#print(number_inputs)

answer = total_heights/number_inputs

print(round(answer))