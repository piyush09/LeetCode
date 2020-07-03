"""
Algo: First element in preorder list is a root.
    This root splits inorder list into left and right subtrees.
    Now one have to pop up the root from preorder list since it's already used as a tree node
    and then repeat the step above for the left and right subtrees.

T.C. - O(N) - Calculation of time complexity by Master theorem, as it is divided into 2 subproblems in constant time.
             Check LC Premium article for detailed solution

S.C. - O(N) - since the entire tree is stored.
"""

class TreeNode:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if inorder:
        # preorder.pop(0) gives root node of the tree, and then get the index of that node in inorder traversal sequence
        ind = inorder.index(preorder.pop(0))
        rootValue = inorder[ind]
        root = TreeNode(inorder[ind]) # root of the node, is the node calculated at this index of inOrder traversal
        root.left = buildTree(preorder, inorder[0:ind]) # buildTree's left half by passing the same preorder and inOrder[0, index-1]
        root.right = buildTree(preorder, inorder[ind+1:]) # buildTree's right half by passing same preorder and inOrder[index+1, end]
        return root

def InorderTraversal(node):
    if node is None:
        return

    # first recur on left child
    InorderTraversal(node.left)

    # then print the data of node
    print (node.val),

    # now recur on right child
    InorderTraversal(node.right)

# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

root = buildTree(preOrder, inOrder)

print ("Root of the Tree is:", root.val)
print ("In Order Traversal of the tree is:",InorderTraversal(root))
