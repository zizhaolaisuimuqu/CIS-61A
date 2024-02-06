from tree import *

def double_tree(t): 
    """Return a tree with the square of every element in t 
    >>> numbers = tree (1,
    ...                 [tree(2,
    ...                       [tree(3),
    ...                        tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(double_tree(numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    """
    return tree(2 * label(t), [double_tree(branch) for branch in branches(t)])
