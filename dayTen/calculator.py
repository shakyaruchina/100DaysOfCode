#Calculator

from art import logo

#add function
def add(n1,n2):
    return n1+n2
#subtract functuon
def subtract(n1,n2):
    return n1-n2
#divide function
def divide(n1,n2):
    return n1/n2
#multiply function
def multiply(n1,n2):
    return n1*n2

#operation dictionary{key:value}
operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply,
} 

def calculator():
    print(logo)
    num1 = float(input("What is the first number ? "))
    #prints each operations key
    for operation in operations:
        print(operation)
    go_continue = True

    while go_continue:
        operation_symbol = input("Pick an operation ")
        num2 = float(input("What is the next number ? "))
        #key value 
        calculation = operations[operation_symbol]
        #add(n1,n2), subtract(n1,n2)
        answer = calculation(num1,num2)
        print(f"{num1} {operation_symbol}{num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start a new calculation:") == "y":
            num1 = answer
        else:
            go_continue = False
            calculator()
#recursion : function that calls itself
calculator()