"""
Algo: For a sorted array, the left half will be in the left subtree, middle value as the root, right half in the right subtree. 
      This holds true for every node.
        
      It is creating a balanced BST, as we are picking up the middle element every time.
      Pass the left and right bounds in the recursive calls.
      
      Calculate middle value, assign it as root and then recursively call for left and right halves with corresponding values of the indexes.
      
T.C. - O(n)- where n is the number of elements in nums list, where TC calculation by using Master theorem, where it divides into n/2 elements everytime.
"""
class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def sortedArrayToBST(self, nums):
        
        def convertToBST(l,r):
            
            # Recursion breaking condition
            if l > r:
                return None
            
            # Calculating middle value
            mid = (l+r)//2
            
            root = TreeNode(nums[mid]) # Root assigned
            root.left = convertToBST(l, mid-1) # root's left is left half of middle value
            root.right = convertToBST(mid+1, r) # root's right is right half of middle value
            
            return root
        
        # Pass the indices from 0 to (len(nums)-1).
        return convertToBST(0, len(nums)-1)

    def preorderTraversal(self, root):
        res = []
        self.helper(root, res) # Calling helper function in it
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val) # Assigning root
            self.helper(root.left, res) # Visiting left subtree
            self.helper(root.right, res) # Visiting right subtree

nums = [-10,-3,0,5,9]

print("Preorder traversal of the sorted array is: ")
print (Solution().preorderTraversal(Solution().sortedArrayToBST(nums)))