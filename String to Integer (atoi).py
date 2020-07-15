"""
Algo: Remove all whitspaces by using strip() function
    Only one operator is allowed, if there are two operators, it is invalid and thus return 0.
    If the length of 'tmp' is 1, it means the 'tmp' is '0' or '+' or '-', so should return 0 in the function
    
    If the length of 'tmp' is greater than 1, it means the 'tmp' is '0...(numbers)' or '+...(numbers)' or '-...(numbers)', then use integer force conversion to make 'tmp' to an integer

    If the result is out of the range of representable values, MAX_INT or MIN_INT is returned.
"""

class Solution:
    def myAtoi(self, str):
        
        str = str.strip() # Removing whitespaces using strip() function
        
        # Base Case
        if (len(str) == 0):
            return 0
        
        # Assigning MAX_INT and MIN_INT values
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        tmp = "0"
        result = 0
        i = 0
        
        if str[0] in "+-": # As only one operator is allowed
            tmp = str[0]
            i = 1
            
        for i in range(i, len(str)):
            if (str[i].isdigit()):
                tmp += str[i] 
            else:           # If it is not a digit, then it broken
                break
                
        if (len(tmp) > 1): # Even in case of a single digit as we are appending with 0
                              # it would become at least 2 digits
            result = int(tmp)
        
        if result > MAX_INT > 0: # if result > MAX_INT, returning MAX_INT
            return MAX_INT
        
        if result < MIN_INT < 0: # if result < MIN_INT, returning MIN_INT
            return MIN_INT
        
        else:
            return result


str  = "4193 with words"   
print (Solution().myAtoi(str))