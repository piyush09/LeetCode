"""
Algo: Call invert of left subtree, call invert of right subtree.
      Swap left and right subtrees.

Time and Space complexities similar to Tree traversal time and space complexities.
T.C. - O(N) - 'N' is the number of nodes as calculated by Master theorem.
S.C. - O(N) - Explained below - When tree is completely skewed
       Auxiliary Space: If size of stack for function calls is not considered, then O(1), otherwise O(N)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def InorderTraversal(node):
    if node is None:
        return

    # first recur on left child
    InorderTraversal(node.left)

    # then print the data of node
    print (node.val),

    # now recur on right child
    InorderTraversal(node.right)


class Solution:
    def invertTree(self, root):
        # Inverting left and right subtrees and swapping them.
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Inorder Traversal of input binary tree: ")
    InorderTraversal(root)

    print ("\n Inverting binary tree:")
    Solution().invertTree(root)

    print("Inorder Traversal of Inverted binary tree: ")
    InorderTraversal(root)

main()