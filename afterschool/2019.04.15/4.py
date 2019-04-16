import random
import turtle
screen = turtle.Screen()
image1 = "동전앞면.gif"
image2 = "동전뒷면.gif"
screen.addshape(image1)
screen.addshape(image2)
t1 = turtle.Turtle()

coin = random.randint(0, 1)
if coin == 0:
    t1.shape(image1)
    t1.stamp()
else :
    t1.shape(image2)
    t1.stamp()

turtle.exitonclick()
