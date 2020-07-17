"""
Non Interview Solution
Algo: Floor the number by powering it to 0.5, then check if the obtained value's
      square is equal to the original number, if so, it is perfect square.
"""

import math
class Solution:
    def isPerfectSquare(self, num):
        
        if (((math.floor((num) ** (0.5))) ** 2) == num):
            return True
        else:
            return False

num = 14
print(Solution().isPerfectSquare(num))
        