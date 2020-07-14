"""
Algo: Traverse the tree iteratively.
      Find the split point.
      The point where both the nodes won't be part of same subtree or one is parent of other.

T.C. - O(N) - where N is the number of nodes in the BST. In the worst case, need to visit all the nodes of the BST.

S.C. - O(1) - Constant Space Complexity
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        # Take p's and q's value in it
        pValue = p.val
        qValue = q.val

        # Start from root node of tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node
            parentValue = node.val

            # If both 'p' and 'q' are greater than parent
            if (pValue > parentValue and qValue > parentValue):
                node = node.right

            # If both 'p' and 'q' are smaller than parent
            elif (pValue < parentValue and qValue < parentValue):
                node = node.left

            else:
                return node  # It is the split node or LCA node.

def main():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    print("Lowest Common Ancestor of BST is: ")
    print(Solution().lowestCommonAncestor(root, root.left, root.right))

main()