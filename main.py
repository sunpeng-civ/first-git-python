# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import turtle,math

x1,y1 = 100, 100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

distance1 = math.sqrt((x1-x4)**2+(y1-y4)**2)
turtle.write(distance1)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
