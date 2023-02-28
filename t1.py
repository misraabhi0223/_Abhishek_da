from turtle import *

def square():
    for i in range(4):
        fd(d)
        lt(90)

def polygon(side=3, dis=50):
    for i in range(side):
        fd(dis)
        lt(360/side)


square()
polygon(5, 100)
polygon(6, 100)
hideturtle()
mainloop()3
