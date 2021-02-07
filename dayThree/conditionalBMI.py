#Conditional BMI

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight/(height**2)
if BMI<1.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI<30:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Yout BMI is {BMI}, you are clinically obese.")







