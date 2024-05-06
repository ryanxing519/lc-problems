import math


class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # formula for sum:
        # (n * (n+1)) / 2
        # we are looking for a case where k consectutive terms add up to the sum N
        # x + (x+1) + (x+2) + (x+3) .. + total k terms
        # kx + (k*(k-1)) / 2 = N
        # kx = N - (k*(k-1))/2
        # we can loop for k values and sub into RHS, if RHS is divisible by k, we know we've found a consecutive
        # sequence starting from the number x
        ans = 1
        for i in range(2, int(math.sqrt(2 * n)) + 1):
            if (n - (i * (i - 1)) / 2) % i == 0:
                ans += 1
        return ans
