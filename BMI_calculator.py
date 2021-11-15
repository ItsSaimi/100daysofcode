#----body mass index calculator----
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in meters:"))
result=weight/height**2
print("A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. ")

print("Your BMI is:")
print(int(result))
