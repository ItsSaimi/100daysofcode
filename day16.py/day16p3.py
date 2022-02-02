# import turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.width(2)
# t.speed(15)
# col = ('white', 'pink', 'cyan')
# for i in range (300):
#         t.pencolor(col[i%3])
#         t.forward(1*4)
#         t.right(121)
import turtle
spiral = turtle.Turtle()

for i in range(45):
    spiral.forward(1*10)
    spiral.right(144)
    spiral.color("cyan")
    spiral.shape("turtle")

turtle.done