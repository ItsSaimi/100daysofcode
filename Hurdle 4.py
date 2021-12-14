def turn_right():
    turn_left()
    turn_left()
    turn_left()
def my_sol():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while at_goal() != True:
    if wall_in_front():
        my_sol()
    else:
        move()
#its the solution of the hurdle 4
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
