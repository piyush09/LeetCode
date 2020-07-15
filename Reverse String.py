class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(0,len(s)//2): # Iterating till  half the length of the string
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i] # Swapping 'i'th character from beginning and end for the string

s = ["H","a","n","n","a","h"]
Solution().reverseString(s) # In Place String Reversal
print(s)