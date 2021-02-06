#BMI Calculator from users weight and height
#input height
height = input("Enter your height in m: ")
#input weight
weight = input("Enter your weight in kg: ")
#change data type
actual_weight = float(weight)
actual_height = float(height)
BMI = actual_weight/(actual_height**2)
#integer data type
print(int(BMI))
