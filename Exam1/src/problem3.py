"""
Test 1, problem 3.

Authors: David Mutchler, Dave Fisher, their colleagues and Elle Nowakowski.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3   function. """
    # Test 1 is ALREADY DONE (here).
    problem3(rg.Point(20, 20), 200, 10, 'blue')

    # Test 2 is ALREADY DONE (here).
    problem3(rg.Point(100, 100), 100, 2, 'green')

    # Test 3 is ALREADY DONE (here).
    problem3(rg.Point(50, 30), 30, 50, 'yellow')


def problem3(point, dist, n, color):
    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- A positive integer dist.
      -- A positive integer n.
      -- A string that can be used as a color, e.g. 'blue'.
    What goes out:  Nothing (i.e., None).
    Side effects:
      -- Constructs an rg.RoseWindow
         -- Set the width to 500 and height to 300.
         -- Make the title be "Exam 1 Problem 3".
         
      -- Draws a circle (let's call it TOP_LEFT) with radius 10,
            centered at the given rg.Point,
            and with the given color as its fill color.
            
      -- Draws n additional circles moving down and to the right.
          -- Each circle has radius 10 and the given fill color.
          -- Let's call the bottommost (hence also rightmost)
               of the n additional circles the BOTTOM circle.
             It is drawn so that the distance between the center of the
               TOP_LEFT circle and the center of the BOTTOM circle:
                -- Is the given  dist  in the X-direction.
                -- Is 100 in the Y-direction.
          -- The circles between the TOP_LEFT and BOTTOM circles
               are evenly spaced.
        
      -- Draws n additional circles moving *up* and to the right.
          -- Each circle has radius 10 and the given fill color.
          -- Let's call the rightmost (hence also topmost)
               of these n additional circles the TOP_RIGHT circle.
             It is drawn so that the distance between the center of the
               BOTTOM circle and the center of the TOP_RIGHT circle:
                -- Is the given  dist  in the X-direction.
                -- Is 100 in the Y-direction.
          -- The circles between the BOTTOM and TOP_RIGHT circles
               are evenly spaced.
               
      -- All circles should appear at once (no render delays).
         At the end of this function the window should call
           the  close_on_mouse_click  function.

    Type hints:
        :type point: rg.Point
        :type dist:  int
        :type n:     int
        :type color: str
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------

    title = 'Exam 1 Problem 3'
    window = rg.RoseWindow(500, 300, title)

    top_left = rg.Circle(point, 10)
    top_left.fill_color = color
    top_left.attach_to(window)
    x1 = top_left.center.x
    y1 = top_left.center.y

    for _ in range(n):
        circle = rg.Circle(rg.Point(x1 + (dist / n), y1 + (100 / n)), 10)
        circle.fill_color = color
        circle.attach_to(window)
        x1 = x1 + (dist / n)
        y1 = y1 + (100 / n)
        window.render()

    for _ in range(n):
        circle = rg.Circle(rg.Point(x1 + (dist / n), y1 - (100 / n)), 10)
        circle.fill_color = color
        circle.attach_to(window)
        x1 = x1 + (dist / n)
        y1 = y1 - (100 / n)
        window.render()

    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
