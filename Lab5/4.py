def squares(s):
    """Returns a new list containing square roots of the elements of the original list
    that are perfect squares.
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    result = []
    for num in s:
        if int(num ** 0.5) ** 2 == num:
            result += [int(num**0.5)]
    return result