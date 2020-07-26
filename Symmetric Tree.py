"""
Algo: Tree is symmetric - If their two roots have the same value.
      The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

T.C. - O(N) - 'N' is the total number of nodes in the tree - As the entire tree is traversed once.
S.C. - O(N) - In the worst case, the tree is linear and the height is O(N).
              Space complexity due to recursive calls on the stack is O(N) in the worst case.
"""
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    
    def isMirror(self, root1, root2):

        if root1 is None and root2 is None:
            return True

        # Checking recursively for left and right subtrees
        if (root1 is not None and root2 is not None):
            if (root1.val == root2.val):
                return (self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left))

        return False
        
    
    def isSymmetric(self, root):
        return self.isMirror(root, root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print("Checking whether tree is symmetric returning True or False: ")
print(Solution().isSymmetric(root))