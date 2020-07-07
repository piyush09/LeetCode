"""
Algo: Bigger ugly numbers can be generated by multiplying smaller ugly numbers by 2, 3 and 5.
      Have 3 pointers, namely i2, i3, and i5, they will keep track of which multiple of 2, 3, 5 of smaller ugly number are being pointed.
      Append smallest next ugly number, increment the pointer that generated that smallest ugly number.
      If two or three u2, u3, and u5 are the same, their corresponding pointer will also be incremented,
      As if statements are in parallel.
      After n-1 loops, n ugly numbers are generated, and the last number ugly[-1] is the answer.

T.C. - O(N) - as (N-1) iterations are there in the while loop.
"""

class Solution:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = 0  # Taking three pointers i2, i3 and i5
        i3 = 0
        i5 = 0

        while (n > 1):
            u2 = 2 * ugly[i2]
            u3 = 3 * ugly[i3]
            u5 = 5 * ugly[i5]

            umin = min(u2, u3, u5)
            # if two or three u2, u3, and u5 are the same, their corresponding pointer will also be incremented
            # As if statements are in parallel.
            if (umin == u2):
                i2 += 1
            if (umin == u3):
                i3 += 1
            if (umin == u5):
                i5 += 1

            ugly.append(umin)
            n -= 1

        return ugly[-1]


n = 10
print (Solution().nthUglyNumber(n))