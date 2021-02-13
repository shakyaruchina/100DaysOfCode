#A program that calculates the sum of all the even numbers from 1 to 100. The first even number would be 2 and the last one is 100.

total = 0
#(1-100)
for evennumber in range(1,101,2):
    total+=evennumber
print(total)