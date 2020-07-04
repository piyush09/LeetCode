"""
Algo: Two pointers: moving end forward to find a valid window, moving start forward to find a smaller window
     counter (count of characters in t) and hash_map (tCharDict) to determine if the window is valid or not

    General way for substring problems is to use a hashmap alogn with two pointers.

T.C. - O(|S|+|T|), where |S| and |T| are lengths of the strings S and T.
S.C. - O(|S|+|T|). It's |S| when the window size is equal to the entire string S.
        It's |T| when T has all unique characters.
"""

from collections import Counter
class Solution:

    def minWindow(self, s,t):

        tCharDict = Counter(t) # Counting frequency of characters in t

        # Two pointers
        start = 0 # Moving start forward to find a smaller window
        end = 0 # Moving end forward to find a valid window

        # If minimum window length doesn't change, then there is no valid window
        minWindowLength = len(s)+1

        minWindowStart = 0 # Start point of minimum window

        countChars = len(t) # As a counter for how many characters still need to be there in window

        while (end < len(s)):

            # If the current character is desired
            if s[end] in tCharDict:

                if (tCharDict[s[end]] > 0):
                    countChars -= 1 # Decrease the counter of characters in t string

                tCharDict[s[end]] -= 1 # Decrease the value in the hashmap

            while (countChars == 0): # If current window has all desired characters

                if ((end-start+1) < minWindowLength): # Checking if this window is smaller
                    minWindowLength = end-start+1
                    minWindowStart = start

                if s[start] in tCharDict: # if s[start] is required,
                    tCharDict[s[start]] += 1

                    if (tCharDict[s[start]] > 0): # Updating the counter only if current character is critical
                        countChars += 1

                start += 1 # Moving start forward to find smaller window

            end += 1 # Moving end forward to find another valid window

        # If minimum window length is not changing, then no valid window
        if (minWindowLength == len(s)+1):
            return ""
        else:
            return s[minWindowStart: minWindowStart + minWindowLength]

S = "ADOBECODEBANC"
T = "ABC"

test = Solution()
print (test.minWindow(S,T))