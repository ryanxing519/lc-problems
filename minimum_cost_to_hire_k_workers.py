import heapq


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:

        exp = [(w/q, q) for q, w in zip(quality, wage)]
        exp.sort()

        heap = []

        q_sum, ans = 0, float("inf")

        for ratio, quality in exp:
            heapq.heappush(heap, -quality)
            q_sum += quality

            if len(heap) > k:
                q_sum -= abs(heapq.heappop(heap))
            if len(heap) == k:
                ans = min(ans, ratio * q_sum)

        return ans
