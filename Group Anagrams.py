import collections
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        ans = collections.defaultdict(list)

        for s in strs:  # Iterating through each string in strs list
            count = [0] * 26  # Initializing count as list of zeros of size 26

            for c in s:
                # ord() function getting unicode value and then subtracting value of
                count[ord(c) - ord('a')] += 1

            # Converting count list to tuple, and for that key appending corresponding string 's' to it

            # print (tuple(count)) # tuple of (count) is the count list containing number of each character in a string
            ans[tuple(count)].append(s)

        # print (ans.keys()) # keys of "ans" is the count list containing number of each character in a string

        return ans.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()

print (test.groupAnagrams(strs))
