"""
Algo: Traverse all children of the root accordingly, Visit the root.
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
    def postorderTraversal(self, root):
        res = []
        self.helper(root, res) # Calling helper function in it
        return res

    def helper(self, root, res):
        if root:
            for child in root.children: # Visiting all the children of the root
                self.helper(child, res)
            res.append(root.val) # Assigning root


def main():
    root = TreeNode(1)

    root.children.append(TreeNode(3))
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(4))

    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    print("N-ary Tree postorder traversal is: ")
    print (Solution().postorderTraversal(root))

main()