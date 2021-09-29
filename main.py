import turtle
t = turtle.Pen()
t.reset()

t.speed(6)
# def myCircle(red, green, blue):
#     t.color(red,green,blue)
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()
#
# def mySquare(size, colorFill):
#     if colorFill == True:
#         t.begin_fill()
#     for x in range(1,5):
#         t.forward(size)
#         t.left(90)
#     if colorFill == True:
#         t.end_fill()
#
# mySquare(50,True)
# mySquare(150,False)

# def myStar(size, myFill):
#     if myFill == True:
#         t.begin_fill()
#     for x in range(1, 19):
#         t.forward(size)
#         if x % 2 == 0:
#             t.left(175)
#         else:
#             t.left(225)
#     if myFill == True:
#         t.end_fill()
#
# t.color(0.9,0.75,0)
# myStar(120, True)
# t.color(0,0,0)
# myStar(120, False)

# def myOctagon(size,myFill):
#     if myFill == True:
#         t.begin_fill()
#     for x in range(1,9):
#         t.forward(size)
#         t.left(45)
#     if myFill == True:
#         t.end_fill()
#
# t.color(0.9,0.75,0)
# myOctagon(50, True)
# t.color(0,0,0)
# myOctagon(50, False)
#
# def draw_star ( size , points ) :
#     for x in range(1, points):
#         t.forward(size)
#         if x % 2 == 0:
#             t.left(175)
#         else:
#             t.left(225)
#
# draw_star(50,)

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Blue")
t.pencolor("Purle")
a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b == 210:
        break
    t.hideturtle


turtle.done()














# mySquare(25)
# mySquare(50)
# mySquare(75)
# mySquare(100)
# mySquare(125)


turtle.mainloop()