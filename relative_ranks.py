class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        sorted_score = sorted(score, reverse=True)
        rankings = {sorted_score[i]: i for i in range(len(sorted_score))}
        ans = []

        for s in score:
            if rankings[s] == 0:
                ans.append("Gold Medal")
            elif rankings[s] == 1:
                ans.append("Silver Medal")
            elif rankings[s] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rankings[s] + 1))

        return ans
