
"""
Algo: Using Dictionary Approach
"""
class Node:
    '''Structure of linked list node'''

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def clone(head):
    dic, prev, node = {}, None, head
    while node:
        if node not in dic:
            # Use a dictionary to map the original node to its copy
            dic[node] = Node(node.val)
        if prev:
            # Make the previous node point to the copy instead of the original.
            prev.next = dic[node]
        else:
            # If there is no prev, then we are at the head. Store it to return later.
            head = dic[node]
        if node.random:
            if node.random not in dic:
                # If node.random points to a node that we have not yet encountered, store it in the dictionary.
                dic[node.random] = Node(node.random.val)
            # Make the copy's random property point to the copy instead of the original.
            dic[node].random = dic[node.random]

        # Store prev and advance to the next node.
        prev, node = dic[node], node.next
    return head

def print_dlist(root):
    '''Function to print the doubly linked list'''

    curr = root
    while curr != None:
        print('Data =', curr.val, ', Random =', curr.random.val)
        curr = curr.next


####### Driver code #######
'''Create a doubly linked list'''
original_list = Node(1)
original_list.next = Node(2)
original_list.next.next = Node(3)
original_list.next.next.next = Node(4)
original_list.next.next.next.next = Node(5)

'''Set the random pointers'''

# 1's random points to 3
original_list.random = original_list.next.next

# 2's random points to 1
original_list.next.random = original_list

# 3's random points to 5
original_list.next.next.random = original_list.next.next.next.next

# 4's random points to 5
original_list.next.next.next.random = original_list.next.next.next.next

# 5's random points to 2
original_list.next.next.next.next.random = original_list.next

'''Print the original linked list'''
print('Original list:')
print_dlist(original_list)

'''Create a duplicate linked list'''
cloned_list = clone(original_list)

'''Print the duplicate linked list'''
print('\nCloned list:')
print_dlist(cloned_list)