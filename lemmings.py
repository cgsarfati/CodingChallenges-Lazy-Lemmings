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

# BRUTE FORCE
def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    worst = 0

    for hole in range(num_holes):
        # lookng at all cafes, find distance to hole. pick min distance.
        dist = min([abs(hole - cafe) for cafe in cafes])

        # compare to longest distance. if dist > worst, replace.
        worst = max(worst, dist)

    return worst

# BINARY SEARCH
def furthest_optimized(num_holes, cafes):

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
