"""
Algo: Use 2 pointers - slow and fast approach for this solution.
      Each time, slow goes 1 step while fast goes 2 steps.
      When fast arrives at the end, slow will arrive right in the middle.

T.C. - O(N) - One pass solution for iterating through all the nodes in the Linked List
S.C. - O(1) - Constant space as only 2 pointers are being used in this approach.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self, head):
        
        # Initialising both slow and fast as head of the linked list
        slow = head
        fast = head
        
        while fast and fast.next:
            
            fast = fast.next.next # Moving fast by two steps
            slow = slow.next # Moving slow by 1 step in it
        
        return slow.val # slow is the middle of the linked list in it

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.val)
            temp = temp.next

llist = Solution()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("Linked List is:")
llist.printList()

print ("Middle of the Linked List is:")

print (llist.middleNode(llist.head))