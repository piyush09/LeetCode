"""
Similar to Problem "Longest Palindromic Substring"
Also refer to the submitted solution on LeetCode platform

Algo: Idea is that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from
      it's center, and there are only '2n-1' such centers.
      Center of a palindrome can be in between two letters.
      Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's

      Call the palindrome function for odd substring and for even substring
T.C. - O(N^2) - Expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).
S.C. - O(1) - Constant space is used.
"""

result = []

def countSubstrings(s):


    for i in range(len(s)):

        palindromeAt(s, i, i)
        palindromeAt(s, i, i + 1)


    print (result)
    return (len(result))


def palindromeAt(s, l, r):
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        l -= 1
        r += 1

        if ((s[(l+1):r]) != ""):
            result.append(s[(l+1):r])

    # return s[l + 1:r]

# print (countSubstrings("aaa"))

print (countSubstrings("abc"))