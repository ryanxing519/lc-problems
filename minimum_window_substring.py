import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s_cnt, t_cnt = collections.defaultdict(int), collections.defaultdict(int)
        for char in t:
            t_cnt[char] += 1

        have, want = 0, len(t_cnt)

        l = 0
        ans = ''

        for r in range(len(s)):
            s_cnt[s[r]] += 1
            if s_cnt[s[r]] == t_cnt[s[r]]:
                have += 1

            while have == want:
                # we need to calculate the answer here
                ans = s[l:r+1] if r+1-l < len(ans) or ans == '' else ans
                s_cnt[s[l]] -= 1
                if s_cnt[s[l]] < t_cnt[s[l]]:
                    have -= 1
                l += 1
a
        return ans