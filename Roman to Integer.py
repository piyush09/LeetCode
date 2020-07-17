class Solution:
    def romanToInt(self, s):
        
        decimal_value = 0
        roman_conversion = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        
        for i in range(0, len(s)-1):
            
            if (roman_conversion[s[i]] < roman_conversion[s[i+1]]):
                decimal_value = decimal_value - roman_conversion[s[i]]
                
            else:
                decimal_value = decimal_value + roman_conversion[s[i]]
                
        decimal_value = decimal_value + roman_conversion[s[-1]]
        
        return decimal_value
        
s = "MCMXCIV"
print(Solution().romanToInt(s))