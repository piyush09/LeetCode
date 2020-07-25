"""
Algo: Calculate Odd numbers between 1 and (low-1).
      Calculate Odd numbers between 1 and (high).
      Return their difference.

T.C. - O(1)
S.C. - O(1)
"""

class Solution:
    def countOdds(self, low, high):
        
        odd1 = low // 2 # Odd numbers between 1 and (low-1)
        odd2 = (high+1) // 2 # Odd numbers between 1 and (high)
        
        return (odd2 - odd1)

low = 8
high = 10

print(Solution().countOdds(low, high))