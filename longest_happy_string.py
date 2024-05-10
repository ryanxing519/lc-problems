class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [[a, "a"], [b, "b"], [c, "c"]]
        ans = []

        while True:
            counts.sort(reverse=True)
            if counts[0][0] == 0:
                break

            if len(ans) < 2 or (ans[-1] != counts[0][1] or ans[-2] != counts[0][1]):
                ans.append(counts[0][1])
                counts[0][0] -= 1
            elif counts[1][0] >= 1:
                ans.append(counts[1][1])
                counts[1][0] -= 1
            else:
                break

        return "".join(ans)
