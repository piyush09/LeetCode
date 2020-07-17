class Solution:
    def isSubsequence(self, s, t):
        
        m = len(s) # Taking length of small string
        n = len(t) # Taking length of very long string
        
        # Initializing values to 0
        i= 0 
        j = 0
        
        while (i <m and j < n): # 
            
            if (s[i] == t[j]): # If the characters are matching, then increment index of smaller string
                i = i+1
            j = j+1 # In any case, we have to increment index of long string
        
        # If the value of i, is same as the length of small string, then there is subsequence and return True, otherwise return False
        return (i==m) 
        
s = "axc"
t = "ahbgdc"

print(Solution().isSubsequence(s,t))