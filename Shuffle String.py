"""
Algo: Initialize null output string equal to the length of input string.
      Enumerate through indices - assign the index at the output string 
      as the value at iterating through string 's'.

T.C. - O(N)
S.C. - O(N)
"""
class Solution:
    def restoreString(self, s, indices):
        
        outputString = ['']*len(s) # Initialising empty string string of length of (s) in it
        
        for val, index in enumerate(indices):
            
            outputString[index] = s[val] # Assign the index at output string as the value of string 's'
            
        return "".join(outputString) # Return the output string

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print (Solution().restoreString(s, indices))