"""
Algo: Check String Concatenation Approach
T.C. - O(N)
S.C. - O(1)
"""

class Solution:
    def fizzBuzz(self, n):
        
        # String Concatenation Approach
        answer = [] # Initialising empty answer list
        
        for i in range(1,n+1):
            
            temp = "" # Initializng null temporary string
            
            if i%3 == 0:
                temp += "Fizz" # Appending "Fizz" in temp string, if divisible by 3
                
            if i%5 == 0:
                temp += "Buzz" # Appending "Buzz" in temp string, if divisible by 5
            # "FizzBuzz" will be automatically appended in temp string, when string is divisible both by 3 and 5
            
            # if string is not divisible by 3 and 5, then appending the corresponding number as string
            if not (i%3 == 0 or i%5 == 0):
                temp = str(i)
            
            answer.append(temp)
            
        return answer

n = 15

print(Solution().fizzBuzz(n))