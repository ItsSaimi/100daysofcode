def greet(n):
    #n = input("What is your name?")
    n = n.capitalize()
    print(f"Hello there {n}!")
    print(f"Asslamm o elikum!")
    print("Hope You are good",n)
n = input("What is your name?")
#n = n.capitalize()
greet(n)
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")