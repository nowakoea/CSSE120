"""
Test 3 problem 1

Authors: David Fisher, David Mutchler, their colleagues
         and Elle Nowakowski.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
import sys
import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1a()
    test_problem1b()


def test_problem1a():
    """ Tests the    problem1a    function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1a   function:')
    print('--------------------------------------------------')

    # Test 1:
    print()
    print("Test #1:")
    list1 = [('once', 'upon', 'sad', 'gargoyle', 'funny'),
             ('hello', 'goodbye', 'teacher'),
             ('funny', 'sad', 'fetish'),
             [],
             ['ok'],
             ('nope', 'yep', '', 'sad')
             ]
    expected = 3
    actual = problem1a(list1, 'sad')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 2:
    print()
    print("Test #2:")
    list1 = [('once', 'upon', 'sad', 'gargoyle', 'funny'),
             ('hello', 'goodbye', 'teacher'),
             ('funny', 'sad', 'fetish'),
             [],
             ['ok'],
             ('nope', 'yep', '', 'sad')
             ]
    expected = 2
    actual = problem1a(list1, 'funny')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 3:
    print()
    print("Test #3:")
    list1 = [('once', 'upon', 'sad', 'gargoyle', 'funny'),
             ('hello', 'goodbye', 'teacher'),
             ('funny', 'sad', 'fetish'),
             [],
             ['ok'],
             ('nope', 'yep', '', 'sad')
             ]
    expected = 1
    actual = problem1a(list1, 'yep')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 4:
    print()
    print("Test #4:")
    list1 = [('once', 'upon', 'sad', 'gargoyle', 'funny'),
             ('hello', 'goodbye', 'teacher'),
             ('funny', 'sad', 'fetish'),
             [],
             ['ok'],
             ('nope', 'yep', '', 'sad')
             ]
    expected = 0
    actual = problem1a(list1, 'good')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 5:
    print()
    print("Test #5:")
    list1 = [('once', 'upon', 'sad', 'gargoyle', 'funny'),
             ('hello', 'goodbye', 'teacher'),
             ('funny', 'sad', 'fetish'),
             [],
             ['ok'],
             ('nope', 'yep', '', 'sad')
             ]
    expected = 1
    actual = problem1a(list1, '')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()

    # Test 6:
    print()
    print("Test #6:")
    list1 = []
    for _ in range(100):
        list1.append("x")
        list1.append("o")
    expected = 300
    actual = problem1a([[], list1, list1, [], list1], 'x')
    print("Expected:", expected)
    print("Actual:  ", actual)
    if expected == actual:
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()


def problem1a(sequence_of_sequences, word_to_look_for):
    """
    What comes in:
      -- A sequence of subsequences,
           where each subsequence contains only words (i.e., strings).
      -- A word_to_look_for
    What goes out:
      Returns a count for how many times the word was found.
    Side effects: None.
    Examples:
      Suppose that the given sequence is:
         [('once', 'upon', 'sad', 'gargoyle', 'funny'),
          ('hello', 'goodbye', 'teacher'),
          ('funny', 'sad', 'fetish'),
          [],
          ['ok'],
          ('nope', 'yep', '', 'sad')
         ]
      Then:
        If the  word_to_look_for  is 'sad', this function returns 3.
        If the  word_to_look_for  is 'funny', this function returns 2.
        If the  word_to_look_for  is 'yep', this function returns 1.
        If the  word_to_look_for  is 'good', this function returns 0.
        If the  word_to_look_for  is '', this function returns 1.
    Type hints:
      :type sequence_of_sequences: sequence of sequences of strings
      :type word_to_look_for:      str
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # ------------------------------------------------------------------
    counter = 0

    for j in range(len(sequence_of_sequences)):

        sublist = sequence_of_sequences[j]

        for k in range(len(sublist)):

            if sublist[k] == word_to_look_for:
                counter = counter + 1

    return counter


def test_problem1b():
    """ Tests the    problem1b    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1b   function:')
    print('--------------------------------------------------')

    clist1 = [rg.Circle(rg.Point(100, 100), 20),
              rg.Circle(rg.Point(200, 100), 40),
              rg.Circle(rg.Point(300, 100), 30)]
    clist2 = [
        rg.Circle(rg.Point(190, 200), 20), rg.Circle(rg.Point(300, 200), 30)]
    clist3 = [
        rg.Circle(rg.Point(150, 300), 30), rg.Circle(rg.Point(300, 300), 300)]

    # Test 1:
    print()
    print("Test #1")
    expected = 0.5714285714285714
    actual = problem1b([clist1, clist2, clist3], 25, 35)
    print("Expected:", expected)
    print("Actual:", actual)
    # Use extra caution with the return value since round is called on it.
    if not (actual is not None and type(actual) is float):
        print_failure_message()
    else:
        if round(expected, 6) == round(actual, 6):
            print("Test passed SUCCESSFULLY!")
        else:
            print_failure_message()

    clist1 = [rg.Circle(rg.Point(100, 100), 20),
              rg.Circle(rg.Point(200, 100), 40),
              rg.Circle(rg.Point(300, 100), 30)]
    clist2 = [
        rg.Circle(rg.Point(190, 200), 20), rg.Circle(rg.Point(300, 200), 30)]
    clist3 = [
        rg.Circle(rg.Point(150, 300), 30), rg.Circle(rg.Point(300, 300), 300)]

    # Test 2:
    print()
    print("Test #2")
    expected = 0.0
    actual = problem1b([clist1, clist2, clist3], 0, 1000)
    print("Expected:", expected)
    print("Actual:", actual)
    # Use extra caution with the return value since round is called on it.
    if not (actual is not None and type(actual) is float):
        print_failure_message()
    else:
        if round(expected, 6) == round(actual, 6):
            print("Test passed SUCCESSFULLY!")
        else:
            print_failure_message()

    clist1 = [rg.Circle(rg.Point(100, 100), 2),
              rg.Circle(rg.Point(200, 100), 40),
              rg.Circle(rg.Point(300, 100), 30)]
    clist2 = [
        rg.Circle(rg.Point(190, 200), 20), rg.Circle(rg.Point(300, 200), 30)]
    clist3 = [
        rg.Circle(rg.Point(150, 300), 30), rg.Circle(rg.Point(300, 300), 300)]

    # Test 3:
    print()
    print("Test #3")
    expected = 1.0
    actual = problem1b([clist1, clist2, clist3], 3, 5)
    print("Expected:", expected)
    print("Actual:", actual)
    # Use extra caution with the return value since round is called on it.
    if not (actual is not None and type(actual) is float):
        print_failure_message()
    else:
        if round(expected, 6) == round(actual, 6):
            print("Test passed SUCCESSFULLY!")
        else:
            print_failure_message()


def problem1b(seq_of_seq, min_radius, max_radius):
    """
        What goes in:
        -- seq_of_seq, a sequence containing subsequences,
            where each subsequence contains onl rg.Circle objects
        -- two integers: min_radius and max_radius
    What goes out:
      -- A value from 0.0 to 1.0 representing the fraction of circles that were modified.
         0 if no circles were modified
         1 if all circles were modified
         A value between 0 to 1 if some were modified (i.e. 0.5 if half were modified)
    Side Effects:
      -- Circles with a radius < min_radius have their radius set to min_radius
      -- Circles with a radius > max_radius have their radius set to max_radius

    For example
        clist1 = [rg.Circle(rg.Point(100, 100), 20), rg.Circle(rg.Point(200, 100), 40),
                  rg.Circle(rg.Point(300, 100), 30)]
        clist2 = [rg.Circle(rg.Point(190, 200), 20), rg.Circle(rg.Point(300, 200), 30)]
        clist3 = [rg.Circle(rg.Point(150, 300), 30), rg.Circle(rg.Point(300, 300), 300)]

        percentage_modified = problem1b([clist1, clist2, clist3], 25, 35)

        After this function the circles have the values modified to:
        clist1 = [rg.Circle(rg.Point(100, 100), 25), rg.Circle(rg.Point(200, 100), 35),
                  rg.Circle(rg.Point(300, 100), 30)]
        clist2 = [rg.Circle(rg.Point(190, 200), 25), rg.Circle(rg.Point(300, 200), 30)]
        clist3 = [rg.Circle(rg.Point(150, 300), 30), rg.Circle(rg.Point(300, 300), 35)]

        and percentage_modified is roughly 0.571428 since 4 of the 7 circles were modified.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #     The testing code is already written for you (above).
    # -----------------------------------------------------------------
    counter = 0
    counter1 = 0
    for j in range(len(seq_of_seq)):

        sublist = seq_of_seq[j]

        for k in range(len(sublist)):
            counter1 = counter1 + 1

            if sublist[k].radius < min_radius:
                counter = counter + 1
            elif sublist[k].radius > max_radius:
                counter = counter + 1

    return counter / counter1


# ----------------------------------------------------------------------
# Students: Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
# ----------------------------------------------------------------------
def print_failure_message(message='  *** FAILED the above test. ***',
                          flush_time=1.0):
    """ Prints a message onto stderr, hence in RED. """
    time.sleep(flush_time)
    print(message,
          file=sys.stderr, flush=True)
    time.sleep(flush_time)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
