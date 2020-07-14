class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0

        else:
            lDepth = self.maxDepth(root.left)
            rDepth = self.maxDepth(root.right)

            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Maximum Depth of Binary Tree is: ")
    print(Solution().maxDepth(root))

main()
