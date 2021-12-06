print("Welcome to online pizza delivery.")
print("S for Small(280PKR),M for Medium(450PKR),L for Large(650PKR).")
size = input("Which size do you want S,M or L:")
print("Pepproni for small pizza 50PKR,Peproni for Medium or Large 100PKR.")
pepproni = input("Do you want pepproni Y or N:")
print("Extra Cheese for 80PKR.")
cheese = input("Do you want extra Cheese Y or N:")

bill = 0
if size == "S" :
    bill+=250
elif size == "M":
    bill+=450
elif size == "L" :   
    bill+=650 
if pepproni == "Y":
    if size == "S":
        bill +=50    
    else :
        bill +=100
if cheese == "Y":
    bill+=80
print(f"Your final bill is PKR{bill}")    
