"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and ELle Nowakowski.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

Elle = rg.SimpleTurtle('turtle')
Elle.pen = rg.Pen('blue', 3)
Elle.speed = 20

# The first circle will have a radius of 50 pixels:
radius = 50

# Do the indented code 10 times.  Each time draws a circle.
for k in range(30):
    # Put the pen down, then draw a circle of the given size:
    Elle.draw_circle(radius)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    Elle.pen_up()
    Elle.right(45)
    Elle.forward(10)
    Elle.left(45 + k)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT circle be 3 pixels smaller.
    Elle.pen_down()
    radius = radius - 1.5

nick = rg.SimpleTurtle('turtle')
nick.pen = rg.Pen('red', 3)
nick.speed = 30

# The first octagon will have side lengths of 50 pixels:
sides = 8
length = 50

# Do the indented code 10 times.  Each time draws an octagon.
for k in range(30):
    # Put the pen down, then draw a octagon of the given side number and
    # length:
    nick.draw_regular_polygon(sides, length)

    # Move a little below and to the right of where the previous
    # octagon started.  Do this with the pen up (so nothing is drawn).
    nick.pen_up()
    nick.right(45)
    nick.forward(10)
    nick.left(45 - k)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT octagon be 3 pixels smaller.
    nick.pen_down()
    length = length - 1.5

window.close_on_mouse_click()
