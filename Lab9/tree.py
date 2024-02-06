class Tree:

    #constructor
    def __init__(self, label, branches = []):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    
    #selectors
    def is_leaf(self):
        return not self.branches












# #Constructor
# def tree(label, branches=[]):
#     for branch in branches:
#         assert is_tree(branch)
#     return [label] + list(branches)

# #Selectors
# def label(tree):
#     return tree[0]

# def branches(tree):
#     return tree[1:]

# def is_tree(tree):
#     if type(tree) != list or len(tree) < 1:
#         return False
#     return True

# def is_leaf(tree):
#     return not branches(tree)

# #Test Trees
# t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
# t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
# t3 = tree(8,
#           [tree(4,
#                 [tree(2), tree(3)]),
#            tree(3,
#                 [tree(1), tree(1,
#                                [tree(1), tree(1)])])])
# 
#addition
def print_tree(t, indent=0):
    print('  ' * indent + str(t.label))
    for branch in t.branches:
        print_tree(branch, indent + 1)