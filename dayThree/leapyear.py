#Leap year or not

year = int(input("Which year do you want to check?"))

if year % 4 ==0:
    if year % 100 !=0:
        print("Leap year")
    elif year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year") 