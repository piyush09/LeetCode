"""
Algo: Iterate through the string and use stack to calculate all the in between values.
      Calculate between values such as product, division, negative numbers and positive numbers.
      Maintain sign in order to operate it on the next numeric character value.
      Append them into the stack, which could be summed at the end.

T.C. - O(n), iterating through all n characters in the input string.
"""

def calculate(s):

    # If no string, return 0
    if not s:
        return "0"

    # Stack will contain all the values in it, as for in between product, division and negative values
    # Add them all at the end
    stack = []
    num = 0
    sign = "+"

    for i in range(len(s)):

        # If s[i] is a digit, then consider it
        # ord(s[i])-ord("0"), returns the value corresponding to that digit or can use int(s[i]) in order to get integer value
        if s[i].isdigit():
            num = num * 10 + int(s[i])

        # sign is used to do the operation, as per the previous character, as in the case of last character, needs to
        # preserve the sign accordingly, in order to calculate the operation as per the previous sign on it.
        # If s[i] is in one of the operands, then consider it
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num) # In multiplication, popping last element and calculating the product.
            else:
                stack.append(int(stack.pop() / num)) # In division, popping last element and calculating the division values.

            num = 0 # Making num as 0 is important in it
            sign = s[i] # Preserving sign for operation on next numeric character

    # Return sum of all elements of the stack
    return sum(stack)

s = "3+2*2"
# s = "3/2"
print (calculate(s))
