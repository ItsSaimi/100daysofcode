print("This program will show you how many days,weeks and months remaining untill you die at the age of 90years.")
age=int(input("Enter your age:"))
age_remaining=90-age 
days_remaining=age_remaining*365
weeks_remaining=age_remaining*52
months_remaining=age_remaining*12

print(f"You have {days_remaining} days or {weeks_remaining} weeks or {months_remaining} months remaining untill you get 90 years old.")
