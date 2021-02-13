#Write a program that autimatically prints the solution to the FizzBuzz game.

for n in range(1,101):
    if n%3 ==0 and n%5 == 0:
        n ="FizzBizz"
    elif n%3 == 0:
        n = "Fizz"
    elif n%5 == 0:
        n = "Bizz"
    print(n)