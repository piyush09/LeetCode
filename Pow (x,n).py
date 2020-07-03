"""
Algo: Recursive Solution
      If power(n) becomes 0, then return 1 in the recursion.
      If power(n) is not divisible by 2, then multiply with x and do recursive call for         power as (n-1).
      If power(n) is divisible by 2, then do recursive call for power as (n/2).

"""

def myPow(x, n):

    if not n:  # If n. is equal to 0, return 1
        return 1
    if n < 0:  # If n is negative, then return Pow() for negative of input 'n' value.
        return 1 / myPow(x, -n)
    if n % 2:  # If n is not divisible by 2, then recursively call with (n-1) as power.
        return x * myPow(x, n - 1)
    return myPow(x * x, n / 2)  # Otherwise recursively call with (n/2) as power.

x = 2.0
n = -2
print (myPow(x,n))

