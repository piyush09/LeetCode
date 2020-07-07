"""
Algo: Using Arrays, direct access table
      Using Linked List for chaining

"""

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        index = key % (self.m)
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            current = self.h[index]

            while True:

                if (current.pair[0] == key):
                    current.pair = (key, value)
                    return

                if current.next == None:
                    break
                current = current.next

            current.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        index = key % self.m
        current = self.h[index]
        while current:
            if (current.pair[0] == key):
                return current.pair[1]
            else:
                current = current.next
        return (-1)

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        index = key % self.m
        current = prev = self.h[index]

        if not current:
            return

        if (current.pair[0] == key):
            self.h[index] = current.next

        else:
            current = current.next

            while current:
                if (current.pair[0] == key):
                    prev.next = current.next
                    break

                else:
                    current, prev = current.next, prev.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

hashMap = MyHashMap();
hashMap.put(1, 1)
hashMap.put(2, 2)
print (hashMap.get(1))            # returns 1
print (hashMap.get(3))            # returns -1 (not found)
print (hashMap.put(2, 1))         # update the existing value
print (hashMap.get(2))            # returns 1
print (hashMap.remove(2))         # remove the mapping for 2
print (hashMap.get(2))            # returns -1 (not found)