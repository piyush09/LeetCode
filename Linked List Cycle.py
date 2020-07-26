"""
Algo: Traverse the linked list one by one and put node addresses in a set.
      At any point, if NULL is reached then return false. 
      If next of current node points to any of the previously stored nodes in set, 
      then there exists a cycle.
      
T.C. - O(N), 'N' number of nodes in the linked list, as complete linked list is traversed.
S.C. - O(N) - Space required to store the elements in the set.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList: 
   
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


    def hasCycle(self):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        node_set= set() # Initialising node_set
        temp_node = self.head # Assigning temp_node to head node
        
        while(temp_node): # Iterating over all nodes in Linked List
            
            if temp_node in node_set : # Checking if the current node is in node_set then there exists a cycle
                return True
            
            node_set.add(temp_node) # If node not in node_set, adding it to the node_set
            temp_node = temp_node.next # Iterating to the next node
            
        return False # Iterated over all nodes and no node is repeated, hence there is no cycle

llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(10) 

llist.head.next.next.next.next = llist.head
        
if( llist.hasCycle()): 
    print ("Loop found") 
else : 
    print ("No Loop ") 