"""
Algo: Idea is that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from
      it's center, and there are only '2n-1' such centers.
      Center of a palindrome can be in between two letters.
      Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's

      Call the palindrome function for odd substring and for even substring
T.C. - O(N^2) - Expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
S.C. - O(1) - Constant space is used.
"""


def longestPalindrome(s):

    # Initialising resulting palindromic substring to empty
    res = ""

    # For pointer ranging from 0 to end of string, it is checked whether that is the center of the palindrome
    for i in range(len(s)):
        odd = palindromeAt(s, i, i) # Checking for odd palindrome with center at pointer 'i'
        even = palindromeAt(s, i, i + 1) # Checking for even palindrome with centers at pointers 'i' and 'i+1'

        # Calculating the maximum value out of res, odd, even by taking the key as length, the one with maximum length out of them
        res = max(res, odd, even, key=len)
    return res

# starting at l,r expand outwards to find the biggest palindrome
def palindromeAt(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[(l + 1):r] # Note s[1:1] is empty, as in if same integer in start and end, then return is empty
                     # In general, It will return s[l] to s[r-1], both inclusive, if s[l:r] is used.

print (longestPalindrome("ababac"))
# print (longestPalindrome("abcba"))