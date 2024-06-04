from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        cnts = Counter(s)
        ans = odd = 0
        for letter, cnt in cnts.items():
            ans += (cnt // 2) * 2
            if cnt % 2 == 1: odd = 1
        return cnt + odd
