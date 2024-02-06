def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    >>> count_stair_ways(5)
    8
    """
    if n == 0 or n == 1:
        return 1
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)