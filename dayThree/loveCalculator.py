#Love Calculator

print("Welcome to Love Calculator")

#\n breaks the line
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#upper() changes user input into uppercase
nameA = name1.upper()
nameB = name2.upper()
#count() counting the given string in user input
tA = nameA.count("T")
tB = nameB.count("T")
#count() data type is integer
t = tA+tB
rA = nameA.count("R")
rB = nameB.count("R")
r = rA+rB
uA = nameA.count("U")
uB = nameB.count("U")
u = uA+uB
eA = nameA.count("E")
eB = nameB.count("E")
e = eA+eB
lA = nameA.count("L")
lB = nameB.count("L")
l = lA+lB
oA = nameA.count("O")
oB = nameB.count("O")
o = oA+oB
vA = nameA.count("V")
vB = nameB.count("V")
v = vA+vB
#adding two digits(string addition)
#converting the integer to string
total = str(t+r+u+e)+str(l+o+v+e)
#if conditions
if (total<10) or (total>90):
    print(f"Your love score is {total},you go together like coke and mentos.")
elif (total>=40) and (total<=50):
    print(f"Your love score is {total}, you are alright together.")
else:
    print(f"Your love score is {total}.")

