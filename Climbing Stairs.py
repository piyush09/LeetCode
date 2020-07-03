"""
Algo: Use concept of Fibonacci number
    Fib(N) = Fib(N-1) + Fib(N-2)
    Find nth number of the fibonacci series with Fib(1)=1 and Fib(2)=2.
T.C. - O(N) - Single loop upto n to calculate nth fibonacci number.
S.C.- O(1) - Constant space is used.
"""
def climbStairs(n):
    if (n == 1):
        return 1

    first = 1 # Initialize first as ways to climb 1 stair to 1
    second = 2 # Initialize second as ways to climb 2 stairs to 2

    # Iterate till number 'n'
    for i in range(3, (n + 1)):
        third = first + second
        first = second
        second = third

    return second

# n = 2
n = 4
print (climbStairs(n))