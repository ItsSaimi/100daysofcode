#METHOD1
#t = 0
#for n in range (2, 101, 2):
 #   t += n
  #  print(t)
#print(f"The sum of even numbers is {t}.")

#METHOD2
t_2 = 0
for n in range (1, 101):
    if n % 2 == 0 :
        t_2 += n
print(t_2)