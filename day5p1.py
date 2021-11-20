import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
num_names = len(names)
random_ch = random.randint(0, num_names-1)
ptptb = names[random_ch]
print(ptptb+" will buy the meal today.")


