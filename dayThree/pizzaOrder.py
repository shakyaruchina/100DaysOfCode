#Pizza order

print("Welcome to Pizzaria")
size = input("What size pizza would you like? S, M, L ? ")
add_pepperoni = input("Would you like to add pepperoni? Y or N? ")
extra_cheese = input("Would you like to add some extra cheese? Y or N ")

price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
else:
    price+=25
if add_pepperoni == "Y":
    if size == "S":
        price +=2
    else:
        price +=3
#else is optional        
if extra_cheese == "Y":
    price +=1
print(f"Your final bill is: ${price}")