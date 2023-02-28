from turtle import *
speed(0)

fillcolor('Green')
pencolor('Orange')
pensize(3)
side = 3
pu()
goto(-150, 0)
pd()
for i in range(side):
    fd(150)
    for i in range(side):
        fd(100)
        begin_fill()
        for i in range(side):
            fd(50)
            dot(10)
            for i in range(side):
                fd(25)
                lt(360/side)
            rt(360/side)
        end_fill()
        lt(360/side)
       # write(i, font=("Arial", 10, "normal"))
    rt(360/side)

hideturtle()
mainloop()