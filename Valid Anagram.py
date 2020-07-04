"""
Algo: Assumption: Characters are stored using 8 bits and there can be 256 possible    characters.

     Create count arrays of size 256 for both strings and Initialize all values in count arrays as 0.
     Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
     Compare count arrays. If both count arrays are same, then return true.

T.C. - O(N)
"""

class Solution:
    def isAnagram(self,s, t):

        NO_OF_CHARS = 256

        # Initializing both the count arrays as 0
        count1 = [0] * NO_OF_CHARS
        count2 = [0] * NO_OF_CHARS

        # For each character, incrementing count in corresponding count array
        for i in s:
            count1[ord(i)] += 1

        for i in t:
            count2[ord(i)] += 1

        # Returning False, if initially only lengths of the two strings are not equal
        if (len(s) != len(t)):
            return False

        # Companring both the count arrays
        for i in range(NO_OF_CHARS):
            if (count1[i] != count2[i]):
                return False

        # Returning True if there is no instance of False case
        return True

s = "anagram"
t = "nagaram"
test = Solution()
print (test.isAnagram(s,t))