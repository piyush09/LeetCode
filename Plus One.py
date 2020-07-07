"""
Algo: Add one to the last number in the digits list.
     Iterate till current val in digits list is greater than 9, if so
     In case, iterator is 0, then make value as 0 and insert 1 in the beginning of the list.
     calculate the carry, add it to previous digit, and make this digit as modulus value with 10.
     Decrement the iterator.

T.C. - O(N) - Iterating as many number of times as the number of digits in the worst case.
S.C. - O(1) - Constant space is being used.
"""

class Solution:
    def plusOne(self, digits):

        digits[-1] += 1
        i = len(digits) - 1

        while (digits[i] > 9):

            if (i == 0):
                digits[i] = digits[i] % 10
                digits.insert(0, 1)
                break

            carry = (digits[i]) / 10
            digits[i - 1] += carry
            digits[i] = digits[i] % 10
            i -= 1

        return digits

digits = [9, 9, 9, 9]
print (Solution().plusOne(digits))