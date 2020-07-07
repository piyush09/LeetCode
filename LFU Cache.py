"""
OrderedDict is dict + doubly linked list.

count2Node - is dict of OrderedDict.

"""

import collections
from collections import defaultdict
from collections import OrderedDict

class Node:

    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:

    def __init__(self, capacity):
        self.cap = capacity  # type capacity: int
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]

        # Clean Memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        # Checking min count
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):

        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
            return

        if len(self.key2node) == self.cap:
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print (cache.get(1))
cache.put(3, 3)    # evicts key 2
print (cache.get(2)) # returns -1 (not found)
print (cache.get(3))       # returns 3.
cache.put(4, 4)    # evicts key 1.
print (cache.get(1))      # returns -1 (not found)
print (cache.get(3))      # returns 3
print (cache.get(4))     # returns 4