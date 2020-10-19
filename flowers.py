# VSFX 705 - Example Flower
#
# From the book:
# Think Python: An Introduction to Software Design by allen B. Downey
# https://code.google.com/p/thinkocaml/source/browse/html/code/flower.py?r=15
# This code has been changed from the above source using TurtleWorld into
# the standard turtle graphics
#
# modified by: Deborah R. Fowler
# March 28, 2013
#
# 1. For practice, make the petal and flower more general so that fill and color
#    are parameters. Add an outline parameter as well
# 2. If you see code with other turtle packages you can always interpret the code
#    ie. lt means left turn so t.left and so on
#
# modified by: Jan 5, 2020
# updated to python 3: fill 0,1 changed to begin_fill and end_fill
# green is darker in python 3 than 2.7, changed from green to limegreen


import turtle

def petal(t, r, angle):
    """Use the Turtle (t) to draw a petal using two arcs
    with the radius (r) and angle.
    """
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t, n, r, angle):
    """Use the Turtle (t) to draw a flower with (n) petals,
    each with the radius (r) and angle.
    """
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Pen()

# draw a sequence of three flowers, as shown in the book.
# I've added color and fill

#remember to speed up your turtle
bob.speed(0)

bob.color("red")
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

bob.color("limegreen")
move(bob, 100)
flower(bob, 10, 40.0, 80.0)

bob.color("blue")
move(bob, 100)
flower(bob, 20, 140.0, 20.0)

# now draw them filled
bob.pu()
bob.goto(0,150)
bob.color("red")
bob.begin_fill()
move(bob, -100)
flower(bob, 7, 60.0, 60.0)
bob.end_fill()

bob.color("limegreen")
bob.begin_fill()
move(bob, 100)
flower(bob, 10, 40.0, 80.0)
bob.end_fill()

bob.color("blue")
bob.begin_fill()
move(bob, 100)
flower(bob, 20, 140.0, 20.0)
bob.end_fill()

# you could also draw them outlined
bob.pu()
bob.goto(0,300)
move(bob, -100)
bob.color("yellow")
bob.begin_fill()
move(bob, 100)
flower(bob, 10, 40.0, 80.0)
bob.end_fill()
bob.color("black")
bob.width(1)
flower(bob, 10, 40.0, 80.0)

turtle.exitonclick()