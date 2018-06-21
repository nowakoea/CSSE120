"""
Test 1, problem 2.

Authors: David Mutchler, Dave Fisher, their colleagues and Elle Nowakowski.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem2()


def run_test_problem2():
    """ Tests the   problem2  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem2  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    title = 'Exam 1 Problem 2 - Three cars'
    win1 = rg.RoseWindow(700, 400, title)

    # Test 1:
    square1 = rg.Rectangle(rg.Point(175, 100), rg.Point(325, 200))
    square1.fill_color = 'blue'
    problem2(square1, win1)

    # Test 2:
    square2 = rg.Rectangle(rg.Point(385, 300), rg.Point(355, 270))
    square2.fill_color = 'red'
    problem2(square2, win1)

    # Test 3:
    square3 = rg.Rectangle(rg.Point(550, 125), rg.Point(450, 225))
    square3.fill_color = 'green'
    problem2(square3, win1)

    win1.close_on_mouse_click()

    # A fourth test on ANOTHER window.
    title = 'One car'
    win2 = rg.RoseWindow(300, 300, title)

    # Test 4:
    square4 = rg.Rectangle(rg.Point(210, 180), rg.Point(90, 120))
    square4.fill_color = 'yellow'
    problem2(square4, win2)

    win2.close_on_mouse_click()


def problem2(rect, window):
    """
    See   problem2_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      Draws the given rg.Rectangle with tires on it to make it look
      like a car / tractor, as follows:
      
        -- There are two tires, drawn on TOP of the given rg.Rectangle.
             (Achieve this by attaching the rg.Rectangle to the given
             rg.RoseWindow  ** BEFORE **  attaching anything else.)
        
        -- Each tire consists of two filled circles:
             -- a larger BLACK circle (the "rubber" of the tire) and
                a smaller COLORED circle (the "hub" of the tire).
                
        -- For each tire, the colored hub must be on TOP of the black
             rubber part of the tire.  Achieve this by attaching
             the hub to the given rg.RoseWindow  ** AFTER **
             attaching the rubber part to the given rg.RoseWindow.
             
        -- The hub FILL COLORS should be as follows:
             -- The fill color of the hub of the LEFT (front) tire
                  of the tractor should be RED.
             -- The fill color of the hub of the RIGHT (rear) tire
                  of the tractor should be the same color as the
                  fill color of the given rg.Rectangle.

        -- The tires should be SIZED as follows, where W is the WIDTH
             of the given rg.Rectangle:
             -- LEFT (front) BLACK circle ("rubber") has radius 1/4 of W
             -- RIGHT (rear) BLACK circle ("rubber") has radius 1/3 of W
             -- Each colored HUB has radius that is 1/2 of the radius
                  of the black (rubber) circle that it is on top of.
        
        -- The tires should be PLACED as follows:
            -- The LEFT (front) rubber and hub should both be centered
                 at the LOWER LEFT corner of the given rg.Rectangle.
            -- The RIGHT (rear) rubber and hub should both be centered
                 at the LOWER RIGHT corner of the given rg.Rectangle.

      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rect:   rg.Rectangle
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------
    # IMPORTANT:  *** READ THIS! ***
    #
    #   For each tire, its COLORED hub (the smaller circle of the tire)
    #   must be attached to the window   ** AFTER **
    #   its BLACK rubber (the larger circle of the tire) is attached.
    #
    # Otherwise the BLACK will be on TOP of the smaller COLORED circle
    # and you won't be able to see the colored circle.
    # ------------------------------------------------------------------

    rect.attach_to(window)
    w = rect.get_width()
    left_point = rect.get_lower_left_corner()
    right_point = rect.get_lower_right_corner()
    color = rect.fill_color

    left_black_circle = rg.Circle(left_point, w / 4)
    left_black_circle.fill_color = 'black'
    left_black_circle.attach_to(window)

    right_black_circle = rg.Circle(right_point, w / 3)
    right_black_circle.fill_color = 'black'
    right_black_circle.attach_to(window)

    left_radius = left_black_circle.radius
    right_radius = right_black_circle.radius

    left_hub = rg.Circle(left_point, left_radius / 2)
    left_hub.fill_color = 'red'
    left_hub.attach_to(window)

    right_hub = rg.Circle(right_point, right_radius / 2)
    right_hub.fill_color = color
    right_hub.attach_to(window)

    window.render()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
