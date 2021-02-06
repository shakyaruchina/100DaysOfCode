#Tip Calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill ? $"))
tip_percentage = int(input("What percentage would you like to tip? 10, 12 or 15"))
num_of_people = int(input("How many people to split the bill? "))
pay = tip_percentage/100 *bill + bill
bill_per_person = pay/num_of_people
per_person = round(bill_per_person,2)
#per_person = "{:.2f}",format(bill_per_person)
print(f"Each person should pay: ${per_person}")
