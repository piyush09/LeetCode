"""
Algo: Use Stack approach for this solution.
      Keep a stack as a characters stack. Iterate characters of S (String) one by one.

      If the next character is same as the last character in stack, pop the last character from stack.
      If the next character is different, append it to the end of stack.

T.C. - O(N) - One Pass Solution
S.C. - O(N) - Storing the output in it
"""

class Solution:
    def removeDuplicates(self, S):
        
        stack = []
        for char in S: # Iterating through every character in the string
            if stack and stack[-1] == char: # If previous char is same, then pop the element from the stack
                stack.pop()
            else:
                stack.append(char) # Otherwise, add the char at the end of the stack
        
        return ''.join(stack) # Join all the elements of the stack and return them
                    
str = "abbaca"   
print (Solution().removeDuplicates(str))         
        