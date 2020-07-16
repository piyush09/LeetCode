class Solution:
    def licenseKeyFormatting(self, S, K):
        
        S = S.upper().replace('-','') # Converting 'S' to Upper case and then replacing '-' in it
        size = len(S) # Getting length of the string
        
        # Getting s1 value to get the first group of the string
        if (size % K == 0):
            s1 = K
        else:
            s1 = size % K
        
        # Calculating the resultant string
        result = S[0:s1] # Getting first group of resultant string and putting it into the 'result' answer
        
        while (s1 < size):
            result = result + '-' + S[s1:s1+K] # 'K' characters are added each time in the value of the result
            s1 = s1 + K
        
        return result # Returning the result value

S = "5F3Z-2e-9-w"
K = 4

print(Solution().licenseKeyFormatting(S,K))
        
        
        
        
        