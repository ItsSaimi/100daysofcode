import math
def my_c(height, width, cover):
    area = height*width
    n_of_c = math.ceil(area/cover)
    print(f"You will need {n_of_c} of paint cans.")

test_h = int(input("Enter the height of the wall:"))
test_w = int(input("Enter the width of the wall:")) 
coverage = 5
my_c(test_h, test_w, cover=coverage)