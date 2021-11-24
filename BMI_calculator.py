#----body mass index calculator----
weight=float(input("Enter your weight in kilograms:"))
height=float(input("Enter your height in meters:"))
result=weight/height**2
print("A BMI of 25.0 or more is overweight, while the healthy range is 18.5 to 24.9. ")

print("Your BMI is:")
print(int(result))
if (result >= 18.5) and (result <= 24.9):
    print("You are healthy.")
elif(result < 18.5):
    print("You are underweight.")

else:
    print("You are overweight.")

   
