"""
Other Common Used Approach is to do inorder traversal in recursive way (which will provide array in sorted ascending order), and get the (k-1)th element of this array.


Algo: Don't do entire inorder traversal, stop after reaching kth element in it.

T.C. - O(H+k), where 'H' is height of tree, which is O(log N+k) for balanced tree, and
                O(N+k) for completely unbalanced tree, with all nodes in left subtree.

        Complexity is because of stack which contains atleast H+k elements,                   as before popping out, one has to go to the leaf.

S.C. - O(H+k), same as T.C. - O(N+k) in worst case, and O(log N+k) in average case.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):

        stack = []

        # Endless loop, will terminate, when finding the required answer
        while True:

            # Going to the leftmost leaf of the tree
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()  # Popping element from the stack
            k -= 1  # Decrementing k every time

            # When k becomes 0, it will return root's value in it,
            # which would be kth smallest value
            if (k == 0):
                return root.val

            # At this point, it goes into the right child of the root
            root = root.right

def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    print("Kth smallest element in BST is: ")
    print(Solution().kthSmallest(root, 3))

main()