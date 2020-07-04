"""
Algo: Take two pointers - left and right.
      Compare each character from left and right. If they are equal, compare until left and right of string are equal or right becomes less then left

T.C. - O(N), as need to traverse at minimum till N/2 characters in the input string.
S.C. - O(1), Constant space is used.
"""

class Solution:
    def isPalindrome(self, s):

        l = 0  # Initialising left pointer to 0
        r = len(s) - 1  # Initialising right pointer to (len(string)-1)

        # Iterating till left pointer is less than right pointer
        while (l < r):

            if not s[l].isalnum():  # If character is not alpha numeric, then increment the left pointer
                l += 1

            elif not s[r].isalnum():  # If character is not alpha numeric, then decrement the right pointer
                r -= 1

            else:

                # If characters are not matching, then return False
                if (s[l].lower() != s[r].lower()):
                    return False

                # Characters are matching, then increment and decrement pointers respectively
                else:
                    l += 1
                    r -= 1

        # If reached the condition that l is not less than r, then return True
        return True

str = "A man, a plan, a canal: Panama"
test = Solution()
print (test.isPalindrome(str))
