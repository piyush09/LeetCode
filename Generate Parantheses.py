"""
Algo: Choice at each stage would be whether to open or close a bracket.
      Backtrack for adding left parantheses, then only when current number of left parantheses is less than the required pairs of parantheses
      Backtrack for adding right parantheses only when count of right parantheses is less than count of left parantheses.

      Place N*2 parantheses, where N is the number of opening parantheses

T.C. - Quite complex, check in the LeetCode solution.
S.C. - O(N) - O(2*N) - 'N' is the number of pairs of parantheses.

"""

def generateParenthesis(n):
    ans = []

    def backtrack(S='', left=0, right=0):

        # If current string's (S) length is 2*N, then append it to the answer
        if (len(S) == 2 * n):
            ans.append(S)

        # Constraint is backtrack then only when current number of
        # left parantheses is less than the required pairs of parantheses.
        if left < n:
            backtrack(S + '(', left + 1, right)

        # Constraint is we cannot close parantheses, unless there is left parantheses to match with it,
        # so backtrack for right parantheses only when count of right parantheses is less than count of left parantheses.
        if right < left:
            backtrack(S + ')', left, right + 1)

    backtrack()
    print ("Number of possible parantheses are :",len(ans))
    return ans

N = 3
print(generateParenthesis(N))