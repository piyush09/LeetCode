"""
Algo: Check whether each digit is non-zero and divides the number.
      convert the number into a character array (string in Python), and
      then convert back to integer to check (n % d == 0)
      Check if each digit of the number is self dividing, then add it to output

S.C. - O(D) - to store the output, as list of all self dividing numbers.
"""
class Solution:
    def selfDividingNumbers(self, left, right):

        output = []
        for num in range(left, right + 1, 1):
            i = 0
            for char in str(num):

                if (int(char) == 0):
                    break

                if ((num % int(char)) != 0):
                    break

                i += 1

            if (i == len(str(num))): # Checking if each digit of the number is self dividing, then adding it to output
                output.append(num)

        return output

left = 1
right = 22

print (Solution().selfDividingNumbers(left, right))