"""
Algo: Dictionary (Hashmap) is used to store index of characters already seen.
     Enumerate through the string of characters, if character already exists, and start index < char index,
        then update start value.
    Otherwise, update the maxLength value.
    Also, update the latest index of iterating character in useCharacter dictionary.

T.C. - O(N) - 'N' number of characters in the string, as iterating through the string once.
S.C. - O(min(m,n)) - space complexity for the dictionary or hashmap.
"""

def lengthOfLongestSubstring(s):

    if (len(s) == 0):
        return 0

    # usedChar dictionary maintaining used characters with 'character' as 'key' and 'index' of character as 'value'
    usedChar = {}

    # maxLength is length of longest substring without repeating characters, start is to maintain 'start' index and put as 0
    maxLength = start = 0
    maxSubstr = ""
    # Enumerating through the string keeping track of index and character
    for index, char in enumerate(s):

        # If 'char' character already exists in usedChar dictionary and
        # If start index is less than index of char in usedChar dictionary
        if char in usedChar and (start <= usedChar[char]):
            start = usedChar[char]+1
        else:
        # Update the maxLength accordingly, as (index-start+1),
        # considering start is updated continuously with latest index of that character
            maxLength = max(maxLength, index-start+1)
        # Printing the maximu substring as well
            maxSubstr = s[start:index+1]

        # Updating the index, to store the latest index of the iterating character in usedChar dictionary
        usedChar[char] = index

    print ("Maximum Substring is:", maxSubstr)
    return maxLength


# s = "abcabcbb"
s = "pwwkew"
print (lengthOfLongestSubstring(s))
