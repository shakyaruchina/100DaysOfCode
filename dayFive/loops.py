#Loops

#for loops 
#for item in list_of_items:


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")


#range function
#for number in range(a,b): (1-9)

total = 0
for number in range(1,101):
    total += number
    print(number)