"""
Algo: Do level order traversal, by doing breadth first search for the tree nodes.
For every other level, traverse from right to left way.
Maintain a variable leftToRight, mark it true while traversing left to right and when from right to left mark it false

While traversing from right to left, append the node values at the beginning of the queue.

T.C - O(N), 'N' Number of nodes, as each node is traversed once.
S.C. - O(N), 'N' Number of nodes, as there is possibility of maximum N/2 nodes at lowest level, hence O(N) space required to store it
"""

from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)
        leftToRight = True # Initializing leftToRight as True

        while queue:
            levelSize = len(queue) # At Each level, 'queue' contains all the elements at that level

            # At each level, making current level as empty list, in order to add all node values at that
            # level to current level list, with leftToRight is true in normal way, and if false, then appending it to the left of it
            currentLevel = deque()

            for i in range(levelSize): # At this iterating through each node in the current level
                currentNode = queue.popleft() # Removing the leftmost node from the queue and assigning it to current Node

                if leftToRight:
                    # Adding the node to the current level
                    currentLevel.append(currentNode.val) # Adding current iterating node into the current level
                else:
                    # Adding the node values at the beginning of currentLevel list everytime as in this order required is from right to left
                    currentLevel.appendleft(currentNode.val)

                # Inserting children of current node in the queue
                if (currentNode.left):
                    queue.append(currentNode.left) # If there is left child, then appending it into the queue

                if (currentNode.right):
                    queue.append(currentNode.right) # If there is right child, then appending it into the queue

            leftToRight = not leftToRight # Changing leftToRight to alternate value in every level

            result.append(currentLevel)

        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Zigzag Level Order Traversal is: ")
print(Solution().zigzagLevelOrder(root))