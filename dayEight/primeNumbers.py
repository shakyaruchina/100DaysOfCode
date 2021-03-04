#Write a function that checks whether if the number passed into is a prime number or not.

def prime_checker(number):
    if number == 2:
        print("It's a prime number")
    elif number %2 == 0 or number %3 ==0:
        print("It's not a prime number")
    else:
        print("It's a prime number")

#Other method

# for i in range(2, number):
#     if number % i ==0:
#         is_prime =False
# if is_prime:
#     print("It is a prime number")
# else:
#     print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)