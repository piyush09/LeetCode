"""
Algo: Use recursion technique.
      If there is no more digits, then current combination is done.
      If there are digits to be checked, then:
        combination = combination + letter
        recurse(combination+letter, next_digits[1:])

T.C. - O(3^N * 4^M) - where N - number of digits mapping to 3 letters (2,3,4,5,6,8)
      and 4 letters(7,9)

S.C. - O(3^N * 4^M) - as one has to keep these many solutions.
"""

digit2Letters = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

def recurse(combination, next_digits, output):
    if (len(next_digits) == 0):
        output.append(combination) # Appending to the output, when len(next_digits) becomes 0

    else:
        # Iterating in for loop for all the letters of that digit
        for letter in digit2Letters[next_digits[0]]:
            recurse(combination+letter, next_digits[1:], output)

def letterCombinations(digits):
    output = [] # Initialising output to empty

    # If digits are there, then doing backtracking for it
    if digits:
        recurse("", digits, output)
    return output

digits = "23"
print (letterCombinations(digits))