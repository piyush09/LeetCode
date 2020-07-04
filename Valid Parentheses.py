"""
Algo: An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    An empty string is also considered valid.

    If opening bracket, push it onto the stack
    If closing bracket, then check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then pop it off the stack and continue processing. Else, this implies an invalid expression.

T.C. - O(n), as, traverse the given string one character at a time and push and pop operations on a stack take O(1)O(1) time.

S.C. - O(n), as pushing all opening brackets onto the stack and in the worst case,          all the brackets will be pushed onto the stack.
"""

class Solution:
    def isValid(self, s):

        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Initializing parantheses dictionary
        parantheses_dict = {"]": "[", "}": "{", ")": "("}

        for character in s:  # Iterating over each character in string s
            if character in parantheses_dict.values():
                stack.append(character)

            elif character in parantheses_dict.keys():
                if stack == [] or parantheses_dict[character] != stack.pop():
                    # If the stack is empty or no matching parantheses
                    return False
            else:
                # If another character is encountered apart from parantheses
                return False

                # As empty string is also a valid string
        return stack == []

str = "()[]{}"
test = Solution()
print (test.isValid(str))