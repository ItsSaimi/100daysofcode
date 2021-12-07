def my_sol():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
while at_goal() != True:
    if wall_in_front():
        my_sol()
    else:
        move()
    


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
