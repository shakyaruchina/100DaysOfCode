#Eligibility to ride a rollercoaster 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

#bill starting with 0
bill = 0
#nested if statements
if height >= 120:
    print("You can ride the rollarcoaster")
    age = int(input("What is your age"))
    if age <12:
        bill = 5
        print("Child tickets are $5.")
    elif age <=18:
        bill=7
        print("Free ticket.")
    else:
        bill = 12
        print("Adult tickers $12.")
    wants_photo = input("Do you want your photo taken? Y or N ?")
    if wants_photo== "Y":
        #add $3
        bill += 3 #bill = bill + 3
    print(f"Your final bill is {bill}")
else: 
    print("Sorry, you have to grow taller before you can ride.")    
