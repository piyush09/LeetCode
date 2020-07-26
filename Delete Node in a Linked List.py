"""
https://leetcode.com/problems/delete-node-in-a-linked-list/solution/
Check this for the reference.

Algo: Replace the value of the node to be deleted with the value in the node after it, and similarly also change the next pointers.

T.C. - O(1)
S.C. - O(1)

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # Function to initialize head 
    def __init__(self): 
        self.head = None
   
    # Function to insert a new 
    # node at the beginning 
    def push(self, new_data): 
        new_node = ListNode(new_data) 
        new_node.next = self.head 
        self.head = new_node 
   
    # Utility function to print it 
    # the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.val) 
            temp = temp.next

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # Assigning node's next's value to current node's value
        node.val = node.next.val
        
        # Assigning node's next's next to current node's next
        node.next = node.next.next
        
        
llist = Solution()
llist.push(9)
llist.push(1)
llist.push(5)
llist.push(4)

print("Original Linked List is:")
llist.printList()
print ("Deleting Node at a particular value in the Linked List")

print("Linked List after deleting that node")
llist.printList()