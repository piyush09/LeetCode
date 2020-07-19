"""
Algo: Start from carry = 0. If number a has 1-bit in this lowest bit, add 1 to the carry. 
      Same for number b: if number b has 1-bit in lowest bit, add 1 to the carry.

      Append the lowest bit of the carry to the answer, and move the highest bit of the carry to the next order bit.
      Repeat the same steps again, till all bits in a and b are used up. 
      If there is still nonzero carry to add, add it
      Reverse the answer string

T.C. - O(max(N,M)) - where N and M are lengths of the input strings a and b.
S.C. - O(max(N,M)) - for storing the answer.
"""

class Solution:
    def addBinary(self, a, b):
        
        carry = 0
        result = ''
        
        a = list(a) # Making list of all integers in string 'a'
        b = list(b) # Making list of all integers in string 'b'
        
        while a or b or carry:
            
            if a:
                carry += int(a.pop()) # Popping out last element from a list, and making it as integer

            if b:
                carry += int (b.pop())
                
            result += str(carry%2) # If carry is 0 or 2, then it becomes 0, otherwise 1
            carry = carry // 2 # Quotient is carried forward in it
            
        return result[::-1] # Reversing the result, as we are storing it from ones digit in it at 0th place of string
        
a = "11"
b = "1"

print(Solution().addBinary(a,b))