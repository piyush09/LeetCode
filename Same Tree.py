"""
Algo: Check if p and q nodes are not None, and their values are equal.
      If all checks are OK, do the same for the child nodes recursively.

T.C. - O(N) - 'N' is the number of nodes in the tree, as each node is visited exactly once.
S.C. - O(log N) - in best case of completely balanced tree, 
        and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
"""

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        
        if (p is None or q is None): # If both are None, return True.
            return p==q  # If only one is None, then return False

        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # Return True if both nodes values are same, and left tree, right tree of roots are same, 
        # otherwise return False.

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print("Checking whether trees are same or not: ")
print (Solution().isSameTree(p,q))
