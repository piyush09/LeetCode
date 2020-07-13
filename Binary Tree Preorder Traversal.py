"""
Algo: Visit the root, Traverse left subtree, Traverse right subtree.
T.C. - O(N) - 'N' is the number of nodes as calculated by Master theorem.
S.C. - O(N) - Explained below
       Auxiliary Space: If size of stack for function calls is not considered, then O(1), otherwise O(N)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursive solution
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root, res) # Calling helper function in it
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val) # Assigning root
            self.helper(root.left, res) # Visiting left subtree
            self.helper(root.right, res) # Visiting right subtree

def main():
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print("Binary Tree preorder traversal is: ")
    print (Solution().preorderTraversal(root))

main()