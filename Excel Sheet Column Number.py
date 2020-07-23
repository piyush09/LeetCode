"""
Algo: Iterate from left to right.
      Check as base 26 number system, and convert alphabets to numbers accordingly.
      Convert a character to its ASCII value and subtract ASCII value of character 'A' from that value.

T.C. - O(N) - N is the number of characters in the input string.
S.C. - O(1) - Constant Space is being used.
"""

class Solution:
    def titleToNumber(self, s):
        
        result = 0
        for i in range(len(s)):
            result = result * 26 + (ord(s[i]) - ord("A") + 1)
        return result

s = "ZY"
print(Solution().titleToNumber(s))
        