#Split string method
import random 
names_string = input("Give me everybody's names,separated by a comma.")
#divide into lists
names = names_string.split(",")
#person_pay = random.choice(names)

#number of names in the list
pay = len(names)
#random integer
pay = random.randint(0,pay-1)
person_pay = names[pay]
print(person_pay + " is going to buy the meal today.")