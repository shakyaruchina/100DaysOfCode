
def greet():
    #input("What is your name?")
    print("Hello Darling!")
    print("Welcome to learning python")
    print("I hope you have a great time here.")
    print(" ")
greet()

#function with input

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"Welcome to learning python, {name}")
    print("I hope you have a great time here.")
    print(" ")

greet_with_name("Zoro")

#function with more than one input

def greet_with(name,location):
    print(f"My name is {name}")
    print(f"My location is {location}")

#greet_with("Zoro", "East Blue")

#keyword argument

greet_with(location = "East Blue", name = "Zoro")