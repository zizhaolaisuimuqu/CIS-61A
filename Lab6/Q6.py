from tree import *

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
        return tree(label(t1) + label(t2))
    elif is_leaf(t1):
        return tree(label(t1), [add_trees(t1, branch) for branch in branches(t2)])
    elif is_leaf(t2):
        return tree(label(t2), [add_trees(branch, t2) for branch in branches(t1)])
    else:
        return tree(label(t1) + label(t2), [add_trees(branch1, branch2) for branch1, branch2 in zip(branches(t1), branches(t2))])
