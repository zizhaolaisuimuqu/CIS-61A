from tree import *

def cumulative_sum(t):
   """Mutates t so that each node's label becomes the sum of 
      all labels in the corresponding subtree rooted at t.
   >>> #below test case will not work. Don’t test it.
   >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
   >>> cumulative_sum(t)
   >>> t
   Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
   """
   for i in t.branches:
      cumulative_sum(i)
   for b in t.branches:
      t.label += sum([b.label])