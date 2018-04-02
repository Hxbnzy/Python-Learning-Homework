import turtle
from time import sleep
#
# turtle.setup(800, 800, 200, 200)
# turtle.pensize(2)
# for i in range(1):
#     turtle.circle(80, 360)
#     turtle.circle(-80, 360)
#     turtle.left(90)
#     turtle.circle(80, 360)
#     turtle.circle(-80, 360)
#     turtle.penup()
#     turtle.right(90)
#     turtle.fd(-160)
#     turtle.pendown()
#     turtle.left(90)
#     turtle.circle(-165, 360)
#
# turtle.done()

# heart
# import turtle as t
# import math as m
#
# t.setup()
#
# t.fillcolor("red")
# t.seth(130)
# t.begin_fill()
# t.circle(100, 200)
# a = 100*m.cos(m.radians(40))+100*m.sin(m.radians(30))
# aa = a/m.cos(m.radians(30))
# t.fd(aa)
# t.up()
# t.goto(0, 0)
# t.down()
# t.seth(50)
# t.circle(-100, 200)
# t.fd(aa)
# t.end_fill()
# t.up()
# t.goto(300, 300)
#
# t.done()

from pylab import*
t = linspace(0, 2*pi, 100)
x = sin(2*t) + 2*sin(t)
y = - cos(2*t)-2*cos(t)
fill(x, y, 'r')
show()