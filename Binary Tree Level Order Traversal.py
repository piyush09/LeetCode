"""
Algo: Do level order traversal, by doing breadth first search for the tree nodes at each level.

T.C. - O(N) - 'N' is the number of nodes in the tree
            This is due because we traverse each node once.

S.C. - O(N) - 'N' is the number of nodes in the tree - need to return a list containing the level order traversal
        A maximum of N/2 nodes at any level (only at the lowest level),
        therefore, O(N) space is required to store them in the queue
"""

from collections import deque
import operator

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrderTraversal(root):

    result = []

    if root is None:
        return result

    # https: // www.geeksforgeeks.org / deque - in -python /
    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue) # At Each level, 'queue' contains all the elements at that level
        # print("Level Size is:") + str(levelSize)
        currentLevel = [] # At each level, making current level as empty list, in order to add all node values at that
        # level to current level list

        for i in range(levelSize): # At this iterating through each node in the current level
            currentNode = queue.popleft() # Removing the leftmost node from the queue and assigning it to current Node
            # print ("Current Node is:") + str(currentNode.val)

            # Adding the node to the current level
            currentLevel.append(currentNode.val) # Adding current iterating node into the current level

            # Inserting children of current node in the queue
            if (currentNode.left):
                queue.append(currentNode.left) # If there is left child, then appending it into the queue

            if (currentNode.right):
                queue.append(currentNode.right) # If there is right child, then appending it into the queue

        result.append(currentLevel)

    return result



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(9)

    print("Level Order Traversal is: ")
    print(str(levelOrderTraversal(root)))
    levelOrderTraversalResult = levelOrderTraversal(root)

main()