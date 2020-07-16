"""
Algo: Similar to reversing a string.
      "pop" the last digit off of x and "push" it to the back of the rev.
      rev will be the reverse of x.
      
      pop operation:
      
      pop = x % 10
      x = x/10
      
      push operation:
      
      temp = rev * 10 + pop
      rev = temp

T.C. - O(log x) - There are roughly log x to base 10 digits in x.
S.C. - O(1)

"""

class Solution:
    def reverse(self, x):
        
        result = 0
        
        # Getting appropriate symbol
        if(x<0):
            symbol = -1
            x = -x
            
        else:
            symbol = 1
            
        # Reversing the number
        
        while x:
            result = (result * 10) + (x % 10)
            x = x//10
            
        # Returning appropriate result as per the constraint in the question
        if result > pow(2, 31):
            return 0
        else:
            return (result * symbol)

x = -123
print(Solution().reverse(x))
        