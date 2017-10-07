"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    # convert # of holes into a list range
        # 3 --> [0, 1, 2]

    # loop through each item in range w/ counter
    # if current index matches one from cafes list, stop; hold final count value
    # through other iterations, check if total count > current count
    # at the end, you'll have the highest value count from all iterations
    # return that #


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
