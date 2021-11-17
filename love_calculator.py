print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
c_name = name1+name2
lowercase_name = c_name.lower()
t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")
e = lowercase_name.count("e")
true = t+r+u+e
l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")
love = l+o+v+e
love_sc = int(str(true)+str(love))

if (love_sc < 10) or (love_sc > 90):
    print(f"Your love score is {love_sc}, You are like coke and metos.😱")
elif (love_sc >= 40 )and (love_sc <=50):
    print(f"Your love score is {love_sc},You are perfect togather.")
else:
    print(f"Your love score is {love_sc}.")