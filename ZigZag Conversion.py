class Solution:
    def convert(self, s, numRows):
        
        
        # As per the zigzag pattern, if it is single row, it would read as same string and if number of rows is same as length of string, then also it would be similar, as we are reading row by row
        if (numRows == 1 or numRows >= len(s)):
            return s
        
        # Initializing L in this manner (with numRows as the times it would be initialized) , as we need to read row wise in the final output.
        L = [''] * numRows
        
        index = 0 # Index of the output string, which is similar to characters at a particular row
        step = 1 # 'step' denotes moving up and down while writing in the zigzag format
        
        for char in s: # Iterating through each character in string 's'
            L[index] += char
            
            if index == 0: # As when it is starting row, then we need to move down in step and move ahead in the list to add characters accordingly
                step = 1
                
            elif (index == (numRows-1)): # As we reach the end of the row, then it is required to decrease the step accordingly
                step = -1 
            
            index += step # Moving the index as per the movement of step in it
            
        return ''.join(L) # Joining all the elements of list 'L' and returning as single string
            
s = "PAYPALISHIRING" 
numRows = 4

print(Solution().convert(s, numRows))