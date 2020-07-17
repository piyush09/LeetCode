class Solution:
    def numJewelsInStones(self, J, S):
        
        Jset = set(J) # Forming a jewel set for jewels
        
        result = 0 # Initialize the answer value as 0
        for s in S: # Iterating over each element in S
            if s in Jset:
                result += 1 # If s is occuring in hashset Jset (Jewels Set), then incrementing the result
                
        return result

J = "z"
S = "ZZ"

print(Solution().numJewelsInStones(J,S))
        