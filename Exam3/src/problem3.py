"""
Test 3, problem 3.

Authors: David Fisher, David Mutchler, their colleagues
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3()


def test_problem3():
    """ Tests the    problem3    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3   function:')
    print('--------------------------------------------------')

    print()
    print('Test 1: (5)')
    problem3(5)

    print()
    print('Test 2: (1)')
    problem3(1)

    print()
    print('Test 3: (3)')
    problem3(3)

    print()
    print('Test 4: (6)')
    problem3(6)

    print()
    print('Test 5: (9)')
    problem3(9)


def problem3(r):
    """
    What comes in:
      -- r, which is an integer that is >= 1
    What goes out:
      Nothing (i.e. None)
    Side effects:

    Examples:
    Prints a triangle of numbers, with r rows.
    The first row is 1, the 2nd is 12, the 3rd is 123, etc.
    For example, when r = 5:
           1
          121
         12321
        1234321
       123454321

    For example, when r = 3:
         1
        121
       12321

    For example, when r = 3:
            1
           121
          12321
         1234321
        123454321
       12345654321

    For example, when r = 1:
       1

    The line printed at the bottom of the triangle should be directly
    against the left edge of the console (no leading spaces for that line).

    Type hints:
      :type r:      int
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
