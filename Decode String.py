"""
Algo: When a number, or after '[' character is encountered , push it on the stack.
      When a close square bracket ']' is there, pop the last element of the stack.

"""
class Solution:
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        number = ""

        # Iterating over each character in the input string
        for character in s:

            # If character is a digit, then add that character into the number, as it is a digit
            if character.isdigit():
                number += character

            # If character is an opening square bracket, then append empty string, and number into the stack
            # Also make the number as empty string
            elif character == '[':
                stack.append(["", int(number)])
                number = ""

            # If character is closing square bracket, then pop the last element of the stack
            # Append it to the previous element of the stack, as many number of times, it should occur
            elif character == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k

            # If it is a normal character, then just append it to the last element's first key in it
            else:
                stack[-1][0] += character

        # Return first element's first key of the stack in it
        return stack[0][0]

s = "3[a]2[bc]"
print(Solution().decodeString(s))

s = "abc3[cd]xyz"
print(Solution().decodeString(s))