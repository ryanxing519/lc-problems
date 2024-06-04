class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        l = 0
        ans = 0
        cost = 0
        for r in range(len(s)):
            # add to the cost
            cost += abs(ord(t[r]) - ord(s[r]))

            while cost > maxCost:
                cost -= abs(ord(t[l]) - ord(s[l]))
                l += 1
            ans = max(ans, r-l)

        return ans

