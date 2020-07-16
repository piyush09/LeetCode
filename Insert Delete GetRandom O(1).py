"""

Algo: Keep track of the index of the added elements, so while removing them, copy the last one into it.
      list.append() takes O(1), both average and amortized.
      Dictionary get and set functions take O(1) average

T.C. - O(1) time
"""
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.nums = [] # nums list for the numbers
        self.pos = {} # In the pos initialized empty dictionary, then in it, value is added as key and index of element in the array as value in the pos dictionary

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        if val not in self.pos:
            self.nums.append(val) # Length of nums is updated as the value is appended in it
            self.pos[val] = len(self.nums) - 1 
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        
        if val in self.pos:
            idx = self.pos[val] # index of value 'val' in the nums list
            last = self.nums[-1] # Accessing the last added number
            self.nums[idx] = last # Overwriting val index with last addition
            self.pos[last] = idx # Updating last addition's index to it's new spot
            self.nums.pop() # Removing last edition from it's original location... as it has a new location

            del self.pos[val] # Deleting element with value 'val' from the dictionary
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        """
        
        return self.nums[random.randint(0, len(self.nums)-1)]
        
randomSet = RandomizedSet()
print (randomSet.insert(1))
print (randomSet.remove(2))
print (randomSet.insert(2))
print (randomSet.getRandom())
print (randomSet.remove(1))
print (randomSet.insert(2))
print (randomSet.getRandom())


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
