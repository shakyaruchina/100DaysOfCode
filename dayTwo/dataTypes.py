print("Hello"[4])
print("123"+"456")

num_char = len(input("What is your name? "))
#changing int type to string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")
#checking the data type using type
print(type(num_char))
#rounding to 2 characters
print(round(8/3,2))
# "//" gives the integer value i.e 2
print(8//3)
score = 0
score +=1
#f-string any datatype can be added to the print statement
print(f"your score is {score}")

#sum of two digit number
two_digit_number = input("Type a two digit number:")
print(int(two_digit_number[0])+int(two_digit_number[1]))






