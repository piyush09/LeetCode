"""
Algo: Make a set for the numbers already calculated in order to reach the loop.
      If a number is formed, that is already existing in the set, then return False (as it forms loop)
      Else, if n becomes 1, then return True.

T.C. - O(log N) - as calculated by O(243.3+ log N + log log N +).. = O(log N)
                For the next value of a number, it takes O(log N), as each digit of the number is being processed.
S.C. - O(log N) - numbers that are put in the set for a large enough N value.
                 For a large enough N, most space will be taken by N itself. 
"""

class Solution:
    def isHappy(self, n):
        
        possibleNumbers = set() # Set to check numbers that can exist in loop
        while (n is not 1):
            
            if n in possibleNumbers:
                return False
            else:
                possibleNumbers.add(n)

            temp = 0
            for digit in str(n):
                temp += (int(digit) ** 2)

            n = temp
            
        if (n == 1): # If number becomes 1, then return True
            return True


n = 19

print(Solution().isHappy(n))