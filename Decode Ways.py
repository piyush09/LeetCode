"""
Algo: Use a dp array of size (n + 1) to save subproblem solutions.
    dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 1
    dp[i]: represents possible decode ways to the ith char(include i), whose index in string is (i-1)
    Check one digit and two digit combinations and save results in dp array, finally dp[n] will be the end result.

T.C. - O(N), where N is the length of the string
S.C.- O(N), where dp[] array of size(N+1) is created
"""


def numDecodings(s):

    # As if s[0] is 0, then there won't be any decode ways, as there is no mapping for 0
    if (not s or (s[0]=='0')):
        return 0

    # Initializing dp array with length (s+1) with values 0 in it
    dp = [0 for x in range(len(s) + 1)]

    # Base Cases
    # dp[0] = 1, is for creating base
    # dp[1] = 1, if there's one character, if it is not zero, there can only be 1 decode way
    dp[0:2] = [1, 1]


    for i in range(2, len(s) + 1):
        # if (0 < int(s[i - 1:i]) <= 9):

        # Only need to ensure that the s[i-1:i] is not equal to zero, since only zero does not have a mapping
        # to an alphabet and rest of the digits from 1 through 9 have a mapping.

        # Taking the value s[i-1] and checking if it's not equal to 0
        if (int(s[i - 1:i]) != 0):
            dp[i] += dp[i - 1]

        # Taking two values int(s[i-2] and s[i-1]), and checking if the value is between the range [10,26]
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    # Last element in the DP array would return the number of ways to decode input string
    return dp[len(s)]

# s = "12"
s ="226"
print (numDecodings(s))