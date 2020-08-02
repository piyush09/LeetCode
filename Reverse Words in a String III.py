"""
Algo:  Split up the string based on whitespaces. Put the individual words in a list of strings.
       Reverse each individual string and concatenate the result.

T.C. - O(N) - where 'n' is the length of the string.
              Iterating through each individual word and reversing it.
S.C. - O(N) - Result of size n is used.
"""

class Solution:
    def reverseWords(self, s):
        
        words = s.split(" ") # Split string by whitespace
        newWords = [] 
        for word in words: # Iterate through each word and reverse each of the individual word
            newWords.append(word[::-1]) # Reversing each of the individual words in it and appending in new list.
            
        return " ".join(newWords)
        
str = "Let's take LeetCode contest"

print (Solution().reverseWords(str))