"""
Algo: Pass down two parameters: lower_limit (which means that all nodes in the the current subtree must be smaller than this value) and upper_limit (all must be larger than it)

     Compare root of the current subtree with these two values.
     Then, recursively check the left and right subtree of the current one.

T.C.- O(N) - since each node is visited exactly once
T.C.- O(N) - since entire tree is kept.
"""
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):

        # Defining BSTHelper function - to check if nodes follow BST property
        def isBSTHelper(node, lower_limit, upper_limit):

            if not node:
                return True

            if ((node.val <= lower_limit) or (node.val >= upper_limit)):
                return False

            return isBSTHelper(node.left, lower_limit, node.val) and isBSTHelper(node.right, node.val, upper_limit)

        # Passing the root and lower_limit as (-infinity) and upper_limit as (+infinity)
        return isBSTHelper(root, lower_limit=float('-inf'), upper_limit=float('inf'))

def main():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print("Checking if BST is valid: ")
    print(Solution().isValidBST(root))

main()