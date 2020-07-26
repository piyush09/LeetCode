""" 
Algo: Using the formula to calculate digital root in a decimal numeral system.

T.C. - O(1)
S.C. - O(1)
"""
class Solution:
    def addDigits(self, num):
        
        if (num == 0):
            return 0

        if (num % 9 == 0):
            return 9

        return (num % 9)

num = 38
print(Solution().addDigits(num))