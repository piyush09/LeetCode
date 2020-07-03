"""
Algo: 'dp' is an array that contains booleans.
      dp[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

T.C. - O(N^2) - Two for loops are being used
S.C. - O(N) - Creating extra dp[] table of size equal to (len(s)+1)
"""
def wordBreak(s, wordDict):

    # dp[i] means s[:(i+1)] from [0,i] index can be segmented into words in wordDict.
    dp = [False] * (len(s)+1)
    dp[0] = True

    # Iterating through all the indexes till length of string 's'
    for i in range(len(s)):

        # Iterating from 'i' th character till end of input string to check if there is a match
        for j in range(i, len(s)):

            # if dp[i] is true, means there exists a word in wordDict matching from [0,i]
            # And then checking if substring s[i,j] is matching from any string in wordDict
            if (dp[i]) and (s[i: (j+1)] in wordDict):
                dp[j+1] = True


    # If the last index of dp[i] is True, it means there is a matching of entire string in wordDict
    return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]

print (wordBreak(s, wordDict))
