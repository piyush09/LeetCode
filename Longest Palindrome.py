"""
Algo: A palindrome consists of letters with equal partners, plus possibly a unique center (without a partner)
      For each letter check it's occurence in the string, by making a dictionary.
      ((v // 2) * 2) value would take both odd and even values into consideration.
       If length of maxPalindrome is equal to length of string, return it,
       otherwise, add 1 (center character) to it, and return the value.

T.C. - O(N) - N is the length of string 's', need to count each letter.
S.C. - space for storing characters in the dictionary.
"""

import collections
from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        
        # Making a dictionary of all characters in string 's'
        letterCount = Counter(s) 
        maxPalindromeLength = 0
        
        for value in letterCount.values():

            # Adding the ((value // 2)*2) which handles the case of odd values as well
            maxPalindromeLength += ((value // 2) * 2)

        # If Maximum palindrome length is equal to length of string, then just return it          
        if (maxPalindromeLength == len(s)):
            return maxPalindromeLength 
        else:
            # Case when there is odd occurence of a character which can be a middle character
            return (maxPalindromeLength + 1) 
        
str = "abccccdd"

print (Solution().longestPalindrome(str))
        