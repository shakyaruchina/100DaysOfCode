# Life in weeks
# Number of days/months/weeks left to turn 90years old from the current age.

#user input age
age = input("What is your current age? ")
#90-current age 
life_span = int(90-int(age))

days = life_span *365
weeks = life_span *52
months = life_span *12
#printing the result inside f-strings
print(f"You have {days} days, {weeks} weeks and {months} months left.")