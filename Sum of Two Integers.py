"""
Algo: If x and y don't have set bits at same position, then x^y gives sum of x and y.
      To take into account common set bits, bitwise AND (&) is used.
      Bitwise AND of x and y gives all carry bits.

"""
class Solution:
    def getSum(self, a, b):
        
        MAX = 0x7FFFFFFF # hexadecimal way of representing 32 bits integer max
        MIN = 0x80000000 # hexadecimal way of representing 32 bits integer min
        
        mask = 0xFFFFFFFF # to get last 32 bits
        
        while b:
            
            carry = a & b
            a = (a ^ b) & mask
            b = ((carry)<< 1) & mask
        
        if a <= MAX:
            return a
        
        else:
            return (a ^ (~mask)) # '~' will flip the bits 

a = -2
b = 3
print(Solution().getSum(a,b))