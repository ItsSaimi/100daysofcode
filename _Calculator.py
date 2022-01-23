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
 
for symbol in operation:
    print(symbol)
operation_function = input("Select the operation from above:")
num2 = int(input("Enter the second number:"))
c = operation[operation_function]
ans1 = c(num1, num2)
print(f"{num1}{operation_function}{num2} = {ans1}")

# operation_function = input("Select the operation from above:")
# num3 = input("Enter the second number")


