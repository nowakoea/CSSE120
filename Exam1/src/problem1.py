"""
Test 1, problem 1.

Authors: David Mutchler, Dave Fisher, their colleagues and Elle Nowakowski.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import sys


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1a()
    run_test_problem1b()
    run_test_problem1c()


# ----------------------------------------------------------------------
# Students:
#   Do NOT touch the   largest_digit   function below - it has no DONE.
#   Do NOT copy code from the function.
#
# Instead, ** CALL ** the function as needed in the problems below.
# ----------------------------------------------------------------------
def largest_digit(num):
    """
    What comes in:  A nonnegative integer num.
    What goes out:
      Returns the largest digit in the number.
    Side effects: None.
    Examples:
      -- 496 returns 9
      -- 18 returns 8
      -- 2 returns 2
    Type hints:
      :type num: int
    """
    largest_string = "0"
    for digit_string in str(num):
        if digit_string > largest_string:
            largest_string = digit_string
    return int(largest_string)


# ----------------------------------------------------------------------
# Students:
#   Do NOT touch the  smallest_digit  function below - it has no DONE.
#   Do NOT copy code from the function.
#
# Instead, ** CALL ** the function as needed in the problems below.
# ----------------------------------------------------------------------
def smallest_digit(num):
    """
    What comes in:  A nonnegative integer num.
    What goes out:
      Returns the smallest digit in the number.
    Side effects: None.
    Examples:
      -- 496 returns 4
      -- 18 returns 1
      -- 2 returns 2
    Type hints:
      :type num: int
    """
    smallest_string = "9"
    for digit_string in str(num):
        if digit_string < smallest_string:
            smallest_string = digit_string
    return int(smallest_string)


# ----------------------------------------------------------------------
# Students:
#   Do NOT touch the   print_success_or_failure_message   function
#   below - it has no DONE.  Our testing code uses it to print a very
#   visible message (in RED) when your code FAILS a test.
# ----------------------------------------------------------------------
def print_success_or_failure_message(expected, actual, flush_time=0.2):
    """ Prints a message indicating success or failure of the test. """
    if expected == actual:
        # Test passed:
        print("   Test passed SUCCESSFULLY!")

    elif actual == None:
        # Test failed (because the function is not yet implemented):
        print('   Test FAILED.')

    else:
        # Test failed (wrong number returned).
        # Prints a message onto stderr, hence in RED.
        time.sleep(flush_time)
        print('  *** FAILED the above test. ***',
              file=sys.stderr, flush=True)
        time.sleep(flush_time)


# ----------------------------------------------------------------------
# The problems begin here.
# ----------------------------------------------------------------------
def run_test_problem1a():
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 8
    actual = problem1a(185, 207)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 2:
    expected = 6
    actual = problem1a(123, 456)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 3:
    expected = 4
    actual = problem1a(4444, 4444)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 4:
    expected = 0
    actual = problem1a(0, 0)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 5:
    expected = 3
    actual = problem1a(2, 3000)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 6:
    expected = 3
    actual = problem1a(2000, 3)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 7:
    expected = 9
    actual = problem1a(999, 111)
    print()
    print('Test 7 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 8:
    expected = 9
    actual = problem1a(111, 999)
    print()
    print('Test 8 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 9:
    expected = 8
    actual = problem1a(764730377777740054321, 248533387755)
    print()
    print('Test 9 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)


def problem1a(m, n):
    """
    What comes in: Two nonnegative integers, m and n.
    What goes out:
       Returns the overall largest digit used in m or n.
    Side effects: None
    Examples:
        If m is 185 and n is 207, this function should return 8,
        because the largest digit was the 8 digit used in m.

        If m is 123 and n is 456, this function should return 6,
        because the largest digit was the 6 digit used in n.

        If m is 4444 and n is 4444, this function should return 4,
        because the largest digit was the 4 digit used in both m and n.

    Type hints:
      :type m: int
      :type n: int
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   largest_digit   function that is DEFINED ABOVE.
    ####################################################################

    x = largest_digit(m)
    y = largest_digit(n)

    if x > y:
        return x
    else:
        return y


def run_test_problem1b():
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 10
    actual = problem1b(1, 0, 9)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 2:
    expected = 10
    actual = problem1b(9, 1, 0)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 3:
    expected = 10
    actual = problem1b(1, 9, 0)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 4:
    expected = 0
    actual = problem1b(0, 0, 0)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 5:
    expected = 27
    actual = problem1b(99, 99, 99)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 6:
    expected = 18
    actual = problem1b(123, 456, 789)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)


def problem1b(x, y, z):
    """
    What comes in: Three nonnegative integers x, y, and z.
    What goes out: Returns the sum of:
        -- the largest digit in x,
           plus the largest digit in y,
           plus the largest digit in z.
    Side effects: None
    Examples:
        If  x, y, and z are 123, 300, and 456,
        then this function should return 12, because:
             3   [the largest digit in x]
           + 3   [the largest digit in y]
           + 6   [the largest digit in z]
        is  3 + 3 + 6, which is 12.

        If  x, y, and z are 1, 0, and 911,
        then this function should return 10, because:
             1   [the largest digit in x]
           + 0   [the largest digit in y]
           + 9   [the largest digit in z]
        is  1 + 0 + 9, which is 10.

    Type hints:
      :type x: int
      :type y: int
      :type z: int
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    ####################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately use (call)
    #    **  the   largest_digit   function that is DEFINED ABOVE.
    ####################################################################

    a = largest_digit(x)
    b = largest_digit(y)
    c = largest_digit(z)

    return (a + b + c)


def run_test_problem1c():
    # ------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  problem1c  function defined below.
    #   Include at least **   11   ** tests (we wrote 9 for you).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1c   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 5
    actual = problem1c(2, 4)
    print()
    print('Test 1 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 2:
    expected = 3
    actual = problem1c(4, 6)
    print()
    print('Test 2 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 3:
    expected = 2
    actual = problem1c(15, 25)
    print()
    print('Test 3 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 4:
    expected = 1
    actual = problem1c(0, 0)
    print()
    print('Test 4 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 5:
    expected = 0
    actual = problem1c(20, 20)
    print()
    print('Test 5 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 6:
    expected = 2
    actual = problem1c(123, 234)
    print()
    print('Test 6 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 7:
    expected = 8
    actual = problem1c(1, 5)
    print()
    print('Test 7 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 8:
    expected = 9
    actual = problem1c(4, 40)
    print()
    print('Test 8 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 9:
    expected = 37
    actual = problem1c(11, 111111)
    print()
    print('Test 9 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # ------------------------------------------------------------------
    # DONE: 4 (continued).
    # Below this comment, add 2 more test cases of your own choosing.
    # ------------------------------------------------------------------

    # Test 10:
    expected = 7
    actual = problem1c(1, 4)
    print()
    print('Test 10 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)

    # Test 11:
    expected = 5
    actual = problem1c(1, 3)
    print()
    print('Test 11 expected:', expected)
    print('       actual:  ', actual)
    print_success_or_failure_message(expected, actual)


def problem1c(m, n):
    """
    What comes in: Two nonnegative integers, m and n, where m <= n.
    What goes out:
      Let's say that an integer X is a SAME-DIGITS INTEGER if all of
      its digits are the same. That is, the following are all of
      the SAME-DIGITS integers:
           1, 2, 3, ... 9,
          11, 22, 33, ... 99,
         111, 222, 333, ... 999,
        1111, 2222, 3333, ... 9999,
          etc
          
      This function returns the number of SAME-DIGITS integers
      between (2 * m) and (2 * n), inclusive.
      
      ** IMPORTANT: SEE NOTE IN PINK BELOW RE SAME-DIGITS INTEGERS. **
        
    Side effects: None
    Examples:
      -- If m is 2 and n is 4, then this function returns 5,
           because all the integers from (2 * 2) to (2 * 4),
           namely, 4, 5, 6, 7, and 8, are SAME-DIGITS integers.
           
      -- If m is 4 and n is 6, then this function returns 3,
           because of the integers from (2 * 4) to (2 * 6),
           8, 9 and 11 are SAME-DIGITS integers,
           while 10 and 12 are NOT SAME-DIGITS integers.
           
      -- If m is 15 and n is 25, then this function returns 2,
           because 33 and 44 are the only two SAME-DIGITS integers
           between 30 (which is 2 * m) and 50 (which is 2 * n).

    ** IMPORTANT: SEE NOTE IN PINK BELOW RE SAME-DIGITS INTEGERS. **

    Type hints:
      :type m: int
      :type n: int
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   We supplied some of the tests but
    #     *** YOU MUST ADD TWO MORE TESTS IN THE ABOVE TESTING FUNCTION.
    #
    ####################################################################
    # IMPORTANT:  *** READ THIS! ***
    #
    #   Note that an integer X is a SAME-DIGITS integer if and only if
    #   the largest digit in X equals the smallest digit in X.
    #
    #   Don't try to figure out a "formula" for what this function
    #   should return.  Instead, just loop from 2m to 2n, inclusive,
    #   and use the above property to judge whether the integers
    #   that you examine are SAME-DIGITS integers.
    #
    #    **  For full credit you must appropriately use (call)
    #    **  the  smallest_digit  and  largest_digit  functions
    #        DEFINED ABOVE.
    ####################################################################

    total = 0

    for k in range((2 * n) - (2 * m) + 1):
        if largest_digit(k + (m * 2)) == smallest_digit(k + (m * 2)):
            total = total + 1

    return total


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
