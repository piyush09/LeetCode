"""
Algo: Use concept of Fibonacci number
    Fib(N) = Fib(N-1) + Fib(N-2)
    Find nth number of the fibonacci series with Fib(1)=1 and Fib(2)=2.
T.C. - O(N) - Single loop upto n to calculate nth fibonacci number.
S.C.- O(1) - Constant space is used.
"""

"""
Solution 1:
a = 0 # Initializing a as 0
b = 1 # Initializing b as 1

for elem in range(N): # Iterating over all the elements till number N
    temp = b # Assigning value of b to a temporary variable
    b = a + b # Assigning summation of a and b to b, as it would be the next 'b'
    a = temp # As the previous 'b' would now become 'a', which was previously stored in temp variable

return a
"""

class Solution:
    def fib(self, N):

        if (N == 0):
            return 0

        first = 1  # Initialize first as Fib(1) = 1
        second = 1  # Initialize second as Fib(2) = 2

        # Iterate till number 'n'
        for i in range(3, N + 1):
            third = first + second
            first = second
            second = third

        return second

N = 4
print (Solution().fib(N))