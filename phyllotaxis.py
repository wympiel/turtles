# Spiral Phyllotaxis Demo
#
# Example for VSFX 705
# Introduce Phyllotactic Pattern
#
# Author: Deborah R. Fowler
#
# March 21, 2013
# Based on original code in C 1989 using Silicon Graphics Workstations and gl

import math
import turtle


def drawPhyllotacticPattern(t, angle=137.508, size=2, c=4):
    """print a pattern of circles using spiral phyllotactic data"""
    # initialize variables
    phi = angle * (math.pi / 180.0)
    xcenter = 0.0
    ycenter = 0.0

    # for loops iterate in this case from the first value until < 4, so
    for i in range(0, t):
        r = c * math.sqrt(i)
        theta = i * phi
        x = r * math.cos(theta) + xcenter
        y = r * math.sin(theta) + ycenter

        # move the turtle to that position and draw a dot
        turtle.up()
        turtle.setpos(x, y)
        turtle.down()
        turtle.dot()
        turtle.down()


turtle.speed(0)  # make the turtle go as fast as possible
drawPhyllotacticPattern(100, 137.508, 2, 4)
# drawPhyllotacticPattern( 5000, 137.5, 2, 4 )
turtle.mainloop()  # lets you x out of the window


