"""
Algo: Make 3 pointers - prev= None, curr = head and next = None
      Iterate through Linked List:

      Before changing next of current, store next node, then change next of current
      Move prev and curr pointers one step forward.

T.C. - O(N), 'N' number of nodes in the linked list
S.C. - O(1)

"""


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

    def reverseList(self):
        prev = None
        curr = self.head

        while (curr is not None):
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.val)
            temp = temp.next

llist = Solution()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Original Linked List is:")
llist.printList()

print ("Reversing Original Linked List")

llist.reverseList()

print ("Reversed Linked List is:")
llist.printList()

