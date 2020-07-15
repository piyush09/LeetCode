import collections
from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        
        count = Counter(s) # building hashmap for character and how often that character occurs
        index = 0
        
        # Finding the index
        for ch in s: # Iterating over each character in string s
            if count[ch] == 1:
                return index
            else:
                index += 1
                
        return -1 # If no character found with count as 1, then return -1

s = "loveleetcode"
print(Solution().firstUniqChar(s))
            
        