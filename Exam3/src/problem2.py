""""
Test 3, problem 2.

Authors: David Fisher, David Mutchler, their colleagues
         and PUT_YOUR_NAME_HERE. 
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
import traceback

import rosegraphics as rg

import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """

    ####################################################################
    # STUDENTS:  UN-comment these tests as you work the problems.
    ####################################################################

    test_init()

    # NOTE: Once you pass the VISUAL tests for the  draw  method,
    # COMMENT OUT the following call to the  test_draw  function.
    # None of the remaining tests do any drawing.

#     test_draw()
#
#     test_set_color()
#     test_add_line()
#     test_add_list_of_lines()
#     test_get_lines_added()
#     test_combine_with()
#     test_give_lines_to()


########################################################################
# The   LineListController   class (and its methods) begins here.
########################################################################

class LineListController(object):
    """
    A LineListController has:
        -- lines, a list of rg.Line objects
        -- color, a string that corresponds to a rosegraphics color.
            Every rg.Line in self.lines must have its color property
            set to this color value.  When this color changes via the
            set_color method all lines need to have their color property
            updated.  Hence, all the lines always have the same color.
        -- max_lines, an integer that stores the maximum number of
            rg.Line objects allowed in the lines list.
    """

    def __init__(self, lines, color, max_lines):
        """
        What comes in:
          -- lines, which is a list of rg.Line objects
          -- color, which is a string that corresponds to a rosegraphics color
          -- max_lines, which is an integer that specifies the maximum
               number of rg.Line objects allowed in the lines list.
        What goes out: Nothing (i.e., None).
        Side effects:
          -- Stores the arguments (lines, colors, max_lines)
             in the instance variables:

                  self.lines
                  self.color
                  self.max_lines

             You do not need to clone (copy) the  lines  list that is
             given as an argument, although you may do so if you wish.

             You should assume that the length of the given list of
             rg.Line objects is not greater than the given max_lines.
             You do NOT need to test for this; all the test cases will
             supply a list whose length is not bigger than max_lines.

          -- Additionally the color of EACH rg.Line in the  self.lines
               list must be set to the given color.

        Examples:
          line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
          line1.color = 'green'
          line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
          line1.color = 'purple'
          line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
          line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

          llc1 = LineListController([line1, line2, line3, line4], 'red', 10)
            #   llc1.lines     is now [line1, line2, line3, line4]
            #   llc1.color     is now  'red'
            #   llc1.max_lines is now 10
            # and all four lines need to have their color set to 'red'

          line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
          line5.color = 'green'
          line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
          line6.color = 'purple'

          llc2 = LineListController([line5, line6], 'blue', 2)
            #   llc1.lines     is now [line5, line6]
            #   llc1.color     is now  'blue'
            #   llc1.max_lines is now 2
            # lines5 and line6 need to have their color set to 'blue'

        Type hints:
          :type lines: [rg.Line]
          :type color:  string
          :type max_lines:  positive number
        """
        # --------------------------------------------------------------
        # TODO: 2. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def draw(self, window):
        """
        What comes in:
          -- self
          -- window, which is a rg.RoseWindow
        What goes out:
          -- Nothing (i.e. None)
        Side effects:
          -- Draws the lines of this LineListController onto the window
          -- Renders the lines onto the window, but does not close the window
        Examples:
          line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
          line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
          llc1 = LineListController([line1, line2], 'red', 10)

          window = rg.RoseWindow(500, 500, title="Example code")
          llc1.draw(window)
            # Draw adds the two red lines to the window and renders the window
          window.close_on_mouse_click()
        """
        # --------------------------------------------------------------
        # TODO: 3. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------
        
    def set_color(self, color):
        """
        What comes in:
          -- self
          -- color, a string that corresponds to a rosegraphics color
        What goes out:
          -- Nothing (i.e. None)
        Side effects:
          -- Sets the color property of the LineListController to the new
             color
          -- Changes the color property of every rg.Line in the lines list
             to the new color as well.
        Examples:
              line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
              line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
              llc1 = LineListController([line1, line2], 'red', 10)

              llc1.set_color('yellow')
                #   llc1.lines     is still [line1, line2]
                #   llc1.color     is now  'yellow'
                #   llc1.max_lines is still 10
                # lines1 and line1 now have their color set to 'yellow'
        """
        # --------------------------------------------------------------
        # TODO: 4. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def add_line(self, line):
        """
        What comes in:
          -- self
          -- line, which is a rg.Line
        What goes out:
          -- Nothing (i.e. None)
        Side effects:
          -- If the number of lines in the lines list is already at the max_lines
             then return immediately, no line my be added.
          -- If space is available add the given line to the lines property.
          -- Additionally update the new line's color property to match the
             color property of this LineListController
        Examples:
              line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
              line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
              llc1 = LineListController([line1, line2], 'red', 3)

              line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
              llc1.add_line(line3)
                #   llc1.lines     is now [line1, line2, line3]
                #   llc1.color     is still 'red'
                #   llc1.max_lines is still 3
                # lines1, line2, and line3 have their color set to 'red'

              line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))
              line4.color = 'purple'
              llc1.add_line(line4)
                #   llc1.lines     is still [line1, line2, line3]
                #   llc1.color     is still 'red'
                #   llc1.max_lines is still 3
                # lines4 was not added since no room was available.
                # the color of line4 is still 'purple' since it was not added.
        """
        # --------------------------------------------------------------
        # TODO: 5. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def add_list_of_lines(self, lines):
        """
        What comes in:
          -- self
          -- lines, which is a list of rg.Line objects
        What goes out:
          -- Nothing (i.e. None)
        Side effects:
          -- Adds all the lines in the given list of rg.Line objects
             that will fit in this LineListController,
             *** AND DOES SO SIMPLY BY CALLING the  add_line  METHOD APPROPRIATELY.
        Examples:
              See test cases or ask your instructor to provide
              an example.
        """
        # --------------------------------------------------------------
        # TODO: 6. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # NO CREDIT unless this method uses (calls)  add_line  appropriately.
        # --------------------------------------------------------------

    def get_lines_added(self):
        """
        What comes in:
          -- self
        What goes out:
          -- Returns the number of lines that have been added to the LineListController
             via the add_line method. Note that if the add_line method was
             called, but no line was added since the LineListController was
             already at the max_lines then that does not count as a line added
             to the lines list (since no line was added).
        Side effects:
          -- None
        Examples:
              line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
              line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
              llc1 = LineListController([line1, line2], 'red', 3)
              num_lines_added = llc1.get_lines_added()
                #   num_lines_added     is 0
                # since no lines have been added via add_lines

              line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
              llc1.add_line(line3)
              num_lines_added = llc1.get_lines_added()
                #   num_lines_added     is 1
                # since 1 line has been added via add_lines

              line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))
              llc1.add_line(line4)
              num_lines_added = llc1.get_lines_added()
                #   num_lines_added     is 1
                # since line4 was not added (llc1 was already at max_lines value of 3)
        """
        # --------------------------------------------------------------
        # TODO: 7. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def combine_with(self, another_llc, color):
        """
        What comes in:
          -- self
          -- another_llc, which is another LineListController
          -- color, which is a string representing a Rosegraphics color
        What goes out:
          Returns a new LineListController whose:
              -- lines is the sum of this LineListControllers lines plus
                  another_llc lines
              -- color is passed in color
              -- max_lines is the sum of the max_lines of the two
                  LineListControllers objects
             lines are this LineList
        Side effects:
          -- None.
        Examples:
              line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
              line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
              llc1 = LineListController([line1, line2], 'red', 3)

              line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
              line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))
              llc2 = LineListController([line3, line4], 'yellow', 10)

              llc3 = llc1.combine_with(llc2, 'purple')

                #   llc1.lines     is now []
                #   llc1.color     is still 'red'
                #   llc1.max_lines is still 3

                #   llc2.lines     is now []
                #   llc2.color     is still 'yellow'
                #   llc2.max_lines is still 10

                #   llc3.lines     is [line1, line2, line3, line4]
                #   llc3.color     is 'purple'
                #   llc3.max_lines is 13
                # lines1, line2, line3, and line4 have their color set to 'purple'

        Type hints:
          :type another_llc: LineListController
          :type color: string
        """
        # --------------------------------------------------------------
        # TODO: 8. Implement and test this function.
        #     See the testing code (below) for more examples.
        # --------------------------------------------------------------

    def give_lines_to(self, another_llc):
        """
        What comes in:
          -- self
          -- another_llc, which is another LineListController
        What goes out:
          -- Returns the number of lines that were successfully given to
             another_llc
        Side effects:
          -- Gives all the lines from this LineListController to another_llc
          -- This always results in this LineListController having no lines
             remaining regardless of the success of adding it to the another_llc
             lines list.
          -- The another_llc lines property only adds lines that fit
             and updates their color to match the another_llc color property
          -- The lines that are added to another_llc stay in the same order
             relative to one another, and they are added to the end of another_llc's
             line list.  i.e. The first line moved over is the first line in this
             LineListController's lines list, then the second is added, etc.
          -- Lines that cannot be added to the another_llc due to the max_lines
             value should not be modified (i.e. their color should not be changed)
             Note, that they are removed from this LineListController regardless.
        Examples:
              line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
              line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
              llc1 = LineListController([line1, line2], 'red', 3)

              line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
              line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))
              llc2 = LineListController([line3, line4], 'yellow', 10)

              lines_moved = llc2.give_lines_to(llc1)

                #   lines_moved    is 1

                #   llc1.lines     is now [line1, line2, line3]
                #   llc1.color     is still 'red'
                #   llc1.max_lines is still 3
                # lines1, line2, and line3 have their color set to 'red'

                #   llc2.lines     is now []
                #   llc2.color     is still 'yellow'
                #   llc2.max_lines is still 10
                # lines4 is still 'yellow' but it is not with any LineListController
        """
        # --------------------------------------------------------------
        # TODO: 9. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # For full credit, you must appropriately
        # use (call) the RELEVANT METHODS that YOU implemented above.
        # --------------------------------------------------------------
        

########################################################################
# The TEST functions for the  LineListController  class begin here.
########################################################################

# ----------------------------------------------------------------------
# These methods are used in most of the tests:
# ----------------------------------------------------------------------
def equal_line(llc_line, expected_line):
    return (llc_line.start.x == expected_line.start.x and
            llc_line.start.y == expected_line.start.y and
            llc_line.end.x == expected_line.end.x and
            llc_line.end.y == expected_line.end.y and
            llc_line.color == expected_line.color)


def equal_lines(actual_lines, expected_lines):
    if len(actual_lines) != len(expected_lines):
        return False

    lines_are_equal = True
    for k in range(len(actual_lines)):
        print("lines[{}] Actual:   {}\n         Expected: {}".format(
            k, actual_lines[k], expected_lines[k]))
        if not equal_line(actual_lines[k], expected_lines[k]):
            lines_are_equal = False
    return lines_are_equal


def copy_lines_list(lines):
    copy = []
    for line in lines:
        copy.append(line.clone())
    return copy


def test_instance_variables(llc, expected_lines, expected_color, expected_max_lines):
    """
    Tests whether the instance variables for the given llc
    are per the given expected values.
      type: llc:   LineListController
    """
    try:
        format_string = '{:9} {:10}     {:6} {:8}'
        print('            len(lines)  color      max_lines')
        print(format_string.format('Expected:',
                                   len(expected_lines), expected_color, expected_max_lines))
        print(format_string.format('Actual:',
                                   len(llc.lines), llc.color, llc.max_lines))
        if (len(expected_lines) == len(llc.lines) and expected_color == llc.color
                and expected_max_lines == llc.max_lines and equal_lines(llc.lines, expected_lines)):
            print("Test passed SUCCESSFULLY!")
        else:
            print_failure_message()
    except Exception:
        print_failure_message()
        print("An error was thrown in the test code. This is most likely due to your code " +
              "sending incorrect values to be tested.")
        traceback.print_exc()
        print_failure_message("")


def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=0.5):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message,
          file=sys.stderr, flush=True)
    time.sleep(flush_time)


# ----------------------------------------------------------------------
# Specific tests
# ----------------------------------------------------------------------
def test_init():
    """ Tests the   __init__   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'

    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    print()
    print("Test #1:")
    lines1 = [line1, line2, line3, line4]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'red'
        expected_lines1.append(l)

    llc1 = LineListController(copy_lines_list(lines1), 'red', 10)
    test_instance_variables(llc1, expected_lines1, 'red', 10)

    # Test 2
    print()
    print("Test #2:")
    lines2 = [line5, line6]
    expected_lines2 = [line5.clone(), line6.clone()]
    for line in expected_lines2:
        line.color = 'blue'
    expected_line7 = line7.clone()
    expected_line7.color = line7.color
    expected_line8 = line8.clone()
    expected_line8.color = line8.color

    llc2 = LineListController(copy_lines_list(lines2), 'blue', 2)
    test_instance_variables(llc2, expected_lines2, 'blue', 2)

#     # Test 3
#     print()
#     print("Test #3:")
#     print("line7 Actual:   {}\n      Expected: {}".format(
#         line7, expected_line7))
#     if equal_line(line7, expected_line7):
#         print("Test passed SUCCESSFULLY!")
#     else:
#         print_failure_message()
#
#     # Test 4
#     print()
#     print("Test #4:")
#     print("line8 Actual:   {}\n      Expected: {}".format(
#         line8, expected_line8))
#     if equal_line(line8, expected_line8):
#         print("Test passed SUCCESSFULLY!")
#     else:
#         print_failure_message()


def test_draw():
    """ Tests the   draw   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   draw   method.')
    print('See the graphics window for the test results')
    print('Close that window to continue future tests')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'

    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    win = rg.RoseWindow(500, 500, title="Testing draw.  #1")
    lines1 = [line1, line2, line3, line4]
    llc1 = LineListController(copy_lines_list(lines1), 'red', 10)
    llc1.draw(win)

    # Test 2
    lines2 = [line5, line6]
    llc2 = LineListController(copy_lines_list(lines2), 'blue', 2)
    llc2.draw(win)

    title = "You should see a red box (4 lines) and 2 lines of blue."
    win.continue_on_mouse_click(title)
    win.close()


def test_set_color():
    """ Tests the   set_color   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   set_color   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'
    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    print()
    print("Test #1:")
    lines1 = [line1, line2, line3, line4]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'yellow'
        expected_lines1.append(l)

    llc1 = LineListController(copy_lines_list(lines1), 'red', 10)
    llc1.set_color('yellow')
    test_instance_variables(llc1, expected_lines1, 'yellow', 10)

    # Test 2
    print()
    print("Test #2:")
    lines2 = [line5, line6]
    expected_lines2 = [line5.clone(), line6.clone()]
    for line in expected_lines2:
        line.color = 'pink'
    expected_line7 = line7.clone()
    expected_line7.color = line7.color
    expected_line8 = line8.clone()
    expected_line8.color = line8.color

    llc2 = LineListController(copy_lines_list(lines2), 'blue', 2)
    llc2.set_color('pink')
    test_instance_variables(llc2, expected_lines2, 'pink', 2)

    # Test 3
    print()
    print("Test #3:")
    print("line7 Actual:   {}\n      Expected: {}".format(
        line7, expected_line7))
    if equal_line(line7, expected_line7):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 4
    print()
    print("Test #4:")
    print("line8 Actual:   {}\n      Expected: {}".format(
        line8, expected_line8))
    if equal_line(line8, expected_line8):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


def test_add_line():
    """ Tests the   add_line   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   add_line   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'
    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    print()
    print("Test #1:")
    lines1 = [line1, line2, line3, line4]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'red'
        expected_lines1.append(l)
    another_line7 = line7.clone()
    another_line7.color = 'red'
    expected_lines1.append(another_line7)

    llc1 = LineListController(copy_lines_list(lines1), 'red', 10)
    llc1.add_line(line7)
    test_instance_variables(llc1, expected_lines1, 'red', 10)

    # Test 2
    print()
    print("Test #2:")
    lines2 = [line5, line6]
    expected_lines2 = [line5.clone(), line6.clone()]
    for line in expected_lines2:
        line.color = 'blue'

    expected_line7 = line7.clone()
    expected_line7.color = line7.color
    expected_line8 = line8.clone()
    expected_line8.color = line8.color

    llc2 = LineListController(copy_lines_list(lines2), 'blue', 2)
    llc2.add_line(line8)
    test_instance_variables(llc2, expected_lines2, 'blue', 2)

    # Test 3
    print()
    print("Test #3:")
    print("line8 Actual:   {}\n      Expected: {}".format(
        line8, expected_line8))
    if equal_line(line8, expected_line8):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


def test_add_list_of_lines():
    """ Tests the   add_list_of_lines   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print(
        'Testing the   add_list_of_lines   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'
    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    print()
    print("Test #1:")
    lines1 = [line1, line2]
    lines2 = [line3, line4, line5]
    expected_lines1 = []
    for line in (lines1 + lines2):
        l = line.clone()
        l.color = 'red'
        expected_lines1.append(l)

    llc1 = LineListController(copy_lines_list(lines1), 'red', 6)
    llc1.add_list_of_lines(lines2)
    test_instance_variables(llc1, expected_lines1, 'red', 6)

    # Test 2
    lines1 = [line1, line2]
    lines2 = [line3, line4, line5]
    lines3 = [line6, line7]
    expected_lines2 = []
    for line in (lines1 + lines2 + [line6]):
        l = line.clone()
        l.color = 'blue'
        expected_lines2.append(l)

    llc2 = LineListController(copy_lines_list(lines1 + lines2), 'blue', 6)
    llc2.add_list_of_lines(lines3)
    test_instance_variables(llc2, expected_lines2, 'blue', 6)

#     # Test 3
#     print()
#     print("Test #3:")
#     print("line8 Actual:   {}\n      Expected: {}".format(
#         line8, expected_line8))
#     if equal_line(line8, expected_line8):
#         print("Test passed SUCCESSFULLY!")
#     else:
#         print_failure_message()


def test_get_lines_added():
    """ Tests the   get_lines_added   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print(
        'Testing the   get_lines_added   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line1.color = 'green'
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line1.color = 'purple'
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'
    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 1
    lines1 = [line1, line2, line3, line4]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'red'
        expected_lines1.append(l)
    another_line7 = line7.clone()
    another_line7.color = 'red'
    expected_lines1.append(another_line7)

    llc1 = LineListController(copy_lines_list(lines1), 'red', 10)
    llc1.add_line(line7)

    print()
    print("Test #1:")
    expected = 1
    actual = llc1.get_lines_added()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 2
    lines2 = [line5, line6]
    expected_lines2 = [line5.clone(), line6.clone()]
    for line in expected_lines2:
        line.color = 'blue'
    expected_line7 = line7.clone()
    expected_line7.color = line7.color
    expected_line8 = line8.clone()
    expected_line8.color = line8.color

    llc2 = LineListController(copy_lines_list(lines2), 'blue', 2)
    llc2.add_line(line8)

    print()
    print("Test #2:")
    expected = 0
    actual = llc2.get_lines_added()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 3
    llc1.add_line(line8)
    print()
    print("Test #3:")
    expected = 2
    actual = llc1.get_lines_added()
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


def test_combine_with():
    """ Tests the   combine_with   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print(
        'Testing the   combine_with   method of the LineListController class.')
    print('-----------------------------------------------------------')

    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    llc1 = LineListController(copy_lines_list([line1, line2]), 'red', 3)

    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))
    llc2 = LineListController(copy_lines_list([line3, line4]), 'yellow', 10)

    #   llc1.lines     is now []
    #   llc1.color     is still 'red'
    #   llc1.max_lines is still 3

    #   llc2.lines     is now []
    #   llc2.color     is still 'yellow'
    #   llc2.max_lines is still 10

    #   llc3.lines     is [line1, line2, line3, line4]
    #   llc3.color     is 'purple'
    #   llc3.max_lines is 13
    # lines1, line2, line3, and line4 have their color set to 'purple'

    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'

    # Test 1
    print()
    print("Test #1:")
    lines1 = [line1, line2, line3, line4]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'purple'
        expected_lines1.append(l)

    llc3 = llc1.combine_with(llc2, 'purple')
    test_instance_variables(llc3, expected_lines1, 'purple', 13)

    # Test 2
    print()
    print("Test #2:")
    lines2 = [line5, line6]
    expected_lines2 = [line5.clone(), line6.clone()]
    for line in expected_lines2:
        line.color = 'blue'

    llc4 = LineListController(copy_lines_list(lines2), 'red', 2)
    llc5 = LineListController(copy_lines_list([]), 'yellow', 0)
    llc6 = llc5.combine_with(llc4, 'blue')
    test_instance_variables(llc6, expected_lines2, 'blue', 2)


def test_give_lines_to():
    """ Tests the   give_lines_to   method of the LineListController class. """
    print()
    print('-----------------------------------------------------------')
    print(
        'Testing the   give_lines_to   method of the LineListController class.')
    print('-----------------------------------------------------------')

    # Group 1 tests
    line1 = rg.Line(rg.Point(100, 100), rg.Point(200, 100))
    line2 = rg.Line(rg.Point(200, 100), rg.Point(200, 200))
    line3 = rg.Line(rg.Point(200, 200), rg.Point(100, 200))
    line4 = rg.Line(rg.Point(100, 200), rg.Point(100, 100))

    lines1 = [line1, line2, line3]
    expected_lines1 = []
    for line in lines1:
        l = line.clone()
        l.color = 'red'
        expected_lines1.append(l)
    expected_line4 = line4.clone()
    expected_line4.color = 'yellow'

    llc1 = LineListController(copy_lines_list([line1, line2]), 'red', 3)
    llc2 = LineListController(copy_lines_list([line3, line4]), 'yellow', 10)
    real_line4 = llc2.lines[1]
    lines_moved = llc2.give_lines_to(llc1)

    print()
    print("Test #1:")
    test_instance_variables(llc1, expected_lines1, 'red', 3)

    print()
    print("Test #2:")
    test_instance_variables(llc2, [], 'yellow', 10)

    print()
    print("Test #3:")
    print("line4 Actual:   {}\n      Expected: {}".format(
        real_line4, expected_line4))
    if not equal_line(real_line4, expected_line4):
        print_failure_message()

    print()
    print("Test #4:")
    expected = 1
    actual = lines_moved
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Group 2 tests
    line5 = rg.Line(rg.Point(300, 100), rg.Point(400, 100))
    line5.color = 'green'
    line6 = rg.Line(rg.Point(400, 100), rg.Point(400, 200))
    line6.color = 'purple'
    line7 = rg.Line(rg.Point(400, 200), rg.Point(300, 200))
    line7.color = 'purple'
    line8 = rg.Line(rg.Point(300, 200), rg.Point(300, 100))
    line8.color = 'yellow'

    # Test 2
    lines2 = [line5, line6, line7, line8]
    expected_lines2 = []
    for line in lines2:
        line.color = 'blue'
        expected_lines2.append(line)

    llc3 = LineListController(copy_lines_list(lines2), 'red', 4)
    llc4 = LineListController(copy_lines_list([]), 'blue', 20)
    lines_moved = llc3.give_lines_to(llc4)

    print()
    print("Test #5:")
    test_instance_variables(llc4, expected_lines2, 'blue', 20)

    print()
    print("Test #6:")
    test_instance_variables(llc3, [], 'red', 4)

    print()
    print("Test #7:")
    expected = 4
    actual = lines_moved
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
