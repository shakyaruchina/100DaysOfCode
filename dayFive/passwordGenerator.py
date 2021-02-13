#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#user-input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Empty list
x = []
#Empty string
#x = ''
for n in range(0, nr_letters):
    #random.choice(letters)
    #random_user_letter+=random_letter

    #random number for the list (letters)
    random_letter = random.randint(0,len(letters)-1)
    #random number position in the list (letters)
    random_user_letter = letters[random_letter]
    #string concatenation
    # x += random_user_letter
    #adding elements to the list
    x.append(random_user_letter)
    #for loop for symbols
for user_symbol in range(0,nr_symbols):
    random_symbol = random.randint(0,len(symbols)-1)
    random_user_symbol = symbols[random_symbol]
    x.append(random_user_symbol)
    #print(random_user_symbol)
#for loop for numbers
for user_number in range(0,nr_numbers):
    random_number = random.randint(0,len(numbers)-1)
    random_user_number = numbers[random_number]
    x.append(random_user_number)
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    #re-order
    random.shuffle(x)
#print(x)
#join() function as one element
password_generator=(''.join(x))
print(f"Your password is {password_generator}")
  

