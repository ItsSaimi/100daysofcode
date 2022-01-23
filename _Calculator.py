def add (n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2
    
operation={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


num1 = int(input("Enter the first number:"))


should_continue=True
while should_continue:
    for symbol in operation:
        print(symbol)
    operation_function = input("Select the operation:")
    num2 = int(input("Enter the next number:"))
    c = operation[operation_function]
    ans = c(num1, num2)
    print(f"{num1}{operation_function}{num2} = {ans}")
    if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ")=='y':
        num1=ans
    else:
      should_continue = False

# operation_function = input("Select the operation from above:")
# num3 = input("Enter the second number")


