"""
Algo: Visit the root, Traverse all children of the root accordingly.
T.C. - O(N) - 'N' is the number of nodes as calculated by Master theorem, each node is visited once in it.
S.C. - O(N) - Explained below
       Auxiliary Space: If size of stack for function calls is not considered, then O(1), otherwise O(N)
"""

# Definition for a N-ary tree node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

# Recursive solution
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root, res) # Calling helper function in it
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val) # Assigning root
            for child in root.children: # Visiting all the children of the root
                self.helper(child, res)

def main():
    root = TreeNode(1)

    root.children.append(TreeNode(3))
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(4))

    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    print("N-ary Tree preorder traversal is: ")
    print (Solution().preorderTraversal(root))

main()