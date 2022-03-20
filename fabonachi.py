n1=0
n2=1

n=int(input("Enter the index : "))

print(n1)
print(n2)

for i in range(2,n+1):

    last_value=n1+n2
    n1=n2
    n2=last_value

    print(last_value)
