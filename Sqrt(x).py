"""
Non Interview Solution

Algo: Floor the number by powering it to 0.5, return the corresponding value.
"""

import math
class Solution:
    def mySqrt(self, x):
        
        return (math.floor((x)**(0.5)))

x = 8
print(Solution().mySqrt(x))
