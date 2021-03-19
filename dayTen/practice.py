


# import random
# print("Welcome to the password generator!")

# letters = ['a','b','c','d','e','f']
# numbers = ['O','1','2','3','4']
# symbols = ['!','@','#','$']

# nr_letters = int(input("How many letters would you like in your password? \n"))
# nr_symbols = int(input("How many symbols would you like in your password? \n"))
# nr_numbers = int(input("How many numbers would you like in your password? \n"))
# x = []

# for n in range(0,nr_letters):
#     random_letter = random.randint(0,len(letters)-1)
#     random_user_letter = letters[random_letter]
#     x.append(random_user_letter)
# for user_symbol in range(0,nr_symbols):
#     random_symbol = random.randint(0,len(symbols)-1)
#     random_user_symbol = symbols[random_symbol]
#     x.append(random_user_symbol)
# for user_number in range(0,nr_numbers):
#     random_number = random.randint(0,len(numbers)-1)
#     random_user_number = numbers[random_number]
#     x.append(random_user_number)
#     random.shuffle(x)

# password_generator = (''.join(x))

# print(password_generator)